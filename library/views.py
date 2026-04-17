from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BookData
from .serializers import BookDataSerializer
from .embedding_utils import build_faiss_index, search_books
from .ai_utils import generate_answer


@api_view(['GET'])
def fetch_all_books(request):
    books = BookData.objects.all().order_by('-uploaded_at')
    serializer = BookDataSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_book_detail(request, pk):
    try:
        book = BookData.objects.get(id=pk)
    except BookData.DoesNotExist:
        return Response({"error": "Book not found"}, status=404)

    serializer = BookDataSerializer(book)
    return Response(serializer.data)


@api_view(['POST'])
def add_book(request):
    serializer = BookDataSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)


@api_view(['POST'])
def ask_question(request):
    query = request.data.get("question")

    if not query:
        return Response({"error": "Question is required"}, status=400)

    books = BookData.objects.all()

    build_faiss_index(books)
    top_books = search_books(query)

    if not top_books:
        return Response({"error": "No relevant books found"})

    unique_books = []
    seen = set()

    for book in top_books:
        if book.title not in seen:
            unique_books.append(book)
            seen.add(book.title)

    top_books = unique_books

    query_lower = query.lower()
    top_books = [
        book for book in top_books
        if book.title.lower() not in query_lower
    ]

    context = ""
    for book in top_books:
        context += f"""
Book:
Title: {book.title}
Genre: {book.genre}
Summary: {book.ai_summary}
Description: {book.description}
"""

    answer = generate_answer(query, context)
    answer += "\n\nSources: " + ", ".join([book.title for book in top_books])

    sources = [book.title for book in top_books]

    return Response({
        "answer": answer,
        "sources": sources
    })


def dashboard(request):
    books = BookData.objects.all().order_by('-uploaded_at')
    return render(request, "library/dashboard.html", {"books": books})


def book_detail(request, pk):
    book = get_object_or_404(BookData, id=pk)
    return render(request, "library/book_detail.html", {"book": book})


def ask_page(request):
    answer = None
    sources = None

    history = request.session.get("history", [])

    if request.method == "POST":
        query = request.POST.get("question", "").strip()

        if not query:
            answer = "Hmm… try typing something first 😄"
            sources = []
        else:
            books = BookData.objects.all()

            build_faiss_index(books)
            top_books = search_books(query)

            if top_books:
                unique_books = []
                seen = set()

                for book in top_books:
                    if book.title not in seen:
                        unique_books.append(book)
                        seen.add(book.title)

                top_books = unique_books

                query_lower = query.lower()

                top_books = [
                    book for book in top_books
                    if book.title.lower() not in query_lower
                ]

                top_books = top_books[:3]

                if not top_books:
                    answer = "Looks like that book slipped off our shelf 📚😄 Try another search?"
                    sources = []
                else:
                    context = ""
                    for book in top_books:
                        context += f"""
Book:
Title: {book.title}
Genre: {book.genre}
Summary: {book.ai_summary}
Description: {book.description}
"""

                    answer = generate_answer(query, context)
                    answer += "\n\nSources: " + ", ".join([book.title for book in top_books])

                    sources = top_books

            else:
                answer = "Looks like that book slipped off our shelf 📚😄 Try another search?"
                sources = []

        history.append({
            "question": query,
            "answer": answer
        })

        request.session["history"] = history

    return render(request, "library/ask.html", {
        "answer": answer,
        "sources": sources,
        "history": history
    })


def history_page(request):
    history = request.session.get("history", [])
    return render(request, "library/history.html", {"history": history})
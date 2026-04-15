from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BookData
from .serializers import BookDataSerializer
from .rag_utils import find_top_books


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
    top_books = find_top_books(query, books)

    if not top_books:
        return Response({"error": "No relevant books found"})

    results = []

    for book in top_books:
        results.append({
            "title": book.title,
            "summary": book.ai_summary,
            "reason": "Semantically similar to your query"
        })

    return Response({
        "results": results
    })

def home(request):
    results = None

    if request.method == "POST":
        query = request.POST.get("question")

        books = BookData.objects.all()
        top_books = find_top_books(query, books)

        results = [
            {
                "title": book.title,
                "summary": book.ai_summary
            }
            for book in top_books
        ]

    return render(request, "library/index.html", {"results": results})
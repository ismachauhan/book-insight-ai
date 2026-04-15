from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BookData
from .serializers import BookDataSerializer
from .rag_utils import find_most_similar



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
    best_book = find_most_similar(query, books)

    if best_book:
        answer = f"""
Based on your question, this book is relevant:

📖 Title: {best_book.title}
🧠 Summary: {best_book.ai_summary}

This book matches your query because it is semantically similar to your question.
"""
    else:
        answer = "No relevant book found."

    return Response({"answer": answer})
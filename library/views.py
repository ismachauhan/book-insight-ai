from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BookData
from .serializers import BookDataSerializer



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
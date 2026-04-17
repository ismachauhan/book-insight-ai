from django.urls import path
from .views import fetch_all_books, get_book_detail, add_book, ask_question

urlpatterns = [
    path('books/', fetch_all_books),
    path('books/<int:pk>/', get_book_detail),
    path('books/add/', add_book),
    path('ask/', ask_question),
]
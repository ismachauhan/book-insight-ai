import os
import django
import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin

from library.ai_utils import classify_genre, generate_summary

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookinsight.settings')
django.setup()

from library.models import BookData

BASE_URL = "https://books.toscrape.com/"

response = requests.get(BASE_URL)
soup = BeautifulSoup(response.text, "html.parser")


books = soup.find_all("article")
books = books[:10]

for book in books:
    title = book.h3.a['title']

    
    link = book.h3.a['href']
    book_url = urljoin(BASE_URL, link)

   
    if BookData.objects.filter(title=title).exists():
        continue

   
    book_page = requests.get(book_url)
    book_soup = BeautifulSoup(book_page.text, "html.parser")

   
    desc_tag = book_soup.find("meta", {"name": "description"})
    description = desc_tag["content"].strip() if desc_tag else "No description available"

    
    description = description.split("...")[0]

   
    genre = classify_genre(title, description)

    
    summary = generate_summary(description)

    
    author = "Unknown Author"

    
    rating_class = book.p['class'][1]  
    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    rating = rating_map.get(rating_class, 3)

   
    BookData.objects.create(
        title=title,
        description=description,
        ai_summary=summary,
        genre=genre,
        author=author,
        rating=rating,
        source_url=book_url
    )



print("Books saved cleanly without duplicates!")
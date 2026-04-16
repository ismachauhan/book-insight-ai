import os
import django
import requests
from bs4 import BeautifulSoup
import time
from library.ai_utils import classify_genre

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookinsight.settings')
django.setup()

from library.models import BookData

BASE_URL = "https://books.toscrape.com/"

response = requests.get(BASE_URL)
soup = BeautifulSoup(response.text, "html.parser")

# ✅ FIXED
books = soup.find_all("article")
books = books[:3]

for book in books:
    title = book.h3.a['title']

    link = book.h3.a['href']
    book_url = BASE_URL + link

    book_page = requests.get(book_url)
    book_soup = BeautifulSoup(book_page.text, "html.parser")

    desc_tag = book_soup.find("meta", {"name": "description"})
    description = desc_tag["content"].strip() if desc_tag else "No description available"

    genre = classify_genre(title, description)

    # ✅ FAST summary (NO LLM here)
    summary = description[:120] + "..."

    BookData.objects.create(
        title=title,
        description=description,
        ai_summary=summary,
        genre=genre
    )

    # 🧊 small delay (prevents heating)
    time.sleep(1)



print("Books saved safely!")
import os
import django
import requests
from bs4 import BeautifulSoup

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookinsight.settings')
django.setup()

from library.models import BookData

url = "https://books.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article")

for book in books:
    title = book.h3.a['title']
    
    BookData.objects.create(
        title=title,
        description="Sample description",
        source_url=url
    )
print("Books saved successfully!")
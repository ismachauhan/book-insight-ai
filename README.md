#  Book Insight AI

##  Overview

Book Insight AI is a full-stack web application that collects book data from the web and provides intelligent insights using AI techniques. The system is designed to automate data collection, store it efficiently, and enable users to explore and query books through REST APIs.

The project focuses on combining backend development with basic AI integration, demonstrating how structured data can be enhanced with intelligent processing.

---

##  Features

*  **Automated Data Collection**
  Scrapes book data from websites using Python and BeautifulSoup.

*  **Backend Data Management**
  Stores book details such as title, description, rating, and source URL using Django ORM.

*  **AI-Based Insights**

  * Generates summaries for each book
  * Provides simple recommendation logic based on content

*  **REST API Support**
  Built using Django REST Framework:

  * `GET /api/books/` → Fetch all books
  * `GET /api/books/<id>/` → Fetch book details
  * `POST /api/books/add/` → Add a new book

---

##  System Workflow

1. Scrape book data from a website
2. Store data in the database
3. Generate AI-based insights (summary & recommendations)
4. Expose data via REST APIs
5. Allow users to query and explore books

---

##  Tech Stack

* **Backend:** Django, Django REST Framework
* **Language:** Python
* **Web Scraping:** BeautifulSoup, Requests
* **Database:** SQLite (default Django DB)

---

##  Project Structure

```
bookinsight/
│
├── library/              # Main application
│   ├── models.py         # Database models
│   ├── views.py          # API logic
│   ├── serializers.py    # Data serialization
│
├── scraper.py            # Book scraping script
├── manage.py
```

---

##  How to Run the Project

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd bookinsight
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run server

```bash
python manage.py runserver
```

### 6. Run scraper

```bash
python scraper.py
```

---

##  API Endpoints

| Method | Endpoint           | Description       |
| ------ | ------------------ | ----------------- |
| GET    | `/api/books/`      | Fetch all books   |
| GET    | `/api/books/<id>/` | Fetch single book |
| POST   | `/api/books/add/`  | Add new book      |

---

##  Future Improvements

* Implement RAG-based question answering system
* Improve recommendation system using embeddings
* Add frontend interface (React / Next.js)
* Enhance scraping for detailed book metadata

---


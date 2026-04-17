# Book Insight AI

A smart book recommendation system powered by AI and semantic search.
This project uses Retrieval-Augmented Generation (RAG) to suggest books based on user queries.

---

## Features

*  Ask questions like: *"suggest fantasy books"*
*  AI-powered recommendations using local LLM (Mistral via LM Studio)
*  Semantic search using FAISS + Sentence Transformers
*  Stores previous queries (history feature)
*  Clean and modern UI with Tailwind CSS

---

##  Tech Stack

* **Backend:** Django, Django REST Framework
* **AI:** Sentence Transformers, FAISS, Local LLM (LM Studio - Mistral)
* **Frontend:** HTML, Tailwind CSS
* **Database:** SQLite

---

## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/your-username/book-insight-ai.git
cd book-insight-ai
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run server

```
python manage.py runserver
```

### 5. Start AI (IMPORTANT)

* Open **LM Studio**
* Load model: `mistral-7b-instruct-v0.2`
* Start local server at:

```
http://127.0.0.1:1234
```

---

## Screenshots

### Dashboard

<img width="2560" height="1516" alt="Screenshot 2026-04-18 022237" src="https://github.com/user-attachments/assets/e8fbc702-0131-45cf-a159-6a067bb0fa88" />



### Ask AI Page

<img width="2560" height="1516" alt="Screenshot 2026-04-18 022300" src="https://github.com/user-attachments/assets/acc8453a-cb35-4ec3-8166-35d358e7f0bd" />



### AI Answer

<img width="2560" height="1516" alt="Screenshot 2026-04-18 022421" src="https://github.com/user-attachments/assets/6d3909fa-13f3-4f4e-8f59-dec0f83530ed" />



### History Page

<img width="2560" height="1516" alt="Screenshot 2026-04-18 022439" src="https://github.com/user-attachments/assets/1d3b5c17-c272-4be0-8f7a-70b32d9fc521" />


---

## API Endpoints

| Method | Endpoint      | Description      |
| ------ | ------------- | ---------------- |
| GET    | `/books/`     | Fetch all books  |
| GET    | `/book/<id>/` | Get book details |
| POST   | `/ask/`       | Ask AI question  |
| POST   | `/add/`       | Add new book     |

---

##  Sample Query

**Input:**

```
suggest a book like A Light in the Attic
```

**Output:**

```
Book 1:

Title: Where the Sidewalk Ends by Shel Silverstein

Why you might like it: This collection of poems and drawings by Shel Silverstein is similar to "A Light in the Attic." Its whimsical and humorous verses will leave you entertained and amused.

Book 2:

Title: The Phantom Tollbooth by Norton Juster

Why you might like it: This classic children's book also includes playful poetry and illustrations, making it a great match for those who enjoyed "A Light in the Attic."
```

---

## Note

AI responses are generated using a **local LLM (LM Studio)**.
Make sure LM Studio is running before asking questions.

---

## Author

* Isma Chauhan

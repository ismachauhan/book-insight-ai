from sentence_transformers import SentenceTransformer
import numpy as np


model = SentenceTransformer('all-MiniLM-L6-v2')


def get_embedding(text):
    return model.encode(text)


def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (
        np.linalg.norm(vec1) * np.linalg.norm(vec2)
    )
  


def find_top_books(query, books, top_k=3):
    query_embedding = get_embedding(query)

    scores = []

    for book in books:
        text = f"{book.title} {book.description}"
        book_embedding = get_embedding(text)

        score = cosine_similarity(query_embedding, book_embedding)

        scores.append((score, book))

   
    scores.sort(key=lambda x: x[0], reverse=True)

    top_books = [book for _, book in scores[:top_k]]

    return top_books
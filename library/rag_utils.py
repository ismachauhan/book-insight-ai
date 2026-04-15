from sentence_transformers import SentenceTransformer
import numpy as np


model = SentenceTransformer('all-MiniLM-L6-v2')


def get_embedding(text):
    return model.encode(text)


def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (
        np.linalg.norm(vec1) * np.linalg.norm(vec2)
    )


def find_most_similar(query, books):
    query_embedding = get_embedding(query)

    best_score = -1
    best_book = None

    for book in books:
        text = f"{book.title} {book.description}"
        book_embedding = get_embedding(text)

        score = cosine_similarity(query_embedding, book_embedding)

        if score > best_score:
            best_score = score
            best_book = book

    return best_book
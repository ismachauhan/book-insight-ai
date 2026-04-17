from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')


def get_embedding(text):
    return model.encode(text)


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def find_top_books_semantic(query, books, top_k=3):
    query_emb = get_embedding(query)

    scored = []

    for book in books:
        text = f"{book.title} {book.description}"
        book_emb = get_embedding(text)

        score = cosine_similarity(query_emb, book_emb)
        scored.append((score, book))

    scored.sort(reverse=True, key=lambda x: x[0])

    return [book for _, book in scored[:top_k]]
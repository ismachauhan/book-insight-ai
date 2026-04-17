from sentence_transformers import SentenceTransformer
import numpy as np

import faiss


model = SentenceTransformer('all-MiniLM-L6-v2')

index = None
book_list = []


def build_faiss_index(books):
    global index, book_list

    book_list = list(books)

    embeddings = []
    for book in book_list:
        text = f"{book.title} {book.description}"
        emb = model.encode(text)
        embeddings.append(emb)

    embeddings = np.array(embeddings).astype("float32")

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)


def search_books(query, top_k=3):
    global index, book_list

    query_emb = model.encode([query]).astype("float32")

    distances, indices = index.search(query_emb, top_k)

    return [book_list[i] for i in indices[0]]
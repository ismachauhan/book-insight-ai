from sentence_transformers import SentenceTransformer
import numpy as np

try:
    import faiss
except:
    faiss = None


model = SentenceTransformer('all-MiniLM-L6-v2')

index = None
book_list = []
embeddings_cache = []


def build_faiss_index(books):
    global index, book_list, embeddings_cache

    book_list = list(books)

    embeddings = []
    for book in book_list:
        text = f"{book.title} {book.genre} {book.ai_summary} {book.description}"
        emb = model.encode(text)
        embeddings.append(emb)

    embeddings = np.array(embeddings).astype("float32")
    embeddings_cache = embeddings

    if faiss:
        dim = embeddings.shape[1]
        index = faiss.IndexFlatL2(dim)
        index.add(embeddings)


def search_books(query, top_k=3):
    global index, book_list, embeddings_cache

    query_emb = model.encode([query]).astype("float32")

    if faiss and index:
        distances, indices = index.search(query_emb, top_k)
        return [book_list[i] for i in indices[0]]

    scores = np.dot(embeddings_cache, query_emb[0])
    top_indices = np.argsort(scores)[::-1][:top_k]

    return [book_list[i] for i in top_indices]
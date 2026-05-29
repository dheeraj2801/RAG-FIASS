from app.embeddings import generate_embedding
from app.vector_store import search

def retrieve(query: str):
    embedding = generate_embedding(query)

    results = search(embedding)

    return results
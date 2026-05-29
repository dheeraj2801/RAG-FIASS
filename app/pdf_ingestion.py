from app.pdf_loader import load_pdf
from app.chunker import chunk_text
from app.embeddings import generate_embedding
from app.vector_store import add_document

def ingest_pdf(file_path: str):

    text = load_pdf(file_path)

    chunks = chunk_text(text)

    for chunk in chunks:

        embedding = generate_embedding(chunk)

        add_document(chunk, embedding)

    return len(chunks)
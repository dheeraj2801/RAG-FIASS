from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import os

from app.pdf_ingestion import ingest_pdf

from app.embeddings import generate_embedding
from app.vector_store import add_document
from app.retrieval import retrieve

app = FastAPI()

class DocumentRequest(BaseModel):
    text: str

@app.post("/documents")
def add_docs(req: DocumentRequest):

    embedding = generate_embedding(req.text)

    add_document(req.text, embedding)

    return {
        "message": "document added"
    }

@app.get("/search")
def semantic_search(query: str):

    results = retrieve(query)

    return {
        "results": results
    }
    
@app.post("/upload-pdf")
async def upload_pdf(
    file: UploadFile = File(...)
):

    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    chunks = ingest_pdf(file_path)

    os.remove(file_path)

    return {
        "message": "PDF processed",
        "chunks": chunks
    }
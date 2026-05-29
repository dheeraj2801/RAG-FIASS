import faiss
import numpy as np

dimension = 384

index = faiss.IndexFlatL2(dimension)

documents = []

def add_document(text, embedding):
    vector = np.array([embedding]).astype('float32')
    
    index.add(vector)
    
    documents.append(text)
    
def search(query_embedding, k=3):
    vector = np.array([query_embedding]).astype(
        "float32"
    )
    
    distances, indices = index.search(vector, k)
    
    results = []
    
    for idx in indices[0]:
        if idx < len(documents):
            results.append(documents[idx])
            
    return results

# FAISS Index
# faiss.IndexFlatL2

# Means:

# brute force vector search
# exact nearest neighbors
# L2 distance similarity

# Later you’ll replace this with:

# HNSW
# IVF
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def generate_embedding(text: str):
    return model.encode(text)


# What You’re Learning Here

# This converts:

# "Apache Superset dashboard"

# into:

# [0.123, -0.98, ...]

# Dense vectors representing semantic meaning.

# This is the heart of modern retrieval systems.
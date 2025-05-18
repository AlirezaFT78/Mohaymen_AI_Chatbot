import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = None
index = None
document_chunks = []

def load_vector_store():
    global model, index, document_chunks

    model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

    documents = []
    document_chunks = []
    file_paths = [f for f in os.listdir("./data") if f.endswith(".txt")]

    for file_name in file_paths:
        with open(f"./data/{file_name}", "r", encoding="utf-8") as f:
            text = f.read()
            documents.append(text)

    for doc in documents:
        chunks = [doc[i:i+500] for i in range(0, len(doc), 500)]
        document_chunks.extend(chunks)

    embeddings = model.encode(document_chunks, convert_to_numpy=True)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

def get_top_k_chunks(query: str, k: int = 10):
    query_embedding = model.encode([query], convert_to_numpy=True)
    distances, indices = index.search(query_embedding, k)
    return [document_chunks[i] for i in indices[0]]

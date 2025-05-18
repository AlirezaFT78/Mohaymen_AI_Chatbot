import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

FAISS_INDEX_PATH = "./data/faiss.index"
DOCS_PATH = "./data/chunks.npy"
METADATA_PATH = "./data/chunks_metadata.npy"

def load_vector_store(chunk_size=500, overlap=100):
    global model, index, document_chunks, chunk_metadata

    model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

    # Caching Vector Database
    if os.path.exists(FAISS_INDEX_PATH) and os.path.exists(DOCS_PATH) and os.path.exists(METADATA_PATH):
        index = faiss.read_index(FAISS_INDEX_PATH)
        document_chunks = np.load(DOCS_PATH, allow_pickle=True).tolist()
        return
    
    documents = []
    document_chunks = []
    chunk_metadata = []
    
    file_paths = [f for f in os.listdir("./data") if f.endswith(".txt")]

    for file_name in file_paths:
        with open(f"./data/{file_name}", "r", encoding="utf-8") as f:
            text = f.read()
            documents.append((file_name, text))

    for filename, doc in documents:
        chunks = [doc[i:i+chunk_size] for i in range(0, len(doc) - chunk_size + 1, chunk_size - overlap)]
        for i, chunk in enumerate(chunks):
            document_chunks.append(chunk)
            chunk_metadata.append({"file": filename, "chunk_id": i})

    embeddings = model.encode(document_chunks, convert_to_numpy=True)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    
    np.save(DOCS_PATH, document_chunks)
    np.save(METADATA_PATH, chunk_metadata)
    faiss.write_index(index, FAISS_INDEX_PATH)
    
def get_top_k_chunks(query: str, k: int = 10):
    query_embedding = model.encode([query], convert_to_numpy=True)
    distances, indices = index.search(query_embedding, k)
    
    results = []
    for i in indices[0]:
        results.append({
            "text": document_chunks[i],
            "meta": chunk_metadata[i]
        })
    return results

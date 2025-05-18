from functools import lru_cache
from app.vector_store import get_top_k_chunks
from app.llm import generate_answer


@lru_cache(maxsize=128)
def answer_question(query: str) -> str:
    chunks_with_meta = get_top_k_chunks(query)
    context = "\n\n".join(chunk["text"] for chunk in chunks_with_meta)
    answer = generate_answer(context, query)
    return {"answer": answer, "sources": chunks_with_meta}



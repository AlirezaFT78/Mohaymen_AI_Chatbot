from app.vector_store import get_top_k_chunks
from app.llm import generate_answer

def answer_question(query: str) -> str:
    chunks = get_top_k_chunks(query)
    context = "\n\n".join(chunks)
    return generate_answer(context, query)

import logging
import time
from fastapi import FastAPI
from pydantic import BaseModel
from app.rag import answer_question
from app.vector_store import load_vector_store

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
load_vector_store()

class Question(BaseModel):
    query: str

@app.post("/ask")
async def ask_question(question: Question):
    if not question.query or len(question.query.strip()) < 3:
        return {"error": "سوال نامعتبر است. لطفاً سوال مشخص‌تری وارد کنید."}
    try:
        start = time.time()
        response = answer_question(question.query)
        logger.info(f"Answered query in {time.time() - start:.2f}s: {question.query}")
        return response
    except Exception as e:
        logger.error("Error in /ask", exc_info=True)
        return {"error": "خطایی رخ داده است."}

@app.get("/")
async def respond():
    return {"message": "Hello. This is Mohaymen Chatbot API"}


@app.get("/health")
async def health():
    return {"status": "ok"}

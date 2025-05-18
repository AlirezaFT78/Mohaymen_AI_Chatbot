import traceback
from fastapi import FastAPI
from pydantic import BaseModel
from app.rag import answer_question
from app.vector_store import load_vector_store

app = FastAPI()

# Initialize the vector store only once
load_vector_store()

class Question(BaseModel):
    query: str

@app.post("/ask")
async def ask_question(question: Question):
    try:
        response = answer_question(question.query)
        return {"answer": response}
    except Exception as e:
        return {"error": str(e), "trace": traceback.format_exc()}

@app.get("/")
async def repond():
    return {"messege": "Hello. This is Mohaymen Chatbot API"}
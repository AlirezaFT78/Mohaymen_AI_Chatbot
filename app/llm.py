import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)
# Gemini API compatibility via OpenAI library
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE")  
)
LLM_MODEL= os.getenv("LLM_MODEL")

def generate_answer(context: str, question: str) -> str:
    prompt = f"""Use the following context to answer the user's question.

    Context:
    {context}

    Question: {question}
    Answer:"""

    response = client.chat.completions.create(
        model=LLM_MODEL,  
        messages=[
            {"role": "system", "content": "تو دستیار منابع انسانی شرکت مهیمن هستی. فقط به فارسی جواب بده. "},
            {"role": "user", "content": prompt}
        ],
        temperature=0.1,
        max_tokens=500
    )

    return response.choices[0].message.content.strip()


# 🧠 RAG-Based Telegram Question Answering Bot (Persian)

This is a Retrieval-Augmented Generation (RAG) based Q&A system with Telegram integration. It answers Persian-language questions based on local document context using Google's **Gemini API** (via OpenAI-compatible endpoint), **FAISS vector search**, and a **Telegram bot interface**.

---

## 📦 Features

- ✅ Persian question answering from `.txt` documents in `/data/`
- ✅ FAISS vector search with overlapping chunks and token-aware truncation
- ✅ Gemini API (via `openai-python`) for LLM responses
- ✅ FastAPI backend exposed via `/ask` endpoint with health checks
- ✅ Real-time Telegram bot integration with anti-flooding
- ✅ Dockerized with Docker Compose and volume persistence
- ✅ Query caching with `lru_cache`
- ✅ Tests for LLM, API, and bot interaction with mocking support
- ✅ Supports Hugging Face model caching and `.env` config

---

## 🧰 Technologies Used

- FastAPI
- FAISS
- HuggingFace Transformers / SentenceTransformers
- Gemini API via OpenAI-compatible client
- python-telegram-bot
- Docker & Docker Compose
- Pytest

---

## 🚀 Quickstart (Local + Docker)

### 1. 📁 Clone the Repository

```bash
git clone https://github.com/AlirezaFT78/Mohaymen_AI_Chatbot.git
cd Mohaymen_AI_Chatbot
```

---

### 2. ⚙️ Setup `.env` file

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY="your_api_key_here"
OPENAI_API_BASE="https://your_openai_base_url_here"
TELEGRAM_BOT_TOKEN="your_telegram_bot_token_here"
FASTAPI_URL="http://fastapi:8000/ask"
TEST_CHAT_ID="your_test_chat_id_here"
OPENAI_MODEL="gemini-2.0-flash-lite"
```

---

### 3. 🐳 Run with Docker Compose

```bash
docker compose up --build
```

- FastAPI: [http://localhost:8000/docs](http://localhost:8000/docs)
- Telegram bot: responds to user messages

---

## 🤖 Telegram Bot Demo

You can interact with the deployed chatbot via Telegram here:

👉 [@Mohaymen_AI_Task_bot](https://t.me/Mohaymen_AI_Task_bot)

Simply send a question in Persian (based on the loaded documents), and the bot will respond with a context-aware answer powered by Gemini and FAISS.

---

## 🧪 Example Persian Q&A

**User Question:**

```
بالاترین ضریب حقوق برای کدام گروه شغلی است؟
```

**Bot Answer:**

```
‫با توجه به اطلاعات ارائه شده، بالاترین ضریب حقوق برای گروه شغلی "توسعه نرم افزار-Back End" و "امنیت" با ضریب 3.1 است.
```

---

## 📁 Project Structure

```
rag-telegram-bot/
│
├── app/
│   ├── main.py              # FastAPI app
│   ├── telegram_bot.py      # Telegram bot logic
│   ├── llm.py               # Gemini/OpenAI API handler
│   ├── rag.py               # RAG orchestration logic
│   ├── vector_store.py      # FAISS storage and retrieval
│
├── data/                    # Input .txt documents
├── hf_model_cache/          # Model cache directory
├── tests/
│   ├── test_1_llm.py        # LLM API unit test
│   ├── test_2_api.py        # FastAPI /ask test
│   ├── test_3_bot.py        # Bot behavior unit test
│
├── .env
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── start.sh
├── README.md
└── answers.md
```

---

## 🧪 Running Tests

Make sure the virtualenv is active or you're in the container:

```bash
pytest tests/
```

---

## 📌 Future Improvements

- Use Redis or persistent caching instead of in-memory
- Use webhooks instead of polling for Telegram bot
- Add document metadata in responses
- Implement admin panel for document upload
- Optimize Persian chunking with language-aware splitters

---

## 📃 License

MIT License

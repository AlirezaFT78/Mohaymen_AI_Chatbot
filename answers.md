## 📌 Why use RAG over standard LLM prompting?

Standard LLM prompting can produce fluent but inaccurate results because the model relies solely on its training data. RAG combines retrieval and generation: relevant document chunks are retrieved from a local knowledge base and passed as context to the LLM. This is especially useful when working with custom, domain-specific, or Persian-language corpora. It ensures responses are grounded in actual content and reduces hallucination risk.

---

## ⚡ How did you handle latency?

To reduce latency:
- Document embeddings and FAISS index are built once and reused.
- FastAPI runs asynchronously to maximize responsiveness.
- Chunks are small and pre-processed for fast retrieval.
- Gemini (via OpenAI-compatible API) provides fast responses for short prompts.
- The Telegram bot avoids redundant API calls by ignoring invalid or empty queries.

---

## 📈 How would you scale this in production?

For scaling:
- Use cloud deployment for FastAPI with auto-scaling (e.g., GCP Cloud Run or ECS).
- Store the FAISS index and embeddings in mounted cloud volumes.
- Use a reverse proxy (e.g., NGINX) and HTTPS endpoint for FastAPI.
- Switch the bot to webhook mode using a secure tunnel (e.g., Cloudflare Tunnel or managed host).
- Add horizontal FastAPI scaling and a load balancer.
- Integrate a cache layer (e.g., Redis) for frequently asked questions.

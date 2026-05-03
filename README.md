# 🤖 LLM Agent — Multi-Provider AI Backend

A production-ready backend service that routes prompts to multiple LLM providers (Groq, Gemini, OpenAI) with zero code changes — just switch an environment variable. It shows that real apps can't be locked into one LLM provider. If OpenAI goes down or gets expensive, you switch.  

Built with **FastAPI** · **Python** · **Docker-ready**

---

## 🚀 Live Demo

```bash
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What is FastAPI?"}'
```

Response:
```json
{
  "response": "FastAPI is a modern, fast web framework for building APIs with Python...",
  "provider": "groq"
}
```

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                        Client                           │
│              (Swagger UI / curl / Postman)              │
└─────────────────────────┬───────────────────────────────┘
                          │  POST /chat
                          ▼
┌─────────────────────────────────────────────────────────┐
│                    FastAPI Server                       │
│                     (main.py)                           │
│                                                         │
│   PromptRequest { prompt: str }                         │
└─────────────────────────┬───────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                   Agent Router                          │
│                   (agent.py)                            │
│                                                         │
│   Reads LLM_PROVIDER from .env                          │
│   Routes to the correct provider                        │
└──────────┬──────────────┬──────────────┬────────────────┘
           │              │              │
           ▼              ▼              ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│   Groq       │ │   Gemini     │ │   OpenAI     │
│  Provider    │ │  Provider    │ │  Provider    │
│              │ │              │ │              │
│ llama-3.3    │ │ gemini-1.5   │ │ gpt-3.5      │
│ -70b         │ │ -flash       │ │ -turbo       │
└──────┬───────┘ └──────┬───────┘ └──────┬───────┘
       │                │                │
       └────────────────┴────────────────┘
                        │
                        ▼
              { response, provider }
```

---

## 📁 Project Structure

```
llm-agent/
├── app/
│   ├── __init__.py
│   ├── main.py                  # FastAPI app & endpoints
│   ├── agent.py                 # Provider router logic
│   └── providers/
│       ├── __init__.py
│       ├── groq_provider.py     # Groq (Llama 3.3)
│       ├── gemini.py            # Google Gemini
│       └── openai.py            # OpenAI GPT
├── .env                         # API keys (never committed)
├── .gitignore
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## ⚡ Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | FastAPI |
| Language | Python 3.11 |
| LLM Providers | Groq, Google Gemini, OpenAI |
| Server | Uvicorn (ASGI) |
| Config | python-dotenv |
| Containerization | Docker |

---

## 🛠️ Setup & Installation

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/llm-agent.git
cd llm-agent
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the root directory:
```env
LLM_PROVIDER=groq

GROQ_API_KEY=your_groq_key_here
GEMINI_API_KEY=your_gemini_key_here
OPENAI_API_KEY=your_openai_key_here
```

### 5. Run the server
```bash
uvicorn app.main:app --reload
```

Visit **http://127.0.0.1:8000/docs** for the interactive API documentation.

---

## 🔄 Switching Providers

The entire system switches with **one line** in your `.env`:

```env
LLM_PROVIDER=groq      # Uses Llama 3.3 70B (fastest, free)
LLM_PROVIDER=gemini    # Uses Gemini 1.5 Flash (Google)
LLM_PROVIDER=openai    # Uses GPT-3.5 Turbo (OpenAI)
```

No code changes needed. This is the core design principle — provider abstraction.

---

## 🐳 Docker

```bash
# Build
docker build -t llm-agent .

# Run
docker run -p 8000:8000 --env-file .env llm-agent
```

---

## 📡 API Reference

### `GET /`
Health check endpoint.

**Response:**
```json
{ "message": "LLM Agent is running!" }
```

---

### `POST /chat`
Send a prompt to the active LLM provider.

**Request body:**
```json
{
  "prompt": "Your question here"
}
```

**Response:**
```json
{
  "response": "AI generated response...",
  "provider": "groq"
}
```

---

## 🔑 Getting Free API Keys

| Provider | Link | Free Tier |
|----------|------|-----------|
| Groq | console.groq.com | ✅ Generous free tier |
| Gemini | aistudio.google.com | ✅ Free |
| OpenAI | platform.openai.com | ✅ Trial credits |

---

## 🧠 Key Design Decisions

**Provider Abstraction** — Each provider implements the same `generate(prompt) -> str` interface. The router doesn't care which provider it calls, making it trivial to add new providers.

**Environment-based Switching** — No hardcoded provider logic in the API layer. Switching providers is an ops concern, not a code concern.

**Zero Downtime Switching** — Since providers are swapped via env vars, you can switch providers in production without redeploying code.

---

## 🔮 Roadmap

- [ ] Add conversation memory (multi-turn chat)
- [ ] Add automatic fallback if primary provider fails
- [ ] Add request logging to PostgreSQL
- [ ] Add Redis caching for repeated prompts
- [ ] Deploy to AWS EC2 / Render

---

## 👤 Author

Built by **Sneha** — B.Tech CSE student passionate about backend systems and AI.

---

## 📄 License

MIT License

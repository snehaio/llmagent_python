import os
from dotenv import load_dotenv

load_dotenv()

def get_response(prompt: str) -> dict:
    provider = os.getenv("LLM_PROVIDER", "groq").lower()

    if provider == "groq":
        from app.providers.groq_provider import generate
    elif provider == "gemini":
        from app.providers.gemini import generate
    elif provider == "openai":
        from app.providers.openai import generate
    else:
        return {"response": f"Unknown provider: {provider}", "provider": provider}

    response = generate(prompt)
    return {"response": response, "provider": provider}
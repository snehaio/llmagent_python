from fastapi import FastAPI
from pydantic import BaseModel
from app.agent import get_response

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def root():
    return {"message": "LLM Agent is running!"}

@app.post("/chat")
def chat(request: PromptRequest):
    try:
        result = get_response(request.prompt)
        return result
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e), "details": traceback.format_exc()}
        )
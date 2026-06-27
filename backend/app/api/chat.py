from fastapi import APIRouter
from pydantic import BaseModel

from app.services.ai_service import ask_gemini

router = APIRouter(prefix="/chat", tags=["Chat"])


class AskRequest(BaseModel):
    question: str


@router.post("/")
def chat(request: AskRequest):
    answer = ask_gemini(request.question)

    return {
        "question": request.question,
        "answer": answer,
    }
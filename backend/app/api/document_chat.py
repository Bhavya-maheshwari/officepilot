from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ai_service import ask_gemini
from app.services.document_store import documents
print("Chat sees:", documents.keys())


router = APIRouter(
    prefix="/document-chat",
    tags=["Document Chat"]
)


class Question(BaseModel):
    filename: str
    question: str


@router.post("/")
def ask_document(request: Question):

    if request.filename not in documents:
        return {
            "error": "Document not found"
        }

    document = documents[request.filename]

    prompt = f"""
Answer ONLY using the document below.

DOCUMENT
---------
{document}

QUESTION
---------
{request.question}
"""

    answer = ask_gemini(prompt)

    return {
        "answer": answer
    }
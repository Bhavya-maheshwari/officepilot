from fastapi import FastAPI

from app.api.chat import router as chat_router
from app.api.customers import router as customer_router
from app.api.documents import router as document_router
from app.api.document_chat import router as document_chat_router

app = FastAPI(title="OfficePilot")


@app.get("/")
def root():
    return {"message": "Welcome to OfficePilot!"}


@app.get("/health")
def health():
    return {"status": "healthy"}


app.include_router(chat_router)
app.include_router(customer_router)
app.include_router(document_router)
app.include_router(document_chat_router)
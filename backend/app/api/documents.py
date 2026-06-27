from fastapi import APIRouter, UploadFile, File
import os
import shutil
from app.services.pdf_service import extract_text
from app.services.document_store import documents

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text(filepath)
    print("Before upload:", documents)
    documents[file.filename] = text
    print("After upload:", documents.keys())
    

    return {
        "filename": file.filename,
        "characters": len(text),
        "preview": text[:1000]
    }
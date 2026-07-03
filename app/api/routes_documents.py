from fastapi import APIRouter, UploadFile
from app.rag.ingestion import ingest_documents

router = APIRouter()


@router.post("/ingest")
def ingest(file: UploadFile):
    result = ingest_documents([file])
    return result
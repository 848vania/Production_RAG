from fastapi import FastAPI
from app.api.routes_chat import router as chat_router
from app.api.routes_documents import router as document_router
from app.api.routes_eval import router as eval_router

app = FastAPI(title="Enterprise RAG Assistant")

app.include_router(chat_router, prefix="/chat", tags=["chat"])
app.include_router(document_router, prefix="/documents", tags=["documents"])
app.include_router(eval_router, prefix="/evaluation", tags=["evaluation"])


@app.get("/health")
def health_check():
    return {"status": "ok"}
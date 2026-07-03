from fastapi import APIRouter
from app.schemas import ChatRequest, ChatResponse
from app.rag.pipeline import answer_question

router = APIRouter()


@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):
    return answer_question(request.question)
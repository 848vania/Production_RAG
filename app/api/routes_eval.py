from fastapi import APIRouter
from app.evaluation.run_retrieval_eval import run_retrieval_evaluation

router = APIRouter()


@router.post("/run")
def run_eval():
    return run_retrieval_evaluation()
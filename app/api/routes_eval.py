from fastapi import APIRouter
from app.evaluation.run_eval import run_evaluation

router = APIRouter()


@router.post("/run")
def run_eval():
    return run_evaluation()
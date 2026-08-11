from typing import Any 

from app.database.connection import  SessionLocal, init_db
from app.database.crud import create_query_log


def log_interaction(
        question: str,
        response: dict[str, Any],
        retrieval_type: str | None = None,
        model_provider: str | None = None,
    ) -> None:
    """
    Save one RAG interaction

    This function is intentionally safe:
    logging failure should not crash the user-facing answer
    """
    try:
        init_db()

        db = SessionLocal()

        try:
            print("-"*15, "CREATE QUERY LOG")
            create_query_log(
                db=db,
                question=question,
                answer=response.get("answer", ""),
                sources=response.get("sources", []),
                confidence=response.get("confidence", "low"),
                latency_ms=response.get("latency_ms", 0.0),
                cost_usd=response.get('cost_usd'),
                retrieval_type=response.get('retrieval_type', retrieval_type),
                model_provider=response.get('model_provider', model_provider),
                refused=response.get('refused', False),
                reason=response.get('reason'),
            )
            print("-"*15,"DONE")
        finally:
            db.close()

    except Exception as error:
        print(f"Failed to log interaction: {error}")
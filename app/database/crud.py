import json 
from typing import Any 

from sqlalchemy.orm import Session

from app.database.models import QueryLog


def create_query_log(
        db: Session,
        question: str,
        answer: str,
        sources: list[dict[str, Any]],
        confidence: str,
        latency_ms: float,
        cost_usd: float | None = None,
        retrieval_type: str | None = None,
        model_provider: str | None = None,
        refused: bool = False, 
        reason: str | None = None,
) -> QueryLog:
    """
    Save one query interaction to the databse
    """
    log = QueryLog(
        question = question,
        answer = answer,
        sources_json = json.dumps(sources, ensure_ascii=False),
        confidence = confidence,
        latency_ms = latency_ms,
        cost_usd = cost_usd,
        retrieval_type = retrieval_type,
        model_provider = model_provider,
        refused = refused,
        reason = reason,
    )

    db.add(log)
    db.commit()
    db.refresh(log)

    return log 


def get_recent_query_logs(
        db: Session,
        limit: int = 20,
) -> list[QueryLog]:
    """
    Return the most recent query logs 
    """
    return (
        db.query(QueryLog)
        .order_by(QueryLog.created_at.desc())
        .limit(limit)
        .all()
    )


def get_all_query_logs(db: Session) -> list[QueryLog]:
    """
    Return all query logs 

    This is fine for a small portfolio project 
    For roduction, use pagination
    """
    return db.query(QueryLog).all()


def count_query_logs(db: Session) -> int:
    """
    Return total number of logged queries
    """
    return db.query(QueryLog).count()
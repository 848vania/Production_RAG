import json 
from typing import Any 

from app.database.connection import SessionLocal, init_db
from app.database.crud import get_all_query_logs, get_recent_query_logs


def query_log_to_dict(log) -> dict[str, Any]:
    """
    Convert a QueryLog AQLAlchemy object into a dictionary
    """
    try:
        sources = json.loads(log.sources_json)
    except json.JSONDecodeError:
        sources = []

    return {
        'id': log.id,
        'question': log.question,
        'answer': log.answer,
        'sources': sources,
        'confidence': log.confidence,
        'latency_ms': log.latency_ms,
        'cost_usd': log.cost_usd,
        'retrieval_type': log.retrieval_type,
        'model_provider': log.model_provider,
        'refused': log.refused,
        'reason': log.reason,
        'created_at': log.created_at.isoformat()
        if log.created_at 
        else None,
    }

def average_latency_ms(logs) -> float:
    """
    Calculate average latency
    """
    if not logs:
        return 0.0

    return sum(log.latency_ms or 0.0 for log in logs) / len(logs)


def total_estimated_cost_usd(logs) -> float:
    """
    Calculate total estimated cost
    """
    costs = [
        log.cost_usd 
        for log in logs
        if log.cost_usd is not None
    ]

    if not costs:
        return 0.0

    return sum(costs)


def refusal_rate(logs) -> float:
    """
    Percentage of answers that refused
    """
    if not logs:
        return 0.0 

    refused_count = sum(1 for log in logs if log.refused)

    return refused_count / len(logs)


def low_confidence_rate(logs) -> float:
    """
    Percentage of low-confidence responses
    """
    if not logs:
        return 0.0

    low_count = sum(
        1 for log in logs
        if log.confidence == 'low'
    )

    return low_count / len(logs)


def get_monitoring_summary(
        recent_limit: int = 20,
) -> dict[str, Any]:
    """
    Return monitoring summary for dashboard or API
    """
    init_db()

    db = SessionLocal()

    try:
        all_logs = get_all_query_logs(db)
        recent_logs = get_recent_query_logs(db, limit=recent_limit)

        return {
            'total_queries': len(all_logs),
            'average_latency_ms': average_latency_ms(all_logs),
            'total_estimated_cost_usd': total_estimated_cost_usd(all_logs),
            'refusal_rate': refusal_rate(all_logs),
            'low_confidence_rate': low_confidence_rate(all_logs),
            'recent_queries': [
                query_log_to_dict(log)
                for log in recent_logs
            ],
        }
    finally:
        db.close()
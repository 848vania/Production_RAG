from datetime import datetime, timezone

from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String, Text

from app.database.connection import Base 

class QueryLog(Base):
    __tablename__ = "query_logs"

    id = Column(Integer, primary_key=True, index=True)

    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)

    sources_json = Column(Text, nullable=False, default="[]")

    confidence = Column(String, nullable=False, default="low")
    latency_ms = Column(Float, nullable=False, default=0.0)
    cost_usd = Column(Float, nullable=True)

    retrieval_type = Column(String, nullable=True)
    model_provider = Column(String, nullable=True)

    refused = Column(Boolean, nullable=False, default=False)
    reason = Column(String, nullable=True)

    created_at = Column(
        DateTime,
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )
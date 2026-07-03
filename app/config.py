from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    llm_provider: str = "openai"
    openai_api_key: str | None = None
    anthropic_api_key: str | None = None
    gemini_api_key: str | None = None

    embedding_provider: str = "openai"
    vector_db_provider: str = "qdrant"
    qdrant_url: str = "http://localhost:6333"
    qdrant_collection: str = "enterprise_docs"

    top_k: int = 10
    rerank_top_k: int = 5
    min_retrieval_score: float = 0.35

    database_url: str = "sqlite:///logs.db"

    class Config:
        env_file = ".env"


settings = Settings()
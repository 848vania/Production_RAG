from pydantic_settings import BaseSettings


class Settings_Chat(BaseSettings):
    llm_provider: str = "openai"
    openai_api_key: str | None = None
    anthropic_api_key: str | None = None
    gemini_api_key: str | None = None

    openai_model: str | None = None

    ollama_base_url: str | None = "http://localhost:11434"
    local_model_name: str | None = None

    embedding_provider: str = "openai"
    openai_embedding_model: str | None = None
    local_embedding_model: str | None = None

    vector_db_provider: str = "qdrant"
    qdrant_url: str = "http://localhost:6333"
    qdrant_collection: str = "enterprise_docs"

    database_url: str = "sqlite:///logs.db"

    top_k: int = 10
    rerank_top_k: int = 5
    retrieval_score: float = 0.35
    retrieve_metric: str | None = None

    class Config:
        env_file = ".env"


settings = Settings_Chat()
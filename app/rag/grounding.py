def has_sufficient_context(chunks: list[dict], min_score: float) -> bool:
    """
    Check if retrieved chunks are good enough.
    """


def build_refusal_response(question: str, chunks: list[dict]) -> dict:
    """
    Return standardized refusal answer.
    """


def estimate_confidence(chunks: list[dict]) -> str:
    """
    Return high, medium, or low confidence.
    """


def validate_citations(answer: str, sources: list[dict]) -> bool:
    """
    Basic check that cited sources exist.
    """
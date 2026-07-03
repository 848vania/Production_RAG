def is_answerable(chunks: list[dict]) -> bool:
    if not chunks:
        return False

    best_score = max(chunk["score"] for chunk in chunks)
    return best_score >= settings.min_retrieval_score
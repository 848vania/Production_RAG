def rerank(question: str, chunks: list[dict]):
    """
    If reranker is enabled, reorder chunks.
    Otherwise return top chunks from retriever.
    """
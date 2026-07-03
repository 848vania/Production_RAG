def hybrid_retrieve(question: str, top_k: int = 10):
    vector_results = vector_retrieve(question, top_k)
    keyword_results = keyword_retrieve(question, top_k)

    merged = merge_results(vector_results, keyword_results)
    return sorted(merged, key=lambda x: x.score, reverse=True)
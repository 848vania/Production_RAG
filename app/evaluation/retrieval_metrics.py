def recall_at_k(retrieved_sources, expected_sources, k=5):
    retrieved_top_k = retrieved_sources[:k]
    return int(any(src in retrieved_top_k for src in expected_sources))
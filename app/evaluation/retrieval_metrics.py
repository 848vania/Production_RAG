def extract_source_ids(retrieved_chunks: list[dict]) -> list[str]:
    return [
        f"{chunk.get('metadata', {}).get('doc_id')}::{chunk.get('metadata', {}).get('section')}"
        # f"{chunk.get("metadata", {}).get("doc_id")}::{chunk.get("metadata", {}).get("section_title")}" #TODO: REVIEW THE  SYNTAX OF PARENTEHSUS 
        for chunk in retrieved_chunks
        if chunk.get('metadata', {}).get('doc_id')
    ]


def recall_at_k(retrieved_sources:list[str], expected_sources:list[str], k:int=5) -> float:
    """
    1.0 if any expected sources appears in top_k, else 0.0
    """

    retrieved_top_k = retrieved_sources[:k]
    return int(any(src in retrieved_top_k for src in expected_sources))


def precision_at_k(retrieved_sources:list[str], expected_sources:list[str], k:int) -> float:
    """
    Fraction of top-k retrieved sources that are relevant
    """
    if k <= 0:
        return 0.0

    retrieved_top_k = retrieved_sources[:k]
    expected_set = set(expected_sources)

    # Count how many of the top-k items are expected 
    relevant_retrieved = sum(1 for src in retrieved_top_k if src in expected_set)

    return relevant_retrieved / k


def reciprocal_rank(retrieved_sources:list[str], expected_sources:list[str]) -> float:
    """
    1/rank of first relevant source
    """
    expected_set = set(expected_sources)

    for rank, src in enumerate(retrieved_sources, start=1):
        if src in expected_set:
            return 1.0 / rank

    return 0.0


def mean_reciprocal_rank(scores: list[float]) -> float:
    """
    Average reciprocal rank across all queries
    """
    if not scores:
        return 0.0

    return sum(scores) / len(scores)


def evaluate_retrieval(
        retrieved_chunks: list[dict], 
        eval_item: dict
    ) -> dict:
    """
    Run evaluation metrics
    """

    retrieved_sources = extract_source_ids(retrieved_chunks)
    expected_sources = eval_item['expected_sources']

    return {
        "recall_at_1": recall_at_k(retrieved_sources, expected_sources, k=1),
        "recall_at_3": recall_at_k(retrieved_sources, expected_sources, k=3),
        "recall_at_5": recall_at_k(retrieved_sources, expected_sources, k=5),
        "precision_at_5": precision_at_k(retrieved_sources, expected_sources, k=5),
        "reciprocal_rank": reciprocal_rank(retrieved_sources, expected_sources),
    }
from app.rag.retriever import *
from app.rag.keyword_search import *
from app.rag.chunking import *
from unittest.mock import patch


def test_hybrid_retrieval():
    query = "Which are the available work models?"
    top_k = 10

    results = hybrid_retrieve(query, top_k)

    return results

results = test_hybrid_retrieval()
for resu in results:
    print("*"*15)
    print(resu)


@patch("app.rag.retriever.hybrid_retrieve")
@patch("app.rag.retriever.keyword_retrieve")
@patch("app.rag.retriever.vector_retrieve")
def test_retrieve_dispatch_overrides(mock_vector, mock_keyword, mock_hybrid):
    mock_vector.return_value = ["vector_result"]
    mock_keyword.return_value = ["keyword_result"]
    mock_hybrid.return_value = ["hybrid_result"]

    retrieve("question", retrieval_type="vector", vector_top_k=3)
    assert mock_vector.call_args.kwargs["top_k"] == 3

    retrieve("question", retrieval_type="keyword", keyword_top_k=7)
    assert mock_keyword.call_args.kwargs["top_k"] == 7

    retrieve(
        "question",
        retrieval_type="hybrid",
        hybrid_top_k=4,
        vector_weight=0.3,
        keyword_weight=0.7,
    )
    assert mock_hybrid.call_args.kwargs["top_k"] == 4
    assert mock_hybrid.call_args.kwargs["vector_weight"] == 0.3
    assert mock_hybrid.call_args.kwargs["keyword_weight"] == 0.7


test_retrieve_dispatch_overrides()
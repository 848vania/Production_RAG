from app.rag.reranker import *
from app.rag.retriever import hybrid_retrieve
from app.config import settings

def test_reranker():
    query = "which are the availale work models?"
    top_k = 10

    results = hybrid_retrieve(query, top_k)

    # rerank
    reranker = get_reranker()
    reranked_results = reranker.rerank(
        question = query,
        chunks = results,
        top_k= settings.rerank_top_k
    )
    for reranked_result in reranked_results:
        print("*"*15)
        print(reranked_result)

test_reranker()
from app.rag.retriever import * 
from app.rag.keyword_search import * 
from app.rag.chunking import *


def test_hybrid_retrieval():
    query = "Which are the available work models?"
    top_k = 10

    results = hybrid_retrieve(query, top_k) 

    return results

results = test_hybrid_retrieval()
for resu in results:
    print("*"*15)
    print(resu)
from app.rag.embeddings import * 
from app.rag.vector_store import get_vector_store
from app.rag.chunking import chunk_documents
from app.rag.ingestion import load_documents_from_folder
from app.rag.keyword_search import *

embedding = OpenAIEmbeddingProvider()

docs = load_documents_from_folder("data/synthetic_documents")
chunks = chunk_documents(docs)

# Embed Documents 
texts = [chunk.text for  chunk in chunks]
embeddings = embedding.embed_texts(texts)

def vector_retrieve(question: str, top_k: int=5):
    """
    Embed the question and return top-k vector search results
    """
    vector_store = get_vector_store()
    vector_store.upsert_chunks(chunks, embeddings)

    embedded_query = embedding.embed_query(question)
    results = vector_store.search(query_embedding=embedded_query, top_k=top_k)

    results = format_retrieved_context(results)

    return results


def format_retrieved_context(results: dict) -> str:
    """
    Convert retrieved chunks with relevant information
    """

    # Dict 
    # ids: List[IDs]
    # embeddings: Optional[List[Embeddings]]
    # documents: Optional[List[List[Document]]]
    # uris: Optional[List[List[URI]]]
    # metadatas: Optional[List[List[Metadata]]]
    # distances: Optional[List[List[float]]] # SCORES
    # included: Include 

    ids = results['ids'][0]
    documents = results['documents'][0]
    distances = results['distances'][0]
    metadatas = results['metadatas'][0]

    context = []
    for id, document, distance, metadata_raw in zip(ids, documents, distances, metadatas):
        metadata = {
            'document': metadata_raw['doc_title'],
            'section': metadata_raw['section_title'],
            'doc_id': metadata_raw['doc_id']
        }
        result = {
            'chunk_id': id,
            'text': document,
            'score': distance,
            'metadata': metadata
        }
        context.append(result)

    return context


def merge_results(
    vector_results: list[dict],
    keyword_results: list[dict],
    vector_weight: float=0.6,
    keyword_weight: float=0.4,
    ) -> list[dict]:
    """
    Merge vector and keyword results by chunk_id.
    """
    vector_ids = [vector_result['chunk_id'] for vector_result in vector_results]
    keyword_ids = [keyword_result['chunk_id'] for keyword_result in keyword_results]

    final_results = []
    done_ids = []
    for i, vector_id in enumerate(vector_ids):
        vector_result = vector_results[i]
        vector_result['retrieval_method'] = 'vector'
        if vector_id in keyword_ids:

            k_idx = keyword_ids.index(vector_id)
            done_ids.append(vector_id)
            
            keyword_result = keyword_results[k_idx]    

            final_score = vector_weight * vector_result['score'] + keyword_weight * keyword_result['score']

            vector_result['vector_score'] = vector_result['score']
            vector_result['keyword_score'] = keyword_result['score']
            vector_result['score'] = final_score
            vector_result['retrieval_method'] = 'hybrid'
            
        final_results.append(vector_result)

    for keyword_id, keyword_result in zip(keyword_ids, keyword_results):
        if keyword_id not in done_ids:
            keyword_result['retrieval_method'] = 'keyword'            
            final_results.append(keyword_result)

    return final_results


def hybrid_retrieve(question: str, top_k:int=10, vector_weight: float = 0.6, keyword_weight: float = 0.4) -> list[dict]:
    """
    Return top-k merged retrieval results
    """
    vector_results = vector_retrieve(question, top_k)

    build_bm25_index(chunks)
    keyword_results = keyword_retrieve(question, top_k)

    results = merge_results(vector_results, keyword_results, vector_weight=vector_weight, keyword_weight=keyword_weight)

    results.sort(key=lambda x: x['score'], reverse = True)

    return results[:top_k]

def retrieve(question:str) -> list[dict]:
    retrieval_type = settings.retrieval_type.lower()

    if retrieval_type == 'vector':
        return vector_retrieve(question, top_k = settings.vector_top_k)

    elif retrieval_type == 'keyword':
        return keyword_retrieve(question, top_k=settings.keyword_top_k)

    elif retrieval_type == 'hybrid':
        return hybrid_retrieve(
            question= question,
            top_k = settings.hybrid_top_k,
            vector_weight= settings.vector_weight,
            keyword_weight= settings.keyword_weight
        )

    else:
        raise ValueError(f"Unsupported retrieval type: {settings.retrieval_type}")
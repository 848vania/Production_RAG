from app.rag.embeddings import * 
from app.rag.vector_store import get_vector_store
from app.rag.chunking import chunk_documents
from app.rag.ingestion import load_documents_from_folder

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

    return results


def format_retrieved_context(results: dict) -> str:
    """
    Convert retrieved chunks into a context block for the LLM
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
            'section': metadata_raw['section_title']
        }
        result = {
            'chunk_id': id,
            'text': document,
            'score': distance,
            'metadata': metadata
        }
        context.append(result)

    return context

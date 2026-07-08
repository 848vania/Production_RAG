from app.rag.ingestion import load_documents_from_folder
from app.rag.chunking import chunk_documents
from app.rag.embeddings import *
from app.rag.vector_store import * 

def test_vector_store_return_results():
    store = ChromaVectorStore()
    chunks = ["...", "..."]
    embeddings = [[0.1, 0.2], [0.9, 0.8]]

    store.upsert_chunks(chunks, embeddings)
    results = store.search([0.1, 0.2], top_k=2)

    print(f"Results:\n{results}")

    assert len(results) == 1 
    assert "text" in results[0]


def test_synthetic_data():
    vector_store = ChromaVectorStore()
    embedding = OpenAIEmbeddingProvider()

    # Chunk Documents
    docs = load_documents_from_folder("data/synthetic_documents")[:2]
    chunks = chunk_documents(docs)

    # Embed Documents
    texts = [chunk.text for chunk in chunks]
    embeddings = embedding.embed_texts(texts)

    print("+"*15)
    print(f"Chunks: {chunks}")
    print("-"*15)
    print(f"Texts:\n{texts}")
    print("*"*15)
    print(f"Embeddings:\n{embeddings}")

    # Add to Vector Store  
    vector_store.upsert_chunks(chunks, embeddings)
    query = "What is the definition of personal data"
    embedded_query = embedding.embed_query(query)
    results = vector_store.search(embedded_query)
    print("RESULTS:")
    print(results)

# Uncomment for testing
# test_vector_store_return_results()
test_synthetic_data()
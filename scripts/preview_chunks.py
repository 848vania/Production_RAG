from app.rag.ingestion import load_documents_from_folder
from app.rag.chunking import chunk_documents

docs= load_documents_from_folder("data/synthetic_documents")
chunks= chunk_documents(docs)

print(f"Documents:{len(docs)}")
print(f"Chunks:{len(chunks)}")

for chunk in chunks[:5]:
    print("------")
    print(chunk.chunk_id)
    print(chunk.metadata)
    print(chunk.text[:300])
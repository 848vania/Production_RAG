from app.rag.ingestion import load_documents_from_folder

docs = load_documents_from_folder()

print(f"Loaded {len(docs)} documents")

for doc in docs:
    print("------")
    print(doc.doc_id)
    print(doc.source_path)
    print(len(doc.text))
    print(doc.metadata)
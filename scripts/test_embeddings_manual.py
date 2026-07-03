from app.rag.embeddings import * 

texts= ["Remote work requires manager approval.","Expenses over $500 require pre-approval."]
query = "Who approves remote work?"

embedding = OpenAIEmbeddingProvider()

vector_texts = embedding.embed_texts(texts)
print(f"Vectors:\n{vector_texts}")

vector_query = embedding.embed_query(query)
print(f"Query:\n{vector_query}")
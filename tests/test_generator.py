# Local libraries 
from app.rag.providers import * 
from app.rag.generator import * 
from app.rag.vector_store import * 
from app.rag.retriever import *

from dotenv import load_dotenv
import os 

# LLM_PROVIDER = "testing"

# Define variables 
vector_store = ChromaVectorStore()
embedding = OpenAIEmbeddingProvider()


# Loading documents 

docs = load_documents_from_folder("data/synthetic_documents")[:2]
chunks = chunk_documents(docs)

# Embeding documents 

texts = [chunk.text for chunk in chunks]
embeddings = embedding.embed_texts(texts)

# Adding to vector store 

vector_store.upsert_chunks(chunks, embeddings)
query = "What is the definition of personal data"

# Get context
embedding_query = embedding.embed_query(query)
results = vector_store.search(embedding_query)
results = format_retrieved_context(results)

# get response 
response = generate_answer(query, results)


print(response)
from app.rag.retriever import *

question = "Who approves remote work requests?"
results = vector_retrieve(question, top_k=5)
context = format_retrieved_context(results)


for result in context: 
    print("------")
    print(result["score"])
    print(result["metadata"])
    print(result["text"][:350])
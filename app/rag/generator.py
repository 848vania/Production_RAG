from app.rag.providers import *

llm_model = get_llm_provider()

def build_context_block(chunks: list[dict]) -> str:
    """
    Format chunks with source labels
    """

    context = ""
    for i, chunk in enumerate(chunks):
        context += f"[Source {chunk['chunk_id']}]"
        context += f"\nDocument: {chunk['metadata']['document']}"
        context += f"\nSection: {chunk['metadata']['section']}"
        context += f"\nText: {chunk['text']}\n\n"

    return context

def build_rag_prompt(question: str, chunks: list[dict]) -> str:
    """
    Build strict context-only RAG prompt
    """

    context = build_context_block(chunks)

    prompt = f"""You are an enterprise knowledge assistant.
    Answer the user's question using only the provided context. 
    
    Rules:
    1. Use only the context below.
    2. Do not invent facts.
    3. Answer the question and cite the source ID for every factual claim. 
    4. If the context is insufficient, say: 
        'I do not have enough information in the provided documents to answer the question.'
    5. Be concise and clear. 

    Question:
    {question}

    Context: 
    {context}

    Answer:
    """
    return prompt

def generate_answer(question:str, chunks: list[dict]) -> dict:
    """
    Generate answer using LLM and return answer + sources
    """
    query = build_rag_prompt(question, chunks)
    response = llm_model.generate(query)
    response = llm_model.format_response()

    return response 
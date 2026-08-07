from app.rag.providers import *
from app.rag.grounding import format_sources_from_chunks

llm = get_llm_provider()

def build_context_block(chunks: list[dict]) -> str:
    """
    Format chunks with source labels
    """

    context = ""
    for i, chunk in enumerate(chunks):
        context += f"[Source {chunk['chunk_id']}]"
        context += f"\nDocument: {chunk['document']}"
        context += f"\nSection: {chunk['section']}"
        context += f"\nText: {chunk['text']}\n\n"

    return context

def build_rag_prompt(question: str, context) -> str:
    """
    Build strict context-only RAG prompt
    """

    prompt = f"""You are an enterprise knowledge assistant.
    Answer the user's question using only the provided context. 
    
    Rules:
    1. Use only the context below.
    2. Do not invent facts.
    3. Answer the question and cite the source ID for every factual claim as [Source source_number]. 
    4. If the context is insufficient, say: 
        'I do not have enough information in the provided documents to answer the question.'
    6. Be concise and clear. 

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
    sources = format_sources_from_chunks(chunks)
    context = build_context_block(sources)
    prompt = build_rag_prompt(question, context)

    answer = llm.generate(prompt)
    answer = llm.format_response()
    cost = llm.calculate_cost()

    return {
        'answer': answer,
        'sources': sources,
        'cost_usd': cost,
    }
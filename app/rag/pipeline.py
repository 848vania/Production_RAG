import time 

from app.config import settings
from app.rag.retriever import retrieve 
from app.rag.generator import generate_answer
from app.rag.grounding import (
    has_sufficient_context,
    estimate_confidence,
    build_refusal_response,
    validate_citations,
    build_invalid_citation_response
)
from app.rag.reranker import *
from app.schemas import *

def _latency_ms(start_time:float) -> float:
    return round((time.perf_counter() - start_time) * 1000, 2)

def answer_question(question: str) -> dict:
    """
    Full RAG pipeline.
    
    Steps:
    1. Retrieve relevant chunks
    2. Refuse if context is weak.
    3. Generate cited answer.
    4. Validate citations.
    5. Return final response
    """
    start_time = time.perf_counter()

    cleaned_question = question.strip()

    if not cleaned_question:
        return {
            "answer": "Please provide a question.",
            "sources": [],
            "confidence": "low",
            "latency_ms": _latency_ms(start_time),
            "refused": True,
            "reason": "empty question",
            'cost_usd': 0.0
        }
    
    retrieved_chunks = retrieve(
        cleaned_question
    )

    if settings.reranker_enabled:
        reranker = get_reranker()
        retrieved_chunks = reranker.rerank(
            question = cleaned_question,
            chunks = retrieved_chunks,
            top_k= settings.rerank_top_k
        )

    if not has_sufficient_context(
        chunks = retrieved_chunks,
        score_limit = settings.retrieval_score
    ):
        return build_refusal_response(
            question=cleaned_question,
            chunks=retrieved_chunks,
            latency_ms = _latency_ms(start_time),
        )
    
    confidence = estimate_confidence(retrieved_chunks)

    generation_result = generate_answer(
        question=cleaned_question,
        chunks = retrieved_chunks
    )

    answer = generation_result['answer']
    sources = generation_result['sources']
    cost_usd = generation_result['cost_usd']

    citations_are_valid = validate_citations(
        answer = answer,
        sources = sources,
    )

    if not citations_are_valid:
        return build_invalid_citation_response(
            question = cleaned_question,
            chunks = retrieved_chunks,
            latency_ms= _latency_ms(start_time),
        )
    
    return {
        'answer': answer,
        'sources': sources,
        'confidence': confidence,
        'latency_ms': _latency_ms(start_time),
        'refused': False,
        'reason': None,
        'cost_usd': cost_usd,
    }


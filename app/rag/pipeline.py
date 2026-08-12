import time 

from app.config import settings
from app.rag.retriever import retrieve 
from app.rag.generator import generate_answer
from app.monitoring.logger import log_interaction
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


def _with_metadata(response:dict, config=None) -> dict:
    """
    Add shared metadata to all pipeline responses
    """
    retrieval_type = (
        config.retrieval.type
        if config is not None
        else settings.retrieval_type
    )

    model_provider = (
        config.generation.provider
        if config is not None 
        else settings.llm_provider
    )

    response['retrieval_type'] = retrieval_type
    response['model_provider'] = model_provider

    return response


def answer_question(
        question: str,
        config = None,
        log: bool = True,
) -> dict:
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
        response = {
            "answer": "Please provide a question.",
            "sources": [],
            "confidence": "low",
            "latency_ms": _latency_ms(start_time),
            "refused": True,
            "reason": "empty question",
            'cost_usd': 0.0
        }

        response = _with_metadata(response=response, config=config)

        if log:
            log_interaction(cleaned_question, response)

        return response
    
    if config is not None:
        retrieved_chunks = retrieve(
            cleaned_question,
            retrieval_type=config.retrieval.type,
            vector_top_k=config.retrieval.top_k,
            keyword_top_k=config.retrieval.top_k,
            hybrid_top_k=config.retrieval.top_k,
            vector_weight=config.retrieval.vector_weight,
            keyword_weight=config.retrieval.keyword_weight,
        )
    else:
        retrieved_chunks = retrieve(cleaned_question)

    reranker_enabled = config.reranker.enabled if config is not None else settings.reranker_enabled
    reranker_top_k = config.reranker.top_k if config is not None else settings.rerank_top_k

    if reranker_enabled:
        reranker = get_reranker()
        retrieved_chunks = reranker.rerank(
            question = cleaned_question,
            chunks = retrieved_chunks,
            top_k= reranker_top_k
        )

    if not has_sufficient_context(
        chunks = retrieved_chunks,
        score_limit = settings.retrieval_score
    ):
        response = build_refusal_response(
            question=cleaned_question,
            chunks=retrieved_chunks,
            latency_ms = _latency_ms(start_time),
        )

        response = _with_metadata(response, config=config)

        if log:
            log_interaction(cleaned_question, response)

        return response
    
    confidence = estimate_confidence(retrieved_chunks)

    generation_result = generate_answer(
        question=cleaned_question,
        chunks = retrieved_chunks,
        config = config,
    )

    answer = generation_result['answer']
    sources = generation_result['sources']
    cost_usd = generation_result['cost_usd']

    citations_are_valid = validate_citations(
        answer = answer,
        sources = sources,
    )

    if not citations_are_valid:
        response = build_invalid_citation_response(
            question = cleaned_question,
            chunks = retrieved_chunks,
            latency_ms= _latency_ms(start_time),
        )

        response = _with_metadata(response, config=config)

        if log:
            log_interaction(cleaned_question, response)

        return response
    
    response = {
        'answer': answer,
        'sources': sources,
        'confidence': confidence,
        'latency_ms': _latency_ms(start_time),
        'refused': False,
        'reason': None,
        'cost_usd': cost_usd,
    }

    response = _with_metadata(response, config=config)

    if log:
        log_interaction(cleaned_question, response)

    return response
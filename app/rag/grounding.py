import os 
import re
from app.schemas import *

"""
Retrieval Score for L2:
"""


def has_sufficient_context(chunks: list[dict], score_limit: float=0.8) -> bool:
    """
    Check if retrieved chunks are good enough.
    """
    # DICT format
    # {
    #   chunk_id: str
    #   text: str
    #   score: int
    #   metadata: {document: str, section: str}
    # }
    if not chunks:
        return False

    best_score = chunks[0].get('score', 10.0)

    return best_score <= score_limit

def build_refusal_response(question: str, chunks: list[dict], latency_ms: float) -> dict:
    """
    Return standardized refusal when there is not enough context
    """

    return {
        "answer": (
            "I do not have enough information in the provided documents "
            "to answer this question."
        ),
        "sources": [],
        "confidence": "low",
        "latency_ms": latency_ms,
        "refused": True,
        "reason": "insufficient_retrieved_context",
    }

def extract_cited_source_numbers(answer: str) -> list[int]:
    """
    Extract citations like [Source 1], [Source 2] from the answer.
    """
    matches = re.findall(r"[\[(]Source\s+(\d+)[\])]", answer)
    return [int(match) for match in matches]


def estimate_confidence(chunks: list[dict]) -> str:
    """
    Return high, medium, or low confidence.
    """
    if not chunks:
        return "low"
    
    best_score = chunks[0]['score']

    if best_score <= 1:
        return "high"
    if best_score > 1:
        return "medium"
    
    return "low"


def validate_citations(answer: str, sources: list) -> bool:
    """
    Check whether the answer cites only available sources 
    """
    cited_numbers = extract_cited_source_numbers(answer)

    if not cited_numbers:
        return False
    
    valid_numbers = {
        source.get("chunk_id")
        for source in sources
    }

    return all(str(number) in valid_numbers for number in cited_numbers)


def build_invalid_citation_response(
        question: str, 
        chunks: list[dict],
        latency_ms: float,
    ):
    """
    Return safe response when generated answer has invalid or missing citations.
    """
    return {
        "answer": (
            "I found potentially relevant information, but I could not generate "
            "a properly cited answer from the provided documents."
        ),
        "sources": format_sources_from_chunks(chunks),
        "confidence": "low",
        "latency_ms": latency_ms,
        "refused": True,
        "reason": "invalid_or_missing_citations",
    }
    

def format_sources_from_chunks(chunks: list[dict]):
    sources = []

    for index, chunk in enumerate(chunks, start=1):
        metadata = chunk.get('metadata', {})

        sources.append(
            {
                "source_number": index,
                "chunk_id": chunk.get('chunk_id'),
                'document': metadata.get('document'),
                'section': metadata.get('section'),
                'score': chunk.get('score'), 
                'text': chunk.get('text'),
            }
        )
    return sources 
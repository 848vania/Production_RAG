import os 
from app.schemas import *

RETRIEVE_METRIC = os.getenv("RETRIEVE_METRIC")
RETRIEVAL_SCORE = os.getenv('RETRIEVAL_SCORE')

"""
Retrieval Score for L2:
"""


def has_sufficient_context(chunks: list[dict], score_limit: float=RETRIEVAL_SCORE) -> bool:
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
    best_score = chunks[0].get('score', 10.0)

    return best_score <= score_limit

def build_refusal_response(question: str, chunks: list[dict]) -> dict:
    """
    Return standardized refusal answer.
    """
    response = OpenAISources(
        answer = "I do not have enough information in the provided documents to answer this question",
        document = [],
        section = [],
        chunk_id= []
    )
    return response 


def estimate_confidence(chunks: list[dict]) -> str:
    """
    Return high, medium, or low confidence.
    """
    if not chunks:
        return "low"
    
    best_score = chunks[0]['score']

    if best_score <= 1:
        return "high"
    if best_score >= 1:
        return "medium"
    
    return "low"


def validate_citations(answer, chunks: list[dict]) -> bool:
    """
    Basic check that cited sources exist.
    """
    for chunk in chunks: 
        if answer.chunk_id == chunk['chunk_id']:
            if answer.document == chunk['metadata']['document']:
                if answer.section == chunk['metadata']['section_title']:             
                    return True
            else:
                print("WARNING: The chunk ID does NOT match the document and section information:\n{chunk}")
                return False
        
    return False 

def build_invalid_citation_response(
        question: str, 
        chunks: list[dict],
        latency_ms: float,
    ):
    response = OpenAISources(
            answer = "I found potentially relevant information, but I could not generate a properly cited answer from the provided documents.",
            document = [],
            section = [],
            chunk_id= []
        )
    return response 

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
                'score': chunk.get('score'), # TODO: ADD SCORE TO THE build_context_nlock from generator.py
                'text': chunk.get('text'),
            }
        )
    return sources 
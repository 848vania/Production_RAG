import numpy as np
from sentence_transformers import CrossEncoder

from app.config import settings

class Reranker:
    def rerank(self, question:str, chunks:list[dict], top_k:int=5) -> list[dict]:
        raise NotImplementedError


class SimpleReranker(Reranker):
    def rerank(self, question:str, chunks:list[dict], top_k:int=5) -> list[dict]:
        """
        Fallback: return chunks sorted by current score
        """
        # Sort chunks based on their existing 'score' key. Default to 0.0 if missing.
        sorted_chunks = sorted(chunks, key=lambda x:x.get("score", 0.0), reverse = True)
        return sorted_chunks[:top_k]

class LocalCrossEncoderReranker(Reranker):
    def __init__(self, model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2"):
        """
        Initializes a local open-sourcec cross-encoder model.
        """
        self.model = CrossEncoder(model_name)


    def rerank(self, question:str, chunks:list[dict], top_k:int=5) -> list[dict]:
        """
        Optional local reranker
        """
        if not chunks:
            return []

        # Prepare sentence pairs for the cross-encoder
        # Assumes chunks contain a 'text' or 'content' key 
        pairs = [[question, chunk.get('text')] for chunk in chunks]

        # Predict scores (higher means more relevant)
        scores = self.model.predict(pairs)

        # Attach the new reranked score to each chunk 
        for idx, score in enumerate(scores):
            chunks[idx]['rerank_score'] = float(score)

        # Sort chunks by the new cross-encoder score descending 
        reranked_chunks = sorted(chunks, key=lambda x:x['rerank_score'], reverse=True)

        return reranked_chunks[:top_k]


def get_reranker() -> Reranker:
    """
    Return  configured reranker
    """
    reranker_type = settings.reranker_type.lower()

    if reranker_type == 'simple':
        return SimpleReranker()
    elif reranker_type == 'cross-encoder':
        return LocalCrossEncoderReranker()
    else:
        raise ValueError(f"Unsupported reranker type: {settings.reranker_type}")
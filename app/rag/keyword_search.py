from rank_bm25 import BM25Okapi

import pickle 
import numpy as np

def build_bm25_index(chunks: list):
    """
    Tokenixe chunks, build the BM25 index, and saves it along with original text
    """

    tokenized_corpus = [chunk.text.lower().split() for chunk in chunks]

    bm25 = BM25Okapi(tokenized_corpus)

    # Bundle index and original chunks together
    index_data = {
        "bm25": bm25,
        "chunks": chunks
    }

    # Save to a local binary file 
    with open("bm25_index.pkl", "wb") as f:
        pickle.dump(index_data, f)

    print(f"Successfully indexed {len(chunks)} chunks.")


def keyword_retrieve(question:str, top_k:int=5) -> list[dict]:
    """
    Loads the index, scores the question, and returns the top K matching chunks
    """

    # Load index data 
    with open("bm25_index.pkl", "rb") as f:
        index_data = pickle.load(f)

    bm25 = index_data["bm25"]
    chunks = index_data["chunks"]

    # Tokenize query
    tokenized_query = question.lower().split()

    if not tokenized_query:
        return []

    # Get scores for all chunks 
    scores = bm25.get_scores(tokenized_query)

    scores = min_max_normalize(scores)

    # Pair chunks with scores and sort in descending order 
    scored_chunks = [
        {
            "chunk": chunk, 
            "score": float(score)
        }
        for chunk,score in zip(chunks, scores)
    ]
    scored_chunks.sort(key=lambda x: x['score'], reverse = True)

    retrieved_chunks = []
    for scored_chunk in scored_chunks[:top_k]:
        score = scored_chunk['score']
        chunk = scored_chunk['chunk']
        retrieved_chunks.append(
            {
                "chunk_id": chunk.chunk_id,
                "text": chunk.text,
                "score": score,
                "metadata":{
                    "document": chunk.doc_id,
                    "section": chunk.section_title
                }
            }
        )

    return retrieved_chunks


def min_max_normalize(scores):
    min_score = min(scores)
    max_score = max(scores)

    # Avoid division by Zero if all scores are identical 
    if max_score == min_score:
        normalized_scores = [0.0 for _ in scores]

    else:
        normalized_scores = [float((s - min_score) / (max_score)) for s in scores]

    return normalized_scores
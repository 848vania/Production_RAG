import json
from pathlib import Path

from app.evaluation.retrieval_metrics import evaluate_retrieval, extract_source_ids
from app.evaluation.eval_dataset import load_eval_dataset
from app.rag.retriever import retrieve
from app.config import settings
from app.rag.reranker import *

RESULTS_DIR = Path('data/results')
RESULTS_DIR.mkdir(parents=True, exist_ok=True)


def save_results(results: list[dict]) -> None:
    output_path = RESULTS_DIR / "retrieval_eval_results.json"

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(results, file, indent=2, ensure_ascii=False)


def summarize_retrieval_results(results: list[dict]) -> dict:
    if not results:
        return {}

    metric_names = [
        'recall_at_1',
        'recall_at_3',
        'recall_at_5',
        'precision_at_5',
        'reciprocal_rank',
    ]

    summary = {
        'total_questions': len(results),
    }

    for metric in metric_names:
        summary[metric] = sum(
            item['retrieval'][metric]
            for item in results
        ) / len(results)

    output_path = RESULTS_DIR / 'retrieval_eval_summart.json'

    with output_path.open('w', encoding='utf-8') as file:
        json.dump(summary, file, indent=2, ensure_ascii=False)

    return summary
    

def run_retrieval_evaluation() -> dict:
    dataset = load_eval_dataset()
    results = []

    for item in dataset:
        retrieved_chunks = retrieve(item["question"])

        if settings.reranker_enabled:
            reranker = get_reranker()
            retrieved_chunks = reranker.rerank(
                question = item['question'],
                chunks = retrieved_chunks,
                top_k = settings.rerank_top_k
            )

        retrieved_sources = extract_source_ids(retrieved_chunks)

        retrieval_scores = evaluate_retrieval(
            retrieved_chunks = retrieved_chunks, 
            eval_item = item,
        )

        results.append({
            "question_id": item["id"],
            "question": item['question'],
            'answerable': item['answerable'],
            'expected_sources': item['expected_sources'],
            "retrieved_sources": retrieved_sources,
            'retrieved_chunks':[
                {
                    'chunk_id': chunk.get('chunk_id'),
                    'score': chunk.get('score'),
                    'source_id': chunk.get('metadata', {}).get('source_id'),
                    'document': chunk.get('metadata', {}).get('document'),
                    'section': chunk.get('metadata', {}).get('section')
                }
                for chunk in retrieved_chunks
            ],
            'retrieval': retrieval_scores,
        })

    save_results(results)
    return summarize_retrieval_results(results)

# if __name__ == "__main__":
#     summary = run_retrieval_evaluation()
#     print(json.dumps(summary, indent=2))
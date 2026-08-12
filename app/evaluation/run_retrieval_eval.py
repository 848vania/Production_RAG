import json
from pathlib import Path

from app.evaluation.retrieval_metrics import evaluate_retrieval, extract_chunk_ids
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

    output_path = RESULTS_DIR / 'retrieval_eval_summary.json'

    with output_path.open('w', encoding='utf-8') as file:
        json.dump(summary, file, indent=2, ensure_ascii=False)

    return summary
    

def run_retrieval_evaluation(
        save: bool = True,
        output_suffix: str | None = None,
        config = None,
    ) -> dict:
    dataset = load_eval_dataset()
    results = []

    for item in dataset:
        if config is not None:
            retrieved_chunks = retrieve(
                item["question"],
                retrieval_type=config.retrieval.type,
                vector_top_k=config.retrieval.top_k,
                keyword_top_k=config.retrieval.top_k,
                hybrid_top_k=config.retrieval.top_k,
                vector_weight=config.retrieval.vector_weight,
                keyword_weight=config.retrieval.keyword_weight,
            )
        else:
            retrieved_chunks = retrieve(item["question"])

        reranker_enabled = config.reranker.enabled if config is not None else settings.reranker_enabled
        reranker_top_k = config.reranker.top_k if config is not None else settings.rerank_top_k

        if reranker_enabled:
            reranker = get_reranker()
            retrieved_chunks = reranker.rerank(
                question = item['question'],
                chunks = retrieved_chunks,
                top_k = reranker_top_k
            )

        retrieved_sources = extract_chunk_ids(retrieved_chunks)

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
                    'doc_id': chunk.get('metadata', {}).get('doc_id'),
                    'document': chunk.get('metadata', {}).get('document'),
                    'section': chunk.get('metadata', {}).get('section')
                }
                for chunk in retrieved_chunks
            ],
            'retrieval': retrieval_scores,
        })

    summary = summarize_retrieval_results(results)

    if save:
        suffix = f"_{output_suffix}" if output_suffix else ""
        save_json(results, RESULTS_DIR / f'retrieval_eval_results{suffix}.json')
        save_json(summary, RESULTS_DIR / f'retrieval_eval_summary{suffix}.json')

    return {
        'summary': summary,
        'results': results
    }

def save_json(data: dict| list, output_path: Path) -> None:
    """
    Save JSON output.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open('w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
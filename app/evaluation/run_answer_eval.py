import json 
from pathlib import Path 

from app.evaluation.answer_metrics import *
from app.evaluation.eval_dataset import load_eval_dataset
from app.rag.pipeline import answer_question
from app.rag.grounding import filter_cited_sources


RESULTS_DIR = Path('data/results')
RESULTS_DIR.mkdir(parents=True, exist_ok= True)


def save_results(results: list[dict]) -> None:
    output_path = RESULTS_DIR / 'answer_eval_results.json'

    with output_path.open('w', encoding='utf-8') as file:
        json.dump(results, file, indent=2, ensure_ascii=False)


def summarize_answer_results(results: list[dict]) -> dict:
    if not results:
        return {
            'total_questions': 0.0,
            'citation_accuracy': 0.0,
            'refusal_accuracy': 0.0,
            'answer_correctness': 0.0,
            'average_latency_ms': 0.0
        }

    metric_names = [
        'citation_accuracy',
        'refusal_accuracy',
        'answer_correctness'
    ]

    summary = {
        'total_questions': len(results),
    }

    for metric in metric_names:
        summary[metric] = sum(
            item['answer_scores'][metric]
            for item in results
        ) / len(results)

    summary['average_latency_ms'] = sum(item.get('latency_ms', 0.0) for item in results) / len(results)

    costs = [
        item.get('cost_usd')
        for item in results
    ]

    summary['average_cost_usd'] = sum(costs) / len(costs) if costs else None

    # output_path = RESULTS_DIR / 'answer_eval_summary.json'

    # with output_path.open('w', encoding='utf-8') as file:
    #     json.dump(summary, file, indent=2, ensure_ascii=False)

    return summary


def run_answer_evaluation(
        save: bool = True,
        config = None,
        output_suffix: str | None = None,
    ) -> dict:
    dataset = load_eval_dataset()
    results = []

    for item in dataset:
        response = answer_question(
            question = item['question'],
            config=config,
            log = False
        )

        cited_sources = filter_cited_sources(response['answer'], response['sources'])
        retrieved_sources = extract_source_ids(cited_sources)

        answer_scores = evaluate_answers(
            predicted_answer= response['answer'],
            predicted_sources= retrieved_sources,
            eval_item= item
        )

        results.append({
            'question_id': item['id'],
            'question': item['question'],
            'predicted_answer': response['answer'],
            'expected_answer': item['expected_answer'],
            'confidence': response['confidence'],
            'latency_ms': response['latency_ms'],
            'refused': response['refused'],
            'reason': response['reason'],
            'cost_usd': response['cost_usd'],
            'answerable': item['answerable'],
            'expected_sources': item['expected_sources'],
            'retrieved_sources': retrieved_sources,
            'retrieved_chunks': response['sources'],
            'answer_scores': answer_scores
        })

    summary = summarize_answer_results(results)

    if save:
        suffix = f"_{output_suffix}" if output_suffix else ""
        save_json(results, RESULTS_DIR / f'answer_eval_results{suffix}.json')
        save_json(summary, RESULTS_DIR / f'answer_eval_summary{suffix}.json')

    return {
        'summary': summary,
        'results': results,
    }


def save_json(data: dict | list, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open('w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
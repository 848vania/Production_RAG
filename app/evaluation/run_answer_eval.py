import json 
from pathlib import Path 

from app.evaluation.answer_metrics import *
from app.evaluation.eval_dataset import load_eval_dataset
from app.rag.pipeline import answer_question


RESULTS_DIR = Path('data/results')
RESULTS_DIR.mkdir(parents=True, exist_ok= True)


def save_results(results: list[dict]) -> None:
    output_path = RESULTS_DIR / 'answer_eval_results.json'

    with output_path.open('w', encoding='utf-8') as file:
        json.dump(results, file, indent=2, ensure_ascii=False)


def summarize_answer_results(results: list[dict]) -> dict:
    if not results:
        return {}

    metric_names = [
        'citation_accuracy',
        'refusal_accuracy',
        'answer_correctness_simple'
    ]

    summary = {
        'total_questions': len(results),
    }

    for metric in metric_names:
        summary[metric] = sum(
            item['answer_scores'][metric]
            for item in results
        ) / len(results)

    output_path = RESULTS_DIR / 'answer_eval_summary.json'

    with output_path.open('w', encoding='utf-8') as file:
        json.dump(summary, file, indent=2, ensure_ascii=False)

    return summary


def run_answer_evaluation() -> dict:
    dataset = load_eval_dataset()
    results = []

    for item in dataset[:10]:
        response = answer_question(item['question'])

        retrieved_sources = extract_source_ids(response['sources'])

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
            'answerable': item['answerable'],
            'expected_sources': item['expected_sources'],
            'retrieved_sources': retrieved_sources,
            'retrieved_chunks': response['sources'],
            'answer_scores': answer_scores
        })

    save_results(results)
    return summarize_answer_results(results)
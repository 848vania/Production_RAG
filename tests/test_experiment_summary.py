from app.evaluation.experiment_summary import (
    flatten_experiment_result,
    build_markdown_table,
)


def test_flatten_experiment_result():
    result = {
        'experiment_name': 'hybrid',
        'config': {
            'retrieval': {
                'type': 'hybrid',
                'top_k': 10,
                'vector_weight': 0.6,
                'keyword_weight': 0.4,
            },
            'reranker': {
                'enabled': False,
            },
        },
        'retrieval': {
            'recall_at_1': 0.7,
            'recall_at_3': 0.8,
            'recall_at_5': 0.9,
            'precision_at_5': 0.4,
            'reciprocal_rank': 0.75
        },
        'answer': {
            'citation_accuracy': 0.85,
            'refusal_accuracy': 0.9,
            'answer_correctness': 0.8,
            'average_latency_ms': 2000,
            'average_cost_usd': 0.003,
        },
    }

    row = flatten_experiment_result(result)

    assert row['experiment_name'] == 'hybrid'
    assert row['retrieval_type'] == 'hybrid'
    assert row['recall_at_5'] == 0.9


def test_build_markdown_table():
    rows = [
        {
            'experiment_name': 'hybrid',
            'retrieval_type': 'hybrid',
            'reranker_enabled': False,
            'recall_at_5': 0.9,
            'reciprocal_rank': 0.75,
            'citation_accuracy': 0.85,
            'refusal_accuracy': 0.9,
            'answer_correctness': 0.8,
            'average_latency_ms': 2000,
        }
    ]

    markdown = build_markdown_table(rows)

    assert "| Experiment |"  in markdown
    assert 'hybrid' in markdown
    assert '90.0%' in markdown
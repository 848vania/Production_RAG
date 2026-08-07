from unittest.mock import patch

from app.evaluation.experiment_config import load_experiment_config
from app.evaluation.experiment_runner import run_experiment


@patch("app.evaluation.experiment_runner.run_retrieval_evaluation")
@patch("app.evaluation.experiment_runner.run_answer_evaluation")
def test_run_experiment(mock_answer_eval, mock_retrieval_eval):
    mock_retrieval_eval.return_value = {
        'summary': {
            'total_questions': 10,
            'recall_at_5': 0.9,
            'reciprocal_rank': 0.8,
        },
        'results': [],
    }

    mock_answer_eval.return_value = {
        'summary': {
            'total_questions': 10,
            'citation_accuracy': 0.85,
            'refusal_accuracy': 0.9,
            'answer_correctness': 0.8,
            'average_latency_ms': 2000,
            'average_cost_usd': 0.003,
        },
        'results': [],
    }

    config = load_experiment_config('configs/hybrid.yaml')
    result = run_experiment(config)

    assert result['experiment_name'] == 'hybrid'
    assert result['retrieval']['recall_at_5'] == 0.9
    assert result['answer']['citation_accuracy'] == 0.85
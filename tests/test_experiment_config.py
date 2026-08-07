from app.evaluation.experiment_config import load_experiment_config


def test_load_experiment_config():
    config = load_experiment_config('configs/hybrid.yaml')

    assert config.name == 'hybrid'
    assert config.retrieval.type == 'hybrid'
    assert config.retrieval.vector_weight == 0.6
    assert config.reranker.enabled is False
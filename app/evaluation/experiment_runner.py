import json 
from pathlib import Path
from datetime import datetime, timezone 

from app.evaluation.experiment_config import (
    ExperimentConfig,
    load_experiment_config,
    load_experiment_configs,
    experiment_config_to_dict,
)
from app.evaluation.run_retrieval_eval import run_retrieval_evaluation
from app.evaluation.run_answer_eval import run_answer_evaluation


RESULTS_DIR = Path('data/results/experiments')
RESULTS_DIR.mkdir(parents=True, exist_ok=True)


def run_experiment(config: ExperimentConfig) -> dict:
    """
    Run one experiment configuration.

    This runs:
    1. Retrieval evaluation
    2. Answer evaluation 
    3. Combined summary
    """
    started_at = datetime.now(timezone.utc).isoformat()

    retrieval_eval = run_retrieval_evaluation(
        save = True,
        output_suffix=  config.name,
    )

    answer_eval = run_answer_evaluation(
        save=True,
        output_suffix=config.name,
    )

    finished_at = datetime.now(timezone.utc).isoformat()

    experiment_result = {
        'experiment_name': config.name,
        'started_at': started_at,
        'finished_at': finished_at,
        'config': experiment_config_to_dict(config),
        'retrieval': retrieval_eval['summary'],
        'answer': answer_eval['summary'],
    }

    save_experiment_result(experiment_result)

    return experiment_result


def run_experiment_from_path(config_path: str) -> dict:
    """
    Load one config path and run experiment
    """
    config = load_experiment_config(config_path)
    return run_experiment(config)


def run_all_experiments(config_paths: list[str]) -> list[dict]:
    """
    Run multiple experiment configurations
    """
    configs = load_experiment_configs(config_paths)
    results = []

    for config in configs:
        print(f"Running experiment: {config.name}")
        result = run_experiment(config)
        results.append(result)

    save_all_experiment_results(results)

    return results 


def save_experiment_result(result: dict) -> None:
    """
    Save one experiment result.
    """
    output_path = RESULTS_DIR / f"{result['experiment_name']}.json"

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(result, file, indent=2, ensure_ascii=False)


def save_all_experiment_results(results: list[dict]) -> None:
    """
    Save all experiment results into one JSON file
    """
    output_path = RESULTS_DIR / 'all_experiments.json'

    with  output_path.open('w', encoding='utf-8') as file:
        json.dump(results, file, indent=2, ensure_ascii=False)
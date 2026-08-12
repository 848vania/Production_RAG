import requests 
import json 
from pathlib import Path
from typing import Any 

import pandas as pd 


API_BASE_URL = "http://localhost:8000"
RESULTS_DIR = Path('data/results')


def ask_question(question: str) -> dict:
    """
    Call the FastAPI chat endpoint
    """
    response = requests.post(
        f"{API_BASE_URL}/chat/",
        json = {
            "question": question
        },
        timeout = 90,
    )
    response.raise_for_status()
    print(response.json())
    return response.json()


def load_json_file(path: str | Path) -> dict | list | None:
    """
    Safely load a JSON file.
    """
    path = Path(path)

    if not path.exists():
        return None 

    with path.open('r', encoding='utf-8') as file:
        return json.load(file)


def load_experiment_summary() -> pd.DataFrame:
    """
    Load experiment summary CSV if it exists
    """
    csv_path = RESULTS_DIR / 'experiment_summary.csv'

    if not csv_path.exists():
        return  pd.DataFrame()

    return pd.read_csv(csv_path)


def load_retrieval_eval_summary(experiment_name: str | None = None) -> dict:
    """
    Load retieval evaluation  summary
    """
    if experiment_name:
        path = RESULTS_DIR / f'retrieval_eval_summary_{experiment_name}.json'
    else:
        path = RESULTS_DIR / 'retrieval_eval_summary.json'

    data = load_json_file(path)
    return data or {}


def load_answer_eval_summary(experiment_name: str | None =  None) -> dict:
    """
    Load answer evaluation summary
    """
    if experiment_name:
        path = RESULTS_DIR  / f'answer_eval_summary_{experiment_name}.json'
    else:
        path = RESULTS_DIR / 'answer_eval_summary.json'

    data = load_json_file(path)
    return data or {}


def load_answer_eval_results(experiment_name: str | None = None) -> list[dict]:
    """
    Load per-question answer evaluation results
    """
    if experiment_name:
        path = RESULTS_DIR  / f'answer_eval_results_{experiment_name}.json'
    else:
        path = RESULTS_DIR / 'answer_eval_results.json'

    data = load_json_file(path)
    return data or []


def load_retrieval_eval_results(experiment_name: str | None = None) -> list[dict]:
    """
    Load per-question retrieval evaluation results
    """
    if experiment_name:
        path = RESULTS_DIR / f'retrieval_eval_results_{experiment_name}.json'
    else:
        path = RESULTS_DIR / 'retrieval_eval_results.json'

    data =  load_json_file(path)
    return data or [] 


def format_percent(value: float | int | None) -> str:
    """
    Format 0.86 as 86.0%
    """
    if value is None:
        return "-"

    return f'{float(value) * 100:.1f}%'


def format_latency_ms(value: float | int | None) -> str:
    """
    Format  milliseconds as seconds
    """
    if value is None:
        return "-"

    return f"{float(value) / 1000:.2f}s"


def format_cost(value: float | int | None) -> str:
    """
    Format cost
    """
    if  value is None:
        return "-"

    return f"${float(value):.4f}"
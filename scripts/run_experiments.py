from app.evaluation.experiment_runner import *
from app.evaluation.experiment_summary import generate_experiment_summary
from pathlib import Path


CONFIG_PATH = Path('configs')
CONFIG_FILES = [
    'vector_only.yaml',
    'keyword_only.yaml',
    'hybrid.yaml',
    'hybrid_reranker.yaml'
]


def main():
    config_paths = [CONFIG_PATH / config for config in CONFIG_FILES]
    results = run_all_experiments(config_paths)

    print('\nFinished runnning experiments')
    print(f'Total experiments: {len(results)}')

    rows = generate_experiment_summary()

    print("\nExperiment summary:")
    for row in rows:
        print(
            f"- {row['experiment_name']}: "
            f"Recall@5={row['recall_at_5']:.2f}, "
            f"ReciprocalRank={row['reciprocal_rank']:.2f}, "
            f"CitationAcc={row['citation_accuracy']:.2f}, "
            f"Latency={row['average_latency_ms']:.0f}ms"
        )


    print("\nSaved outputs:")
    print('- data/results/experiments/all_experiments.json')
    print('- data/results/experiment_summary.json')
    print('- data/results/experiment_summary.csv')
    print('- data/results/experiment_summary.md')


if __name__ == "__main__":
    main()
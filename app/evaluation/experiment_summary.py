import csv 
import json
from pathlib import Path


RESULTS_DIR = Path('data/results/experiments')
SUMMARY_DIR = Path('data/results')
SUMMARY_DIR.mkdir(parents=True, exist_ok=True)


def load_all_experiment_results(
        input_path: Path = RESULTS_DIR / 'all_experiments.json',
    ) -> list[dict]:
    """
    Load all experiments results
    """
    with input_path.open('r', encoding='utf-8') as file:
        return json.load(file)


def flatten_experiment_result(result: dict) -> dict:
    """
    Convert nested experiment result into one flat row
    """
    retrieval = result["retrieval"]
    answer = result["answer"]
    config = result["config"]

    return {
        "experiment_name": result["experiment_name"],
        "retrieval_type": config["retrieval"]["type"],
        "reranker_enabled": config["reranker"]["enabled"],
        "top_k": config["retrieval"]["top_k"],
        "vector_weight": config["retrieval"]["vector_weight"],
        "keyword_weight": config["retrieval"]["keyword_weight"],
        "recall_at_1": retrieval.get("recall_at_1"),
        "recall_at_3": retrieval.get("recall_at_3"),
        "recall_at_5": retrieval.get("recall_at_5"),
        "precision_at_5": retrieval.get("precision_at_5"),
        "reciprocal_rank": retrieval.get("reciprocal_rank"),
        "citation_accuracy": answer.get("citation_accuracy"),
        "refusal_accuracy": answer.get("refusal_accuracy"),
        "answer_correctness": answer.get("answer_correctness"),
        "average_latency_ms": answer.get("average_latency_ms"),
        "average_cost_usd": answer.get("average_cost_usd"),
    }


def build_experiment_summary(results: list[dict]) -> list[dict]:
    """
    Build flat summary rows
    """
    return [flatten_experiment_result(result) for result in results]


def save_summary_csv(rows: list[dict], output_path: Path) -> None:
    """
    Save experiment summary as CSV.
    """
    if not rows:
        return

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def save_summary_json(rows: list[dict], output_path: Path) -> None:
    """
    Save experiment summary as JSON.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(rows, file, indent=2, ensure_ascii=False)


def format_percent(value: float | None) -> str:
    if value is None:
        return "-"

    return f"{value * 100:.1f}%"


def format_latency(value: float | None) -> str:
    if value is None:
        return "-"

    return f"{value / 1000:.2f}s"


def build_markdown_table(rows: list[dict]) -> str:
    """
    Build Markdown table for README/evaluation_report.md.
    """
    header = (
        "| Experiment | Retrieval | Reranker | Recall@5 | Reciprocal Rank | "
        "Citation Acc. | Refusal Acc. | Answer Correct. | Latency |\n"
    )
    divider = (
        "|---|---|---:|---:|---:|---:|---:|---:|---:|\n"
    )

    lines = [header, divider]

    for row in rows:
        lines.append(
            "| {experiment} | {retrieval} | {reranker} | {recall} | {reciprocal_rank} | "
            "{citation} | {refusal} | {correctness} | {latency} |\n".format(
                experiment=row["experiment_name"],
                retrieval=row["retrieval_type"],
                reranker="yes" if row["reranker_enabled"] else "no",
                recall=format_percent(row["recall_at_5"]),
                reciprocal_rank=f"{row['reciprocal_rank']:.2f}" if row["reciprocal_rank"] is not None else "-",
                citation=format_percent(row["citation_accuracy"]),
                refusal=format_percent(row["refusal_accuracy"]),
                correctness=format_percent(row["answer_correctness"]),
                latency=format_latency(row["average_latency_ms"]),
            )
        )

    return "".join(lines)


def save_markdown_table(markdown: str, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as file:
        file.write(markdown)


def generate_experiment_summary() -> list[dict]:
    """
    Generate CSV, JSON, and Markdown summaries from all experiment results.
    """
    results = load_all_experiment_results()
    rows = build_experiment_summary(results)

    save_summary_json(rows, SUMMARY_DIR / "experiment_summary.json")
    save_summary_csv(rows, SUMMARY_DIR / "experiment_summary.csv")

    markdown = build_markdown_table(rows)
    save_markdown_table(markdown, SUMMARY_DIR / "experiment_summary.md")

    return rows
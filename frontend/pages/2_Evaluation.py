import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import streamlit as st
import pandas as pd

from frontend.utils import (
    format_cost,
    format_latency_ms,
    format_percent,
    load_answer_eval_results,
    load_experiment_summary,
    load_retrieval_eval_results
)

st.set_page_config(
    page_title="Evaluation Dashboard",
    page_icon="📊",
    layout  = 'wide'
)

st.title("Evaluation Dashboard")

st.write(
    """
    This page compares RAG configuration using retrieval metrics, 
    answer-quality metrics, latency, and estimated cost
    """
)

summary_df = load_experiment_summary()

if summary_df.empty:
    st.warning(
        """
        No experiment summary found 

        Run: 

        `python scripts/run_experiments.py`

        Then refresh this page
        """
    )
    st.stop()


# ------------------------------------
# Experiment comparison 
# ------------------------------------

st.header("Experiment Comparison")

display_df = summary_df.copy()

percent_columns = [
    'recall_at_1',
    'recall_at_3',
    'recall_at_5',
    'precision_at_5',
    'citation_accuracy',
    'refusal_accuracy',
    'answer_correctness',
]

for column in percent_columns:
    if column in display_df.columns:
        display_df[column] = display_df[column].apply(format_percent)

if 'average_latency_ms' in display_df.columns:
    display_df['average_latency_ms'] = display_df['average_latency_ms'].apply(format_latency_ms)

if 'average_cost_usd' in display_df.columns:
    display_df['average_cost_usd'] = display_df['average_cost_usd'].apply(format_cost)

st.dataframe(display_df, use_container_width=True)


# ------------------------------------
# Best Experiment Selection 
# ------------------------------------

st.header("Best Configuration")

ranking_metric = st.selectbox(
    "Rank experiments by",
    [
        'recall_at_5',
        'reciprocal_rank',
        'citation_accuracy',
        'refusal_accuracy',
        'answer_correctness',
        'average_latency_ms'
    ],
)

ascending = ranking_metric == 'average_latency_ms'

ranked_df = summary_df.sort_values(
    by=ranking_metric,
    ascending=ascending
)

best = ranked_df.iloc[0]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Best Experiment", best['experiment_name'])

with col2:
    st.metric('Retrieval Type', best['retrieval_type'])

with col3:
    st.metric('Recall@5', format_percent(best.get('recall_at_5')))

with col4:
    st.metric('Reciprocal Rank', f"{best.get('reciprocal_rank',0):.2f}")


# ------------------------------------
# Metric Cards
# ------------------------------------

st.header("Key Metrics")

selected_experiment = st.selectbox(
    "Select experiment for details",
    summary_df['experiment_name'].tolist(),
)

selected_row = summary_df[
    summary_df['experiment_name'] == selected_experiment
].iloc[0]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Recall@5", format_percent(selected_row.get('recall_at_5')))

with col2:
    st.metric("Reciprocal Rank", f"{selected_row.get('reciprocal_rank', 0):.2f}")

with col3:
    st.metric(
        "Citation Accuracy",
        format_percent(selected_row.get('citation_accuracy')),
    )

with col4:
    st.metric(
        'Refusal Accuracy',
        format_percent(selected_row.get('refusal_accuracy')),
    )

col5, col6, col7, col8 = st.columns(4)

with col5:
    st.metric(
        "Answer Correctness",
        format_percent(selected_row.get('answer_correctness')),
    )

with col6:
    st.metric(
        "Average Latency",
        format_latency_ms(selected_row.get("average_latency_ms")),
    )

with col7:
    st.metric(
        "Average Cost",
        format_cost(selected_row.get('average_cost_usd')),
    )

with col8:
    st.metric(
        "Reranker Enabled",
        "Yes" if selected_row.get('reranker_enabled') else "No",
    )

# ------------------------------------
# Charts
# ------------------------------------

st.header("Metric Comparison")

chart_metrics = [
    metric 
    for metric in [
        'recall_at_5',
        'reciprocal_rank',
        'citation_accuracy',
        'refusal_accuracy',
        'answer_correctness',
    ]
    if metric in summary_df.columns
]

chart_df = summary_df.set_index('experiment_name')[chart_metrics]

st.bar_chart(chart_df)


# ------------------------------------
# Failure Case Viewer
# ------------------------------------

st.header("Failure Cases")

answer_results = load_answer_eval_results(selected_experiment)
retrieval_results = load_retrieval_eval_results(selected_experiment)

failure_type = st.selectbox(
    "Failure type",
    [
        "Answer correctness failures",
        "Citation failures",
        "Refusal failures",
        "retrieval failures"
    ],
)

if failure_type == "Answer correctness failures":
    failures = [
        item for item in answer_results
        if item.get("answer_scores", {}).get("answer_correctness", 1) < 1
    ]

elif failure_type == "Citation failures":
    failures = [
        item
        for item in answer_results
        if item.get('answer_scores',{}).get('refusal_accuracy', 1) < 1
    ]

elif failure_type == "Refusal failures":
    failures = [
        item
        for item in answer_results
        if item.get('answer_scores',{}).get('refusal_accuracy', 1) < 1
    ]

else:
    failures = [
        item 
        for item in retrieval_results
        if item.get('retrieval', {}).get('recall_at_5', 1) < 1
    ]

if not failures:
    st.success("No failures found  for this category")
else:
    st.write(f"Found {len(failures)} failure cases.")

    selected_failure_index = st.number_input(
        "Failure index",
        min_value=0,
        max_value=max(len(failures) - 1, 0),
        value=0,
        step=1,
    )

    failure = failures[selected_failure_index]

    st.subheader("Question")
    st.write(failure.get("question"))

    st.subheader("Expected Answer")
    st.write(failure.get("expected_answer"))

    st.subheader("Predicted Answer")
    st.write(failure.get("predicted_answer"))

    st.subheader("Expected Sources")
    st.write(failure.get("expected_sources"))

    st.subheader("Predicted / Retrieved Sources")
    st.write(
        failure.get("predicted_sources")
        or failure.get("retrieved_sources")
        or []
    )

    with st.expander("Raw failure data"):
        st.json(failure)


# -----------------------------
# Raw data
# -----------------------------

with st.expander("Raw experiment summary"):
    st.dataframe(summary_df, use_container_width=True)
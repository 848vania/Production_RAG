import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import pandas as pd
import streamlit as st

from app.monitoring.metrics import get_monitoring_summary
from frontend.utils import format_cost, format_latency_ms, format_percent


st.set_page_config(
    page_title="Monitoring Dashboard",
    page_icon="📈",
    layout = "wide",
)

st.title("Monitoring Dashboard")

st.write(
    """
    This page shows operational metrics from logged chat interactions.
    Evaluation runs are excluded when 'log=False' is used.
    """
)

summary = get_monitoring_summary()

if summary['total_queries'] == 0:
    st.warning(
        """
        No query logs found yet

        Go to the Chat page and ask a few questions, then return here
        """
    )
    st.stop()


# -------------------------
# Metric Cards
# -------------------------

st.header("Operational Summary")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Total Queries", summary['total_queries'])

with col2:
    st.metric(
        "Avg Latency",
        format_latency_ms(summary['average_latency_ms']),
    )

with col3:
    st.metric(
        "Total Cost",
        format_cost(summary['total_estimated_cost_usd']),
    )

with col4:
    st.metric(
        "Refusal Rate",
        format_percent(summary['refusal_rate']),
    )

with col5:
    st.metric(
        "Low Confidence Rate",
        format_percent(summary['low_confidence_rate']),
    )


# -------------------------
# Recent queries table 
# -------------------------

st.header("Recent Queries")

recent_queries = summary['recent_queries']

recent_df = pd.DataFrame(recent_queries)

if recent_df.empty:
    st.info("No recent queries found")
else:
    visible_columns = [
        column 
        for column in [
            'created_at',
            'question',
            'confidence',
            'latency_ms',
            'cost_usd',
            'retrieval_type',
            'model_provider',
            'refused',
            'reason',
        ]
        if column in recent_df.columns
    ]

    display_df = recent_df[visible_columns].copy()

    if 'latency_ms' in display_df.columns:
        display_df['latency_ms'] = display_df['latency_ms'].apply(format_latency_ms)

    if 'cost_usd' in display_df.columns:
        display_df['cost_usd'] = display_df['cost_usd'].apply(format_cost)

    st.dataframe(display_df, use_container_width=True)


# -------------------------
# Query detail viewer 
# -------------------------

st.header("Query Detail")

if not recent_df.empty:
    selected_index = st.number_input(
        "Select recent query index",
        min_value=0,
        max_value= max(len(recent_queries) -1, 0),
        value = 0,
        step = 1,
    )

    selected_query = recent_queries[selected_index]

    st.subheader("Question")
    st.write(selected_query.get("question"))

    st.subheader("Answer")
    st.write(selected_query.get("answer"))

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Confidence", selected_query.get("confidence", "-"))

    with col2:
        st.metric(
            "Latency",
            format_latency_ms(selected_query.get("latency_ms")),
        )

    with col3:
        st.metric(
            "Cost",
            format_cost(selected_query.get("cost_usd")),
        )

    with col4:
        st.metric(
            "Refused",
            "Yes" if selected_query.get("refused") else "No",
        )

    st.subheader("Sources")
    sources = selected_query.get("sources", [])

    if not sources:
        st.write("No sources logged.")
    else:
        for source in sources:
            with st.expander(
                f"{source.get('source_number', '-')}. "
                f"{source.get('document', 'Unknown document')} — "
                f"{source.get('section', 'Unknown section')}"
            ):
                st.write("Doc ID:", source.get("doc_id"))
                st.write("Score:", source.get("score"))
                st.write(source.get("text"))


# -----------------------------
# Basic charts
# -----------------------------

st.header("Monitoring Charts")

if not recent_df.empty:
    chart_df = recent_df.copy()

    if "created_at" in chart_df.columns:
        chart_df["created_at"] = pd.to_datetime(chart_df["created_at"])

    if "latency_ms" in chart_df.columns:
        latency_chart_df = chart_df[["created_at", "latency_ms"]].dropna()

        if not latency_chart_df.empty:
            st.subheader("Latency Over Recent Queries")
            st.line_chart(
                latency_chart_df.set_index("created_at")["latency_ms"]
            )

    if "confidence" in chart_df.columns:
        st.subheader("Confidence Distribution")
        confidence_counts = chart_df["confidence"].value_counts()
        st.bar_chart(confidence_counts)

    if "refused" in chart_df.columns:
        st.subheader("Refusal Distribution")
        refusal_counts = chart_df["refused"].value_counts()
        st.bar_chart(refusal_counts)


with st.expander("Raw monitoring summary"):
    st.json(summary)
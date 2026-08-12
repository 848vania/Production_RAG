import streamlit as st 

# Configure the page title and layout 
st.set_page_config(
    page_title= "Enterprise RAG Assistant",
    page_icon= "🤖",
    layout= 'wide'
)

st.title("Welcome to the Enterprise RAG Assistant")
st.write(
    """
    A production-style Retrieval-Augmented Generation system for answering
    questions over enterprise documents with citations, evaluation, and monitoring.
    """
)

st.markdown(
    """
    ### What this project demonstrates

    - Document ingestion and chunking
    - Vector, keyword, and hybrid retrieval
    - Source-cited LLM answers 
    - Refusal for unsupported questions
    - Retrieval and answer evaluation
    - Experiment comparison 
    - Query logging and monitoring
    """
)

st.markdown(
    """
    ### Pages

    **Chat**
    Ask questions over the synthetic enterprise knowledge base.

    **Evaluation**
    Compate retrieval and answer quality across different RAG configurations.

    **Monitoring**
    Inspect real usage logs, latency, refusal rate, and confidence trends.
    """
)
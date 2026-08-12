import streamlit as st
from frontend.utils import ask_question, format_cost, format_latency_ms


st.set_page_config(
    page_title= "Chat",
    page_icon= "💬",
    layout= 'wide',
)

st.title("AI Assistant Chat")

question = st.text_input(
    "Ask a question",
    placeholder="Who approves remote work requests?",
)

if st.button("Ask") and question.strip():
    with st.spinner("Retrieving sources and generating answer..."):
        try:
            response = ask_question(question)
        except Exception as e:
            st.error(f"Failed to connect to FastAPI server: {e}")

        # Display the response components cleanly 
        st.subheader("Answer")
        st.write(response['answer'])

        col1, col2, col3, col4 =  st.columns(4)

        with col1:
            st.metric("Confidence", response.get('confidence', "-"))

        with col2:
            st.metric("Latency", format_latency_ms(response.get('latency_ms')))

        with col3:
            st.metric("Retrieval", response.get('retrieval_type', '-'))

        with col4:
            st.metric("Model", response.get('model_provider', '-'))

        if response.get('cost_usd') is not None:
            st.caption(f"Estimated cost: {format_cost(response.get('cost_usd'))}")

        if response.get('refused'):
            st.warning(f"Refused: {response.get('reason')}")

        st.subheader("Sources")

        sources = response.get('sources', [])

        if not sources:
            st.write('No sources returned')
        else:
            for source in sources:
                with st.expander(
                    f"{source.get('source_number', '')}. "
                    f"{source.get('document', 'Unknown document')} - "
                    f"{source.get('section', 'Unknown section')}"
                ):
                    st.write("Doc ID:", source.get('doc_id'))
                    st.write("Score:", source.get('score'))
                    st.write(source.get("text"))
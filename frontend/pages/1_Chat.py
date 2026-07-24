import streamlit as st
from utils import *

st.set_page_config(
    page_title= "Chat",
    page_icon= "💬"
)

st.title("AI Assistant Chat")

question = st.text_input("Ask a question")

if st.button("Submit"):
    if question.strip() == "":
        st.warning("Please enter a question first.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = ask_question(question)

                # Display the response components cleanly 
                st.subheader("Answer")
                st.write(response['answer'])

                # Display confidence as metric
                st.metric(label = "Confidence Score", value = f"{response['confidence']}")

                # Display latency as metric
                st.metric(label = "Latency", value = f"{response['latency_ms'] / 1000:.2f}s")

                st.subheader("Sources")
                sources = response['sources']
                # Format sources 
                text_sources = ""
                if not sources:
                    text_sources = "No reliable sources found"
                else:
                    for i,source in enumerate(sources, start=1):
                        text_sources += f"{i}. {source['document']} - {source['section']}\n"
                
                st.write(text_sources)


            except Exception as e:
                st.error(f"Failed to connect to FastAPI server: {e}")
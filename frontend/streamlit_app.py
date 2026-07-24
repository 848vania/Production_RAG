import streamlit as st 

# Configure the page title and layout 
st.set_page_config(
    page_title= "Enterprise RAG Assistant",
    page_icon= "🤖",
    layout= 'wide'
)

st.title("Welcome to the Enterprise RAG Assistant")
st.write("Select a page from the sidebar to get started")
st.info("👈 Click on 'Chat' in the sidebar to ask questions!")
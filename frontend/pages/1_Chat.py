question = st.text_input("Ask a question")

if st.button("Submit"):
    response = call_chat_api(question)
    st.write(response["answer"])
    st.write(response["sources"])
    st.write(response["confidence"])
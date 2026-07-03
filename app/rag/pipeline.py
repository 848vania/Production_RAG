def answer_question(question: str):
    start_time = current_time()

    retrieved_chunks = retrieve_context(question)
    reranked_chunks = rerank(question, retrieved_chunks)

    if not is_answerable(reranked_chunks):
        return refusal_response(question, reranked_chunks)

    answer = generate_answer(question, reranked_chunks)
    grounded_answer = validate_grounding(answer, reranked_chunks)

    log_interaction(
        question=question,
        answer=grounded_answer,
        sources=reranked_chunks,
        latency=elapsed_time(start_time)
    )

    return grounded_answer
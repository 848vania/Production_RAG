def run_evaluation():
    dataset = load_eval_dataset()
    results = []

    for item in dataset:
        response = answer_question(item["question"])
        retrieval_scores = evaluate_retrieval(response, item)
        answer_scores = evaluate_answer(response, item)

        results.append({
            "question_id": item["id"],
            "retrieval": retrieval_scores,
            "answer": answer_scores
        })

    save_results(results)
    return summarize_results(results)
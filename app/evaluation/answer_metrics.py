def refusal_accuracy(predicted_answer: str, answerable: bool):
    refused = "do not have enough information" in predicted_answer.lower()

    if answerable:
        return not refused
    return refused
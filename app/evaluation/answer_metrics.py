
def extract_source_ids(sources: list[dict]) -> list[str]:
    return [
        f"{source.get('doc_id')}::{source.get('section')}"
        for source in sources
    ]

def citation_accuracy(predicted_sources: list[str], expected_sources: list[str]) -> float:
    """
    Whether cited sources overlap expected sources.
    Calculates the Precision of the predicted sources
    """
    if not predicted_sources:
        return 0.0 if expected_sources else 1.0

    pred_set = set(predicted_sources)
    exp_set = set(expected_sources)

    # Calculate how many predicted sourcess were actually correct
    correct_predictions = pred_set.intersection(exp_set)
    return len(correct_predictions) / len(pred_set)


def refusal_accuracy(predicted_answer: str, answerable: bool):
    """
    Checks whether the system refused appropriately
    Returns 1.0 for correct behavior, 0.0 for incorrect behavior
    """
    # Common refusal phrases can be added to this list
    refusal_keywords = [
        'I do not have enough information in the provided documents to answer this question',
        'I found potentially relevant information, but I could not generate a properly cited answer from the provided documents.',
        "do not have enough information",
        'i cannot answer',
        'not mentioned in the text',
        'insufficient information'
    ]

    predicted_lower = predicted_answer.lower()
    refused = any(phrase in predicted_lower for phrase in refusal_keywords)

    # REturn 1.0 for success (True), 0.0 for failure (False)
    return float(refused == (not answerable))


def contains_expected_terms(predicted_answer: str, expected_answer: str) -> float:
    """
    Simple keyword overlap for baseline correctness
    Filters out common stop words to focus on meaningful terms
    """
    import re 

    # Simple tokenization and lowercase conversion
    def get_keywords(text: str) -> set[str]:
        words = re.findall(r'\b\w+\b', text.lower())
        # Filter out common short stop words 
        stop_words = {'the', 'a', 'an', 'and', 'of', 'to', 'in', 'is', 'that', 'it', 'for', 'on', 'with', 'as'}
        return {w for w in words if w not in stop_words}

    pred_words = get_keywords(predicted_answer)
    exp_words = get_keywords(expected_answer)

    if not exp_words:
        return 1.0 if not pred_words else 0.0

    # Calculate Jaccard similarity or simple inclusion recall 
    # Here we use Recall: what % of expected terms did the model guess?
    match_count = len(pred_words.intersection(exp_words))
    return match_count / len(exp_words)


def answer_correctness_simple(predicted_answer: str, expected_answer: str | None) -> float:
    """
    Rule-based approximate correctness
    Combines refusal checking and keyword overlap into a single metric
    """
    # Handle cases where the question is unanswerable (expected_answer is None or empty)
    if not expected_answer:
        # If it was supposed to be unanswerable, check if it refused properly 
        is_correct_refusal = refusal_accuracy(predicted_answer, answerable=False)
        return is_correct_refusal

    # If it was supposed to be answerable, check if it refused by mistake 
    was_falsely_refused = not refusal_accuracy(predicted_answer, answerable=True)
    if was_falsely_refused:
        return 0.0

    # If it answered and was supposed to answer, measure term overlap 
    return contains_expected_terms(predicted_answer, expected_answer)


def evaluate_answers(
        predicted_answer,
        predicted_sources,
        eval_item
    ) -> dict:
    """
    Run answers evaluation metrics
    """

    expected_answer = eval_item['expected_answer']
    expected_sources = eval_item['expected_sources']
    answerable = eval_item['answerable']

    return {
        'citation_accuracy': citation_accuracy(predicted_sources, expected_sources),
        'refusal_accuracy': refusal_accuracy(predicted_answer, answerable=answerable),
        'answer_correctness': answer_correctness_simple(predicted_answer, expected_answer)
    }
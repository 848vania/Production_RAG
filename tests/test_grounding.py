from app.rag.grounding import * 

def test_has_sufficient_context_true():
    chunks = [{"score": 0.82}]

    assert has_sufficient_context(chunks, score_limit=1.1) is True


def test_has_sufficient_context_false_for_high_score():
    chunks = [{"score": 1.5}]

    assert has_sufficient_context(chunks, score_limit=1.1) is False


def test_has_sufficient_context_false_for_empty_chunks():
    assert has_sufficient_context([], score_limit=1.1) is False


def test_estimate_confidence_medium():
    chunks = [{"score": 1.09}]
    assert estimate_confidence(chunks) == "medium"


def test_estimate_confidence_high():
    chunks = [{"score": 0.8}]
    assert estimate_confidence(chunks) == "high"


def test_estimate_confidence_low():
    chunks = []
    assert estimate_confidence(chunks) == "low"


def test_extract_cited_source_numbers():
    answer = "The request requires manager approval. [Source 1] It is reviewed by HR. [Source 2]"
    assert extract_cited_source_numbers(answer) == [1,2]


def test_validate_citations_true():
    answer = "Remote work requires approval. [Source 1]"
    sources = [{"chunk_id": '1'}]

    assert validate_citations(answer, sources) is True


def test_validate_citations_false_for_missing_source():
    answer = "Remote work requires manager approval. [Source 3]"
    sources = [{"chunk_id": '1'}, {"chunk_id": '2'}]

    assert validate_citations(answer, sources) is False 


def test_validate_citations_false_when_no_citations():
    answer = "Remote work requires manager approval"
    sources = [{"chunk_id": '1'}]

    assert validate_citations(answer, sources) is False

# test_has_sufficient_context_true()
# test_has_sufficient_context_false_for_high_score()
# test_has_sufficient_context_false_for_empty_chunks()
# test_estimate_confidence_medium()
# test_estimate_confidence_high()
# test_estimate_confidence_low()
# test_extract_cited_source_numbers()
# test_validate_citations_true()
# test_validate_citations_false_for_missing_source()
test_validate_citations_false_when_no_citations()
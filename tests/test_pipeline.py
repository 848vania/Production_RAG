from app.rag.pipeline import * 
from unittest.mock import patch


@patch("app.rag.pipeline.vector_retrieve")
@patch("app.rag.pipeline.generate_answer")
def test_pipeline_answerable_questions(mock_generate, mock_retrieve):
    mock_retrieve.return_value = [
        {
            "chunk_id": "1",
            "text": "Remote work requests must be approved by the employee's direct manager and HR.",
            "score": 0.89, 
            "metadata": {
                "document": "Remote Work Policy",
                "section": "Approval Process",
            },
        }
    ]

    mock_generate.return_value = {
        "answer": "Remote work must be approved by the employee's direct manager and HR [Source 1]",
        "sources": [
            {
                "source_number": 1,
                "chunk_id": "1",
                "document": "Remote Work Policy",
                "section": "Approval Process",
                "score": 0.89,
                "text": "Remote work requests must be approved by the employee's direct manager and HR."
            }
        ],
    }

    response = answer_question("Who approves remote work requests?")

    assert response['refused'] is False
    assert response['confidence'] == "high"
    assert "manager" in response['answer']


@patch("app.rag.pipeline.vector_retrieve")
@patch("app.rag.pipeline.generate_answer")
def test_pipeline_refuses_low_context(mock_generate, mock_retrieve):
    mock_retrieve.return_value = [
        {
            "chunk_id": "2",
            "text": "Full-time employees may request remote work",
            "score": 1.5,
            "metadata": {
                "document": "Remote Work Policy",
                "section": "Eligibility"
            },
        }
    ]

    response = answer_question("Can employees work from Mars")

    assert response['refused'] is True
    assert response['reason'] == "insufficient_retrieved_context"
    mock_generate.assert_not_called()


@patch("app.rag.pipeline.vector_retrieve")
@patch("app.rag.pipeline.generate_answer")
def test_pipeline_refuses_invalid_citations(mock_generate, mock_retrieve):
    mock_retrieve.return_value = [
        {
            "chunk_id": "3",
            "text": "Remote work requests must be approved by the employee's direct manager and HR.",
            "score": 0.89,
            "metadata": {
                "document": "Remote Work Policy",
                "section": "Approval Process",
            },
        }
    ]

    mock_generate.return_value = {
        "answer": "Remote work requests must be approved by the employee's direct manager and HR.",
        "sources": [{"chunk_id": '5'}],
    }

    response = answer_question("Who approves remote work requests?")

    assert response['refused'] is True
    assert response['reason'] == 'invalid_or_missing_citations'

def test_manual_pipeline():
    response = answer_question("Who approves remote work requests?")
    print(f"RESPONSE:\n{response}")

test_manual_pipeline()
from app.rag.pipeline import *
from unittest.mock import patch
from app.evaluation.experiment_config import load_experiment_config


@patch("app.rag.pipeline.retrieve")
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

    response = answer_question("Who approves remote work requests?", config=None, log=False)

    assert response['refused'] is False
    assert response['confidence'] == "high"
    assert "manager" in response['answer']


@patch("app.rag.pipeline.retrieve")
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

    response = answer_question("Can employees work from Mars", config=None, log=False)

    assert response['refused'] is True
    assert response['reason'] == "insufficient_retrieved_context"
    mock_generate.assert_not_called()


@patch("app.rag.pipeline.retrieve")
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

    response = answer_question("Who approves remote work requests?", config=None, log=False)

    assert response['refused'] is True
    assert response['reason'] == 'invalid_or_missing_citations'


@patch("app.rag.pipeline.retrieve")
@patch("app.rag.pipeline.generate_answer")
def test_answer_question_passes_retrieval_overrides_from_config(mock_generate, mock_retrieve):
    mock_retrieve.return_value = [
        {
            "chunk_id": "1",
            "text": "Remote work requests must be approved by the employee's direct manager and HR.",
            "score": 0.89,
            "metadata": {"document": "Remote Work Policy", "section": "Approval Process"},
        }
    ]
    mock_generate.return_value = {
        "answer": "Remote work must be approved by the employee's direct manager and HR [Source 1]",
        "sources": [{"source_number": 1, "chunk_id": "1", "document": "Remote Work Policy",
                     "section": "Approval Process", "score": 0.89, "text": "..."}],
        "cost_usd": 0.0,
    }

    vector_config = load_experiment_config('configs/vector_only.yaml')
    response_vector = answer_question("Who approves remote work requests?", config=vector_config, log=False)

    hybrid_config = load_experiment_config('configs/hybrid.yaml')
    response_hybrid = answer_question("Who approves remote work requests?", config=hybrid_config, log=False)

    vector_call_type = mock_retrieve.call_args_list[0].kwargs['retrieval_type']
    hybrid_call_type = mock_retrieve.call_args_list[1].kwargs['retrieval_type']

    assert vector_call_type == 'vector'
    assert hybrid_call_type == 'hybrid'
    assert vector_call_type != hybrid_call_type

    assert response_vector['retrieval_type'] == 'vector'
    assert response_hybrid['retrieval_type'] == 'hybrid'


@patch("app.rag.pipeline.get_reranker")
@patch("app.rag.pipeline.retrieve")
@patch("app.rag.pipeline.generate_answer")
def test_answer_question_respects_config_reranker_flag(mock_generate, mock_retrieve, mock_get_reranker):
    mock_retrieve.return_value = [
        {
            "chunk_id": "1",
            "text": "Remote work requests must be approved by the employee's direct manager and HR.",
            "score": 0.89,
            "metadata": {"document": "Remote Work Policy", "section": "Approval Process"},
        }
    ]
    mock_generate.return_value = {
        "answer": "Remote work must be approved by the employee's direct manager and HR [Source 1]",
        "sources": [{"source_number": 1, "chunk_id": "1", "document": "Remote Work Policy",
                     "section": "Approval Process", "score": 0.89, "text": "..."}],
        "cost_usd": 0.0,
    }
    mock_get_reranker.return_value.rerank.return_value = mock_retrieve.return_value

    no_rerank_config = load_experiment_config('configs/hybrid.yaml')
    answer_question("Who approves remote work requests?", config=no_rerank_config, log=False)
    assert mock_get_reranker.called is False

    mock_get_reranker.reset_mock()

    rerank_config = load_experiment_config('configs/hybrid_reranker.yaml')
    answer_question("Who approves remote work requests?", config=rerank_config, log=False)
    assert mock_get_reranker.called is True
    assert mock_get_reranker.return_value.rerank.call_args.kwargs['top_k'] == rerank_config.reranker.top_k


def test_manual_pipeline():
    response = answer_question("Who approves remote work requests?", config=None, log=False)
    print(f"RESPONSE:\n{response}")

test_manual_pipeline()
from unittest.mock import patch, MagicMock

from app.rag.generator import generate_answer


def _mock_llm():
    llm = MagicMock()
    llm.generate.return_value = "raw"
    llm.format_response.return_value = "answer text"
    llm.calculate_cost.return_value = 0.001
    return llm


@patch("app.rag.generator.get_llm_provider")
def test_generate_answer_passes_config_provider_and_model(mock_get_llm_provider):
    mock_get_llm_provider.return_value = _mock_llm()

    class FakeGeneration:
        provider = "openai"
        model = "gpt-x"

    class FakeConfig:
        generation = FakeGeneration()

    generate_answer("question", [], config=FakeConfig())

    mock_get_llm_provider.assert_called_once_with(provider="openai", model="gpt-x")


@patch("app.rag.generator.get_llm_provider")
def test_generate_answer_uses_defaults_when_no_config(mock_get_llm_provider):
    mock_get_llm_provider.return_value = _mock_llm()

    generate_answer("question", [], config=None)

    mock_get_llm_provider.assert_called_once_with(provider=None, model=None)


test_generate_answer_passes_config_provider_and_model()
test_generate_answer_uses_defaults_when_no_config()

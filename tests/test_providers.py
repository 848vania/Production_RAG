from app.rag.providers import get_llm_provider, OpenAIProvider, FakeLLMProvider


def test_get_llm_provider_testing_returns_fake():
    provider = get_llm_provider(provider='testing')
    assert isinstance(provider, FakeLLMProvider)


def test_get_llm_provider_openai_uses_model_override():
    provider = get_llm_provider(provider='openai', model='gpt-test')
    assert isinstance(provider, OpenAIProvider)
    assert provider.model == 'gpt-test'


def test_get_llm_provider_defaults_to_settings():
    from app.rag.providers import settings
    provider = get_llm_provider()
    assert isinstance(provider, OpenAIProvider) or isinstance(provider, FakeLLMProvider)
    if isinstance(provider, OpenAIProvider):
        assert provider.model == settings.openai_model


test_get_llm_provider_testing_returns_fake()
test_get_llm_provider_openai_uses_model_override()
test_get_llm_provider_defaults_to_settings()

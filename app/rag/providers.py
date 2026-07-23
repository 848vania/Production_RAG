# local libraries 
from app.schemas import OpenAIResponse
from app.config import Settings_Chat

from openai import OpenAI

settings = Settings_Chat()

class LLMProvider:
    def generate(self, prompt: str) -> str:
        raise NotImplementedError
    
    def format_response(self, response):
        raise NotImplementedError
    
class OpenAIProvider(LLMProvider):
    def __init__(self):
        super().__init__()
        self.client = OpenAI(api_key=settings.openai_api_key)
        self.model = settings.openai_model

    def generate(self, prompt: str) -> str:
        """
        Generate answer with OpenAI
        """
        self.response = self.client.responses.parse(
            model = self.model,
            input = prompt, 
            text_format = OpenAIResponse,
        )
        return self.response
    
    def format_response(self):
        # Return response of type 'OpenAISources' 

        return self.response.output_parsed.answer

class OllamaProvider(LLMProvider):
    def generate(self, prompt):
        """
        Optional local generation
        """

    def format_response(self):
        return

class FakeLLMProvider(LLMProvider):
    def __init__(self):
        super().__init__()

    def generate(self, prompt):
        """
        Used for tests
        """
        return 
    def format_response(self):
        return 

def get_llm_provider() -> LLMProvider:
    """
    Return provider based on settings
    """
    try:
        if settings.llm_provider == 'openai':
            return OpenAIProvider()
        elif settings.llm_provider == 'testing':
            return FakeLLMProvider()
    except Exception as e:
        print(f"Define a valid LLM Provider. Current is {settings.llm_provider} which raised error: {e}")  
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

    def calculate_cost(self):
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

    def calculate_cost(self):
        INPUT_PRICE_PER_1M = 0.15
        OUTPUT_PRICE_PER_1M = 0.60

        input_tokens = self.response.usage.input_tokens
        output_tokens = self.response.usage.output_tokens 

        input_cost = (input_tokens / 1_000_000) * INPUT_PRICE_PER_1M
        output_cost  = (output_tokens / 1_000_000) * OUTPUT_PRICE_PER_1M
        total_cost = input_cost + output_cost

        return total_cost

class OllamaProvider(LLMProvider):
    def generate(self, prompt):
        """
        Optional local generation
        """

    def format_response(self):
        return

    def calculate_cost(self):
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

    def calculate_cost(self):
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
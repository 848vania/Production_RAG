# local libraries 
from app.schemas import OpenAISources

from openai import OpenAI
from dotenv import load_dotenv
import os 

load_dotenv()

OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-5-mini-2025-08-07")
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai")

class LLMProvider:
    def generate(self, prompt: str) -> str:
        raise NotImplementedError
    
    def format_response(self, response):
        raise NotImplementedError
    
class OpenAIProvider(LLMProvider):
    def __init__(self):
        super().__init__()
        self.client = OpenAI() 
        self.model = OPENAI_MODEL

    def generate(self, prompt: str) -> str:
        """
        Generate answer with OpenAI
        """
        self.response = self.client.responses.parse(
            model = self.model,
            input = prompt, 
            text_format = OpenAISources,
        )
        return self.response
    
    def format_response(self):
        # Return response of type 'OpenAISources' 
        return self.response.output_parsed 

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
        if LLM_PROVIDER == 'openai':
            return OpenAIProvider()
        elif LLM_PROVIDER == 'testing':
            return FakeLLMProvider()
    except Exception as e:
        print(f"Define a valid LLM Provider. Current is {LLM_PROVIDER} which raised error: {e}")  
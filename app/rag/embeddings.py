import os 
import numpy as np 
from dotenv import load_dotenv
from app.schemas import Chunk

load_dotenv()

from langchain_openai import OpenAIEmbeddings


# TODO: Transform the chunks before sending 
# texts = [chunk.text for chunk in chunks]
class EmbeddingProvider:
    def embed_texts(self,texts:list[str]) ->list[list[float]]:
        # returns one vector per text
        raise NotImplementedError

    def embed_query(self,query:str) ->list[float]:
        # returns one vector
        raise NotImplementedError

class FakeEmbeddingProvider(EmbeddingProvider):
    def embed_texts(self, texts):
        return  [[0.1, 0.2, 0.3] for _ in texts]
        
    
    def embed_query(self, query):
        return [0.1, 0.2, 0.3]

class OpenAIEmbeddingProvider(EmbeddingProvider):
    def __init__(self):
        super().__init__()
        self.embeddings = OpenAIEmbeddings(model = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small"))

    
    def embed_texts(self,texts:list[str]) ->list[list[float]]:
        """
        Call OpenAI embeddings API.

        Generates embeddings using OpenAI 

        Args: 
            texts: List of input strings to embed 

        Returns: 
            A numpy array with shape (n,d) and dtype float32, 
            where n in the number of texts and d is the embedding dimension
        """

        if not isinstance(texts, list) or not all(isinstance(t, str) for t in texts):
            raise ValueError("Input 'texts' must be a list of Chunks")
        
        try:
            response = self.embeddings.embed_documents(texts = texts)
        except Exception as e:
            print(f"An error occured during OpenaAI embedding documents: {e}")
            return np.array([])

        embeddings_np = np.array(response, dtype=np.float32)

        return embeddings_np

    def embed_query(self,query:str) ->list[float]:
        """
        Embed one query.
        """
        try:
            query_vector = self.embeddings.embed_query(query)
        except Exception as e:
            print(f"An error occured during OpenAI embedding queries: {e}")
            return np.array([])
        
        query_np = np.array(query_vector, dtype=np.float32)
        
        return query_np
    

class LocalEmbeddingProvider(EmbeddingProvider):
    def embed_texts(self,texts:list[str]) ->list[list[float]]:
        """
        Use sentence-transformers locally.
        """


    def get_embedding_provider() ->EmbeddingProvider:
        """
        Return embedding provider based on settings.
        """
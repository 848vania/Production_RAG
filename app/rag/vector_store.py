# Local libraries 
from app.schemas import Document, Chunk
from app.rag.embeddings import * 
from app.config import Settings_Chat

# External libraries
import chromadb
from chromadb.config import Settings
from typing import List 

settings = Settings_Chat()
class VectorStore:
    def upsert_chunks(self, chunks, embeddings):
        raise NotImplementedError
    
    def search(self, query_embedding, top_k:int=5):
        raise NotImplementedError
    
    def reset(self):
        raise NotImplementedError
    
class ChromaVectorStore(VectorStore):
    def __init__(self, retrieve_metric):
        super().__init__()
        # 1. Intitalize the native persistent database 
        self.client = chromadb.PersistentClient(
            path="./chroma_db",
            settings=Settings(allow_reset=True)
        )

        # 2. Get or create a collection 
        self.collection = self.client.get_or_create_collection(
            name="my_synthetic_documen",
            metadata= {"hnsw:space": retrieve_metric}
        )

    def upsert_chunks(self, chunks, embeddings):
        """
        Store chunk text, metadata, and embeddings.
        """
        texts, metadatas, ids = self.add_custom_chunks(chunks)

        self.collection.add(
            documents = texts,
            embeddings = embeddings,
            metadatas = metadatas,
            ids =  ids
        )
    
    def search(self, query_embedding, top_k:int=10):
        """
        Return top-k matching chunks with scores
        """
        results =  self.collection.query(
            query_embeddings= [query_embedding],
            n_results= top_k
        )
        return results 

    def reset(self):
        self.client.reset()

    def add_custom_chunks(self, chunks):

        if isinstance(chunks[0], Chunk):
            print(f"It's istance")
            texts = [chunk.text for chunk in chunks]
            ids = [chunk.chunk_id for chunk in chunks]

            metadatas = [
                {
                    "doc_id": chunk.doc_id,
                    "doc_title": chunk.doc_title,
                    "section_title": chunk.section_title,
                    **chunk.metadata
                }
                for chunk in chunks
            ]
        else:
            print("It's NOT instance")
            texts = [chunk for chunk in chunks]
            metadatas = [
                {
                    "source": "docs",
                    "topic": f"topic_{i}"
                } 
                for i, _ in enumerate(chunks)
            ]
            ids = [f"id_{i}" for i,_ in enumerate(chunks)]

        # print(f"Texts:\n{texts}")
        # print(f"Metadatas:\n{metadatas}")
        # print(f"IDs:\n{ids}")

        return texts, metadatas, ids

    def add_custom_documents(self, docs: List[Document]):
        # Extract structural primitives out of your Pydantic schemas 
        texts = [doc.text for doc in docs]
        ids = [doc.doc_id for doc in docs]

        # Bundle all other non-text data into the metadata dictionary 
        metadatas = [
            {'title': doc.title, 'source_path': doc.source_path, **doc.metadata}
            for doc in docs
        ]

        # 3. Add directly to the native client 
        self.collection.add(
            documents = texts,
            metadatas=metadatas,
            ids = ids
        )

class QdrantVectorStore(VectorStore):
    def __init__(self):
        super().__init__()

    # TODO: Implement QDRANT vector store 

def get_vector_store():
    """
    Return vector store based on settings.
    """
    try:
        if settings.vector_db_provider == 'chroma':
            return ChromaVectorStore(settings.retrieve_metric)
        elif settings.vector_db_provider == 'qdrant':
            return QdrantVectorStore()
    except Exception as e:
        print(f"Define a valid VECTOR STORE provider. Current is {settings.vector_db_provider} which raised error: {e}")
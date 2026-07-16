from pydantic import BaseModel
from typing import List, Optional

class Document(BaseModel):
    doc_id: str  
    title: str 
    source_path: str 
    text: str 
    metadata: dict 

class Chunk(BaseModel):
    doc_id: str 
    doc_title: str
    section_title: str
    chunk_id: str
    text: str 
    metadata: dict 
    score: Optional[float] = None

class Source(BaseModel):
    document: str
    page: Optional[int] = None
    section: Optional[str] = None
    text: str
    score: float

class OpenAISources(BaseModel):
    answer: str
    document: list[str] = []
    section: list[str] = []
    chunk_id: list[str] = []

class OpenAIResponse(BaseModel):
    answer: str
    sources: list[OpenAISources]

class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    answer: str
    sources: List[Source]
    confidence: str
    latency_ms: float
    cost_usd: Optional[float] = None
    refused: bool
    reason: str 
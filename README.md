# Enterprise RAG Assistant

A production-style Retrieval-Augmented Generation system for answering questions over enterprise documents with citations, evaluation, and monitoring.

## Features
- Document ingestion
- Chunking and metadata extraction
- Vector search
- Hybrid retrieval
- Reranking
- LLM answer generation
- Source citations
- Refusal for unsupported questions
- Evaluation dashboard
- Cost and latency logging

## Architecture
TODO: Include a diagram or link to architecture.md.

## Tech Stack
- FastAPI
- Streamlit
- Qdrant / Chroma
- PostgreSQL / SQLite
- OpenAI / Anthropic / Gemini API
- Optional Ollama local model
- RAGAS or custom evaluation

# Installation steps 
1. Download Ollama
2. Download the models 
    jeffh/intfloat-multilingual-e5-small:q8_0
    qllama/bge-small-en-v1.5:latest          
    all-minilm:l6-v2                         
    llama3.1:latest

## Quick Start
1. Clone repo
2. Create virtual environment
3. Install requirements
4. Copy .env.example to .env
5. Run ingestion
6. Run API
7. Run frontend

## Demo
Add screenshots or a link to a recorded demo.

## Evaluation Results
Summarize Recall@K, faithfulness, citation accuracy, latency, and cost.

## Project Structure
Explain folders briefly.

## Future Improvements
- Access control
- Multi-user support
- Better reranking
- Production monitoring
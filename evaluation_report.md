# Architecture

## Overview
The system ingests documents, splits them into chunks, stores embeddings in a vector database, retrieves relevant context for a user question, and generates a cited answer using an LLM.

## Main Components
1. Document ingestion
2. Chunking
3. Embedding generation
4. Vector search
5. Keyword search
6. Hybrid retrieval
7. Reranking
8. Answer generation
9. Grounding/refusal logic
10. Logging and monitoring
11. Evaluation

## Data Flow
User question -> API -> retrieval -> reranking -> LLM -> cited answer -> logs

## Design Decisions
- Why RAG?
- Why hybrid search?
- Why citations?
- Why evaluation matters?
- Why provider abstraction for LLMs?

## Limitations
- Synthetic dataset
- No real enterprise authentication
- No advanced permission filtering yet
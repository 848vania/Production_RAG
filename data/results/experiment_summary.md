| Experiment | Retrieval | Reranker | Recall@5 | Reciprocal Rank | Citation Acc. | Refusal Acc. | Answer Correct. | Latency |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| vector_only | vector | no | 63.4% | 0.56 | 49.9% | 90.1% | 70.5% | 10.90s |
| keyword_only | keyword | no | 47.9% | 0.36 | 49.8% | 81.7% | 49.6% | 8.39s |
| hybrid | hybrid | no | 54.9% | 0.37 | 54.1% | 87.3% | 64.7% | 8.28s |
| hybrid_reranker | hybrid | yes | 63.4% | 0.60 | 52.2% | 91.5% | 67.6% | 16.88s |

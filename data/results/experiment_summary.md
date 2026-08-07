| Experiment | Retrieval | Reranker | Recall@5 | Reciprocal Rank | Citation Acc. | Refusal Acc. | Answer Correct. | Latency |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| vector_only | vector | no | 63.4% | 0.62 | 16.5% | 90.1% | 65.9% | 17.06s |
| keyword_only | keyword | no | 63.4% | 0.62 | 16.5% | 87.3% | 61.1% | 17.95s |
| hybrid | hybrid | no | 63.4% | 0.62 | 16.5% | 87.3% | 63.9% | 17.48s |
| hybrid_reranker | hybrid | yes | 63.4% | 0.62 | 16.5% | 91.5% | 65.1% | 20.90s |

from app.evaluation.run_retrieval_eval import *

summary = run_retrieval_evaluation()
print(json.dumps(summary, indent=2))
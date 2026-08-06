from app.evaluation.run_answer_eval import *

summary = run_answer_evaluation()
print(json.dumps(summary, indent=2))
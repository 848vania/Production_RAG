from app.database.connection import init_db
from app.monitoring.metrics import get_monitoring_summary
from app.rag.pipeline import answer_question

import json


def main():
    init_db()

    questions = [
        "Who approves remote work requests?",
        "what security requirements apply to remote work?",
        "Can employees work from Mars?",
    ]

    for question in questions:
        response = answer_question(question, log= True)
        print("Question: ", question)
        print("Answer: ", response['answer'])
        print("Refused: ", response['refused'])
        print("------")

    summary = get_monitoring_summary()

    print("Monitoring summary: ")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
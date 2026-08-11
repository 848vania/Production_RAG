from app.database.connection import Base, engine, SessionLocal
from app.database.crud import create_query_log, get_recent_query_logs


def setup_function():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def test_create_query_log():
    db = SessionLocal()

    try:
        log = create_query_log(
            db =db,
            question= "Who approves remote work?",
            answer = 'The direct manager and HR approve it. [Source 1]',
            sources = [
                {
                    'source_number': 1,
                    'document': 'Remote Work Policy',
                    'section': 'Approval Process',
                }
            ],
            confidence= 'high',
            latency_ms= 1200.0,
            cost_usd= 0.001,
            retrieval_type= 'hybrid',
            model_provider= 'openai',
            refused= False,
            reason= None,
        )

        assert log.id is not None
        assert log.question == 'Who approves remote work?'
        assert log.confidence == 'high'

    finally:
        db.close()


def test_get_recent_query_log():
    db = SessionLocal()

    try:
        create_query_log(
            db = db,
            question = 'Question 1',
            answer = 'Answer 1',
            sources = [],
            confidence= 'low',
            latency_ms= 100.0,
            refused= True,
            reason= 'insufficient_retrieved_context',
        )

        logs = get_recent_query_logs(db, limit=10)

        assert len(logs) == 1
        assert logs[0].question == 'Question 1'

    finally:
        db.close()


def test_get_recent_query_logs():
    db = SessionLocal()

    try:
        create_query_log(
            db=db,
            question="Question 1",
            answer="Answer 1",
            sources=[],
            confidence="low",
            latency_ms=100.0,
            refused=True,
            reason="insufficient_retrieved_context",
        )

        logs = get_recent_query_logs(db, limit=10)

        assert len(logs) == 1
        assert logs[0].question == "Question 1"

    finally:
        db.close()
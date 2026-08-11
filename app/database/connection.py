from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config import settings


engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread":  False}
    if settings.database_url.startswith('sqlite')
    else {},
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def get_db_session():
    """
    Create a new database session

    Use this in places where you need toread/write logs 
    """
    db = SessionLocal()
    try:
        return db 
    except Exception:
        db.close()
        raise 


def init_db():
    """
    Create database if they do not exist
    """
    from app.database.models import QueryLog

    Base.metadata.create_all(bind=engine)
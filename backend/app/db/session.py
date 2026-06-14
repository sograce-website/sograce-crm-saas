from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import DATABASE_URL

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    from app.models.tenant import Tenant
    from app.models.user import User
    from app.models.company import Company
    from app.models.contact import Contact
    from app.models.lead import Lead
    from app.models.email import Email
    from app.models.timeline import Timeline
    from app.models.task import Task

    Base.metadata.create_all(bind=engine)

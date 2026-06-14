from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.db.session import get_db
from app.models.company import Company
from app.models.contact import Contact
from app.models.lead import Lead
from app.models.email import Email
from app.models.task import Task

router = APIRouter()

@router.get("/summary")
def summary(db: Session = Depends(get_db)):
    return {
        "companies": db.query(func.count(Company.id)).scalar() or 0,
        "contacts": db.query(func.count(Contact.id)).scalar() or 0,
        "leads": db.query(func.count(Lead.id)).scalar() or 0,
        "emails": db.query(func.count(Email.id)).scalar() or 0,
        "tasks": db.query(func.count(Task.id)).scalar() or 0,
    }

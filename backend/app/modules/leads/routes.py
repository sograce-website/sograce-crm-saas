from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.lead import Lead

router = APIRouter()

@router.get("/")
def list_items(db: Session = Depends(get_db)):
    return db.query(Lead).order_by(Lead.id.desc()).limit(100).all()

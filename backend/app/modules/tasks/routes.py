from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.task import Task

router = APIRouter()

@router.get("/")
def list_items(db: Session = Depends(get_db)):
    return db.query(Task).order_by(Task.id.desc()).limit(100).all()

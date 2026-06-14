from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.timeline import Timeline

router = APIRouter()

@router.get("/")
def list_items(db: Session = Depends(get_db)):
    return db.query(Timeline).order_by(Timeline.id.desc()).limit(100).all()

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.contact import Contact

router = APIRouter()

@router.get("/")
def list_items(db: Session = Depends(get_db)):
    return db.query(Contact).order_by(Contact.id.desc()).limit(100).all()

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric, Date, Text
from datetime import datetime
from app.db.session import Base

class Lead(Base):
    __tablename__ = "leads"
    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, ForeignKey("tenants.id"), index=True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    contact_id = Column(Integer, ForeignKey("contacts.id"))
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    source = Column(String, default="MANUAL")
    status = Column(String, default="NEW")
    level = Column(String, default="C")
    score = Column(Integer, default=0)
    probability = Column(Integer, default=0)
    expected_amount = Column(Numeric(12, 2), default=0)
    next_followup = Column(Date, nullable=True)
    note = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

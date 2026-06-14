from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from datetime import datetime
from app.db.session import Base

class Email(Base):
    __tablename__ = "emails"
    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, ForeignKey("tenants.id"), index=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=True)
    contact_id = Column(Integer, ForeignKey("contacts.id"), nullable=True)
    direction = Column(String, nullable=False)
    subject = Column(Text, default="")
    body = Column(Text, default="")
    from_email = Column(String, default="")
    to_email = Column(Text, default="")
    message_id = Column(String, unique=True, index=True)
    thread_id = Column(String, default="")
    received_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from app.db.session import Base

class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, ForeignKey("tenants.id"), index=True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    first_name = Column(String, default="")
    last_name = Column(String, default="")
    job_title = Column(String, default="")
    email = Column(String, unique=True, index=True)
    phone = Column(String, default="")
    whatsapp = Column(String, default="")
    linkedin = Column(String, default="")
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

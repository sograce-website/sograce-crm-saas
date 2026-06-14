from fastapi import APIRouter
from app.modules.dashboard.routes import router as dashboard_router
from app.modules.companies.routes import router as companies_router
from app.modules.contacts.routes import router as contacts_router
from app.modules.leads.routes import router as leads_router
from app.modules.timeline.routes import router as timeline_router
from app.modules.tasks.routes import router as tasks_router

api_router = APIRouter()
api_router.include_router(dashboard_router, prefix="/dashboard", tags=["Dashboard"])
api_router.include_router(companies_router, prefix="/companies", tags=["Companies"])
api_router.include_router(contacts_router, prefix="/contacts", tags=["Contacts"])
api_router.include_router(leads_router, prefix="/leads", tags=["Leads"])
api_router.include_router(timeline_router, prefix="/timeline", tags=["Timeline"])
api_router.include_router(tasks_router, prefix="/tasks", tags=["Tasks"])

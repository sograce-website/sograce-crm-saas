from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import api_router
from app.db.session import init_db

app = FastAPI(
    title="SOGRACE CRM SaaS",
    version="M1.1",
    description="SOGRACE CRM SaaS - Database + Docker Foundation"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def root():
    return {
        "project": "SOGRACE CRM SaaS",
        "version": "M1.1",
        "status": "online"
    }

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(api_router, prefix="/api/v1")

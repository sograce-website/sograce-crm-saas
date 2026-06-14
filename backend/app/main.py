from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI(title="SOGRACE CRM SaaS", version="M2-UI")

templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/leads", response_class=HTMLResponse)
def leads(request: Request):
    return templates.TemplateResponse("leads.html", {"request": request})

@app.get("/api/status")
def status():
    return {"project": "SOGRACE CRM SaaS", "status": "running", "ui": "enabled"}

@app.get("/health")
def health():
    return {"status": "ok"}

import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.upload import router as upload_router
from app.api.routes.parser import router as parser_router
from app.api.routes.extractor import router as extractor_router
from app.api.routes.health import router as health_router
from app.api.routes.summary import router as summary_router
from app.api.routes.report import router as report_router
from app.api.routes.presentation import router as presentation_router


app = FastAPI(
    title="ProjectPulse AI",
    description="AI-powered Project Health Reporting Agent",
    version="1.0.0",
)

frontend_url = os.getenv("FRONTEND_URL", "http://localhost:5173")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        frontend_url,
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)
app.include_router(parser_router)
app.include_router(extractor_router)
app.include_router(health_router)
app.include_router(summary_router)
app.include_router(report_router)
app.include_router(presentation_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to ProjectPulse AI",
        "status": "running",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}
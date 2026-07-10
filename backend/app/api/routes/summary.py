from fastapi import APIRouter

from app.ai.gemini_service import generate_summary
from app.extractors.project_extractor import extract_project_summary
from app.health.health_engine import HealthEngine

router = APIRouter(
    prefix="/summary",
    tags=["AI Summary"],
)


@router.get("/{filename}")
def summary(filename: str):

    project = extract_project_summary(filename)

    health = HealthEngine(project).calculate()

    text = generate_summary(project, health)

    return {
        "summary": text
    }
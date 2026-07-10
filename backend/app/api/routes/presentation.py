from fastapi import APIRouter

from app.ai.gemini_service import generate_summary
from app.extractors.project_extractor import extract_project_summary
from app.health.health_engine import HealthEngine
from app.presentation.ppt_generator import PPTGenerator

router = APIRouter(
    prefix="/presentation",
    tags=["PowerPoint"],
)


@router.get("/{filename}")
def generate_presentation(filename: str):

    project = extract_project_summary(filename)

    health = HealthEngine(project).calculate()

    summary = generate_summary(project, health)

    ppt = PPTGenerator().generate(
        project,
        health,
        summary,
        filename,
    )

    return {
        "message": "Presentation generated successfully.",
        "file": ppt,
    }
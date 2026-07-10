from fastapi import APIRouter

from app.ai.gemini_service import generate_summary
from app.extractors.project_extractor import extract_project_summary
from app.health.health_engine import HealthEngine
from app.reports.pdf_generator import PDFGenerator

router = APIRouter(
    prefix="/report",
    tags=["PDF Report"],
)


@router.get("/{filename}")
def generate_report(filename: str):

    project = extract_project_summary(filename)

    health = HealthEngine(project).calculate()

    summary = generate_summary(project, health)

    pdf = PDFGenerator().generate(
        project,
        health,
        summary,
        filename,
    )

    return {
        "message": "PDF generated successfully.",
        "file": pdf,
    }
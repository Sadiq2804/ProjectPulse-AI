from fastapi import APIRouter

from app.extractors.project_extractor import extract_project_summary
from app.health.health_engine import HealthEngine

router = APIRouter(
    prefix="/health-score",
    tags=["Health Score"],
)


@router.get("/{filename}")
def calculate_health(filename: str):

    project = extract_project_summary(filename)

    engine = HealthEngine(project)

    return engine.calculate()
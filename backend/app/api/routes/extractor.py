from fastapi import APIRouter, HTTPException

from app.extractors.project_extractor import extract_project_summary

router = APIRouter(
    prefix="/extract",
    tags=["Extractor"],
)


@router.get("/{filename}")
def extract_data(filename: str):
    try:
        data = extract_project_summary(filename)
        return data

    except FileNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Excel file not found.",
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported project workbook format: {str(e)}",
       )
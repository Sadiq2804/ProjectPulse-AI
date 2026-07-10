from pathlib import Path

from fastapi import APIRouter, HTTPException

from app.services.parser_service import parse_excel

router = APIRouter(
    prefix="/parser",
    tags=["Parser"],
)


@router.get("/{filename}")
def parse_uploaded_excel(filename: str):
    file_path = Path("uploads") / filename

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail="File not found",
        )

    sheets = parse_excel(str(file_path))

    return {
        "filename": filename,
        "sheet_count": len(sheets),
        "sheets": list(sheets.keys()),
    }
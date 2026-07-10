from fastapi import APIRouter, File, HTTPException, UploadFile
from app.schemas.upload import UploadResponse
from app.services.file_service import save_uploaded_file

router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)


@router.post("/", response_model=UploadResponse)
async def upload_excel(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".xlsx"):
        raise HTTPException(
            status_code=400,
            detail="Only .xlsx project files are supported.",
        )

    save_uploaded_file(file)

    return UploadResponse(
        filename=file.filename,
        message="File uploaded successfully.",
    )
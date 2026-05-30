from fastapi import (
    APIRouter,
    File,
    HTTPException,
    UploadFile,
)

from app.services.file_service import (
    generate_job_id,
    save_uploaded_file,
    validate_file_extension,
)

from app.services.validation_service import (
    validate_excel_structure,
)
from datetime import datetime

router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)


@router.post("/")
async def upload_excel_file(
    file: UploadFile = File(...),
):

    # Validate extension
    if not validate_file_extension(file.filename):

        raise HTTPException(
            status_code=400,
            detail="Only .xlsx files are allowed",
        )

    # Generate job ID
    job_id = generate_job_id()

    # Save file
    saved_path = save_uploaded_file(
        file=file,
        job_id=job_id,
    )

    validate_excel_structure(saved_path)

    return {
        "message": "File uploaded successfully",
        "job_id": job_id,
        "filename": file.filename,
        "uploaded_at": datetime.utcnow().isoformat(),
        "saved_path": str(saved_path),
    }
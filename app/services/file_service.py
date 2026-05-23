import shutil
import uuid
from pathlib import Path

from fastapi import UploadFile

from fastapi import HTTPException

from app.config.settings import UPLOADS_DIR

ALLOWED_EXTENSIONS = [".xlsx"]


# Extension Validation Function
def validate_file_extension(filename: str) -> bool:

    file_extension = Path(filename).suffix.lower()

    return file_extension in ALLOWED_EXTENSIONS


# Function to save the uploaded file and generate a unique job id
def generate_job_id() -> str:

    return str(uuid.uuid4())


# Function to save the uploaded file to the uploads directory with a unique name
def save_uploaded_file(
    file: UploadFile,
    job_id: str,
) -> Path:

    UPLOADS_DIR.mkdir(exist_ok=True)

    file_path = UPLOADS_DIR / f"{job_id}.xlsx"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return file_path


# Get the path of the uploaded file based on the job id
def get_uploaded_file_path(job_id: str) -> Path:

    file_path = UPLOADS_DIR / f"{job_id}.xlsx"

    if not file_path.exists():

        raise HTTPException(
            status_code=404,
            detail="Uploaded file not found",
        )

    return file_path
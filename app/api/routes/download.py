from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.services.file_service import (
    get_output_file_path,
)

router = APIRouter(
    prefix="/download",
    tags=["Download"],
)


@router.get("/{job_id}")
def download_answers(job_id: str):

    output_file = get_output_file_path(job_id)

    return FileResponse(
        path=output_file,
        media_type="text/markdown",
        filename=output_file.name,
    )
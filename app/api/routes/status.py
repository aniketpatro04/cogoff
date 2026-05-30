from fastapi import APIRouter

from app.config.settings import (
    OUTPUTS_DIR,
    UPLOADS_DIR,
)

router = APIRouter(
    prefix="/status",
    tags=["Status"],
)


@router.get("/{job_id}")
def get_job_status(
    job_id: str,
):

    upload_exists = (
        UPLOADS_DIR /
        f"{job_id}.xlsx"
    ).exists()

    output_exists = (
        OUTPUTS_DIR /
        f"answers_{job_id}.md"
    ).exists()

    return {
        "job_id": job_id,
        "uploaded": upload_exists,
        "processed": output_exists,
        "download_ready": output_exists,
    }
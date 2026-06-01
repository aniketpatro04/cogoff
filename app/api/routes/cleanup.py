from fastapi import APIRouter
from app.services.file_service import delete_output_file

router = APIRouter(prefix="/cleanup", tags=["Processing"])


@router.post("/{job_id}")
def cleanup_output(job_id: str):

    deleted = delete_output_file(job_id)

    if deleted:
        return {
            "message": f"Output file for job {job_id} deleted successfully."
        }
    else:
        return {
            "message": f"No output file found for job {job_id}."
        }

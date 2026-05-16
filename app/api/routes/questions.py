from fastapi import APIRouter

from app.services.excel_service import (
    load_questions,
    get_unanswered_questions,
)

from app.config.settings import EXCEL_PATH

router = APIRouter(prefix="/questions", tags=["Questions"])


@router.get("/unanswered")
def get_unanswered():
    questions = load_questions(EXCEL_PATH)
    unanswered = get_unanswered_questions(questions)

    return {
        "count": len(unanswered),
        "questions": [
            {
                "id": q.id,
                "text": q.text,
            }
            for q in unanswered
        ],
    }
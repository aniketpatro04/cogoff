from fastapi import APIRouter

from app.services.excel_service import (
    load_questions,
    get_unanswered_questions,
)

from app.services.llm_service import generate_answer

from app.services.markdown_service import (
    initialize_markdown,
    append_qa_to_markdown,
    get_markdown_filename,
)

from app.config.settings import EXCEL_PATH

router = APIRouter(prefix="/process", tags=["Processing"])


@router.post("/")
def process_questions():

    markdown_file = get_markdown_filename("outputs")
    initialize_markdown(markdown_file)

    questions = load_questions(EXCEL_PATH)
    unanswered = get_unanswered_questions(questions)

    processed = []

    for question in unanswered[:10]:

        answer = generate_answer(question.text)

        append_qa_to_markdown(
            markdown_file,
            question.text,
            answer,
        )

        processed.append(
            {
                "id": question.id,
                "question": question.text,
            }
        )

    return {
        "processed_count": len(processed),
        "processed_questions": processed,
    }
from fastapi import APIRouter

from app.services.excel_service import (
    load_questions,
    get_unanswered_questions,
    mark_question_as_answered,
)

from app.services.file_service import get_uploaded_file_path
from app.services.llm_service import generate_answer

from app.services.markdown_service import (
    initialize_markdown,
    append_qa_to_markdown,
    get_markdown_filename,
)

import time

from app.config.settings import (
    EXCEL_PATH,
    OUTPUTS_DIR,
    get_random_delay,
)

from app.config.settings import EXCEL_PATH
from app.services.processing_service import process_questions_from_excel

router = APIRouter(prefix="/process", tags=["Processing"])

@router.post("/{job_id}")
def process_uploaded_file(job_id: str):

    excel_path = get_uploaded_file_path(job_id)

    result = process_questions_from_excel(
        excel_path=excel_path,
        job_id=job_id,
    )

    return result


# Version 1 - Legacy Code
# @router.post("/")
# def process_questions():

#     markdown_file = get_markdown_filename(OUTPUTS_DIR)
#     initialize_markdown(markdown_file)

#     questions = load_questions(EXCEL_PATH)
#     unanswered = get_unanswered_questions(questions)

#     processed = []

#     questions_to_process = unanswered[:10]

    
#     for idx, question in enumerate(questions_to_process):

#         answer = generate_answer(question.text)

#         append_qa_to_markdown(
#             markdown_file,
#             question.text,
#             answer,
#         )

#         processed.append(
#             {
#                 "id": question.id,
#                 "question": question.text,
#             }
#         )

#         mark_question_as_answered(EXCEL_PATH, question.id)

#         if idx < len(questions_to_process) - 1:

#             delay = get_random_delay()

#             print(f"Sleeping for {delay:.2f} seconds")

#             time.sleep(delay)

#     return {
#         "processed_count": len(processed),
#         "processed_questions": processed,
#     }
"""
Processing service for handling file processing logic, including reading questions from Excel, generating answers using LLM, and writing to markdown. Isoloates Business and Application logic from API routes for better maintainability and separation of concerns.
"""

import time

from app.config.settings import get_random_delay

from app.services.excel_service import (
    get_unanswered_questions,
    load_questions,
    mark_question_as_answered,
)

from app.services.llm_service import generate_answer

from app.services.markdown_service import (
    append_qa_to_markdown,
    get_output_markdown_path,
    initialize_markdown,
)
from app.services.validation_service import (
    validate_question_count,
)
from app.services.file_service import (
    delete_uploaded_file,
)





def process_questions_from_excel(
    excel_path,
    job_id,
):

    markdown_path = get_output_markdown_path(job_id)

    initialize_markdown(markdown_path)

    questions = load_questions(excel_path)

    validate_question_count(questions)

    unanswered = get_unanswered_questions(questions)

    processed = []
    failed = []

    for idx, question in enumerate(unanswered):

        try:

            answer = generate_answer(question.text)

            append_qa_to_markdown(
                markdown_path,
                question.text,
                answer,
            )

            mark_question_as_answered(
                excel_path,
                question.id,
            )

            processed.append(
                {
                    "id": question.id,
                    "question": question.text,
                }
            )

            # Delay
            if idx < len(unanswered) - 1:

                delay = get_random_delay()

                print(
                    f"Sleeping for {delay:.2f} seconds"
                )

                time.sleep(delay)

        except Exception as e:

            print(
                f"Error processing question "
                f"{question.id}: {str(e)}"
            )

            failed.append(
                {
                    "id": question.id,
                    "question": question.text,
                    "error": str(e),
                }
            )

    # Cleanup uploaded file after processing
    delete_uploaded_file(job_id)


    return {
        "processed_count": len(processed),
        "failed_count": len(failed),
        "output_file": str(markdown_path),
        "processed_questions": processed,
        "failed_questions": failed,
        "processed_questions": processed
    }
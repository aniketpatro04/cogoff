from ast import If

from app.services.excel_service import (
    load_questions,
    get_unanswered_questions,
    mark_question_as_answered,
)
from app.services.llm_service import generate_answer
from app.services.markdown_service import (
    initialize_markdown,
    append_qa_to_markdown,
)

from app.services.sheets_service import load_questions_from_sheets, mark_question_as_answered_sheet

from app.config.settings import EXCEL_PATH, MARKDOWN_PATH
from app.utils.logger import logger

import time
from app.config.settings import get_random_delay


# Toggle for Google Sheets Usage
USE_GOOGLE_SHEETS = True #Default is True, Set to False to use Excel instead

def process_question(question):

    try:
        logger.info(f"Processing question ID: {question.id}")

        answer = generate_answer(question.text)

        append_qa_to_markdown(
            MARKDOWN_PATH,
            question.text,
            answer,
        )

        if USE_GOOGLE_SHEETS:
             mark_question_as_answered_sheet(question.id)
        else:
            mark_question_as_answered(EXCEL_PATH, question.id)

        logger.info(f"Completed question ID: {question.id}")
        return True

    except Exception as e:
        logger.error(f"Failed question ID: {question.id} | Error: {e}")
        return False



def main():


    print("Hello! Let's Cognitively Offload You!")
    print("🚀 Starting AI Q&A Pipeline...")

    logger.info("Pipeline started")

    processed_count = 0
    failed_count = 0

    try:
        initialize_markdown(MARKDOWN_PATH)

        if USE_GOOGLE_SHEETS:
            questions = load_questions_from_sheets()
        else:
            questions = load_questions(EXCEL_PATH)

        unanswered = get_unanswered_questions(questions)

        if not unanswered:
            logger.info("No unanswered questions found. Nothing to process.")
            print("✅ No new questions to process.")
            return
        
        for idx,question in enumerate(unanswered):

            print(f"🔄 Processing Question {idx}: {question.text[:50]}...")
            success = process_question(question)

            if success:
                print(f"✅ Completed Question {idx}")
                processed_count += 1
            else:
                print(f"❌ Failed Question {idx}")
                failed_count += 1
            
            delay = get_random_delay()
            logger.info(f"Sleeping for {delay:.2f} seconds before next request")
            time.sleep(delay)

        
        # Code for v2.0.0
        # for question in unanswered:
        #     success = process_question(question)

        #     if success:
        #         processed_count += 1
        #     else:
        #         failed_count += 1

    except Exception as e:
        logger.critical(f"Pipeline failed | Error: {e}")

    logger.info(
        f"Pipeline finished | Processed: {processed_count} | Failed: {failed_count}"
    )

    print("🏁 Pipeline finished")
    print(f"Processed: {processed_count}, Failed: {failed_count}")


if __name__ == "__main__":
    main()

from services.excel_service import (
    load_questions,
    get_unanswered_questions,
    mark_question_as_answered,
)
from services.llm_service import generate_answer
from services.markdown_service import (
    initialize_markdown,
    append_qa_to_markdown,
)


from config.settings import EXCEL_PATH, MARKDOWN_PATH
from utils.logger import logger

# EXCEL_PATH = "data/questions.xlsx"
# MARKDOWN_PATH = "outputs/answers.md"

def process_question(question):

    try:
        logger.info(f"Processing question ID: {question.id}")

        answer = generate_answer(question.text)

        append_qa_to_markdown(
            MARKDOWN_PATH,
            question.text,
            answer,
        )

        mark_question_as_answered(EXCEL_PATH, question.id)

        logger.info(f"Completed question ID: {question.id}")
        return True

    except Exception as e:
        logger.error(f"Failed question ID: {question.id} | Error: {e}")
        return False

    # Old Code for v1.00
    # Generate the answer from the LLM
    # answer = generate_answer(question.text)

    # # Append the question and the generated answer to the md file
    # append_qa_to_markdown(
    #     MARKDOWN_PATH,
    #     question.text,
    #     answer
    # )

    # # Change the status of the question to answered
    # mark_question_as_answered(EXCEL_PATH, question.id)



def main():


    print("Hello! Let's Cognitively Offload You!")

    logger.info("Pipeline started")

    processed_count = 0
    failed_count = 0

    try:
        initialize_markdown(MARKDOWN_PATH)

        questions = load_questions(EXCEL_PATH)
        unanswered = get_unanswered_questions(questions)

        if not unanswered:
            logger.info("No unanswered questions found. Nothing to process.")
            print("✅ No new questions to process.")
            return

        for question in unanswered:
            success = process_question(question)

            if success:
                processed_count += 1
            else:
                failed_count += 1

    except Exception as e:
        logger.critical(f"Pipeline failed | Error: {e}")

    logger.info(
        f"Pipeline finished | Processed: {processed_count} | Failed: {failed_count}"
    )

    print(f"Processed: {processed_count}, Failed: {failed_count}")

    # Old Code for v1.00
    # initialize_markdown(MARKDOWN_PATH)

    # questions = load_questions(EXCEL_PATH)
    # unanswered = get_unanswered_questions(questions)

    # print("Processing Questions.....")


    # for question in unanswered:
    #     process_question(question)

    # print("Oflloading Done!")


if __name__ == "__main__":
    main()

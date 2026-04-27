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

EXCEL_PATH = "data/questions.xlsx"
MARKDOWN_PATH = "outputs/answers.md"

def process_question(question):

    # Generate the answer from the LLM
    answer = generate_answer(question.text)

    # Append the question and the generated answer to the md file
    append_qa_to_markdown(
        MARKDOWN_PATH,
        question.text,
        answer
    )

    # Change the status of the question to answered
    mark_question_as_answered(EXCEL_PATH, question.id)



def main():
    print("Hello! Let's Cognitively Offload You!")

    initialize_markdown(MARKDOWN_PATH)

    questions = load_questions(EXCEL_PATH)
    unanswered = get_unanswered_questions(questions)

    print("Processing Questions.....")


    for question in unanswered:
        process_question(question)

    print("Oflloading Done!")


if __name__ == "__main__":
    main()

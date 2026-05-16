import pandas as pd
from app.models.question import Question
from app.utils.logger import logger



# Parsing Questions for Correct Data Type Validation
def parse_question_text(value) -> str:
    if pd.isna(value):
        return ""
    return str(value).strip()


# Parsing the Answered Tag Value for Invalid Results
def parse_answered_flag(value) -> bool:
    if pd.isna(value):
        return False

    if isinstance(value, bool):
        return value

    if isinstance(value, str):
        return value.strip().lower() in ["true", "yes", "1"]

    if isinstance(value, (int, float)):
        return value == 1

    return False

# Question Length and Text Validation
def is_valid_question(question: Question) -> bool:
    if not question.text:
        return False

    if len(question.text) < 5:
        return False

    return True



# Gettting the List of all the questions
def load_questions(file_path: str) -> list[Question]:


    try:
        df = pd.read_excel(file_path)


        questions = []

        # The iterrows function allows to iterate over a table (dataframe) and returns the tupe containing the index and the data as a series
        for idx,row in df.iterrows():

            question_text = parse_question_text(row.get("Questions"))
            is_answered = parse_answered_flag(row.get("Answered"))

            questions.append(
                Question(
                    id = idx,
                    text = question_text,
                    is_answered=is_answered
                )
            )
        
        logger.info(f"Loaded {len(questions)} questions")
        return questions
    
    except Exception as e:
        logger.error(f"Failed to load Excel file | Error: {e}")
        raise


# Getting the list of Unanswered questions
# Using List Comprehension
def get_unanswered_questions(questions: list[Question]) -> list[Question]:

    filtered = []

    for q in questions:
        if not q.text:
            logger.warning(f"Skipping empty question at ID {q.id}")
            continue

        if not is_valid_question(q):
            logger.warning(f"Invalid question format at ID {q.id}: {q.text}")
            continue

        if not q.is_answered:
            filtered.append(q)

    logger.info(f"Found {len(filtered)} valid unanswered questions")
    return filtered
    
    # filtered = [q for q in questions if not q.is_answered and q.text]
    # logger.info(f"Found {len(filtered)} unanswered questions")
    # return filtered


    #return [q for q in questions if not q.is_answered and q.text.strip()]


# Function to mark the question as answered
def mark_question_as_answered(file_path: str, question_id: int) -> None:


    try:
        df = pd.read_excel(file_path)

        df.at[question_id, "Answered"] = True
        df.to_excel(file_path, index=False)

        logger.info(f"Marked question {question_id} as answered")

    except Exception as e:
        
        logger.error(f"Failed to update Excel | Question ID: {question_id} | Error: {e}")
        raise


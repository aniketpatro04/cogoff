import pandas as pd
from models.question import Question
from utils.logger import logger



# Gettting the List of all the questions
def load_questions(file_path: str) -> list[Question]:


    try:
        df = pd.read_excel(file_path)


        questions = []

        # The iterrows function allows to iterate over a table (dataframe) and returns the tupe containing the index and the data as a series
        for idx,row in df.iterrows():

            question_text = str(row.get("Questions", "")).strip()
            is_answered = bool(row.get("Answered", False))

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
    
    filtered = [q for q in questions if not q.is_answered and q.text]
    logger.info(f"Found {len(filtered)} unanswered questions")
    return filtered
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


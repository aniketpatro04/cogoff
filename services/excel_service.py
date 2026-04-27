import pandas as pd
from models.question import Question



# Gettting the List of all the questions
def load_questions(file_path: str) -> list[Question]:

    df = pd.read_excel(file_path)


    questions = []

    # The iterrows function allows to iterate over a table (dataframe) and returns the tupe containing the index and the data as a series
    for idx,row in df.iterrows():

        questions.append(
            Question(
                id = idx,
                text = row.get("Questions" , ""),
                is_answered=bool(row.get("Answered" , False))
            )
        )

    return questions


# Getting the list of Unanswered questions
# Using List Comprehension
def get_unanswered_questions(questions: list[Question]) -> list[Question]:
    return [q for q in questions if not q.is_answered and q.text.strip()]


# Function to mark the question as answered
def mark_question_as_answered(file_path: str, question_id: int) -> None:


    df = pd.read_excel(file_path)
    df.at[question_id, "Answered"] = True
    df.to_excel(file_path, index=False)


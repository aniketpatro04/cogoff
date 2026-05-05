import gspread
from google.oauth2 import service_account
from models.question import Question
from utils.logger import logger
from config.settings import (
    GOOGLE_SHEET_NAME,
    GOOGLE_WORKSHEET_NAME,
    GOOGLE_CREDENTIALS_FILE,
)

# Function to get the Google Sheet
def _get_worksheet():
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]

    creds = service_account.Credentials.from_service_account_file(
        GOOGLE_CREDENTIALS_FILE, scopes=scope
    )

    client = gspread.authorize(creds)

    sheet = client.open(GOOGLE_SHEET_NAME)
    worksheet = sheet.worksheet(GOOGLE_WORKSHEET_NAME)
    logger.info("Loading Worksheet Successful")

    return worksheet

def load_questions_from_sheets() -> list[Question]:

    try:
        worksheet = _get_worksheet()
        records = worksheet.get_all_records()

        questions = []
        for idx, row in enumerate(records, start=2):  # row index starts at 2 (header)
            question_text = str(row.get("Questions", "")).strip()
            is_answered = str(row.get("Answered", "")).lower() in ["true", "yes", "1"]

            questions.append(
                Question(
                    id=idx,
                    text=question_text,
                    is_answered=is_answered,
                )
            )

        logger.info(f"Loaded {len(questions)} questions from Google Sheets")
        return questions
    
    except Exception as e:
        logger.error(f"Failed to load from Google Sheets | Error: {e}")
        raise


def mark_question_as_answered_sheet(question_id: int) -> None:
    try:
        worksheet = _get_worksheet()
        worksheet.update_cell(question_id, 2, "TRUE")  # Column 2 = Answered

        logger.info(f"Marked question {question_id} as answered in Google Sheets")

    except Exception as e:
        logger.error(f"Failed to update Google Sheet | Error: {e}")
        raise
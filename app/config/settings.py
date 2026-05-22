"""
    File for configuring file paths, LLM Models and application wide settings.

    The File Paths are picked from the .env file of the application. In case no path is provided,
    the default location is chosen. 

    The Model name can be configured with the MODEL_NAME Setting
"""


import os
from dotenv import load_dotenv
import random
from pathlib import Path

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

OUTPUTS_DIR = BASE_DIR / "outputs"
LOGS_DIR = BASE_DIR / "logs"
UPLOADS_DIR = BASE_DIR / "uploads"
EXCEL_PATH = BASE_DIR / "data" / "questions.xlsx"

#EXCEL_PATH = os.getenv("EXCEL_PATH", "data/questions.xlsx") # Default Path incase variable is not found
MARKDOWN_PATH = os.getenv("MARKDOWN_PATH", "outputs/answers.md")


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.5-flash") # Defaults to Gemini-2.5-flash (Change If Required)


# Google Sheets Configuration
# Google Sheets Config

GOOGLE_SHEET_NAME = os.getenv("GOOGLE_SHEET_NAME" , "questions")
GOOGLE_WORKSHEET_NAME = os.getenv("GOOGLE_WORKSHEET_NAME", "Sheet1")
GOOGLE_SHEET_KEY = os.getenv("GOOGLE_SHEET_KEY" , "Your_Sheet_key_here") #change this to your own sheet key

GOOGLE_CREDENTIALS_FILE = os.getenv(
    "GOOGLE_CREDENTIALS_FILE",
    "credentials/google_service_account.json"
)


MIN_DELAY_SECONDS = int(os.getenv("MIN_DELAY_SECONDS", 5))
MAX_DELAY_SECONDS = int(os.getenv("MAX_DELAY_SECONDS", 10))

def get_random_delay() -> float:
    return random.uniform(MIN_DELAY_SECONDS, MAX_DELAY_SECONDS)

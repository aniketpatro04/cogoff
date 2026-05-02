"""
    File for configuring file paths, LLM Models and application wide settings.

    The File Paths are picked from the .env file of the application. In case no path is provided,
    the default location is chosen. 

    The Model name can be configured with the MODEL_NAME Setting
"""


import os
from dotenv import load_dotenv

load_dotenv()

EXCEL_PATH = os.getenv("EXCEL_PATH", "data/questions.xlsx") # Default Path incase variable is not found
MARKDOWN_PATH = os.getenv("MARKDOWN_PATH", "outputs/answers.md")

MODEL_NAME = os.getenv("MODEL_NAME", "gemini-1.5-flash") # Defaults to Gemini-1.5-flash

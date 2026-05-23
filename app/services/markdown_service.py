from datetime import datetime
import os

from app.utils.logger import logger

from pathlib import Path
from app.config.settings import OUTPUTS_DIR


def get_markdown_filename(base_path: str) -> str:
    date_str = datetime.now().date()
    return f"{base_path}/answers_{date_str}.md"

#Initialising a Markdown file if not already
def initialize_markdown(file_path: str) -> None:

    try:
        if not os.path.exists(file_path):

            with open(file_path, "w") as f:
                f.write(f"# Daily Q&A Log - {datetime.now().date()}\n\n")
            logger.info("Markdown file initialized")

    except Exception as e:
        logger.error(f"Failed to initialize markdown | Error: {e}")
        raise

    # if not os.path.exists(file_path):
    #     with open(file_path, "w") as f:
    #         f.write(f"# Daily Q&A Log - {datetime.now().date()}\n\n")



def append_qa_to_markdown(file_path: str, question: str, answer: str) -> None:

    try:
        with open(file_path, "a") as f:
            f.write(f"## Question\n{question}\n\n")
            f.write(f"### Answer\n{answer}\n\n")
            f.write("---\n\n")

        logger.info("Appended Q&A to markdown")

    except Exception as e:
        logger.error(f"Failed to write markdown | Error: {e}")
        raise

    # with open(file_path, "a") as f:
    #     f.write(f"## Question\n{question}\n\n")
    #     f.write(f"### Answer\n{answer}\n\n")
    #     f.write("---\n\n")


# Function to get the path of the markdown file for a given job id
def get_output_markdown_path(job_id: str) -> Path:

    OUTPUTS_DIR.mkdir(exist_ok=True)

    return OUTPUTS_DIR / f"answers_{job_id}.md"
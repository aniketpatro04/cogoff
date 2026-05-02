from datetime import datetime
import os

from utils.logger import logger

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
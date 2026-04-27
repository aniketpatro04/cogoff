from datetime import datetime
import os

#Initialising a Markdown file if not already
def initialize_markdown(file_path: str) -> None:


    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write(f"# Daily Q&A Log - {datetime.now().date()}\n\n")



def append_qa_to_markdown(file_path: str, question: str, answer: str) -> None:
    with open(file_path, "a") as f:
        f.write(f"## Question\n{question}\n\n")
        f.write(f"### Answer\n{answer}\n\n")
        f.write("---\n\n")
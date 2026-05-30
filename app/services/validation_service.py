from pathlib import Path

import pandas as pd

from fastapi import HTTPException

from app.config.settings import MAX_QUESTIONS_PER_REQUEST


REQUIRED_COLUMNS = [
    "Questions"
]

def validate_excel_structure(
    excel_path: Path,
) -> None:
    """
    Validate uploaded Excel file structure.
    """

    try:
        df = pd.read_excel(excel_path)

    except Exception as exc:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid Excel file: {str(exc)}"
        )

    for column in REQUIRED_COLUMNS:

        if column not in df.columns:

            raise HTTPException(
                status_code=400,
                detail=(
                    f"Required column '{column}' "
                    f"not found."
                )
            )

    if df.empty:

        raise HTTPException(
            status_code=400,
            detail="Excel file is empty."
        )

    questions = (
        df["Questions"]
        .dropna()
        .astype(str)
        .str.strip()
    )

    if questions.empty:

        raise HTTPException(
            status_code=400,
            detail=(
                "Questions column contains "
                "no valid questions."
            )
        )
    

def validate_question_count(
    questions: list,
) -> None:

    if len(questions) > MAX_QUESTIONS_PER_REQUEST:

        raise HTTPException(
            status_code=400,
            detail=(
                f"Maximum "
                f"{MAX_QUESTIONS_PER_REQUEST} "
                f"questions allowed per request."
            )
        )
from dataclasses import dataclass

@dataclass
class Question:
    id: int
    text: str
    is_answered: bool
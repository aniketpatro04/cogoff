# 🧠 AI Question Answering Pipeline (Phase 1)

## 📌 Overview

This project is a **Phase 1 implementation of an AI-powered question answering pipeline** designed to offload cognitive effort by automatically answering questions collected throughout the day.

The system reads user-defined questions from an Excel sheet, generates answers using an LLM (Google Gemini), and stores the results in a structured Markdown file.

---

## ⚙️ How It Works

The pipeline follows a simple flow:

```
Excel (Questions) → Filter Unanswered → LLM (Gemini) → Markdown Output → Mark as Answered
```

### Step-by-step:

1. Load questions from Excel
2. Filter unanswered questions
3. Send each question to the LLM
4. Generate answers
5. Append Q&A to a Markdown file
6. Mark the question as answered in Excel

---

## 📂 Project Structure

```
project/
│
├── main.py
│
├── services/
│   ├── excel_service.py
│   ├── llm_service.py
│   └── markdown_service.py
│
├── models/
│   └── question.py
│
├── data/
│   └── questions.xlsx
│
└── outputs/
    └── answers.md
```

---

## 🧩 Core Components

### 1. `excel_service.py`

Handles all Excel-related operations.

**Functions:**

* `load_questions(file_path: str) -> list[Question]`
  Loads all questions from the Excel file.

* `get_unanswered_questions(questions: list[Question]) -> list[Question]`
  Filters only unanswered questions.

* `mark_question_as_answered(file_path: str, question_id: int) -> None`
  Updates the Excel file to mark a question as answered.

---

### 2. `llm_service.py`

Handles interaction with the LLM (Google Gemini).

**Functions:**

* `generate_answer(question_text: str) -> str`
  Sends a question to the LLM and returns the generated answer.

---

### 3. `markdown_service.py`

Handles output formatting and storage.

**Functions:**

* `initialize_markdown(file_path: str) -> None`
  Creates the Markdown file if it does not exist and adds a header.

* `append_qa_to_markdown(file_path: str, question: str, answer: str) -> None`
  Appends a formatted Q&A entry to the Markdown file.

---

### 4. `models/question.py`

Defines the core data structure.

**Question Model:**

* `id: int`
* `text: str`
* `is_answered: bool`

---

### 5. `main.py`

Orchestrates the entire pipeline.

**Flow:**

* Initialize markdown file
* Load questions
* Filter unanswered
* Process each question:

  * Generate answer
  * Save to Markdown
  * Mark as answered

---

## 📊 Excel Sheet Format (IMPORTANT)

Your Excel file must follow this structure:

| Questions             | Answered |
| --------------------- | -------- |
| What is a black hole? | FALSE    |
| Why do stars twinkle? | FALSE    |

### Column Requirements:

* **Questions** → (Required) Text of the question
* **Answered** → (Required) Boolean (TRUE/FALSE or empty)

### Notes:

* Empty or blank questions are ignored
* Only rows with `Answered = FALSE` are processed

---

## 📄 Output Format

The generated Markdown file will look like:

```markdown
# Daily Q&A Log - YYYY-MM-DD

## Question
What is a black hole?

### Answer
A black hole is a region in space where gravity is so strong...

---

## Question
Why do stars twinkle?

### Answer
Stars twinkle due to atmospheric turbulence...

---
```

---

## 🚀 Setup Instructions

### 1. Install Dependencies

```bash
pip install pandas openpyxl python-dotenv google-generativeai
```

---

### 2. Create `.env` File

```
GEMINI_API_KEY=your_api_key_here
```

---

### 3. Run the Pipeline

```bash
python main.py
```

---

## ⚠️ Limitations (Phase 1)

* No logging
* No retry mechanism
* No scheduling (manual execution)
* No error handling for API failures
* Excel file is rewritten on each update

---

## 🔮 Next Steps (Phase 2)

* Add logging and observability
* Implement retry logic
* Automate execution using cron
* Improve error handling and robustness

---

## 🧠 Key Idea

This project is not just a script — it is the foundation of an **asynchronous AI knowledge processing pipeline** that can evolve into a full-scale AI system.

---

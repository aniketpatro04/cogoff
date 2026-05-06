# 🧠 AI Question Answering Pipeline (v2.0.0)

## 📌 Overview

This project is an AI-powered asynchronous question answering pipeline designed to help users offload cognitive effort by automatically collecting and answering questions.

Users can log questions throughout the day (via Excel or Google Sheets), and the system:

Fetches unanswered questions
Generates answers using an LLM (Google Gemini)
Stores results in structured Markdown files
Marks questions as answered
Runs safely with logging, retries, and rate limiting

---

## 🧩 Core Features (Phase 2 & 2.5)

✅ Multi-Input Support

1. Excel (local)
2. Google Sheets (via API)

## ⚙️ How It Works

The pipeline follows a simple flow:

```
Fetch Questions (From Excel or Sheets) → Filter for Unanswered Questions → Generate Answers (Using LLM) → Push answers to Markdown File → Mark the question as Answered
```

### Step-by-step:

1. Load questions from Excel / Sheets
2. Filter unanswered questions
3. Send each question to the LLM
4. Generate answers
5. Append Q&A to a Markdown file
6. Mark the question as answered in Excel

---

## 🔗 Google Sheets Setup

Create a Service Account (Google Cloud)
Enable:
Google Sheets API
Google Drive API

Download JSON key → place in:

credentials/google_service_account.json

Share your Google Sheet with:

<client_email from JSON>

Configure .env:

GEMINI_API_KEY=your_key

GOOGLE_SHEET_NAME=Your Sheet Name
GOOGLE_WORKSHEET_NAME=Sheet1
GOOGLE_CREDENTIALS_FILE=credentials/google_service_account.json


## 📊 Excel Sheet Format (IMPORTANT)

Your Excel file must follow this structure:

| Questions             | Answered |
| --------------------- | -------- |
| What is a black hole? | FALSE    |
| Why do stars twinkle? | FALSE    |

### Column Requirements:

* **Questions** → (Required) Text of the question
* **Answered** → (Required) Boolean (TRUE/FALSE or empty)

---

## 🚀 Setup and Run Instructions

### 1. Install Dependencies

Check out the pyproject.toml file for the dependencies and install the required dependencies using pip or uv.


---

### 2. Create and Update your `.env` File

```
GEMINI_API_KEY=your_api_key_here
GOOGLE_SHEET_KEY=yout_google_sheet_key
```

Add the Google Sheet Key if you want to access the sheet using a key. Should work without it as well if the service account is set up.

---

### 3. Create and Setup your Google Service Account

Setup a Service Account and Enable Dricve and Sheet Acess. 
Don't forget to share your questions sheet to this Service Account. 
(This UX will be improved in Phase 3)

---

### 4. Run the Pipeline

You can run the pipeline using the below command or using uv 

```bash
python main.py
```

```uv
un run main.py
```

---

## 🔮 Next Steps (Phase 3)

* Add And Compose Into Docker File
* UI Improvements
* Rate Limits for LLM Calls
* Better Scheduling UX

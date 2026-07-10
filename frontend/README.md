# ProjectPulse AI 🚀

## Overview

ProjectPulse AI is an AI-powered Project Health Reporting Agent that analyzes Microsoft Excel project workbooks and automatically generates project insights, dashboards, executive summaries, PDF reports, and PowerPoint presentations.

---

## Features

- 📂 Upload Excel Project Workbook (.xlsx/.xls)
- 📊 Automatic Project Data Extraction
- 📈 Project Health Score Calculation
- 🚦 RAG (Red-Amber-Green) Analysis
- 📋 Executive Summary Generation
- 📄 PDF Report Generation
- 📽️ PowerPoint Presentation Generation
- 🤖 Gemini AI Integration with Local Fallback

---

## Tech Stack

### Backend
- FastAPI
- Pandas
- Pydantic
- ReportLab
- python-pptx
- Google Gemini API

### Frontend
- React
- Vite
- Material UI
- Axios
- Recharts

---

## Folder Structure

```text
ProjectPulse-AI/
├── backend/
├── frontend/
├── README.md
└── .gitignore
```

---

## Installation

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## API Endpoints

- POST /upload
- GET /extract/{filename}
- GET /health-score/{filename}
- GET /summary/{filename}
- GET /report/{filename}
- GET /presentation/{filename}

---

## Gemini AI Fallback

If the Gemini API quota is exceeded, ProjectPulse AI automatically generates a local executive summary so the application remains functional without interruption.

---

## Screenshots

(Add your screenshots here)

- Dashboard
- KPI Cards
- Charts
- Task Table
- PDF Report
- PowerPoint Presentation

---

## Author

**Sadiq Hussain Ansari**
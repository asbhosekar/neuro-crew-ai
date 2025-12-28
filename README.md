# 🧠 Neuro Patient Tracker

**AI-powered Patient Tracking System for Neurologists with Prognosis Analysis**

Built using Microsoft AutoGen multi-agent framework.

## 🎯 Overview

A comprehensive patient tracking system designed for neurologists to:
- Track patient visits and neurological assessments over time
- Monitor conditions: Epilepsy, Migraines, Parkinson's, MS, etc.
- Generate prognosis reports with trend analysis
- Predict condition trajectories based on historical data

## 🤖 Agent Architecture

| Agent | Role |
|-------|------|
| **Clinical Architect** | Designs data models, ensures HIPAA compliance |
| **Backend Developer** | Builds FastAPI services, database layer |
| **Prognosis Analyst** | Analyzes trends, predicts trajectories |
| **QA Validator** | Tests code, validates medical logic |
| **Report Generator** | Creates prognosis reports, summaries |
| **Documentation Agent** | Generates API docs, user guides |

## 📁 Project Structure

```
neuro-patient-tracker/
├── src/
│   ├── agents/           # AutoGen agent definitions
│   ├── models/           # Pydantic data models
│   ├── services/         # Business logic
│   ├── api/              # FastAPI endpoints
│   └── config/           # Configuration
├── tests/                # Unit & integration tests
├── output/               # Generated artifacts
└── docs/                 # Documentation
```

## 🚀 Quick Start

```bash
# Create virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows

# Install dependencies
pip install -e ".[dev]"

# Set up environment
copy .env.example .env
# Edit .env with your OPENAI_API_KEY

# Run the system
python -m src.main
```

## 📊 Key Features

- **Patient Management**: CRUD operations for patient records
- **Visit Tracking**: Log appointments with neurological assessments
- **Prognosis Engine**: Longitudinal analysis of patient condition
- **Trend Analysis**: Track symptom severity, medication efficacy
- **Report Generation**: Clinical summaries and prognosis reports

## 🔧 Tech Stack

- **Framework**: Microsoft AutoGen
- **LLM**: OpenAI GPT-4o-mini
- **API**: FastAPI
- **Database**: SQLAlchemy + SQLite
- **Validation**: Pydantic v2

---
*Built with AI-powered multi-agent collaboration*

# NeuroCrew AI - Cumulative Work Log

## Session: December 28, 2025

### Project Overview
**Name:** NeuroCrew AI (neuro-crew-ai)  
**GitHub:** https://github.com/asbhosekar/neuro-crew-ai  
**Purpose:** AI-powered Patient Tracking System for Neurologists with Prognosis Analysis  
**Framework:** Microsoft AutoGen 0.4+ (pyautogen)

---

## Work Completed

### 1. Clinical Agents Created

| Agent | File | Purpose |
|-------|------|---------|
| **BaseAgent** | `src/agents/base_agent.py` | Abstract base class for all agents |
| **NeurologistAgent** | `src/agents/neurologist.py` | Primary clinical expert - red flags, workup recommendations, cognitive score interpretation |
| **PrognosisAnalystAgent** | `src/agents/prognosis_analyst.py` | Trend analysis, trajectory prediction, risk assessment |
| **TreatmentAdvisorAgent** | `src/agents/treatment_advisor.py` | Treatment recommendations, first-line treatments, escalation criteria |
| **ReportGeneratorAgent** | `src/agents/report_generator.py` | Clinical documentation, structured reports |
| **QAValidatorAgent** | `src/agents/qa_validator.py` | Data validation, assessment score validation, vital signs validation |
| **ClinicalArchitectAgent** | `src/agents/clinical_architect.py` | System architecture for clinical workflows |

### 2. AutoGen Orchestration

**File:** `src/orchestrator.py`

- **NeuroCrew class** - Main orchestrator using `RoundRobinGroupChat`
- **SingleAgentChat class** - For direct single-agent consultations
- Termination conditions: `MaxMessageTermination` + `TextMentionTermination`
- Async conversation flow with `run_stream()`

**Key Methods:**
- `run_conversation(task, patient_id)` - Multi-agent collaboration
- `run_prognosis_analysis(patient_data)` - Specialized prognosis workflow
- `consult(question)` - General clinical consultation
- `consult_neurologist/prognosis/treatment()` - Single agent consultations

### 3. Main Entry Point

**File:** `src/main.py`

Interactive CLI menu:
1. Demo with sample patient (multi-agent)
2. Single agent demo (Neurologist)
3. Single agent demo (Prognosis)
4. Single agent demo (Treatment)
5. Show cost summary
0. Exit

### 4. HIPAA-Compliant Audit Logging

**File:** `src/logging/audit_logger.py`

| Log File | Purpose | Retention |
|----------|---------|-----------|
| `logs/audit.log` | System events, conversation start/end | 365 days |
| `logs/agents.log` | Clinical conversations with content | 50MB × 20 files |
| `logs/phi_access.log` | PHI access tracking (hashed patient IDs) | 7 years |
| `logs/app.log` | General application logs | 10MB × 10 files |

**Key Features:**
- PHI patient IDs are SHA-256 hashed (HIPAA compliant)
- Correlation IDs link related events
- Structured JSON logging
- `AuditEventType` enum for event classification

**Event Types:**
- `SYSTEM_START`, `SYSTEM_STOP`
- `AGENT_INITIALIZED`, `AGENT_MESSAGE`
- `AGENT_CONVERSATION_START`, `AGENT_CONVERSATION_END`
- `PHI_ACCESS`, `PHI_CREATE`, `PHI_UPDATE`, `PHI_DELETE`
- `PROGNOSIS_GENERATED`, `TREATMENT_SUGGESTED`

### 5. LLM Runtime Telemetry

**File:** `src/logging/telemetry.py`

| Feature | Description |
|---------|-------------|
| Token Tracking | Input/output/total tokens per call |
| Cost Calculation | Real-time cost based on model pricing |
| Latency Metrics | Response time per LLM call |
| Session Reports | JSON + TXT summary reports |
| JSONL Logging | `logs/llm_telemetry.jsonl` for analysis |

**Model Pricing (per 1K tokens):**
```python
MODEL_PRICING = {
    "gpt-4o-mini": {"input": 0.00015, "output": 0.0006},
    "gpt-4o": {"input": 0.005, "output": 0.015},
    "gpt-4-turbo": {"input": 0.01, "output": 0.03},
}
```

**Note:** Token tracking infrastructure is in place but requires deeper AutoGen integration to capture actual LLM calls.

### 6. Configuration

**File:** `src/config/settings.py`

- `OPENAI_API_KEY` - from .env or environment
- `OPENAI_MODEL` - default: gpt-4o-mini
- `LOGS_DIR` - default: logs/
- `DEBUG` - debug mode flag

### 7. Dependencies Updated

**File:** `pyproject.toml`

```toml
dependencies = [
    "pyautogen>=0.2.0",
    "openai>=1.0.0",
    "pydantic>=2.0.0",
    "fastapi>=0.100.0",
    "uvicorn>=0.23.0",
    "sqlalchemy>=2.0.0",
    "python-dotenv>=1.0.0",
    "opentelemetry-api>=1.20.0",
    "opentelemetry-sdk>=1.20.0",
    "opentelemetry-exporter-otlp>=1.20.0",
]
```

---

## Project Structure (Final)

```
neuro-crew-ai/
├── pyproject.toml
├── README.md
├── cumulative-work-log.md
├── .env                          # OPENAI_API_KEY (not in git)
├── logs/
│   ├── audit.log
│   ├── agents.log
│   ├── phi_access.log
│   ├── app.log
│   ├── autogen_trace.log
│   ├── llm_telemetry.jsonl
│   └── session_*_report.json/txt
└── src/
    ├── __init__.py
    ├── main.py                   # Entry point
    ├── orchestrator.py           # AutoGen orchestration
    ├── agents/
    │   ├── __init__.py
    │   ├── base_agent.py
    │   ├── neurologist.py
    │   ├── prognosis_analyst.py
    │   ├── treatment_advisor.py
    │   ├── report_generator.py
    │   ├── qa_validator.py
    │   ├── clinical_architect.py
    │   └── backend_developer.py
    ├── config/
    │   ├── __init__.py
    │   └── settings.py
    ├── logging/
    │   ├── __init__.py
    │   ├── audit_logger.py
    │   └── telemetry.py
    └── models/
        ├── __init__.py
        └── schemas.py
```

---

## How to Run

```powershell
cd c:\Zero_to_agentic\agentic-sdlc-autogen
python -m src.main
```

---

## Key Technical Decisions

1. **AutoGen 0.4+ API** - Using new `autogen_agentchat` imports instead of deprecated `autogen`
2. **RoundRobinGroupChat** - For multi-agent collaboration
3. **Async/Await** - All conversations are async with `asyncio.run()`
4. **PHI Hashing** - Patient IDs hashed with SHA-256 for HIPAA compliance
5. **Structured Logging** - JSON format for easy parsing and analysis
6. **Correlation IDs** - UUID-based tracking across related log events

---

## Known Limitations / Future Work

1. **LLM Telemetry Integration** - Token tracking infrastructure exists but needs deeper AutoGen model client wrapping to capture actual usage
2. **Database Integration** - SQLAlchemy is included but patient database not yet implemented
3. **FastAPI Endpoints** - Web API not yet built (FastAPI/Uvicorn ready)
4. **Unit Tests** - Test framework configured but tests not yet written
5. **Authentication** - No user auth yet (needed for HIPAA compliance)

---

## Git Commits This Session

1. Initial agent structure
2. Created 4 clinical agents (Neurologist, Report Generator, QA Validator, Treatment Advisor)
3. Added AutoGen orchestrator and main entry point
4. Fixed AutoGen 0.4+ API compatibility
5. Added HIPAA-compliant audit logging system
6. Added LLM runtime telemetry for cost tracking
7. Fixed telemetry method signatures
8. Added clinical conversation logging to agents.log

---

## Next Session Ideas

- [ ] Implement actual LLM token capture in telemetry
- [ ] Add patient database with SQLAlchemy
- [ ] Build FastAPI REST endpoints
- [ ] Add user authentication for HIPAA
- [ ] Write unit tests
- [ ] Add more specialized agents (Pharmacist, Radiologist, etc.)
- [ ] Implement Selector/SelectorGroupChat for dynamic agent selection

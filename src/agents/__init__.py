"""
Neuro Patient Tracker - Agent Definitions

AutoGen agents for the multi-agent neurology patient tracking system.
"""

from .base_agent import BaseAgent
from .clinical_architect import ClinicalArchitectAgent
from .prognosis_analyst import PrognosisAnalystAgent
from .neurologist import NeurologistAgent
from .report_generator import ReportGeneratorAgent
from .qa_validator import QAValidatorAgent
from .treatment_advisor import TreatmentAdvisorAgent

# Technical agents (optional)
from .backend_developer import BackendDeveloperAgent

__all__ = [
    # Base
    "BaseAgent",
    # Clinical Agents
    "ClinicalArchitectAgent",
    "PrognosisAnalystAgent", 
    "NeurologistAgent",
    "ReportGeneratorAgent",
    "QAValidatorAgent",
    "TreatmentAdvisorAgent",
    # Technical Agents
    "BackendDeveloperAgent",
]

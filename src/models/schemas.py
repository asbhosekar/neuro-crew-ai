"""
Neuro Patient Tracker - Data Models

Pydantic models for Patient, Visit, and Prognosis tracking.
"""
from datetime import date, datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


# =============================================================================
# Enums
# =============================================================================

class Gender(str, Enum):
    """Patient gender options."""
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class NeurologicalCondition(str, Enum):
    """Supported neurological conditions."""
    EPILEPSY = "epilepsy"
    MIGRAINE = "migraine"
    PARKINSONS = "parkinsons"
    MULTIPLE_SCLEROSIS = "multiple_sclerosis"
    ALZHEIMERS = "alzheimers"
    STROKE = "stroke"
    NEUROPATHY = "neuropathy"
    OTHER = "other"


class PrognosisTrend(str, Enum):
    """Prognosis trend indicators."""
    IMPROVING = "improving"
    STABLE = "stable"
    DECLINING = "declining"
    UNKNOWN = "unknown"


class SeverityLevel(str, Enum):
    """Severity classification."""
    MILD = "mild"
    MODERATE = "moderate"
    SEVERE = "severe"
    CRITICAL = "critical"


# =============================================================================
# Patient Models
# =============================================================================

class PatientBase(BaseModel):
    """Base patient information."""
    first_name: str = Field(..., min_length=1, max_length=100)
    last_name: str = Field(..., min_length=1, max_length=100)
    date_of_birth: date
    gender: Gender
    email: Optional[str] = None
    phone: Optional[str] = None
    primary_condition: NeurologicalCondition


class PatientCreate(PatientBase):
    """Model for creating a new patient."""
    pass


class Patient(PatientBase):
    """Full patient model with ID and metadata."""
    id: str = Field(..., description="Unique patient identifier")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = True

    class Config:
        from_attributes = True


# =============================================================================
# Visit Models
# =============================================================================

class VitalSigns(BaseModel):
    """Patient vital signs during visit."""
    blood_pressure_systolic: Optional[int] = None
    blood_pressure_diastolic: Optional[int] = None
    heart_rate: Optional[int] = None
    temperature: Optional[float] = None
    weight_kg: Optional[float] = None


class NeurologicalAssessment(BaseModel):
    """Neurological examination results."""
    # Cognitive scores (0-30 scale, higher = better)
    mmse_score: Optional[int] = Field(None, ge=0, le=30, description="Mini-Mental State Exam")
    moca_score: Optional[int] = Field(None, ge=0, le=30, description="Montreal Cognitive Assessment")
    
    # Motor function (0-100 scale, higher = better)
    motor_function_score: Optional[int] = Field(None, ge=0, le=100)
    
    # Pain/Symptom severity (0-10 scale, lower = better)
    symptom_severity: Optional[int] = Field(None, ge=0, le=10)
    seizure_frequency: Optional[int] = Field(None, ge=0, description="Episodes per month")
    
    # Additional observations
    notes: Optional[str] = None


class MedicationRecord(BaseModel):
    """Medication information."""
    name: str
    dosage: str
    frequency: str
    start_date: date
    end_date: Optional[date] = None
    is_active: bool = True
    side_effects: Optional[str] = None


class VisitBase(BaseModel):
    """Base visit information."""
    patient_id: str
    visit_date: datetime = Field(default_factory=datetime.utcnow)
    chief_complaint: str
    vitals: Optional[VitalSigns] = None
    assessment: Optional[NeurologicalAssessment] = None
    medications: list[MedicationRecord] = []
    diagnosis_notes: Optional[str] = None
    treatment_plan: Optional[str] = None
    follow_up_date: Optional[date] = None


class VisitCreate(VisitBase):
    """Model for creating a new visit."""
    pass


class Visit(VisitBase):
    """Full visit model with ID and metadata."""
    id: str = Field(..., description="Unique visit identifier")
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True


# =============================================================================
# Prognosis Models
# =============================================================================

class TrendDataPoint(BaseModel):
    """Single data point in trend analysis."""
    visit_date: datetime
    score: float
    metric_name: str


class PrognosisAnalysis(BaseModel):
    """Prognosis analysis results."""
    patient_id: str
    analysis_date: datetime = Field(default_factory=datetime.utcnow)
    condition: NeurologicalCondition
    
    # Trend analysis
    overall_trend: PrognosisTrend
    cognitive_trend: Optional[PrognosisTrend] = None
    motor_trend: Optional[PrognosisTrend] = None
    symptom_trend: Optional[PrognosisTrend] = None
    
    # Scores and predictions
    current_severity: SeverityLevel
    predicted_severity_3mo: Optional[SeverityLevel] = None
    predicted_severity_6mo: Optional[SeverityLevel] = None
    
    # Trend data for visualization
    trend_data: list[TrendDataPoint] = []
    
    # Clinical insights
    summary: str
    recommendations: list[str] = []
    risk_factors: list[str] = []
    
    # Confidence
    confidence_score: float = Field(..., ge=0, le=1)


class PrognosisReport(BaseModel):
    """Complete prognosis report for a patient."""
    id: str
    patient: Patient
    analysis: PrognosisAnalysis
    visit_history: list[Visit] = []
    generated_at: datetime = Field(default_factory=datetime.utcnow)
    generated_by: str = "PrognosisAnalystAgent"

    class Config:
        from_attributes = True

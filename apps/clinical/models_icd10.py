"""
Core data entities, enums, and types for ICD-10 Diagnostics & Pathology Taxonomy.
"""

from typing import Dict, List, Optional, Set, Tuple, Any
from dataclasses import dataclass, field
from enum import Enum


class DiagnosticRiskTier(Enum):
    EMERGENCY = "EMERGENCY"
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MODERATE = "MODERATE"
    MILD = "MILD"


@dataclass
class ICD10DiagnosticRecord:
    code: str
    preferred_name: str
    chapter_name: str
    chapter_range: str
    risk_tier: DiagnosticRiskTier
    key_symptoms: List[str]
    diagnostic_criteria: List[str]
    differential_diagnoses: List[str]
    first_line_drug_classes: List[str]
    contraindicated_drug_classes: List[str]
    required_laboratory_workup: List[str]
    lifestyle_management_guidelines: List[str]

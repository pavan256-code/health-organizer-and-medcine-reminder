"""
Core data entities, enums, and types for Clinical Pharmacology & Interaction Surveillance.
"""

from typing import Dict, List, Optional, Set, Tuple, Any
from dataclasses import dataclass, field
from enum import Enum


class InteractionSeverity(Enum):
    CONTRAINDICATED = "CONTRAINDICATED"
    MAJOR = "MAJOR"
    MODERATE = "MODERATE"
    MINOR = "MINOR"
    THERAPEUTIC_DUPLICATION = "THERAPEUTIC_DUPLICATION"
    UNKNOWN = "UNKNOWN"


class EvidenceLevel(Enum):
    EXCELLENT_RCT = "EXCELLENT_RCT"
    WELL_DOCUMENTED = "WELL_DOCUMENTED"
    THEORETICAL = "THEORETICAL"
    CASE_REPORTS = "CASE_REPORTS"


class CYPEnzyme(Enum):
    CYP1A2 = "CYP1A2"
    CYP2B6 = "CYP2B6"
    CYP2C9 = "CYP2C9"
    CYP2C19 = "CYP2C19"
    CYP2D6 = "CYP2D6"
    CYP2E1 = "CYP2E1"
    CYP3A4 = "CYP3A4"
    CYP3A5 = "CYP3A5"


@dataclass
class DrugInteractionRecord:
    pair_id: str
    primary_drug: str
    secondary_drug: str
    severity: InteractionSeverity
    mechanism_of_action: str
    clinical_effect: str
    risk_summary: str
    management_guidelines: str
    evidence_level: EvidenceLevel
    cyp_pathway: Optional[CYPEnzyme] = None
    onset_timeline: str = "RAPID"
    monitoring_parameters: List[str] = field(default_factory=list)


@dataclass
class DrugMonograph:
    name: str
    pharmacological_class: str
    summary_description: str
    primary_indications: List[str]
    contraindications: List[str]
    black_box_warnings: List[str]
    standard_dosage_adult: str
    renal_adjustment_threshold: str
    hepatic_impairment_guidance: str
    adverse_reactions_common: List[str]
    adverse_reactions_severe: List[str]

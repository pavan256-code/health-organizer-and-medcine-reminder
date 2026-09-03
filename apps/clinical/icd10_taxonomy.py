"""
Comprehensive Clinical Diagnostics & ICD-10 Pathology Classification Engine.
Aggregates chapter-specific diagnostic taxonomy registries into a unified search engine.
"""

from typing import Dict, List, Optional, Any
from apps.clinical.models_icd10 import DiagnosticRiskTier, ICD10DiagnosticRecord
from apps.clinical.icd10_circulatory import REGISTRY_CIRCULATORY
from apps.clinical.icd10_respiratory import REGISTRY_RESPIRATORY
from apps.clinical.icd10_endocrine import REGISTRY_ENDOCRINE
from apps.clinical.icd10_digestive import REGISTRY_DIGESTIVE
from apps.clinical.icd10_musculoskeletal import REGISTRY_MUSCULOSKELETAL
from apps.clinical.icd10_neurological import REGISTRY_NEUROLOGICAL

CLINICAL_ICD10_REGISTRY: Dict[str, ICD10DiagnosticRecord] = {}

CLINICAL_ICD10_REGISTRY.update(REGISTRY_CIRCULATORY)
CLINICAL_ICD10_REGISTRY.update(REGISTRY_RESPIRATORY)
CLINICAL_ICD10_REGISTRY.update(REGISTRY_ENDOCRINE)
CLINICAL_ICD10_REGISTRY.update(REGISTRY_DIGESTIVE)
CLINICAL_ICD10_REGISTRY.update(REGISTRY_MUSCULOSKELETAL)
CLINICAL_ICD10_REGISTRY.update(REGISTRY_NEUROLOGICAL)


class ICD10DiagnosticsEngine:
    """High-performance diagnostic search and clinical decision support engine."""

    @classmethod
    def get_by_code(cls, code: str) -> Optional[ICD10DiagnosticRecord]:
        return CLINICAL_ICD10_REGISTRY.get(code.strip().lower())

    @classmethod
    def search_by_name(cls, query: str) -> List[ICD10DiagnosticRecord]:
        q = query.strip().lower()
        return [
            rec for rec in CLINICAL_ICD10_REGISTRY.values()
            if q in rec.preferred_name.lower() or q in rec.code.lower()
        ]

    @classmethod
    def search_by_symptom(cls, symptom: str) -> List[ICD10DiagnosticRecord]:
        s = symptom.strip().lower()
        return [
            rec for rec in CLINICAL_ICD10_REGISTRY.values()
            if any(s in sym.lower() for sym in rec.key_symptoms)
        ]

    @classmethod
    def get_by_risk_tier(cls, tier: DiagnosticRiskTier) -> List[ICD10DiagnosticRecord]:
        return [
            rec for rec in CLINICAL_ICD10_REGISTRY.values()
            if rec.risk_tier == tier
        ]

    @classmethod
    def get_total_conditions_count(cls) -> int:
        return len(CLINICAL_ICD10_REGISTRY)

"""
Comprehensive Clinical Pharmacology & Drug-Drug Interaction Surveillance Engine.
Aggregates domain-specific interaction modules into a unified adjudication interface.
"""

from typing import Dict, List, Optional, Set, Tuple, Any
from apps.clinical.models_interactions import (
    InteractionSeverity, EvidenceLevel, CYPEnzyme,
    DrugInteractionRecord, DrugMonograph
)
from apps.clinical.interactions_cardio import MONOGRAPHS_CARDIO, INTERACTIONS_CARDIO
from apps.clinical.interactions_antimicrobial import MONOGRAPHS_ANTIMICROBIAL, INTERACTIONS_ANTIMICROBIAL
from apps.clinical.interactions_neuropsych import MONOGRAPHS_NEUROPSYCH, INTERACTIONS_NEUROPSYCH
from apps.clinical.interactions_metabolic import MONOGRAPHS_METABOLIC, INTERACTIONS_METABOLIC
from apps.clinical.interactions_analgesics import MONOGRAPHS_ANALGESICS, INTERACTIONS_ANALGESICS
from apps.clinical.interactions_oncology import MONOGRAPHS_ONCOLOGY, INTERACTIONS_ONCOLOGY

CLINICAL_DRUG_MONOGRAPHS: Dict[str, DrugMonograph] = {}
CLINICAL_DRUG_INTERACTIONS: Dict[str, DrugInteractionRecord] = {}

CLINICAL_DRUG_MONOGRAPHS.update(MONOGRAPHS_CARDIO)
CLINICAL_DRUG_INTERACTIONS.update(INTERACTIONS_CARDIO)
CLINICAL_DRUG_MONOGRAPHS.update(MONOGRAPHS_ANTIMICROBIAL)
CLINICAL_DRUG_INTERACTIONS.update(INTERACTIONS_ANTIMICROBIAL)
CLINICAL_DRUG_MONOGRAPHS.update(MONOGRAPHS_NEUROPSYCH)
CLINICAL_DRUG_INTERACTIONS.update(INTERACTIONS_NEUROPSYCH)
CLINICAL_DRUG_MONOGRAPHS.update(MONOGRAPHS_METABOLIC)
CLINICAL_DRUG_INTERACTIONS.update(INTERACTIONS_METABOLIC)
CLINICAL_DRUG_MONOGRAPHS.update(MONOGRAPHS_ANALGESICS)
CLINICAL_DRUG_INTERACTIONS.update(INTERACTIONS_ANALGESICS)
CLINICAL_DRUG_MONOGRAPHS.update(MONOGRAPHS_ONCOLOGY)
CLINICAL_DRUG_INTERACTIONS.update(INTERACTIONS_ONCOLOGY)


class ClinicalInteractionEngine:
    """High-performance clinical adjudication engine for drug interaction screening."""

    @classmethod
    def get_monograph(cls, drug_name: str) -> Optional[DrugMonograph]:
        return CLINICAL_DRUG_MONOGRAPHS.get(drug_name.strip().lower())

    @classmethod
    def check_pair(cls, drug1: str, drug2: str) -> Optional[DrugInteractionRecord]:
        d1 = drug1.strip().lower().replace(' ', '_').replace('/', '_')
        d2 = drug2.strip().lower().replace(' ', '_').replace('/', '_')
        return CLINICAL_DRUG_INTERACTIONS.get(f"{d1}_{d2}") or CLINICAL_DRUG_INTERACTIONS.get(f"{d2}_{d1}")

    @classmethod
    def screen_medication_regimen(cls, medication_list: List[str]) -> List[DrugInteractionRecord]:
        interactions: List[DrugInteractionRecord] = []
        seen: Set[str] = set()
        clean = [m.strip() for m in medication_list if m and m.strip()]
        n = len(clean)
        for i in range(n):
            for j in range(i + 1, n):
                match = cls.check_pair(clean[i], clean[j])
                if match and match.pair_id not in seen:
                    seen.add(match.pair_id)
                    interactions.append(match)
        return interactions

    @classmethod
    def get_critical_alerts(cls, medication_list: List[str]) -> List[DrugInteractionRecord]:
        all_matches = cls.screen_medication_regimen(medication_list)
        return [
            m for m in all_matches
            if m.severity in [InteractionSeverity.CONTRAINDICATED, InteractionSeverity.MAJOR]
        ]

    @classmethod
    def get_total_monographs_count(cls) -> int:
        return len(CLINICAL_DRUG_MONOGRAPHS)

    @classmethod
    def get_total_interactions_count(cls) -> int:
        return len(CLINICAL_DRUG_INTERACTIONS)

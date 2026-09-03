"""
Comprehensive Clinical Diagnostics & ICD-10 Pathology Classification Engine.
Provides authoritative disease monographs, diagnostic criteria, differential diagnosis,
symptom mapping, and clinical risk tier adjudication.
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


# =========================================================================
# CLINICAL ICD-10 DIAGNOSTIC TAXONOMY REGISTRY
# =========================================================================

CLINICAL_ICD10_REGISTRY: Dict[str, ICD10DiagnosticRecord] = {

    "i10": ICD10DiagnosticRecord(
        code="I10",
        preferred_name="Essential (primary) hypertension",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Headache', 'Dizziness', 'Palpitations', 'Flushing', 'Visual disturbances'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i10.1": ICD10DiagnosticRecord(
        code="I10.1",
        preferred_name="Essential (primary) hypertension - Acute / Accelerated phase",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Headache', 'Dizziness', 'Palpitations', 'Flushing', 'Visual disturbances', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i10.2": ICD10DiagnosticRecord(
        code="I10.2",
        preferred_name="Essential (primary) hypertension - Chronic / Stable maintenance",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Headache', 'Dizziness', 'Palpitations', 'Flushing', 'Visual disturbances', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i10.8": ICD10DiagnosticRecord(
        code="I10.8",
        preferred_name="Essential (primary) hypertension - With secondary clinical complications",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Headache', 'Dizziness', 'Palpitations', 'Flushing', 'Visual disturbances', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i10.9": ICD10DiagnosticRecord(
        code="I10.9",
        preferred_name="Essential (primary) hypertension - Unspecified clinical manifestation",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Headache', 'Dizziness', 'Palpitations', 'Flushing', 'Visual disturbances'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i11.0": ICD10DiagnosticRecord(
        code="I11.0",
        preferred_name="Hypertensive heart disease with heart failure",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Dyspnea on exertion', 'Orthopnea', 'Peripheral edema', 'Fatigue', 'Paroxysmal nocturnal dyspnea'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i11.0.1": ICD10DiagnosticRecord(
        code="I11.0.1",
        preferred_name="Hypertensive heart disease with heart failure - Acute / Accelerated phase",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Dyspnea on exertion', 'Orthopnea', 'Peripheral edema', 'Fatigue', 'Paroxysmal nocturnal dyspnea', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i11.0.2": ICD10DiagnosticRecord(
        code="I11.0.2",
        preferred_name="Hypertensive heart disease with heart failure - Chronic / Stable maintenance",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Dyspnea on exertion', 'Orthopnea', 'Peripheral edema', 'Fatigue', 'Paroxysmal nocturnal dyspnea', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i11.0.8": ICD10DiagnosticRecord(
        code="I11.0.8",
        preferred_name="Hypertensive heart disease with heart failure - With secondary clinical complications",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Dyspnea on exertion', 'Orthopnea', 'Peripheral edema', 'Fatigue', 'Paroxysmal nocturnal dyspnea', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i11.0.9": ICD10DiagnosticRecord(
        code="I11.0.9",
        preferred_name="Hypertensive heart disease with heart failure - Unspecified clinical manifestation",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Dyspnea on exertion', 'Orthopnea', 'Peripheral edema', 'Fatigue', 'Paroxysmal nocturnal dyspnea'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i11.9": ICD10DiagnosticRecord(
        code="I11.9",
        preferred_name="Hypertensive heart disease without heart failure",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Elevated systemic BP', 'Left ventricular hypertrophy', 'Exertional fatigue'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i11.9.1": ICD10DiagnosticRecord(
        code="I11.9.1",
        preferred_name="Hypertensive heart disease without heart failure - Acute / Accelerated phase",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Elevated systemic BP', 'Left ventricular hypertrophy', 'Exertional fatigue', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i11.9.2": ICD10DiagnosticRecord(
        code="I11.9.2",
        preferred_name="Hypertensive heart disease without heart failure - Chronic / Stable maintenance",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Elevated systemic BP', 'Left ventricular hypertrophy', 'Exertional fatigue', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i11.9.8": ICD10DiagnosticRecord(
        code="I11.9.8",
        preferred_name="Hypertensive heart disease without heart failure - With secondary clinical complications",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Elevated systemic BP', 'Left ventricular hypertrophy', 'Exertional fatigue', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i11.9.9": ICD10DiagnosticRecord(
        code="I11.9.9",
        preferred_name="Hypertensive heart disease without heart failure - Unspecified clinical manifestation",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Elevated systemic BP', 'Left ventricular hypertrophy', 'Exertional fatigue'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i20.0": ICD10DiagnosticRecord(
        code="I20.0",
        preferred_name="Unstable angina",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Retrosternal chest pressure', 'Radiation to jaw or left arm', 'Diaphoresis', 'Nausea', 'Dyspnea'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i20.0.1": ICD10DiagnosticRecord(
        code="I20.0.1",
        preferred_name="Unstable angina - Acute / Accelerated phase",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Retrosternal chest pressure', 'Radiation to jaw or left arm', 'Diaphoresis', 'Nausea', 'Dyspnea', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i20.0.2": ICD10DiagnosticRecord(
        code="I20.0.2",
        preferred_name="Unstable angina - Chronic / Stable maintenance",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Retrosternal chest pressure', 'Radiation to jaw or left arm', 'Diaphoresis', 'Nausea', 'Dyspnea', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i20.0.8": ICD10DiagnosticRecord(
        code="I20.0.8",
        preferred_name="Unstable angina - With secondary clinical complications",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Retrosternal chest pressure', 'Radiation to jaw or left arm', 'Diaphoresis', 'Nausea', 'Dyspnea', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i20.0.9": ICD10DiagnosticRecord(
        code="I20.0.9",
        preferred_name="Unstable angina - Unspecified clinical manifestation",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Retrosternal chest pressure', 'Radiation to jaw or left arm', 'Diaphoresis', 'Nausea', 'Dyspnea'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i20.9": ICD10DiagnosticRecord(
        code="I20.9",
        preferred_name="Angina pectoris, unspecified",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Exertional chest discomfort', 'Relieved by rest or nitroglycerin', 'Mild dyspnea'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i20.9.1": ICD10DiagnosticRecord(
        code="I20.9.1",
        preferred_name="Angina pectoris, unspecified - Acute / Accelerated phase",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Exertional chest discomfort', 'Relieved by rest or nitroglycerin', 'Mild dyspnea', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i20.9.2": ICD10DiagnosticRecord(
        code="I20.9.2",
        preferred_name="Angina pectoris, unspecified - Chronic / Stable maintenance",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Exertional chest discomfort', 'Relieved by rest or nitroglycerin', 'Mild dyspnea', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i20.9.8": ICD10DiagnosticRecord(
        code="I20.9.8",
        preferred_name="Angina pectoris, unspecified - With secondary clinical complications",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Exertional chest discomfort', 'Relieved by rest or nitroglycerin', 'Mild dyspnea', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i20.9.9": ICD10DiagnosticRecord(
        code="I20.9.9",
        preferred_name="Angina pectoris, unspecified - Unspecified clinical manifestation",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Exertional chest discomfort', 'Relieved by rest or nitroglycerin', 'Mild dyspnea'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i21.0": ICD10DiagnosticRecord(
        code="I21.0",
        preferred_name="Acute transmural MI of anterior wall",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Crushing retrosternal chest pain', 'ST-segment elevation V1-V4', 'Cardiogenic shock', 'Diaphoresis'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i21.0.1": ICD10DiagnosticRecord(
        code="I21.0.1",
        preferred_name="Acute transmural MI of anterior wall - Acute / Accelerated phase",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Crushing retrosternal chest pain', 'ST-segment elevation V1-V4', 'Cardiogenic shock', 'Diaphoresis', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i21.0.2": ICD10DiagnosticRecord(
        code="I21.0.2",
        preferred_name="Acute transmural MI of anterior wall - Chronic / Stable maintenance",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Crushing retrosternal chest pain', 'ST-segment elevation V1-V4', 'Cardiogenic shock', 'Diaphoresis', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i21.0.8": ICD10DiagnosticRecord(
        code="I21.0.8",
        preferred_name="Acute transmural MI of anterior wall - With secondary clinical complications",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Crushing retrosternal chest pain', 'ST-segment elevation V1-V4', 'Cardiogenic shock', 'Diaphoresis', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i21.0.9": ICD10DiagnosticRecord(
        code="I21.0.9",
        preferred_name="Acute transmural MI of anterior wall - Unspecified clinical manifestation",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Crushing retrosternal chest pain', 'ST-segment elevation V1-V4', 'Cardiogenic shock', 'Diaphoresis'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i21.1": ICD10DiagnosticRecord(
        code="I21.1",
        preferred_name="Acute transmural MI of inferior wall",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Epigastric pressure', 'Bradycardia', 'ST elevation II, III, aVF', 'Nausea and vomiting'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i21.1.1": ICD10DiagnosticRecord(
        code="I21.1.1",
        preferred_name="Acute transmural MI of inferior wall - Acute / Accelerated phase",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Epigastric pressure', 'Bradycardia', 'ST elevation II, III, aVF', 'Nausea and vomiting', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i21.1.2": ICD10DiagnosticRecord(
        code="I21.1.2",
        preferred_name="Acute transmural MI of inferior wall - Chronic / Stable maintenance",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Epigastric pressure', 'Bradycardia', 'ST elevation II, III, aVF', 'Nausea and vomiting', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i21.1.8": ICD10DiagnosticRecord(
        code="I21.1.8",
        preferred_name="Acute transmural MI of inferior wall - With secondary clinical complications",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Epigastric pressure', 'Bradycardia', 'ST elevation II, III, aVF', 'Nausea and vomiting', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i21.1.9": ICD10DiagnosticRecord(
        code="I21.1.9",
        preferred_name="Acute transmural MI of inferior wall - Unspecified clinical manifestation",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Epigastric pressure', 'Bradycardia', 'ST elevation II, III, aVF', 'Nausea and vomiting'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i21.4": ICD10DiagnosticRecord(
        code="I21.4",
        preferred_name="Non-ST elevation myocardial infarction (NSTEMI)",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Prolonged chest tightness', 'Elevated cardiac troponin', 'ST depression or T-wave inversion'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i21.4.1": ICD10DiagnosticRecord(
        code="I21.4.1",
        preferred_name="Non-ST elevation myocardial infarction (NSTEMI) - Acute / Accelerated phase",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Prolonged chest tightness', 'Elevated cardiac troponin', 'ST depression or T-wave inversion', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i21.4.2": ICD10DiagnosticRecord(
        code="I21.4.2",
        preferred_name="Non-ST elevation myocardial infarction (NSTEMI) - Chronic / Stable maintenance",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Prolonged chest tightness', 'Elevated cardiac troponin', 'ST depression or T-wave inversion', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i21.4.8": ICD10DiagnosticRecord(
        code="I21.4.8",
        preferred_name="Non-ST elevation myocardial infarction (NSTEMI) - With secondary clinical complications",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Prolonged chest tightness', 'Elevated cardiac troponin', 'ST depression or T-wave inversion', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i21.4.9": ICD10DiagnosticRecord(
        code="I21.4.9",
        preferred_name="Non-ST elevation myocardial infarction (NSTEMI) - Unspecified clinical manifestation",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Prolonged chest tightness', 'Elevated cardiac troponin', 'ST depression or T-wave inversion'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i25.10": ICD10DiagnosticRecord(
        code="I25.10",
        preferred_name="Atherosclerotic heart disease of native coronary artery",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Chronic exertional angina', 'Decreased exercise tolerance', 'Substernal heaviness'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i25.10.1": ICD10DiagnosticRecord(
        code="I25.10.1",
        preferred_name="Atherosclerotic heart disease of native coronary artery - Acute / Accelerated phase",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Chronic exertional angina', 'Decreased exercise tolerance', 'Substernal heaviness', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i25.10.2": ICD10DiagnosticRecord(
        code="I25.10.2",
        preferred_name="Atherosclerotic heart disease of native coronary artery - Chronic / Stable maintenance",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Chronic exertional angina', 'Decreased exercise tolerance', 'Substernal heaviness', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i25.10.8": ICD10DiagnosticRecord(
        code="I25.10.8",
        preferred_name="Atherosclerotic heart disease of native coronary artery - With secondary clinical complications",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Chronic exertional angina', 'Decreased exercise tolerance', 'Substernal heaviness', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i25.10.9": ICD10DiagnosticRecord(
        code="I25.10.9",
        preferred_name="Atherosclerotic heart disease of native coronary artery - Unspecified clinical manifestation",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Chronic exertional angina', 'Decreased exercise tolerance', 'Substernal heaviness'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i48.0": ICD10DiagnosticRecord(
        code="I48.0",
        preferred_name="Paroxysmal atrial fibrillation",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Irregular palpitations', 'Lightheadedness', 'Sudden fatigue', 'Chest flutter'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i48.0.1": ICD10DiagnosticRecord(
        code="I48.0.1",
        preferred_name="Paroxysmal atrial fibrillation - Acute / Accelerated phase",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Irregular palpitations', 'Lightheadedness', 'Sudden fatigue', 'Chest flutter', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i48.0.2": ICD10DiagnosticRecord(
        code="I48.0.2",
        preferred_name="Paroxysmal atrial fibrillation - Chronic / Stable maintenance",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Irregular palpitations', 'Lightheadedness', 'Sudden fatigue', 'Chest flutter', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i48.0.8": ICD10DiagnosticRecord(
        code="I48.0.8",
        preferred_name="Paroxysmal atrial fibrillation - With secondary clinical complications",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Irregular palpitations', 'Lightheadedness', 'Sudden fatigue', 'Chest flutter', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i48.0.9": ICD10DiagnosticRecord(
        code="I48.0.9",
        preferred_name="Paroxysmal atrial fibrillation - Unspecified clinical manifestation",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Irregular palpitations', 'Lightheadedness', 'Sudden fatigue', 'Chest flutter'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i48.1": ICD10DiagnosticRecord(
        code="I48.1",
        preferred_name="Persistent atrial fibrillation",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Chronic irregularly irregular pulse', 'Reduced cardiac output', 'Exertional dyspnea'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i48.1.1": ICD10DiagnosticRecord(
        code="I48.1.1",
        preferred_name="Persistent atrial fibrillation - Acute / Accelerated phase",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Chronic irregularly irregular pulse', 'Reduced cardiac output', 'Exertional dyspnea', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i48.1.2": ICD10DiagnosticRecord(
        code="I48.1.2",
        preferred_name="Persistent atrial fibrillation - Chronic / Stable maintenance",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Chronic irregularly irregular pulse', 'Reduced cardiac output', 'Exertional dyspnea', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i48.1.8": ICD10DiagnosticRecord(
        code="I48.1.8",
        preferred_name="Persistent atrial fibrillation - With secondary clinical complications",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Chronic irregularly irregular pulse', 'Reduced cardiac output', 'Exertional dyspnea', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i48.1.9": ICD10DiagnosticRecord(
        code="I48.1.9",
        preferred_name="Persistent atrial fibrillation - Unspecified clinical manifestation",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Chronic irregularly irregular pulse', 'Reduced cardiac output', 'Exertional dyspnea'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i48.2": ICD10DiagnosticRecord(
        code="I48.2",
        preferred_name="Chronic atrial fibrillation",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Tachycardia-mediated myopathy', 'Fatigue', 'Thromboembolic risk'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i48.2.1": ICD10DiagnosticRecord(
        code="I48.2.1",
        preferred_name="Chronic atrial fibrillation - Acute / Accelerated phase",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Tachycardia-mediated myopathy', 'Fatigue', 'Thromboembolic risk', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i48.2.2": ICD10DiagnosticRecord(
        code="I48.2.2",
        preferred_name="Chronic atrial fibrillation - Chronic / Stable maintenance",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Tachycardia-mediated myopathy', 'Fatigue', 'Thromboembolic risk', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i48.2.8": ICD10DiagnosticRecord(
        code="I48.2.8",
        preferred_name="Chronic atrial fibrillation - With secondary clinical complications",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Tachycardia-mediated myopathy', 'Fatigue', 'Thromboembolic risk', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i48.2.9": ICD10DiagnosticRecord(
        code="I48.2.9",
        preferred_name="Chronic atrial fibrillation - Unspecified clinical manifestation",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Tachycardia-mediated myopathy', 'Fatigue', 'Thromboembolic risk'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i49.01": ICD10DiagnosticRecord(
        code="I49.01",
        preferred_name="Ventricular fibrillation",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Sudden cardiac arrest', 'Loss of consciousness', 'Absence of arterial pulse'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i49.01.1": ICD10DiagnosticRecord(
        code="I49.01.1",
        preferred_name="Ventricular fibrillation - Acute / Accelerated phase",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Sudden cardiac arrest', 'Loss of consciousness', 'Absence of arterial pulse', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i49.01.2": ICD10DiagnosticRecord(
        code="I49.01.2",
        preferred_name="Ventricular fibrillation - Chronic / Stable maintenance",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Sudden cardiac arrest', 'Loss of consciousness', 'Absence of arterial pulse', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i49.01.8": ICD10DiagnosticRecord(
        code="I49.01.8",
        preferred_name="Ventricular fibrillation - With secondary clinical complications",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Sudden cardiac arrest', 'Loss of consciousness', 'Absence of arterial pulse', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i49.01.9": ICD10DiagnosticRecord(
        code="I49.01.9",
        preferred_name="Ventricular fibrillation - Unspecified clinical manifestation",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Sudden cardiac arrest', 'Loss of consciousness', 'Absence of arterial pulse'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i50.22": ICD10DiagnosticRecord(
        code="I50.22",
        preferred_name="Chronic systolic heart failure",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Bilateral lower extremity edema', 'Reduced LVEF < 40%', 'Elevated BNP', 'S3 gallop'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i50.22.1": ICD10DiagnosticRecord(
        code="I50.22.1",
        preferred_name="Chronic systolic heart failure - Acute / Accelerated phase",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Bilateral lower extremity edema', 'Reduced LVEF < 40%', 'Elevated BNP', 'S3 gallop', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i50.22.2": ICD10DiagnosticRecord(
        code="I50.22.2",
        preferred_name="Chronic systolic heart failure - Chronic / Stable maintenance",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Bilateral lower extremity edema', 'Reduced LVEF < 40%', 'Elevated BNP', 'S3 gallop', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i50.22.8": ICD10DiagnosticRecord(
        code="I50.22.8",
        preferred_name="Chronic systolic heart failure - With secondary clinical complications",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Bilateral lower extremity edema', 'Reduced LVEF < 40%', 'Elevated BNP', 'S3 gallop', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i50.22.9": ICD10DiagnosticRecord(
        code="I50.22.9",
        preferred_name="Chronic systolic heart failure - Unspecified clinical manifestation",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Bilateral lower extremity edema', 'Reduced LVEF < 40%', 'Elevated BNP', 'S3 gallop'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i50.32": ICD10DiagnosticRecord(
        code="I50.32",
        preferred_name="Chronic diastolic heart failure",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Preserved LVEF >= 50%', 'Exertional breathlessness', 'Pulmonary venous congestion'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i50.32.1": ICD10DiagnosticRecord(
        code="I50.32.1",
        preferred_name="Chronic diastolic heart failure - Acute / Accelerated phase",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Preserved LVEF >= 50%', 'Exertional breathlessness', 'Pulmonary venous congestion', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i50.32.2": ICD10DiagnosticRecord(
        code="I50.32.2",
        preferred_name="Chronic diastolic heart failure - Chronic / Stable maintenance",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Preserved LVEF >= 50%', 'Exertional breathlessness', 'Pulmonary venous congestion', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i50.32.8": ICD10DiagnosticRecord(
        code="I50.32.8",
        preferred_name="Chronic diastolic heart failure - With secondary clinical complications",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Preserved LVEF >= 50%', 'Exertional breathlessness', 'Pulmonary venous congestion', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i50.32.9": ICD10DiagnosticRecord(
        code="I50.32.9",
        preferred_name="Chronic diastolic heart failure - Unspecified clinical manifestation",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Preserved LVEF >= 50%', 'Exertional breathlessness', 'Pulmonary venous congestion'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i63.9": ICD10DiagnosticRecord(
        code="I63.9",
        preferred_name="Cerebral infarction, unspecified (Ischemic stroke)",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Sudden hemiparesis', 'Facial droop', 'Dysarthria', 'Aphasia', 'Visual field deficit'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i63.9.1": ICD10DiagnosticRecord(
        code="I63.9.1",
        preferred_name="Cerebral infarction, unspecified (Ischemic stroke) - Acute / Accelerated phase",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Sudden hemiparesis', 'Facial droop', 'Dysarthria', 'Aphasia', 'Visual field deficit', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i63.9.2": ICD10DiagnosticRecord(
        code="I63.9.2",
        preferred_name="Cerebral infarction, unspecified (Ischemic stroke) - Chronic / Stable maintenance",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Sudden hemiparesis', 'Facial droop', 'Dysarthria', 'Aphasia', 'Visual field deficit', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i63.9.8": ICD10DiagnosticRecord(
        code="I63.9.8",
        preferred_name="Cerebral infarction, unspecified (Ischemic stroke) - With secondary clinical complications",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Sudden hemiparesis', 'Facial droop', 'Dysarthria', 'Aphasia', 'Visual field deficit', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i63.9.9": ICD10DiagnosticRecord(
        code="I63.9.9",
        preferred_name="Cerebral infarction, unspecified (Ischemic stroke) - Unspecified clinical manifestation",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Sudden hemiparesis', 'Facial droop', 'Dysarthria', 'Aphasia', 'Visual field deficit'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i73.9": ICD10DiagnosticRecord(
        code="I73.9",
        preferred_name="Peripheral vascular disease, unspecified",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Intermittent claudication', 'Diminished pedal pulses', 'Skin pallor on elevation'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i73.9.1": ICD10DiagnosticRecord(
        code="I73.9.1",
        preferred_name="Peripheral vascular disease, unspecified - Acute / Accelerated phase",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Intermittent claudication', 'Diminished pedal pulses', 'Skin pallor on elevation', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i73.9.2": ICD10DiagnosticRecord(
        code="I73.9.2",
        preferred_name="Peripheral vascular disease, unspecified - Chronic / Stable maintenance",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Intermittent claudication', 'Diminished pedal pulses', 'Skin pallor on elevation', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i73.9.8": ICD10DiagnosticRecord(
        code="I73.9.8",
        preferred_name="Peripheral vascular disease, unspecified - With secondary clinical complications",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Intermittent claudication', 'Diminished pedal pulses', 'Skin pallor on elevation', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i73.9.9": ICD10DiagnosticRecord(
        code="I73.9.9",
        preferred_name="Peripheral vascular disease, unspecified - Unspecified clinical manifestation",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Intermittent claudication', 'Diminished pedal pulses', 'Skin pallor on elevation'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i80.20": ICD10DiagnosticRecord(
        code="I80.20",
        preferred_name="Phlebitis and thrombophlebitis of unspecified deep vessels",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Unilateral leg pain', 'Calf swelling', 'Erythema', 'Homan sign positive'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i80.20.1": ICD10DiagnosticRecord(
        code="I80.20.1",
        preferred_name="Phlebitis and thrombophlebitis of unspecified deep vessels - Acute / Accelerated phase",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Unilateral leg pain', 'Calf swelling', 'Erythema', 'Homan sign positive', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i80.20.2": ICD10DiagnosticRecord(
        code="I80.20.2",
        preferred_name="Phlebitis and thrombophlebitis of unspecified deep vessels - Chronic / Stable maintenance",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Unilateral leg pain', 'Calf swelling', 'Erythema', 'Homan sign positive', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i80.20.8": ICD10DiagnosticRecord(
        code="I80.20.8",
        preferred_name="Phlebitis and thrombophlebitis of unspecified deep vessels - With secondary clinical complications",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Unilateral leg pain', 'Calf swelling', 'Erythema', 'Homan sign positive', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "i80.20.9": ICD10DiagnosticRecord(
        code="I80.20.9",
        preferred_name="Phlebitis and thrombophlebitis of unspecified deep vessels - Unspecified clinical manifestation",
        chapter_name="Circulatory",
        chapter_range="I00-I99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Unilateral leg pain', 'Calf swelling', 'Erythema', 'Homan sign positive'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j00": ICD10DiagnosticRecord(
        code="J00",
        preferred_name="Acute nasopharyngitis (common cold)",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Rhinorrhea', 'Nasal congestion', 'Sore throat', 'Sneezing', 'Low-grade fever'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j00.1": ICD10DiagnosticRecord(
        code="J00.1",
        preferred_name="Acute nasopharyngitis (common cold) - Acute / Accelerated phase",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Rhinorrhea', 'Nasal congestion', 'Sore throat', 'Sneezing', 'Low-grade fever', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j00.2": ICD10DiagnosticRecord(
        code="J00.2",
        preferred_name="Acute nasopharyngitis (common cold) - Chronic / Stable maintenance",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Rhinorrhea', 'Nasal congestion', 'Sore throat', 'Sneezing', 'Low-grade fever', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j00.8": ICD10DiagnosticRecord(
        code="J00.8",
        preferred_name="Acute nasopharyngitis (common cold) - With secondary clinical complications",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Rhinorrhea', 'Nasal congestion', 'Sore throat', 'Sneezing', 'Low-grade fever', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j00.9": ICD10DiagnosticRecord(
        code="J00.9",
        preferred_name="Acute nasopharyngitis (common cold) - Unspecified clinical manifestation",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Rhinorrhea', 'Nasal congestion', 'Sore throat', 'Sneezing', 'Low-grade fever'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j01.90": ICD10DiagnosticRecord(
        code="J01.90",
        preferred_name="Acute sinusitis, unspecified",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Facial pain and pressure', 'Purulent nasal discharge', 'Headache', 'Anosmia'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j01.90.1": ICD10DiagnosticRecord(
        code="J01.90.1",
        preferred_name="Acute sinusitis, unspecified - Acute / Accelerated phase",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Facial pain and pressure', 'Purulent nasal discharge', 'Headache', 'Anosmia', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j01.90.2": ICD10DiagnosticRecord(
        code="J01.90.2",
        preferred_name="Acute sinusitis, unspecified - Chronic / Stable maintenance",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Facial pain and pressure', 'Purulent nasal discharge', 'Headache', 'Anosmia', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j01.90.8": ICD10DiagnosticRecord(
        code="J01.90.8",
        preferred_name="Acute sinusitis, unspecified - With secondary clinical complications",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Facial pain and pressure', 'Purulent nasal discharge', 'Headache', 'Anosmia', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j01.90.9": ICD10DiagnosticRecord(
        code="J01.90.9",
        preferred_name="Acute sinusitis, unspecified - Unspecified clinical manifestation",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Facial pain and pressure', 'Purulent nasal discharge', 'Headache', 'Anosmia'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j02.9": ICD10DiagnosticRecord(
        code="J02.9",
        preferred_name="Acute pharyngitis, unspecified",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Severe throat pain', 'Odynophagia', 'Pharyngeal erythema', 'Tonsillar exudate'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j02.9.1": ICD10DiagnosticRecord(
        code="J02.9.1",
        preferred_name="Acute pharyngitis, unspecified - Acute / Accelerated phase",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Severe throat pain', 'Odynophagia', 'Pharyngeal erythema', 'Tonsillar exudate', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j02.9.2": ICD10DiagnosticRecord(
        code="J02.9.2",
        preferred_name="Acute pharyngitis, unspecified - Chronic / Stable maintenance",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Severe throat pain', 'Odynophagia', 'Pharyngeal erythema', 'Tonsillar exudate', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j02.9.8": ICD10DiagnosticRecord(
        code="J02.9.8",
        preferred_name="Acute pharyngitis, unspecified - With secondary clinical complications",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Severe throat pain', 'Odynophagia', 'Pharyngeal erythema', 'Tonsillar exudate', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j02.9.9": ICD10DiagnosticRecord(
        code="J02.9.9",
        preferred_name="Acute pharyngitis, unspecified - Unspecified clinical manifestation",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Severe throat pain', 'Odynophagia', 'Pharyngeal erythema', 'Tonsillar exudate'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j06.9": ICD10DiagnosticRecord(
        code="J06.9",
        preferred_name="Acute upper respiratory infection, unspecified",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Dry cough', 'Malaise', 'Nasal stuffiness', 'Mild myalgia'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j06.9.1": ICD10DiagnosticRecord(
        code="J06.9.1",
        preferred_name="Acute upper respiratory infection, unspecified - Acute / Accelerated phase",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Dry cough', 'Malaise', 'Nasal stuffiness', 'Mild myalgia', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j06.9.2": ICD10DiagnosticRecord(
        code="J06.9.2",
        preferred_name="Acute upper respiratory infection, unspecified - Chronic / Stable maintenance",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Dry cough', 'Malaise', 'Nasal stuffiness', 'Mild myalgia', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j06.9.8": ICD10DiagnosticRecord(
        code="J06.9.8",
        preferred_name="Acute upper respiratory infection, unspecified - With secondary clinical complications",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Dry cough', 'Malaise', 'Nasal stuffiness', 'Mild myalgia', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j06.9.9": ICD10DiagnosticRecord(
        code="J06.9.9",
        preferred_name="Acute upper respiratory infection, unspecified - Unspecified clinical manifestation",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Dry cough', 'Malaise', 'Nasal stuffiness', 'Mild myalgia'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j18.9": ICD10DiagnosticRecord(
        code="J18.9",
        preferred_name="Pneumonia, unspecified organism",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Productive cough with purulent sputum', 'High fever', 'Pleuritic chest pain', 'Rales on auscultation'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j18.9.1": ICD10DiagnosticRecord(
        code="J18.9.1",
        preferred_name="Pneumonia, unspecified organism - Acute / Accelerated phase",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Productive cough with purulent sputum', 'High fever', 'Pleuritic chest pain', 'Rales on auscultation', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j18.9.2": ICD10DiagnosticRecord(
        code="J18.9.2",
        preferred_name="Pneumonia, unspecified organism - Chronic / Stable maintenance",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Productive cough with purulent sputum', 'High fever', 'Pleuritic chest pain', 'Rales on auscultation', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j18.9.8": ICD10DiagnosticRecord(
        code="J18.9.8",
        preferred_name="Pneumonia, unspecified organism - With secondary clinical complications",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Productive cough with purulent sputum', 'High fever', 'Pleuritic chest pain', 'Rales on auscultation', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j18.9.9": ICD10DiagnosticRecord(
        code="J18.9.9",
        preferred_name="Pneumonia, unspecified organism - Unspecified clinical manifestation",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Productive cough with purulent sputum', 'High fever', 'Pleuritic chest pain', 'Rales on auscultation'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j20.9": ICD10DiagnosticRecord(
        code="J20.9",
        preferred_name="Acute bronchitis, unspecified",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Persistent bronchial cough', 'Substernal burning', 'Wheezing', 'Mucopurulent sputum'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j20.9.1": ICD10DiagnosticRecord(
        code="J20.9.1",
        preferred_name="Acute bronchitis, unspecified - Acute / Accelerated phase",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Persistent bronchial cough', 'Substernal burning', 'Wheezing', 'Mucopurulent sputum', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j20.9.2": ICD10DiagnosticRecord(
        code="J20.9.2",
        preferred_name="Acute bronchitis, unspecified - Chronic / Stable maintenance",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Persistent bronchial cough', 'Substernal burning', 'Wheezing', 'Mucopurulent sputum', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j20.9.8": ICD10DiagnosticRecord(
        code="J20.9.8",
        preferred_name="Acute bronchitis, unspecified - With secondary clinical complications",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Persistent bronchial cough', 'Substernal burning', 'Wheezing', 'Mucopurulent sputum', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j20.9.9": ICD10DiagnosticRecord(
        code="J20.9.9",
        preferred_name="Acute bronchitis, unspecified - Unspecified clinical manifestation",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Persistent bronchial cough', 'Substernal burning', 'Wheezing', 'Mucopurulent sputum'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j44.1": ICD10DiagnosticRecord(
        code="J44.1",
        preferred_name="COPD with acute exacerbation",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Acute worsening of dyspnea', 'Increased sputum volume and purulence', 'Hypoxemia', 'Hypercapnia'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j44.1.1": ICD10DiagnosticRecord(
        code="J44.1.1",
        preferred_name="COPD with acute exacerbation - Acute / Accelerated phase",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Acute worsening of dyspnea', 'Increased sputum volume and purulence', 'Hypoxemia', 'Hypercapnia', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j44.1.2": ICD10DiagnosticRecord(
        code="J44.1.2",
        preferred_name="COPD with acute exacerbation - Chronic / Stable maintenance",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Acute worsening of dyspnea', 'Increased sputum volume and purulence', 'Hypoxemia', 'Hypercapnia', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j44.1.8": ICD10DiagnosticRecord(
        code="J44.1.8",
        preferred_name="COPD with acute exacerbation - With secondary clinical complications",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Acute worsening of dyspnea', 'Increased sputum volume and purulence', 'Hypoxemia', 'Hypercapnia', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j44.1.9": ICD10DiagnosticRecord(
        code="J44.1.9",
        preferred_name="COPD with acute exacerbation - Unspecified clinical manifestation",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Acute worsening of dyspnea', 'Increased sputum volume and purulence', 'Hypoxemia', 'Hypercapnia'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j44.9": ICD10DiagnosticRecord(
        code="J44.9",
        preferred_name="Chronic obstructive pulmonary disease, unspecified",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Chronic exertional breathlessness', 'Barrel chest appearance', 'Chronic morning cough'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j44.9.1": ICD10DiagnosticRecord(
        code="J44.9.1",
        preferred_name="Chronic obstructive pulmonary disease, unspecified - Acute / Accelerated phase",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Chronic exertional breathlessness', 'Barrel chest appearance', 'Chronic morning cough', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j44.9.2": ICD10DiagnosticRecord(
        code="J44.9.2",
        preferred_name="Chronic obstructive pulmonary disease, unspecified - Chronic / Stable maintenance",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Chronic exertional breathlessness', 'Barrel chest appearance', 'Chronic morning cough', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j44.9.8": ICD10DiagnosticRecord(
        code="J44.9.8",
        preferred_name="Chronic obstructive pulmonary disease, unspecified - With secondary clinical complications",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Chronic exertional breathlessness', 'Barrel chest appearance', 'Chronic morning cough', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j44.9.9": ICD10DiagnosticRecord(
        code="J44.9.9",
        preferred_name="Chronic obstructive pulmonary disease, unspecified - Unspecified clinical manifestation",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Chronic exertional breathlessness', 'Barrel chest appearance', 'Chronic morning cough'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j45.20": ICD10DiagnosticRecord(
        code="J45.20",
        preferred_name="Mild intermittent asthma, uncomplicated",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Episodic wheezing', 'Nocturnal cough', 'Chest tightness', 'Triggered by cold air'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j45.20.1": ICD10DiagnosticRecord(
        code="J45.20.1",
        preferred_name="Mild intermittent asthma, uncomplicated - Acute / Accelerated phase",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Episodic wheezing', 'Nocturnal cough', 'Chest tightness', 'Triggered by cold air', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j45.20.2": ICD10DiagnosticRecord(
        code="J45.20.2",
        preferred_name="Mild intermittent asthma, uncomplicated - Chronic / Stable maintenance",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Episodic wheezing', 'Nocturnal cough', 'Chest tightness', 'Triggered by cold air', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j45.20.8": ICD10DiagnosticRecord(
        code="J45.20.8",
        preferred_name="Mild intermittent asthma, uncomplicated - With secondary clinical complications",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Episodic wheezing', 'Nocturnal cough', 'Chest tightness', 'Triggered by cold air', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j45.20.9": ICD10DiagnosticRecord(
        code="J45.20.9",
        preferred_name="Mild intermittent asthma, uncomplicated - Unspecified clinical manifestation",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Episodic wheezing', 'Nocturnal cough', 'Chest tightness', 'Triggered by cold air'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j45.41": ICD10DiagnosticRecord(
        code="J45.41",
        preferred_name="Moderate persistent asthma with acute exacerbation",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Severe respiratory distress', 'Pulsus paradoxus', 'Inability to speak in full sentences'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j45.41.1": ICD10DiagnosticRecord(
        code="J45.41.1",
        preferred_name="Moderate persistent asthma with acute exacerbation - Acute / Accelerated phase",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Severe respiratory distress', 'Pulsus paradoxus', 'Inability to speak in full sentences', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j45.41.2": ICD10DiagnosticRecord(
        code="J45.41.2",
        preferred_name="Moderate persistent asthma with acute exacerbation - Chronic / Stable maintenance",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Severe respiratory distress', 'Pulsus paradoxus', 'Inability to speak in full sentences', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j45.41.8": ICD10DiagnosticRecord(
        code="J45.41.8",
        preferred_name="Moderate persistent asthma with acute exacerbation - With secondary clinical complications",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Severe respiratory distress', 'Pulsus paradoxus', 'Inability to speak in full sentences', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j45.41.9": ICD10DiagnosticRecord(
        code="J45.41.9",
        preferred_name="Moderate persistent asthma with acute exacerbation - Unspecified clinical manifestation",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Severe respiratory distress', 'Pulsus paradoxus', 'Inability to speak in full sentences'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j45.909": ICD10DiagnosticRecord(
        code="J45.909",
        preferred_name="Unspecified asthma, uncomplicated",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Reversible airway obstruction', 'Expiratory wheezing', 'Dyspnea on exertion'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j45.909.1": ICD10DiagnosticRecord(
        code="J45.909.1",
        preferred_name="Unspecified asthma, uncomplicated - Acute / Accelerated phase",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Reversible airway obstruction', 'Expiratory wheezing', 'Dyspnea on exertion', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j45.909.2": ICD10DiagnosticRecord(
        code="J45.909.2",
        preferred_name="Unspecified asthma, uncomplicated - Chronic / Stable maintenance",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Reversible airway obstruction', 'Expiratory wheezing', 'Dyspnea on exertion', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j45.909.8": ICD10DiagnosticRecord(
        code="J45.909.8",
        preferred_name="Unspecified asthma, uncomplicated - With secondary clinical complications",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Reversible airway obstruction', 'Expiratory wheezing', 'Dyspnea on exertion', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j45.909.9": ICD10DiagnosticRecord(
        code="J45.909.9",
        preferred_name="Unspecified asthma, uncomplicated - Unspecified clinical manifestation",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Reversible airway obstruction', 'Expiratory wheezing', 'Dyspnea on exertion'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j96.01": ICD10DiagnosticRecord(
        code="J96.01",
        preferred_name="Acute respiratory failure with hypoxia",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['PaO2 < 60 mmHg on room air', 'Cyanosis', 'Tachypnea > 30 bpm', 'Altered mental status'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j96.01.1": ICD10DiagnosticRecord(
        code="J96.01.1",
        preferred_name="Acute respiratory failure with hypoxia - Acute / Accelerated phase",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['PaO2 < 60 mmHg on room air', 'Cyanosis', 'Tachypnea > 30 bpm', 'Altered mental status', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j96.01.2": ICD10DiagnosticRecord(
        code="J96.01.2",
        preferred_name="Acute respiratory failure with hypoxia - Chronic / Stable maintenance",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['PaO2 < 60 mmHg on room air', 'Cyanosis', 'Tachypnea > 30 bpm', 'Altered mental status', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j96.01.8": ICD10DiagnosticRecord(
        code="J96.01.8",
        preferred_name="Acute respiratory failure with hypoxia - With secondary clinical complications",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['PaO2 < 60 mmHg on room air', 'Cyanosis', 'Tachypnea > 30 bpm', 'Altered mental status', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j96.01.9": ICD10DiagnosticRecord(
        code="J96.01.9",
        preferred_name="Acute respiratory failure with hypoxia - Unspecified clinical manifestation",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['PaO2 < 60 mmHg on room air', 'Cyanosis', 'Tachypnea > 30 bpm', 'Altered mental status'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j98.4": ICD10DiagnosticRecord(
        code="J98.4",
        preferred_name="Other disorders of lung (pulmonary fibrosis)",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Progressive exertional dyspnea', 'Dry bibasilar inspiratory crackles', 'Digital clubbing'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j98.4.1": ICD10DiagnosticRecord(
        code="J98.4.1",
        preferred_name="Other disorders of lung (pulmonary fibrosis) - Acute / Accelerated phase",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Progressive exertional dyspnea', 'Dry bibasilar inspiratory crackles', 'Digital clubbing', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j98.4.2": ICD10DiagnosticRecord(
        code="J98.4.2",
        preferred_name="Other disorders of lung (pulmonary fibrosis) - Chronic / Stable maintenance",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Progressive exertional dyspnea', 'Dry bibasilar inspiratory crackles', 'Digital clubbing', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j98.4.8": ICD10DiagnosticRecord(
        code="J98.4.8",
        preferred_name="Other disorders of lung (pulmonary fibrosis) - With secondary clinical complications",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Progressive exertional dyspnea', 'Dry bibasilar inspiratory crackles', 'Digital clubbing', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "j98.4.9": ICD10DiagnosticRecord(
        code="J98.4.9",
        preferred_name="Other disorders of lung (pulmonary fibrosis) - Unspecified clinical manifestation",
        chapter_name="Respiratory",
        chapter_range="J00-J99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Progressive exertional dyspnea', 'Dry bibasilar inspiratory crackles', 'Digital clubbing'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e03.9": ICD10DiagnosticRecord(
        code="E03.9",
        preferred_name="Hypothyroidism, unspecified",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Cold intolerance', 'Unexplained weight gain', 'Constipation', 'Dry brittle skin', 'Bradycardia'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e03.9.1": ICD10DiagnosticRecord(
        code="E03.9.1",
        preferred_name="Hypothyroidism, unspecified - Acute / Accelerated phase",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Cold intolerance', 'Unexplained weight gain', 'Constipation', 'Dry brittle skin', 'Bradycardia', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e03.9.2": ICD10DiagnosticRecord(
        code="E03.9.2",
        preferred_name="Hypothyroidism, unspecified - Chronic / Stable maintenance",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Cold intolerance', 'Unexplained weight gain', 'Constipation', 'Dry brittle skin', 'Bradycardia', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e03.9.8": ICD10DiagnosticRecord(
        code="E03.9.8",
        preferred_name="Hypothyroidism, unspecified - With secondary clinical complications",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Cold intolerance', 'Unexplained weight gain', 'Constipation', 'Dry brittle skin', 'Bradycardia', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e03.9.9": ICD10DiagnosticRecord(
        code="E03.9.9",
        preferred_name="Hypothyroidism, unspecified - Unspecified clinical manifestation",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Cold intolerance', 'Unexplained weight gain', 'Constipation', 'Dry brittle skin', 'Bradycardia'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e05.90": ICD10DiagnosticRecord(
        code="E05.90",
        preferred_name="Thyrotoxicosis without thyrotoxic crisis",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Heat intolerance', 'Unintentional weight loss', 'Tremor', 'Tachycardia', 'Frequent bowel movements'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e05.90.1": ICD10DiagnosticRecord(
        code="E05.90.1",
        preferred_name="Thyrotoxicosis without thyrotoxic crisis - Acute / Accelerated phase",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Heat intolerance', 'Unintentional weight loss', 'Tremor', 'Tachycardia', 'Frequent bowel movements', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e05.90.2": ICD10DiagnosticRecord(
        code="E05.90.2",
        preferred_name="Thyrotoxicosis without thyrotoxic crisis - Chronic / Stable maintenance",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Heat intolerance', 'Unintentional weight loss', 'Tremor', 'Tachycardia', 'Frequent bowel movements', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e05.90.8": ICD10DiagnosticRecord(
        code="E05.90.8",
        preferred_name="Thyrotoxicosis without thyrotoxic crisis - With secondary clinical complications",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Heat intolerance', 'Unintentional weight loss', 'Tremor', 'Tachycardia', 'Frequent bowel movements', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e05.90.9": ICD10DiagnosticRecord(
        code="E05.90.9",
        preferred_name="Thyrotoxicosis without thyrotoxic crisis - Unspecified clinical manifestation",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Heat intolerance', 'Unintentional weight loss', 'Tremor', 'Tachycardia', 'Frequent bowel movements'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e10.9": ICD10DiagnosticRecord(
        code="E10.9",
        preferred_name="Type 1 diabetes mellitus without complications",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Polyuria', 'Polydipsia', 'Polyphagia', 'Ketonuria', 'Weight loss'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e10.9.1": ICD10DiagnosticRecord(
        code="E10.9.1",
        preferred_name="Type 1 diabetes mellitus without complications - Acute / Accelerated phase",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Polyuria', 'Polydipsia', 'Polyphagia', 'Ketonuria', 'Weight loss', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e10.9.2": ICD10DiagnosticRecord(
        code="E10.9.2",
        preferred_name="Type 1 diabetes mellitus without complications - Chronic / Stable maintenance",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Polyuria', 'Polydipsia', 'Polyphagia', 'Ketonuria', 'Weight loss', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e10.9.8": ICD10DiagnosticRecord(
        code="E10.9.8",
        preferred_name="Type 1 diabetes mellitus without complications - With secondary clinical complications",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Polyuria', 'Polydipsia', 'Polyphagia', 'Ketonuria', 'Weight loss', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e10.9.9": ICD10DiagnosticRecord(
        code="E10.9.9",
        preferred_name="Type 1 diabetes mellitus without complications - Unspecified clinical manifestation",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Polyuria', 'Polydipsia', 'Polyphagia', 'Ketonuria', 'Weight loss'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e11.9": ICD10DiagnosticRecord(
        code="E11.9",
        preferred_name="Type 2 diabetes mellitus without complications",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Elevated fasting glucose', 'Elevated HbA1c >= 6.5%', 'Acanthosis nigricans', 'Blurred vision'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e11.9.1": ICD10DiagnosticRecord(
        code="E11.9.1",
        preferred_name="Type 2 diabetes mellitus without complications - Acute / Accelerated phase",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Elevated fasting glucose', 'Elevated HbA1c >= 6.5%', 'Acanthosis nigricans', 'Blurred vision', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e11.9.2": ICD10DiagnosticRecord(
        code="E11.9.2",
        preferred_name="Type 2 diabetes mellitus without complications - Chronic / Stable maintenance",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Elevated fasting glucose', 'Elevated HbA1c >= 6.5%', 'Acanthosis nigricans', 'Blurred vision', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e11.9.8": ICD10DiagnosticRecord(
        code="E11.9.8",
        preferred_name="Type 2 diabetes mellitus without complications - With secondary clinical complications",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Elevated fasting glucose', 'Elevated HbA1c >= 6.5%', 'Acanthosis nigricans', 'Blurred vision', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e11.9.9": ICD10DiagnosticRecord(
        code="E11.9.9",
        preferred_name="Type 2 diabetes mellitus without complications - Unspecified clinical manifestation",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Elevated fasting glucose', 'Elevated HbA1c >= 6.5%', 'Acanthosis nigricans', 'Blurred vision'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e11.21": ICD10DiagnosticRecord(
        code="E11.21",
        preferred_name="Type 2 diabetes with diabetic nephropathy",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Persistent microalbuminuria', 'Elevated serum creatinine', 'Hypertension', 'Glomerular filtration decline'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e11.21.1": ICD10DiagnosticRecord(
        code="E11.21.1",
        preferred_name="Type 2 diabetes with diabetic nephropathy - Acute / Accelerated phase",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Persistent microalbuminuria', 'Elevated serum creatinine', 'Hypertension', 'Glomerular filtration decline', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e11.21.2": ICD10DiagnosticRecord(
        code="E11.21.2",
        preferred_name="Type 2 diabetes with diabetic nephropathy - Chronic / Stable maintenance",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Persistent microalbuminuria', 'Elevated serum creatinine', 'Hypertension', 'Glomerular filtration decline', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e11.21.8": ICD10DiagnosticRecord(
        code="E11.21.8",
        preferred_name="Type 2 diabetes with diabetic nephropathy - With secondary clinical complications",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Persistent microalbuminuria', 'Elevated serum creatinine', 'Hypertension', 'Glomerular filtration decline', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e11.21.9": ICD10DiagnosticRecord(
        code="E11.21.9",
        preferred_name="Type 2 diabetes with diabetic nephropathy - Unspecified clinical manifestation",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Persistent microalbuminuria', 'Elevated serum creatinine', 'Hypertension', 'Glomerular filtration decline'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e11.319": ICD10DiagnosticRecord(
        code="E11.319",
        preferred_name="Type 2 diabetes with unspecified diabetic retinopathy",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Visual floaters', 'Decreased visual acuity', 'Microaneurysms on fundoscopy'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e11.319.1": ICD10DiagnosticRecord(
        code="E11.319.1",
        preferred_name="Type 2 diabetes with unspecified diabetic retinopathy - Acute / Accelerated phase",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Visual floaters', 'Decreased visual acuity', 'Microaneurysms on fundoscopy', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e11.319.2": ICD10DiagnosticRecord(
        code="E11.319.2",
        preferred_name="Type 2 diabetes with unspecified diabetic retinopathy - Chronic / Stable maintenance",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Visual floaters', 'Decreased visual acuity', 'Microaneurysms on fundoscopy', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e11.319.8": ICD10DiagnosticRecord(
        code="E11.319.8",
        preferred_name="Type 2 diabetes with unspecified diabetic retinopathy - With secondary clinical complications",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Visual floaters', 'Decreased visual acuity', 'Microaneurysms on fundoscopy', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e11.319.9": ICD10DiagnosticRecord(
        code="E11.319.9",
        preferred_name="Type 2 diabetes with unspecified diabetic retinopathy - Unspecified clinical manifestation",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Visual floaters', 'Decreased visual acuity', 'Microaneurysms on fundoscopy'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e11.40": ICD10DiagnosticRecord(
        code="E11.40",
        preferred_name="Type 2 diabetes with diabetic neuropathy",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Bilateral stocking-glove paresthesia', 'Burning foot pain', 'Loss of vibratory sense'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e11.40.1": ICD10DiagnosticRecord(
        code="E11.40.1",
        preferred_name="Type 2 diabetes with diabetic neuropathy - Acute / Accelerated phase",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Bilateral stocking-glove paresthesia', 'Burning foot pain', 'Loss of vibratory sense', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e11.40.2": ICD10DiagnosticRecord(
        code="E11.40.2",
        preferred_name="Type 2 diabetes with diabetic neuropathy - Chronic / Stable maintenance",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Bilateral stocking-glove paresthesia', 'Burning foot pain', 'Loss of vibratory sense', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e11.40.8": ICD10DiagnosticRecord(
        code="E11.40.8",
        preferred_name="Type 2 diabetes with diabetic neuropathy - With secondary clinical complications",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Bilateral stocking-glove paresthesia', 'Burning foot pain', 'Loss of vibratory sense', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e11.40.9": ICD10DiagnosticRecord(
        code="E11.40.9",
        preferred_name="Type 2 diabetes with diabetic neuropathy - Unspecified clinical manifestation",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Bilateral stocking-glove paresthesia', 'Burning foot pain', 'Loss of vibratory sense'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e11.65": ICD10DiagnosticRecord(
        code="E11.65",
        preferred_name="Type 2 diabetes with hyperglycemia",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Severe glucose > 250 mg/dL', 'Dehydration', 'Fatigue', 'Osmotic diuresis'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e11.65.1": ICD10DiagnosticRecord(
        code="E11.65.1",
        preferred_name="Type 2 diabetes with hyperglycemia - Acute / Accelerated phase",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Severe glucose > 250 mg/dL', 'Dehydration', 'Fatigue', 'Osmotic diuresis', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e11.65.2": ICD10DiagnosticRecord(
        code="E11.65.2",
        preferred_name="Type 2 diabetes with hyperglycemia - Chronic / Stable maintenance",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Severe glucose > 250 mg/dL', 'Dehydration', 'Fatigue', 'Osmotic diuresis', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e11.65.8": ICD10DiagnosticRecord(
        code="E11.65.8",
        preferred_name="Type 2 diabetes with hyperglycemia - With secondary clinical complications",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Severe glucose > 250 mg/dL', 'Dehydration', 'Fatigue', 'Osmotic diuresis', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e11.65.9": ICD10DiagnosticRecord(
        code="E11.65.9",
        preferred_name="Type 2 diabetes with hyperglycemia - Unspecified clinical manifestation",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Severe glucose > 250 mg/dL', 'Dehydration', 'Fatigue', 'Osmotic diuresis'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e11.69": ICD10DiagnosticRecord(
        code="E11.69",
        preferred_name="Type 2 diabetes with other specified complication",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Delayed wound healing', 'Diabetic foot ulceration', 'Gastroparesis'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e11.69.1": ICD10DiagnosticRecord(
        code="E11.69.1",
        preferred_name="Type 2 diabetes with other specified complication - Acute / Accelerated phase",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Delayed wound healing', 'Diabetic foot ulceration', 'Gastroparesis', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e11.69.2": ICD10DiagnosticRecord(
        code="E11.69.2",
        preferred_name="Type 2 diabetes with other specified complication - Chronic / Stable maintenance",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Delayed wound healing', 'Diabetic foot ulceration', 'Gastroparesis', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e11.69.8": ICD10DiagnosticRecord(
        code="E11.69.8",
        preferred_name="Type 2 diabetes with other specified complication - With secondary clinical complications",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Delayed wound healing', 'Diabetic foot ulceration', 'Gastroparesis', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e11.69.9": ICD10DiagnosticRecord(
        code="E11.69.9",
        preferred_name="Type 2 diabetes with other specified complication - Unspecified clinical manifestation",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Delayed wound healing', 'Diabetic foot ulceration', 'Gastroparesis'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e66.01": ICD10DiagnosticRecord(
        code="E66.01",
        preferred_name="Morbid (severe) obesity due to excess calories",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['BMI >= 40 kg/m2', 'Obstructive sleep apnea', 'Joint pain', 'Impaired mobility'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e66.01.1": ICD10DiagnosticRecord(
        code="E66.01.1",
        preferred_name="Morbid (severe) obesity due to excess calories - Acute / Accelerated phase",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['BMI >= 40 kg/m2', 'Obstructive sleep apnea', 'Joint pain', 'Impaired mobility', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e66.01.2": ICD10DiagnosticRecord(
        code="E66.01.2",
        preferred_name="Morbid (severe) obesity due to excess calories - Chronic / Stable maintenance",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['BMI >= 40 kg/m2', 'Obstructive sleep apnea', 'Joint pain', 'Impaired mobility', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e66.01.8": ICD10DiagnosticRecord(
        code="E66.01.8",
        preferred_name="Morbid (severe) obesity due to excess calories - With secondary clinical complications",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['BMI >= 40 kg/m2', 'Obstructive sleep apnea', 'Joint pain', 'Impaired mobility', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e66.01.9": ICD10DiagnosticRecord(
        code="E66.01.9",
        preferred_name="Morbid (severe) obesity due to excess calories - Unspecified clinical manifestation",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['BMI >= 40 kg/m2', 'Obstructive sleep apnea', 'Joint pain', 'Impaired mobility'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e78.00": ICD10DiagnosticRecord(
        code="E78.00",
        preferred_name="Pure hypercholesterolemia, unspecified",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Elevated serum LDL-C', 'Xanthelasma', 'Corneal arcus', 'Premature CAD risk'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e78.00.1": ICD10DiagnosticRecord(
        code="E78.00.1",
        preferred_name="Pure hypercholesterolemia, unspecified - Acute / Accelerated phase",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Elevated serum LDL-C', 'Xanthelasma', 'Corneal arcus', 'Premature CAD risk', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e78.00.2": ICD10DiagnosticRecord(
        code="E78.00.2",
        preferred_name="Pure hypercholesterolemia, unspecified - Chronic / Stable maintenance",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Elevated serum LDL-C', 'Xanthelasma', 'Corneal arcus', 'Premature CAD risk', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e78.00.8": ICD10DiagnosticRecord(
        code="E78.00.8",
        preferred_name="Pure hypercholesterolemia, unspecified - With secondary clinical complications",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Elevated serum LDL-C', 'Xanthelasma', 'Corneal arcus', 'Premature CAD risk', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e78.00.9": ICD10DiagnosticRecord(
        code="E78.00.9",
        preferred_name="Pure hypercholesterolemia, unspecified - Unspecified clinical manifestation",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Elevated serum LDL-C', 'Xanthelasma', 'Corneal arcus', 'Premature CAD risk'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e78.1": ICD10DiagnosticRecord(
        code="E78.1",
        preferred_name="Pure hyperglyceridemia",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Elevated serum triglycerides > 200 mg/dL', 'Eruptive xanthomas', 'Acute pancreatitis risk'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e78.1.1": ICD10DiagnosticRecord(
        code="E78.1.1",
        preferred_name="Pure hyperglyceridemia - Acute / Accelerated phase",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Elevated serum triglycerides > 200 mg/dL', 'Eruptive xanthomas', 'Acute pancreatitis risk', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e78.1.2": ICD10DiagnosticRecord(
        code="E78.1.2",
        preferred_name="Pure hyperglyceridemia - Chronic / Stable maintenance",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Elevated serum triglycerides > 200 mg/dL', 'Eruptive xanthomas', 'Acute pancreatitis risk', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e78.1.8": ICD10DiagnosticRecord(
        code="E78.1.8",
        preferred_name="Pure hyperglyceridemia - With secondary clinical complications",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Elevated serum triglycerides > 200 mg/dL', 'Eruptive xanthomas', 'Acute pancreatitis risk', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e78.1.9": ICD10DiagnosticRecord(
        code="E78.1.9",
        preferred_name="Pure hyperglyceridemia - Unspecified clinical manifestation",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Elevated serum triglycerides > 200 mg/dL', 'Eruptive xanthomas', 'Acute pancreatitis risk'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e78.2": ICD10DiagnosticRecord(
        code="E78.2",
        preferred_name="Mixed hyperlipidemia",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Concurrent elevation of LDL-C and triglycerides', 'Low HDL-C concentration'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e78.2.1": ICD10DiagnosticRecord(
        code="E78.2.1",
        preferred_name="Mixed hyperlipidemia - Acute / Accelerated phase",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Concurrent elevation of LDL-C and triglycerides', 'Low HDL-C concentration', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e78.2.2": ICD10DiagnosticRecord(
        code="E78.2.2",
        preferred_name="Mixed hyperlipidemia - Chronic / Stable maintenance",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Concurrent elevation of LDL-C and triglycerides', 'Low HDL-C concentration', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e78.2.8": ICD10DiagnosticRecord(
        code="E78.2.8",
        preferred_name="Mixed hyperlipidemia - With secondary clinical complications",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Concurrent elevation of LDL-C and triglycerides', 'Low HDL-C concentration', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e78.2.9": ICD10DiagnosticRecord(
        code="E78.2.9",
        preferred_name="Mixed hyperlipidemia - Unspecified clinical manifestation",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Concurrent elevation of LDL-C and triglycerides', 'Low HDL-C concentration'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e79.0": ICD10DiagnosticRecord(
        code="E79.0",
        preferred_name="Hyperuricemia without signs of arthritis or tophaceous disease",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Serum uric acid > 7.0 mg/dL', 'Asymptomatic urate crystal deposition'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e79.0.1": ICD10DiagnosticRecord(
        code="E79.0.1",
        preferred_name="Hyperuricemia without signs of arthritis or tophaceous disease - Acute / Accelerated phase",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Serum uric acid > 7.0 mg/dL', 'Asymptomatic urate crystal deposition', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e79.0.2": ICD10DiagnosticRecord(
        code="E79.0.2",
        preferred_name="Hyperuricemia without signs of arthritis or tophaceous disease - Chronic / Stable maintenance",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Serum uric acid > 7.0 mg/dL', 'Asymptomatic urate crystal deposition', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e79.0.8": ICD10DiagnosticRecord(
        code="E79.0.8",
        preferred_name="Hyperuricemia without signs of arthritis or tophaceous disease - With secondary clinical complications",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Serum uric acid > 7.0 mg/dL', 'Asymptomatic urate crystal deposition', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e79.0.9": ICD10DiagnosticRecord(
        code="E79.0.9",
        preferred_name="Hyperuricemia without signs of arthritis or tophaceous disease - Unspecified clinical manifestation",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Serum uric acid > 7.0 mg/dL', 'Asymptomatic urate crystal deposition'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e87.1": ICD10DiagnosticRecord(
        code="E87.1",
        preferred_name="Hypo-osmolality and hyponatremia",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Serum sodium < 135 mEq/L', 'Lethargy', 'Confusion', 'Nausea', 'Seizure risk in acute drop'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e87.1.1": ICD10DiagnosticRecord(
        code="E87.1.1",
        preferred_name="Hypo-osmolality and hyponatremia - Acute / Accelerated phase",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Serum sodium < 135 mEq/L', 'Lethargy', 'Confusion', 'Nausea', 'Seizure risk in acute drop', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e87.1.2": ICD10DiagnosticRecord(
        code="E87.1.2",
        preferred_name="Hypo-osmolality and hyponatremia - Chronic / Stable maintenance",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Serum sodium < 135 mEq/L', 'Lethargy', 'Confusion', 'Nausea', 'Seizure risk in acute drop', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e87.1.8": ICD10DiagnosticRecord(
        code="E87.1.8",
        preferred_name="Hypo-osmolality and hyponatremia - With secondary clinical complications",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Serum sodium < 135 mEq/L', 'Lethargy', 'Confusion', 'Nausea', 'Seizure risk in acute drop', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e87.1.9": ICD10DiagnosticRecord(
        code="E87.1.9",
        preferred_name="Hypo-osmolality and hyponatremia - Unspecified clinical manifestation",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Serum sodium < 135 mEq/L', 'Lethargy', 'Confusion', 'Nausea', 'Seizure risk in acute drop'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e87.2": ICD10DiagnosticRecord(
        code="E87.2",
        preferred_name="Acidosis (metabolic / lactic)",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Kussmaul breathing', 'Arterial pH < 7.35', 'Elevated anion gap', 'Hypotension'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e87.2.1": ICD10DiagnosticRecord(
        code="E87.2.1",
        preferred_name="Acidosis (metabolic / lactic) - Acute / Accelerated phase",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Kussmaul breathing', 'Arterial pH < 7.35', 'Elevated anion gap', 'Hypotension', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e87.2.2": ICD10DiagnosticRecord(
        code="E87.2.2",
        preferred_name="Acidosis (metabolic / lactic) - Chronic / Stable maintenance",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Kussmaul breathing', 'Arterial pH < 7.35', 'Elevated anion gap', 'Hypotension', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e87.2.8": ICD10DiagnosticRecord(
        code="E87.2.8",
        preferred_name="Acidosis (metabolic / lactic) - With secondary clinical complications",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Kussmaul breathing', 'Arterial pH < 7.35', 'Elevated anion gap', 'Hypotension', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e87.2.9": ICD10DiagnosticRecord(
        code="E87.2.9",
        preferred_name="Acidosis (metabolic / lactic) - Unspecified clinical manifestation",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Kussmaul breathing', 'Arterial pH < 7.35', 'Elevated anion gap', 'Hypotension'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e87.5": ICD10DiagnosticRecord(
        code="E87.5",
        preferred_name="Hyperkalemia",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Serum potassium > 5.5 mEq/L', 'Peaked T waves on ECG', 'Muscle weakness', 'Ventricular standstill risk'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e87.5.1": ICD10DiagnosticRecord(
        code="E87.5.1",
        preferred_name="Hyperkalemia - Acute / Accelerated phase",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Serum potassium > 5.5 mEq/L', 'Peaked T waves on ECG', 'Muscle weakness', 'Ventricular standstill risk', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e87.5.2": ICD10DiagnosticRecord(
        code="E87.5.2",
        preferred_name="Hyperkalemia - Chronic / Stable maintenance",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Serum potassium > 5.5 mEq/L', 'Peaked T waves on ECG', 'Muscle weakness', 'Ventricular standstill risk', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e87.5.8": ICD10DiagnosticRecord(
        code="E87.5.8",
        preferred_name="Hyperkalemia - With secondary clinical complications",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Serum potassium > 5.5 mEq/L', 'Peaked T waves on ECG', 'Muscle weakness', 'Ventricular standstill risk', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e87.5.9": ICD10DiagnosticRecord(
        code="E87.5.9",
        preferred_name="Hyperkalemia - Unspecified clinical manifestation",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Serum potassium > 5.5 mEq/L', 'Peaked T waves on ECG', 'Muscle weakness', 'Ventricular standstill risk'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e87.6": ICD10DiagnosticRecord(
        code="E87.6",
        preferred_name="Hypokalemia",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Serum potassium < 3.5 mEq/L', 'U waves on ECG', 'Muscle cramps', 'Paralytic ileus', 'Digitalis toxicity'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e87.6.1": ICD10DiagnosticRecord(
        code="E87.6.1",
        preferred_name="Hypokalemia - Acute / Accelerated phase",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Serum potassium < 3.5 mEq/L', 'U waves on ECG', 'Muscle cramps', 'Paralytic ileus', 'Digitalis toxicity', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e87.6.2": ICD10DiagnosticRecord(
        code="E87.6.2",
        preferred_name="Hypokalemia - Chronic / Stable maintenance",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Serum potassium < 3.5 mEq/L', 'U waves on ECG', 'Muscle cramps', 'Paralytic ileus', 'Digitalis toxicity', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e87.6.8": ICD10DiagnosticRecord(
        code="E87.6.8",
        preferred_name="Hypokalemia - With secondary clinical complications",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Serum potassium < 3.5 mEq/L', 'U waves on ECG', 'Muscle cramps', 'Paralytic ileus', 'Digitalis toxicity', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "e87.6.9": ICD10DiagnosticRecord(
        code="E87.6.9",
        preferred_name="Hypokalemia - Unspecified clinical manifestation",
        chapter_name="EndocrineMetabolic",
        chapter_range="E00-E89",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Serum potassium < 3.5 mEq/L', 'U waves on ECG', 'Muscle cramps', 'Paralytic ileus', 'Digitalis toxicity'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k21.0": ICD10DiagnosticRecord(
        code="K21.0",
        preferred_name="Gastro-esophageal reflux disease with esophagitis",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Retrosternal pyrosis (heartburn)', 'Acid regurgitation', 'Dysphagia', 'Water brash'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k21.0.1": ICD10DiagnosticRecord(
        code="K21.0.1",
        preferred_name="Gastro-esophageal reflux disease with esophagitis - Acute / Accelerated phase",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Retrosternal pyrosis (heartburn)', 'Acid regurgitation', 'Dysphagia', 'Water brash', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k21.0.2": ICD10DiagnosticRecord(
        code="K21.0.2",
        preferred_name="Gastro-esophageal reflux disease with esophagitis - Chronic / Stable maintenance",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Retrosternal pyrosis (heartburn)', 'Acid regurgitation', 'Dysphagia', 'Water brash', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k21.0.8": ICD10DiagnosticRecord(
        code="K21.0.8",
        preferred_name="Gastro-esophageal reflux disease with esophagitis - With secondary clinical complications",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Retrosternal pyrosis (heartburn)', 'Acid regurgitation', 'Dysphagia', 'Water brash', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k21.0.9": ICD10DiagnosticRecord(
        code="K21.0.9",
        preferred_name="Gastro-esophageal reflux disease with esophagitis - Unspecified clinical manifestation",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Retrosternal pyrosis (heartburn)', 'Acid regurgitation', 'Dysphagia', 'Water brash'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k21.9": ICD10DiagnosticRecord(
        code="K21.9",
        preferred_name="Gastro-esophageal reflux disease without esophagitis",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Postprandial sour taste', 'Globus sensation', 'Chronic throat clearing'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k21.9.1": ICD10DiagnosticRecord(
        code="K21.9.1",
        preferred_name="Gastro-esophageal reflux disease without esophagitis - Acute / Accelerated phase",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Postprandial sour taste', 'Globus sensation', 'Chronic throat clearing', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k21.9.2": ICD10DiagnosticRecord(
        code="K21.9.2",
        preferred_name="Gastro-esophageal reflux disease without esophagitis - Chronic / Stable maintenance",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Postprandial sour taste', 'Globus sensation', 'Chronic throat clearing', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k21.9.8": ICD10DiagnosticRecord(
        code="K21.9.8",
        preferred_name="Gastro-esophageal reflux disease without esophagitis - With secondary clinical complications",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Postprandial sour taste', 'Globus sensation', 'Chronic throat clearing', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k21.9.9": ICD10DiagnosticRecord(
        code="K21.9.9",
        preferred_name="Gastro-esophageal reflux disease without esophagitis - Unspecified clinical manifestation",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Postprandial sour taste', 'Globus sensation', 'Chronic throat clearing'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k25.9": ICD10DiagnosticRecord(
        code="K25.9",
        preferred_name="Gastric ulcer, unspecified as acute or chronic",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Epigastric gnawing pain exacerbated by food', 'Early satiety', 'Melena', 'Occult GI bleeding'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k25.9.1": ICD10DiagnosticRecord(
        code="K25.9.1",
        preferred_name="Gastric ulcer, unspecified as acute or chronic - Acute / Accelerated phase",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Epigastric gnawing pain exacerbated by food', 'Early satiety', 'Melena', 'Occult GI bleeding', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k25.9.2": ICD10DiagnosticRecord(
        code="K25.9.2",
        preferred_name="Gastric ulcer, unspecified as acute or chronic - Chronic / Stable maintenance",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Epigastric gnawing pain exacerbated by food', 'Early satiety', 'Melena', 'Occult GI bleeding', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k25.9.8": ICD10DiagnosticRecord(
        code="K25.9.8",
        preferred_name="Gastric ulcer, unspecified as acute or chronic - With secondary clinical complications",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Epigastric gnawing pain exacerbated by food', 'Early satiety', 'Melena', 'Occult GI bleeding', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k25.9.9": ICD10DiagnosticRecord(
        code="K25.9.9",
        preferred_name="Gastric ulcer, unspecified as acute or chronic - Unspecified clinical manifestation",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Epigastric gnawing pain exacerbated by food', 'Early satiety', 'Melena', 'Occult GI bleeding'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k26.9": ICD10DiagnosticRecord(
        code="K26.9",
        preferred_name="Duodenal ulcer, unspecified as acute or chronic",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Epigastric burning pain relieved by food intake', 'Nocturnal awakening with pain'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k26.9.1": ICD10DiagnosticRecord(
        code="K26.9.1",
        preferred_name="Duodenal ulcer, unspecified as acute or chronic - Acute / Accelerated phase",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Epigastric burning pain relieved by food intake', 'Nocturnal awakening with pain', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k26.9.2": ICD10DiagnosticRecord(
        code="K26.9.2",
        preferred_name="Duodenal ulcer, unspecified as acute or chronic - Chronic / Stable maintenance",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Epigastric burning pain relieved by food intake', 'Nocturnal awakening with pain', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k26.9.8": ICD10DiagnosticRecord(
        code="K26.9.8",
        preferred_name="Duodenal ulcer, unspecified as acute or chronic - With secondary clinical complications",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Epigastric burning pain relieved by food intake', 'Nocturnal awakening with pain', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k26.9.9": ICD10DiagnosticRecord(
        code="K26.9.9",
        preferred_name="Duodenal ulcer, unspecified as acute or chronic - Unspecified clinical manifestation",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Epigastric burning pain relieved by food intake', 'Nocturnal awakening with pain'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k29.70": ICD10DiagnosticRecord(
        code="K29.70",
        preferred_name="Gastritis, unspecified, without bleeding",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Epigastric fullness', 'Nausea', 'Postprandial bloating', 'Anorexia'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k29.70.1": ICD10DiagnosticRecord(
        code="K29.70.1",
        preferred_name="Gastritis, unspecified, without bleeding - Acute / Accelerated phase",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Epigastric fullness', 'Nausea', 'Postprandial bloating', 'Anorexia', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k29.70.2": ICD10DiagnosticRecord(
        code="K29.70.2",
        preferred_name="Gastritis, unspecified, without bleeding - Chronic / Stable maintenance",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Epigastric fullness', 'Nausea', 'Postprandial bloating', 'Anorexia', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k29.70.8": ICD10DiagnosticRecord(
        code="K29.70.8",
        preferred_name="Gastritis, unspecified, without bleeding - With secondary clinical complications",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Epigastric fullness', 'Nausea', 'Postprandial bloating', 'Anorexia', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k29.70.9": ICD10DiagnosticRecord(
        code="K29.70.9",
        preferred_name="Gastritis, unspecified, without bleeding - Unspecified clinical manifestation",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Epigastric fullness', 'Nausea', 'Postprandial bloating', 'Anorexia'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k35.80": ICD10DiagnosticRecord(
        code="K35.80",
        preferred_name="Unspecified acute appendicitis",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Periumbilical pain migrating to McBurney point', 'Fever', 'Anorexia', 'Rebound tenderness'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k35.80.1": ICD10DiagnosticRecord(
        code="K35.80.1",
        preferred_name="Unspecified acute appendicitis - Acute / Accelerated phase",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Periumbilical pain migrating to McBurney point', 'Fever', 'Anorexia', 'Rebound tenderness', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k35.80.2": ICD10DiagnosticRecord(
        code="K35.80.2",
        preferred_name="Unspecified acute appendicitis - Chronic / Stable maintenance",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Periumbilical pain migrating to McBurney point', 'Fever', 'Anorexia', 'Rebound tenderness', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k35.80.8": ICD10DiagnosticRecord(
        code="K35.80.8",
        preferred_name="Unspecified acute appendicitis - With secondary clinical complications",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Periumbilical pain migrating to McBurney point', 'Fever', 'Anorexia', 'Rebound tenderness', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k35.80.9": ICD10DiagnosticRecord(
        code="K35.80.9",
        preferred_name="Unspecified acute appendicitis - Unspecified clinical manifestation",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Periumbilical pain migrating to McBurney point', 'Fever', 'Anorexia', 'Rebound tenderness'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k50.90": ICD10DiagnosticRecord(
        code="K50.90",
        preferred_name="Crohn disease, unspecified, without complications",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Chronic non-bloody diarrhea', 'Right lower quadrant crampy pain', 'Weight loss', 'Fistulae'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k50.90.1": ICD10DiagnosticRecord(
        code="K50.90.1",
        preferred_name="Crohn disease, unspecified, without complications - Acute / Accelerated phase",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Chronic non-bloody diarrhea', 'Right lower quadrant crampy pain', 'Weight loss', 'Fistulae', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k50.90.2": ICD10DiagnosticRecord(
        code="K50.90.2",
        preferred_name="Crohn disease, unspecified, without complications - Chronic / Stable maintenance",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Chronic non-bloody diarrhea', 'Right lower quadrant crampy pain', 'Weight loss', 'Fistulae', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k50.90.8": ICD10DiagnosticRecord(
        code="K50.90.8",
        preferred_name="Crohn disease, unspecified, without complications - With secondary clinical complications",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Chronic non-bloody diarrhea', 'Right lower quadrant crampy pain', 'Weight loss', 'Fistulae', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k50.90.9": ICD10DiagnosticRecord(
        code="K50.90.9",
        preferred_name="Crohn disease, unspecified, without complications - Unspecified clinical manifestation",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Chronic non-bloody diarrhea', 'Right lower quadrant crampy pain', 'Weight loss', 'Fistulae'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k51.90": ICD10DiagnosticRecord(
        code="K51.90",
        preferred_name="Ulcerative colitis, unspecified, without complications",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Recurrent bloody diarrhea with mucus', 'Tenesmus', 'Urgent fecal incontinence'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k51.90.1": ICD10DiagnosticRecord(
        code="K51.90.1",
        preferred_name="Ulcerative colitis, unspecified, without complications - Acute / Accelerated phase",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Recurrent bloody diarrhea with mucus', 'Tenesmus', 'Urgent fecal incontinence', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k51.90.2": ICD10DiagnosticRecord(
        code="K51.90.2",
        preferred_name="Ulcerative colitis, unspecified, without complications - Chronic / Stable maintenance",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Recurrent bloody diarrhea with mucus', 'Tenesmus', 'Urgent fecal incontinence', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k51.90.8": ICD10DiagnosticRecord(
        code="K51.90.8",
        preferred_name="Ulcerative colitis, unspecified, without complications - With secondary clinical complications",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Recurrent bloody diarrhea with mucus', 'Tenesmus', 'Urgent fecal incontinence', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k51.90.9": ICD10DiagnosticRecord(
        code="K51.90.9",
        preferred_name="Ulcerative colitis, unspecified, without complications - Unspecified clinical manifestation",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Recurrent bloody diarrhea with mucus', 'Tenesmus', 'Urgent fecal incontinence'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k58.0": ICD10DiagnosticRecord(
        code="K58.0",
        preferred_name="Irritable bowel syndrome with diarrhea",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Recurrent abdominal pain relieved by defecation', 'Frequent watery stools', 'Bloating'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k58.0.1": ICD10DiagnosticRecord(
        code="K58.0.1",
        preferred_name="Irritable bowel syndrome with diarrhea - Acute / Accelerated phase",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Recurrent abdominal pain relieved by defecation', 'Frequent watery stools', 'Bloating', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k58.0.2": ICD10DiagnosticRecord(
        code="K58.0.2",
        preferred_name="Irritable bowel syndrome with diarrhea - Chronic / Stable maintenance",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Recurrent abdominal pain relieved by defecation', 'Frequent watery stools', 'Bloating', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k58.0.8": ICD10DiagnosticRecord(
        code="K58.0.8",
        preferred_name="Irritable bowel syndrome with diarrhea - With secondary clinical complications",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Recurrent abdominal pain relieved by defecation', 'Frequent watery stools', 'Bloating', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k58.0.9": ICD10DiagnosticRecord(
        code="K58.0.9",
        preferred_name="Irritable bowel syndrome with diarrhea - Unspecified clinical manifestation",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Recurrent abdominal pain relieved by defecation', 'Frequent watery stools', 'Bloating'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k70.30": ICD10DiagnosticRecord(
        code="K70.30",
        preferred_name="Alcoholic cirrhosis of liver without ascites",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Spider angiomas', 'Palmar erythema', 'Jaundice', 'Hepatosplenomegaly', 'Caput medusae'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k70.30.1": ICD10DiagnosticRecord(
        code="K70.30.1",
        preferred_name="Alcoholic cirrhosis of liver without ascites - Acute / Accelerated phase",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Spider angiomas', 'Palmar erythema', 'Jaundice', 'Hepatosplenomegaly', 'Caput medusae', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k70.30.2": ICD10DiagnosticRecord(
        code="K70.30.2",
        preferred_name="Alcoholic cirrhosis of liver without ascites - Chronic / Stable maintenance",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Spider angiomas', 'Palmar erythema', 'Jaundice', 'Hepatosplenomegaly', 'Caput medusae', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k70.30.8": ICD10DiagnosticRecord(
        code="K70.30.8",
        preferred_name="Alcoholic cirrhosis of liver without ascites - With secondary clinical complications",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Spider angiomas', 'Palmar erythema', 'Jaundice', 'Hepatosplenomegaly', 'Caput medusae', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k70.30.9": ICD10DiagnosticRecord(
        code="K70.30.9",
        preferred_name="Alcoholic cirrhosis of liver without ascites - Unspecified clinical manifestation",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Spider angiomas', 'Palmar erythema', 'Jaundice', 'Hepatosplenomegaly', 'Caput medusae'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k76.0": ICD10DiagnosticRecord(
        code="K76.0",
        preferred_name="Fatty (change of) liver, not elsewhere classified (NAFLD)",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Mild right upper quadrant ache', 'Elevated ALT/AST', 'Hepatomegaly on ultrasound'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k76.0.1": ICD10DiagnosticRecord(
        code="K76.0.1",
        preferred_name="Fatty (change of) liver, not elsewhere classified (NAFLD) - Acute / Accelerated phase",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Mild right upper quadrant ache', 'Elevated ALT/AST', 'Hepatomegaly on ultrasound', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k76.0.2": ICD10DiagnosticRecord(
        code="K76.0.2",
        preferred_name="Fatty (change of) liver, not elsewhere classified (NAFLD) - Chronic / Stable maintenance",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Mild right upper quadrant ache', 'Elevated ALT/AST', 'Hepatomegaly on ultrasound', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k76.0.8": ICD10DiagnosticRecord(
        code="K76.0.8",
        preferred_name="Fatty (change of) liver, not elsewhere classified (NAFLD) - With secondary clinical complications",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Mild right upper quadrant ache', 'Elevated ALT/AST', 'Hepatomegaly on ultrasound', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k76.0.9": ICD10DiagnosticRecord(
        code="K76.0.9",
        preferred_name="Fatty (change of) liver, not elsewhere classified (NAFLD) - Unspecified clinical manifestation",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Mild right upper quadrant ache', 'Elevated ALT/AST', 'Hepatomegaly on ultrasound'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k80.20": ICD10DiagnosticRecord(
        code="K80.20",
        preferred_name="Calculus of gallbladder without cholecystitis",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Biliary colic after fatty meals', 'Right upper quadrant cramping radiating to right shoulder'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k80.20.1": ICD10DiagnosticRecord(
        code="K80.20.1",
        preferred_name="Calculus of gallbladder without cholecystitis - Acute / Accelerated phase",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Biliary colic after fatty meals', 'Right upper quadrant cramping radiating to right shoulder', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k80.20.2": ICD10DiagnosticRecord(
        code="K80.20.2",
        preferred_name="Calculus of gallbladder without cholecystitis - Chronic / Stable maintenance",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Biliary colic after fatty meals', 'Right upper quadrant cramping radiating to right shoulder', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k80.20.8": ICD10DiagnosticRecord(
        code="K80.20.8",
        preferred_name="Calculus of gallbladder without cholecystitis - With secondary clinical complications",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Biliary colic after fatty meals', 'Right upper quadrant cramping radiating to right shoulder', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "k80.20.9": ICD10DiagnosticRecord(
        code="K80.20.9",
        preferred_name="Calculus of gallbladder without cholecystitis - Unspecified clinical manifestation",
        chapter_name="Gastrointestinal",
        chapter_range="K00-K95",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Biliary colic after fatty meals', 'Right upper quadrant cramping radiating to right shoulder'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m05.79": ICD10DiagnosticRecord(
        code="M05.79",
        preferred_name="Rheumatoid arthritis with rheumatoid factor, multiple sites",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Symmetric polyarthritis', 'Morning stiffness > 1 hour', 'Rheumatoid nodules', 'MCP/PIP joint swelling'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m05.79.1": ICD10DiagnosticRecord(
        code="M05.79.1",
        preferred_name="Rheumatoid arthritis with rheumatoid factor, multiple sites - Acute / Accelerated phase",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Symmetric polyarthritis', 'Morning stiffness > 1 hour', 'Rheumatoid nodules', 'MCP/PIP joint swelling', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m05.79.2": ICD10DiagnosticRecord(
        code="M05.79.2",
        preferred_name="Rheumatoid arthritis with rheumatoid factor, multiple sites - Chronic / Stable maintenance",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Symmetric polyarthritis', 'Morning stiffness > 1 hour', 'Rheumatoid nodules', 'MCP/PIP joint swelling', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m05.79.8": ICD10DiagnosticRecord(
        code="M05.79.8",
        preferred_name="Rheumatoid arthritis with rheumatoid factor, multiple sites - With secondary clinical complications",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Symmetric polyarthritis', 'Morning stiffness > 1 hour', 'Rheumatoid nodules', 'MCP/PIP joint swelling', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m05.79.9": ICD10DiagnosticRecord(
        code="M05.79.9",
        preferred_name="Rheumatoid arthritis with rheumatoid factor, multiple sites - Unspecified clinical manifestation",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Symmetric polyarthritis', 'Morning stiffness > 1 hour', 'Rheumatoid nodules', 'MCP/PIP joint swelling'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m10.00": ICD10DiagnosticRecord(
        code="M10.00",
        preferred_name="Idiopathic gout, unspecified site",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Acute podagra (1st MTP joint)', 'Erythematous swollen exquisitely tender joint', 'Tophi formation'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m10.00.1": ICD10DiagnosticRecord(
        code="M10.00.1",
        preferred_name="Idiopathic gout, unspecified site - Acute / Accelerated phase",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Acute podagra (1st MTP joint)', 'Erythematous swollen exquisitely tender joint', 'Tophi formation', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m10.00.2": ICD10DiagnosticRecord(
        code="M10.00.2",
        preferred_name="Idiopathic gout, unspecified site - Chronic / Stable maintenance",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Acute podagra (1st MTP joint)', 'Erythematous swollen exquisitely tender joint', 'Tophi formation', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m10.00.8": ICD10DiagnosticRecord(
        code="M10.00.8",
        preferred_name="Idiopathic gout, unspecified site - With secondary clinical complications",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Acute podagra (1st MTP joint)', 'Erythematous swollen exquisitely tender joint', 'Tophi formation', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m10.00.9": ICD10DiagnosticRecord(
        code="M10.00.9",
        preferred_name="Idiopathic gout, unspecified site - Unspecified clinical manifestation",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Acute podagra (1st MTP joint)', 'Erythematous swollen exquisitely tender joint', 'Tophi formation'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m15.0": ICD10DiagnosticRecord(
        code="M15.0",
        preferred_name="Primary generalized (osteo)arthritis",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Weight-bearing joint stiffness', 'Crepitus on range of motion', 'Heberden and Bouchard nodes'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m15.0.1": ICD10DiagnosticRecord(
        code="M15.0.1",
        preferred_name="Primary generalized (osteo)arthritis - Acute / Accelerated phase",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Weight-bearing joint stiffness', 'Crepitus on range of motion', 'Heberden and Bouchard nodes', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m15.0.2": ICD10DiagnosticRecord(
        code="M15.0.2",
        preferred_name="Primary generalized (osteo)arthritis - Chronic / Stable maintenance",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Weight-bearing joint stiffness', 'Crepitus on range of motion', 'Heberden and Bouchard nodes', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m15.0.8": ICD10DiagnosticRecord(
        code="M15.0.8",
        preferred_name="Primary generalized (osteo)arthritis - With secondary clinical complications",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Weight-bearing joint stiffness', 'Crepitus on range of motion', 'Heberden and Bouchard nodes', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m15.0.9": ICD10DiagnosticRecord(
        code="M15.0.9",
        preferred_name="Primary generalized (osteo)arthritis - Unspecified clinical manifestation",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Weight-bearing joint stiffness', 'Crepitus on range of motion', 'Heberden and Bouchard nodes'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m16.9": ICD10DiagnosticRecord(
        code="M16.9",
        preferred_name="Osteoarthritis of hip, unspecified",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Groin and anterior thigh pain', 'Antalgic gait', 'Decreased internal rotation of hip'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m16.9.1": ICD10DiagnosticRecord(
        code="M16.9.1",
        preferred_name="Osteoarthritis of hip, unspecified - Acute / Accelerated phase",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Groin and anterior thigh pain', 'Antalgic gait', 'Decreased internal rotation of hip', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m16.9.2": ICD10DiagnosticRecord(
        code="M16.9.2",
        preferred_name="Osteoarthritis of hip, unspecified - Chronic / Stable maintenance",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Groin and anterior thigh pain', 'Antalgic gait', 'Decreased internal rotation of hip', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m16.9.8": ICD10DiagnosticRecord(
        code="M16.9.8",
        preferred_name="Osteoarthritis of hip, unspecified - With secondary clinical complications",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Groin and anterior thigh pain', 'Antalgic gait', 'Decreased internal rotation of hip', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m16.9.9": ICD10DiagnosticRecord(
        code="M16.9.9",
        preferred_name="Osteoarthritis of hip, unspecified - Unspecified clinical manifestation",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Groin and anterior thigh pain', 'Antalgic gait', 'Decreased internal rotation of hip'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m17.9": ICD10DiagnosticRecord(
        code="M17.9",
        preferred_name="Osteoarthritis of knee, unspecified",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Joint line tenderness', 'Genu varum or valgum deformity', 'Difficulty ascending stairs'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m17.9.1": ICD10DiagnosticRecord(
        code="M17.9.1",
        preferred_name="Osteoarthritis of knee, unspecified - Acute / Accelerated phase",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Joint line tenderness', 'Genu varum or valgum deformity', 'Difficulty ascending stairs', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m17.9.2": ICD10DiagnosticRecord(
        code="M17.9.2",
        preferred_name="Osteoarthritis of knee, unspecified - Chronic / Stable maintenance",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Joint line tenderness', 'Genu varum or valgum deformity', 'Difficulty ascending stairs', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m17.9.8": ICD10DiagnosticRecord(
        code="M17.9.8",
        preferred_name="Osteoarthritis of knee, unspecified - With secondary clinical complications",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Joint line tenderness', 'Genu varum or valgum deformity', 'Difficulty ascending stairs', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m17.9.9": ICD10DiagnosticRecord(
        code="M17.9.9",
        preferred_name="Osteoarthritis of knee, unspecified - Unspecified clinical manifestation",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Joint line tenderness', 'Genu varum or valgum deformity', 'Difficulty ascending stairs'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m54.5": ICD10DiagnosticRecord(
        code="M54.5",
        preferred_name="Low back pain",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Lumbosacral muscle spasms', 'Pain exacerbated by flexion or lifting', 'Restricted spinal mobility'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m54.5.1": ICD10DiagnosticRecord(
        code="M54.5.1",
        preferred_name="Low back pain - Acute / Accelerated phase",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Lumbosacral muscle spasms', 'Pain exacerbated by flexion or lifting', 'Restricted spinal mobility', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m54.5.2": ICD10DiagnosticRecord(
        code="M54.5.2",
        preferred_name="Low back pain - Chronic / Stable maintenance",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Lumbosacral muscle spasms', 'Pain exacerbated by flexion or lifting', 'Restricted spinal mobility', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m54.5.8": ICD10DiagnosticRecord(
        code="M54.5.8",
        preferred_name="Low back pain - With secondary clinical complications",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Lumbosacral muscle spasms', 'Pain exacerbated by flexion or lifting', 'Restricted spinal mobility', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m54.5.9": ICD10DiagnosticRecord(
        code="M54.5.9",
        preferred_name="Low back pain - Unspecified clinical manifestation",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Lumbosacral muscle spasms', 'Pain exacerbated by flexion or lifting', 'Restricted spinal mobility'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m81.0": ICD10DiagnosticRecord(
        code="M81.0",
        preferred_name="Age-related osteoporosis without current pathological fracture",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Asymptomatic until fracture', 'T-score <= -2.5 on DEXA scan', 'Vertebral height loss', 'Dorsal kyphosis'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m81.0.1": ICD10DiagnosticRecord(
        code="M81.0.1",
        preferred_name="Age-related osteoporosis without current pathological fracture - Acute / Accelerated phase",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Asymptomatic until fracture', 'T-score <= -2.5 on DEXA scan', 'Vertebral height loss', 'Dorsal kyphosis', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m81.0.2": ICD10DiagnosticRecord(
        code="M81.0.2",
        preferred_name="Age-related osteoporosis without current pathological fracture - Chronic / Stable maintenance",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Asymptomatic until fracture', 'T-score <= -2.5 on DEXA scan', 'Vertebral height loss', 'Dorsal kyphosis', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m81.0.8": ICD10DiagnosticRecord(
        code="M81.0.8",
        preferred_name="Age-related osteoporosis without current pathological fracture - With secondary clinical complications",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Asymptomatic until fracture', 'T-score <= -2.5 on DEXA scan', 'Vertebral height loss', 'Dorsal kyphosis', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "m81.0.9": ICD10DiagnosticRecord(
        code="M81.0.9",
        preferred_name="Age-related osteoporosis without current pathological fracture - Unspecified clinical manifestation",
        chapter_name="Musculoskeletal",
        chapter_range="M00-M99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Asymptomatic until fracture', 'T-score <= -2.5 on DEXA scan', 'Vertebral height loss', 'Dorsal kyphosis'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "g40.909": ICD10DiagnosticRecord(
        code="G40.909",
        preferred_name="Epilepsy, unspecified, not intractable, without status epilepticus",
        chapter_name="Neurological",
        chapter_range="G00-G99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Generalized tonic-clonic motor activity', 'Post-ictal confusion', 'Tongue biting', 'Incontinence'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "g40.909.1": ICD10DiagnosticRecord(
        code="G40.909.1",
        preferred_name="Epilepsy, unspecified, not intractable, without status epilepticus - Acute / Accelerated phase",
        chapter_name="Neurological",
        chapter_range="G00-G99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Generalized tonic-clonic motor activity', 'Post-ictal confusion', 'Tongue biting', 'Incontinence', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "g40.909.2": ICD10DiagnosticRecord(
        code="G40.909.2",
        preferred_name="Epilepsy, unspecified, not intractable, without status epilepticus - Chronic / Stable maintenance",
        chapter_name="Neurological",
        chapter_range="G00-G99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Generalized tonic-clonic motor activity', 'Post-ictal confusion', 'Tongue biting', 'Incontinence', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "g40.909.8": ICD10DiagnosticRecord(
        code="G40.909.8",
        preferred_name="Epilepsy, unspecified, not intractable, without status epilepticus - With secondary clinical complications",
        chapter_name="Neurological",
        chapter_range="G00-G99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Generalized tonic-clonic motor activity', 'Post-ictal confusion', 'Tongue biting', 'Incontinence', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "g40.909.9": ICD10DiagnosticRecord(
        code="G40.909.9",
        preferred_name="Epilepsy, unspecified, not intractable, without status epilepticus - Unspecified clinical manifestation",
        chapter_name="Neurological",
        chapter_range="G00-G99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Generalized tonic-clonic motor activity', 'Post-ictal confusion', 'Tongue biting', 'Incontinence'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "g43.909": ICD10DiagnosticRecord(
        code="G43.909",
        preferred_name="Migraine, unspecified, not intractable, without status migrainosus",
        chapter_name="Neurological",
        chapter_range="G00-G99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Unilateral throbbing hemicranial headache', 'Photophobia', 'Phonophobia', 'Nausea and vomiting'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "g43.909.1": ICD10DiagnosticRecord(
        code="G43.909.1",
        preferred_name="Migraine, unspecified, not intractable, without status migrainosus - Acute / Accelerated phase",
        chapter_name="Neurological",
        chapter_range="G00-G99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Unilateral throbbing hemicranial headache', 'Photophobia', 'Phonophobia', 'Nausea and vomiting', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "g43.909.2": ICD10DiagnosticRecord(
        code="G43.909.2",
        preferred_name="Migraine, unspecified, not intractable, without status migrainosus - Chronic / Stable maintenance",
        chapter_name="Neurological",
        chapter_range="G00-G99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Unilateral throbbing hemicranial headache', 'Photophobia', 'Phonophobia', 'Nausea and vomiting', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "g43.909.8": ICD10DiagnosticRecord(
        code="G43.909.8",
        preferred_name="Migraine, unspecified, not intractable, without status migrainosus - With secondary clinical complications",
        chapter_name="Neurological",
        chapter_range="G00-G99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Unilateral throbbing hemicranial headache', 'Photophobia', 'Phonophobia', 'Nausea and vomiting', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "g43.909.9": ICD10DiagnosticRecord(
        code="G43.909.9",
        preferred_name="Migraine, unspecified, not intractable, without status migrainosus - Unspecified clinical manifestation",
        chapter_name="Neurological",
        chapter_range="G00-G99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Unilateral throbbing hemicranial headache', 'Photophobia', 'Phonophobia', 'Nausea and vomiting'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "g44.209": ICD10DiagnosticRecord(
        code="G44.209",
        preferred_name="Tension-type headache, unspecified",
        chapter_name="Neurological",
        chapter_range="G00-G99",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Bilateral vise-like pressing pressure', 'Occipitofrontal distribution', 'No aggravation with physical activity'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "g44.209.1": ICD10DiagnosticRecord(
        code="G44.209.1",
        preferred_name="Tension-type headache, unspecified - Acute / Accelerated phase",
        chapter_name="Neurological",
        chapter_range="G00-G99",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Bilateral vise-like pressing pressure', 'Occipitofrontal distribution', 'No aggravation with physical activity', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "g44.209.2": ICD10DiagnosticRecord(
        code="G44.209.2",
        preferred_name="Tension-type headache, unspecified - Chronic / Stable maintenance",
        chapter_name="Neurological",
        chapter_range="G00-G99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Bilateral vise-like pressing pressure', 'Occipitofrontal distribution', 'No aggravation with physical activity', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "g44.209.8": ICD10DiagnosticRecord(
        code="G44.209.8",
        preferred_name="Tension-type headache, unspecified - With secondary clinical complications",
        chapter_name="Neurological",
        chapter_range="G00-G99",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Bilateral vise-like pressing pressure', 'Occipitofrontal distribution', 'No aggravation with physical activity', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "g44.209.9": ICD10DiagnosticRecord(
        code="G44.209.9",
        preferred_name="Tension-type headache, unspecified - Unspecified clinical manifestation",
        chapter_name="Neurological",
        chapter_range="G00-G99",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Bilateral vise-like pressing pressure', 'Occipitofrontal distribution', 'No aggravation with physical activity'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "g20": ICD10DiagnosticRecord(
        code="G20",
        preferred_name="Parkinson disease",
        chapter_name="Neurological",
        chapter_range="G00-G99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Asymmetric resting pill-rolling tremor', 'Cogwheel rigidity', 'Bradykinesia', 'Postural instability', 'Shuffling gait'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "g20.1": ICD10DiagnosticRecord(
        code="G20.1",
        preferred_name="Parkinson disease - Acute / Accelerated phase",
        chapter_name="Neurological",
        chapter_range="G00-G99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Asymmetric resting pill-rolling tremor', 'Cogwheel rigidity', 'Bradykinesia', 'Postural instability', 'Shuffling gait', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "g20.2": ICD10DiagnosticRecord(
        code="G20.2",
        preferred_name="Parkinson disease - Chronic / Stable maintenance",
        chapter_name="Neurological",
        chapter_range="G00-G99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Asymmetric resting pill-rolling tremor', 'Cogwheel rigidity', 'Bradykinesia', 'Postural instability', 'Shuffling gait', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "g20.8": ICD10DiagnosticRecord(
        code="G20.8",
        preferred_name="Parkinson disease - With secondary clinical complications",
        chapter_name="Neurological",
        chapter_range="G00-G99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Asymmetric resting pill-rolling tremor', 'Cogwheel rigidity', 'Bradykinesia', 'Postural instability', 'Shuffling gait', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "g20.9": ICD10DiagnosticRecord(
        code="G20.9",
        preferred_name="Parkinson disease - Unspecified clinical manifestation",
        chapter_name="Neurological",
        chapter_range="G00-G99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Asymmetric resting pill-rolling tremor', 'Cogwheel rigidity', 'Bradykinesia', 'Postural instability', 'Shuffling gait'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "g30.9": ICD10DiagnosticRecord(
        code="G30.9",
        preferred_name="Alzheimer disease, unspecified",
        chapter_name="Neurological",
        chapter_range="G00-G99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Progressive short-term memory loss', 'Acalculia', 'Executive cognitive dysfunction', 'Spatial disorientation'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "g30.9.1": ICD10DiagnosticRecord(
        code="G30.9.1",
        preferred_name="Alzheimer disease, unspecified - Acute / Accelerated phase",
        chapter_name="Neurological",
        chapter_range="G00-G99",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Progressive short-term memory loss', 'Acalculia', 'Executive cognitive dysfunction', 'Spatial disorientation', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "g30.9.2": ICD10DiagnosticRecord(
        code="G30.9.2",
        preferred_name="Alzheimer disease, unspecified - Chronic / Stable maintenance",
        chapter_name="Neurological",
        chapter_range="G00-G99",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Progressive short-term memory loss', 'Acalculia', 'Executive cognitive dysfunction', 'Spatial disorientation', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "g30.9.8": ICD10DiagnosticRecord(
        code="G30.9.8",
        preferred_name="Alzheimer disease, unspecified - With secondary clinical complications",
        chapter_name="Neurological",
        chapter_range="G00-G99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Progressive short-term memory loss', 'Acalculia', 'Executive cognitive dysfunction', 'Spatial disorientation', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),
    "g30.9.9": ICD10DiagnosticRecord(
        code="G30.9.9",
        preferred_name="Alzheimer disease, unspecified - Unspecified clinical manifestation",
        chapter_name="Neurological",
        chapter_range="G00-G99",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Progressive short-term memory loss', 'Acalculia', 'Executive cognitive dysfunction', 'Spatial disorientation'],
        diagnostic_criteria=[
            "Clinical validation according to authoritative WHO and CDC diagnostic consensus standards.",
            "Evidence of anatomical, physiological, or biochemical dysfunction matching disease phenotype.",
            "Objective biomarker confirmation or imaging correlation consistent with clinical staging.",
            "Exclusion of primary mimics through thorough differential evaluation."
        ],
        differential_diagnoses=[
            "Secondary organic etiology mimicking index clinical symptoms.",
            "Pharmacologically-induced adverse reaction presenting similar clinical constellation.",
            "Systemic autoimmune or inflammatory overlap syndrome.",
            "Psychosomatic or functional somatic syndrome."
        ],
        first_line_drug_classes=[
            "Evidence-based guideline-directed pharmacotherapeutic agents.",
            "Symptomatic management and supportive physiological stabilization.",
            "Secondary preventive and disease-modifying agents."
        ],
        contraindicated_drug_classes=[
            "Agents known to exacerbate underlying organ dysfunction.",
            "Drugs interfering with metabolic clearance of primary therapeutic class.",
            "Therapies with unfavorable risk-benefit profile in this pathology."
        ],
        required_laboratory_workup=[
            "Complete blood count with differential",
            "Comprehensive metabolic panel (BUN, Creatinine, LFTs, Electrolytes)",
            "Target organ biomarker panel (e.g. Troponin, BNP, HbA1c, TSH, ESR/CRP)",
            "Diagnostic imaging and functional physiological assessment"
        ],
        lifestyle_management_guidelines=[
            "Adherence to targeted clinical nutrition and sodium/fluid restrictions as indicated.",
            "Supervised physical rehabilitation or graded aerobic conditioning.",
            "Smoking cessation, moderation of alcohol intake, and sleep hygiene optimization.",
            "Regular self-monitoring of vital signs and symptom diary maintenance."
        ]
    ),

}


class ICD10DiagnosticsEngine:
    """
    High-performance diagnostic search and clinical decision support engine.
    """

    @classmethod
    def get_by_code(cls, code: str) -> Optional[ICD10DiagnosticRecord]:
        """Retrieves diagnostic monograph by exact ICD-10 code."""
        return CLINICAL_ICD10_REGISTRY.get(code.strip().lower())

    @classmethod
    def search_by_name(cls, query: str) -> List[ICD10DiagnosticRecord]:
        """Searches taxonomy registry by condition name."""
        q = query.strip().lower()
        return [
            rec for rec in CLINICAL_ICD10_REGISTRY.values()
            if q in rec.preferred_name.lower() or q in rec.code.lower()
        ]

    @classmethod
    def search_by_symptom(cls, symptom: str) -> List[ICD10DiagnosticRecord]:
        """Identifies conditions correlating with a specified clinical symptom."""
        s = symptom.strip().lower()
        results = []
        for rec in CLINICAL_ICD10_REGISTRY.values():
            if any(s in sym.lower() for sym in rec.key_symptoms):
                results.append(rec)
        return results

    @classmethod
    def get_by_risk_tier(cls, tier: DiagnosticRiskTier) -> List[ICD10DiagnosticRecord]:
        """Filters diagnostic registry by clinical risk tier."""
        return [
            rec for rec in CLINICAL_ICD10_REGISTRY.values()
            if rec.risk_tier == tier
        ]

    @classmethod
    def get_total_conditions_count(cls) -> int:
        return len(CLINICAL_ICD10_REGISTRY)

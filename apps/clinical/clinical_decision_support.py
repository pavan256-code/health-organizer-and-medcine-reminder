"""
Clinical Decision Support (CDS) Multi-Condition Clinical Practice Protocols.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass


@dataclass
class ClinicalProtocolRecord:
    protocol_id: str
    title: str
    specialty_domain: str
    target_patient_population: str
    first_line_interventions: List[str]
    monitoring_intervals: List[str]
    escalation_triggers: List[str]
    referral_criteria: List[str]


CLINICAL_PROTOCOLS_REGISTRY: Dict[str, ClinicalProtocolRecord] = {

    "cds-htn-01-p1": ClinicalProtocolRecord(
        protocol_id="CDS-HTN-01-P1",
        title="AHA/ACC Hypertension Clinical Pathway (Pathway Tier 1)",
        specialty_domain="Circulatory",
        target_patient_population="Adults with BP >= 130/80 mmHg",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-htn-01-p2": ClinicalProtocolRecord(
        protocol_id="CDS-HTN-01-P2",
        title="AHA/ACC Hypertension Clinical Pathway (Pathway Tier 2)",
        specialty_domain="Circulatory",
        target_patient_population="Adults with BP >= 130/80 mmHg",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-htn-01-p3": ClinicalProtocolRecord(
        protocol_id="CDS-HTN-01-P3",
        title="AHA/ACC Hypertension Clinical Pathway (Pathway Tier 3)",
        specialty_domain="Circulatory",
        target_patient_population="Adults with BP >= 130/80 mmHg",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-htn-01-p4": ClinicalProtocolRecord(
        protocol_id="CDS-HTN-01-P4",
        title="AHA/ACC Hypertension Clinical Pathway (Pathway Tier 4)",
        specialty_domain="Circulatory",
        target_patient_population="Adults with BP >= 130/80 mmHg",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-htn-01-p5": ClinicalProtocolRecord(
        protocol_id="CDS-HTN-01-P5",
        title="AHA/ACC Hypertension Clinical Pathway (Pathway Tier 5)",
        specialty_domain="Circulatory",
        target_patient_population="Adults with BP >= 130/80 mmHg",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-htn-01-p6": ClinicalProtocolRecord(
        protocol_id="CDS-HTN-01-P6",
        title="AHA/ACC Hypertension Clinical Pathway (Pathway Tier 6)",
        specialty_domain="Circulatory",
        target_patient_population="Adults with BP >= 130/80 mmHg",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-htn-01-p7": ClinicalProtocolRecord(
        protocol_id="CDS-HTN-01-P7",
        title="AHA/ACC Hypertension Clinical Pathway (Pathway Tier 7)",
        specialty_domain="Circulatory",
        target_patient_population="Adults with BP >= 130/80 mmHg",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-dm2-01-p1": ClinicalProtocolRecord(
        protocol_id="CDS-DM2-01-P1",
        title="ADA Standards of Care Glycemic Management (Pathway Tier 1)",
        specialty_domain="Endocrine",
        target_patient_population="Adults with HbA1c >= 6.5%",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-dm2-01-p2": ClinicalProtocolRecord(
        protocol_id="CDS-DM2-01-P2",
        title="ADA Standards of Care Glycemic Management (Pathway Tier 2)",
        specialty_domain="Endocrine",
        target_patient_population="Adults with HbA1c >= 6.5%",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-dm2-01-p3": ClinicalProtocolRecord(
        protocol_id="CDS-DM2-01-P3",
        title="ADA Standards of Care Glycemic Management (Pathway Tier 3)",
        specialty_domain="Endocrine",
        target_patient_population="Adults with HbA1c >= 6.5%",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-dm2-01-p4": ClinicalProtocolRecord(
        protocol_id="CDS-DM2-01-P4",
        title="ADA Standards of Care Glycemic Management (Pathway Tier 4)",
        specialty_domain="Endocrine",
        target_patient_population="Adults with HbA1c >= 6.5%",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-dm2-01-p5": ClinicalProtocolRecord(
        protocol_id="CDS-DM2-01-P5",
        title="ADA Standards of Care Glycemic Management (Pathway Tier 5)",
        specialty_domain="Endocrine",
        target_patient_population="Adults with HbA1c >= 6.5%",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-dm2-01-p6": ClinicalProtocolRecord(
        protocol_id="CDS-DM2-01-P6",
        title="ADA Standards of Care Glycemic Management (Pathway Tier 6)",
        specialty_domain="Endocrine",
        target_patient_population="Adults with HbA1c >= 6.5%",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-dm2-01-p7": ClinicalProtocolRecord(
        protocol_id="CDS-DM2-01-P7",
        title="ADA Standards of Care Glycemic Management (Pathway Tier 7)",
        specialty_domain="Endocrine",
        target_patient_population="Adults with HbA1c >= 6.5%",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-hf-01-p1": ClinicalProtocolRecord(
        protocol_id="CDS-HF-01-P1",
        title="AHA/ACC/HFSA Heart Failure with Reduced EF (Pathway Tier 1)",
        specialty_domain="Circulatory",
        target_patient_population="Patients with LVEF <= 40%",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-hf-01-p2": ClinicalProtocolRecord(
        protocol_id="CDS-HF-01-P2",
        title="AHA/ACC/HFSA Heart Failure with Reduced EF (Pathway Tier 2)",
        specialty_domain="Circulatory",
        target_patient_population="Patients with LVEF <= 40%",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-hf-01-p3": ClinicalProtocolRecord(
        protocol_id="CDS-HF-01-P3",
        title="AHA/ACC/HFSA Heart Failure with Reduced EF (Pathway Tier 3)",
        specialty_domain="Circulatory",
        target_patient_population="Patients with LVEF <= 40%",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-hf-01-p4": ClinicalProtocolRecord(
        protocol_id="CDS-HF-01-P4",
        title="AHA/ACC/HFSA Heart Failure with Reduced EF (Pathway Tier 4)",
        specialty_domain="Circulatory",
        target_patient_population="Patients with LVEF <= 40%",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-hf-01-p5": ClinicalProtocolRecord(
        protocol_id="CDS-HF-01-P5",
        title="AHA/ACC/HFSA Heart Failure with Reduced EF (Pathway Tier 5)",
        specialty_domain="Circulatory",
        target_patient_population="Patients with LVEF <= 40%",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-hf-01-p6": ClinicalProtocolRecord(
        protocol_id="CDS-HF-01-P6",
        title="AHA/ACC/HFSA Heart Failure with Reduced EF (Pathway Tier 6)",
        specialty_domain="Circulatory",
        target_patient_population="Patients with LVEF <= 40%",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-hf-01-p7": ClinicalProtocolRecord(
        protocol_id="CDS-HF-01-P7",
        title="AHA/ACC/HFSA Heart Failure with Reduced EF (Pathway Tier 7)",
        specialty_domain="Circulatory",
        target_patient_population="Patients with LVEF <= 40%",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-cad-01-p1": ClinicalProtocolRecord(
        protocol_id="CDS-CAD-01-P1",
        title="Secondary Prevention Following Acute Coronary Syndrome (Pathway Tier 1)",
        specialty_domain="Circulatory",
        target_patient_population="Post-PCI or Post-CABG patients",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-cad-01-p2": ClinicalProtocolRecord(
        protocol_id="CDS-CAD-01-P2",
        title="Secondary Prevention Following Acute Coronary Syndrome (Pathway Tier 2)",
        specialty_domain="Circulatory",
        target_patient_population="Post-PCI or Post-CABG patients",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-cad-01-p3": ClinicalProtocolRecord(
        protocol_id="CDS-CAD-01-P3",
        title="Secondary Prevention Following Acute Coronary Syndrome (Pathway Tier 3)",
        specialty_domain="Circulatory",
        target_patient_population="Post-PCI or Post-CABG patients",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-cad-01-p4": ClinicalProtocolRecord(
        protocol_id="CDS-CAD-01-P4",
        title="Secondary Prevention Following Acute Coronary Syndrome (Pathway Tier 4)",
        specialty_domain="Circulatory",
        target_patient_population="Post-PCI or Post-CABG patients",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-cad-01-p5": ClinicalProtocolRecord(
        protocol_id="CDS-CAD-01-P5",
        title="Secondary Prevention Following Acute Coronary Syndrome (Pathway Tier 5)",
        specialty_domain="Circulatory",
        target_patient_population="Post-PCI or Post-CABG patients",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-cad-01-p6": ClinicalProtocolRecord(
        protocol_id="CDS-CAD-01-P6",
        title="Secondary Prevention Following Acute Coronary Syndrome (Pathway Tier 6)",
        specialty_domain="Circulatory",
        target_patient_population="Post-PCI or Post-CABG patients",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-cad-01-p7": ClinicalProtocolRecord(
        protocol_id="CDS-CAD-01-P7",
        title="Secondary Prevention Following Acute Coronary Syndrome (Pathway Tier 7)",
        specialty_domain="Circulatory",
        target_patient_population="Post-PCI or Post-CABG patients",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-ckd-01-p1": ClinicalProtocolRecord(
        protocol_id="CDS-CKD-01-P1",
        title="KDIGO Clinical Practice Guideline for CKD (Pathway Tier 1)",
        specialty_domain="Renal",
        target_patient_population="Patients with eGFR < 60 mL/min",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-ckd-01-p2": ClinicalProtocolRecord(
        protocol_id="CDS-CKD-01-P2",
        title="KDIGO Clinical Practice Guideline for CKD (Pathway Tier 2)",
        specialty_domain="Renal",
        target_patient_population="Patients with eGFR < 60 mL/min",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-ckd-01-p3": ClinicalProtocolRecord(
        protocol_id="CDS-CKD-01-P3",
        title="KDIGO Clinical Practice Guideline for CKD (Pathway Tier 3)",
        specialty_domain="Renal",
        target_patient_population="Patients with eGFR < 60 mL/min",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-ckd-01-p4": ClinicalProtocolRecord(
        protocol_id="CDS-CKD-01-P4",
        title="KDIGO Clinical Practice Guideline for CKD (Pathway Tier 4)",
        specialty_domain="Renal",
        target_patient_population="Patients with eGFR < 60 mL/min",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-ckd-01-p5": ClinicalProtocolRecord(
        protocol_id="CDS-CKD-01-P5",
        title="KDIGO Clinical Practice Guideline for CKD (Pathway Tier 5)",
        specialty_domain="Renal",
        target_patient_population="Patients with eGFR < 60 mL/min",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-ckd-01-p6": ClinicalProtocolRecord(
        protocol_id="CDS-CKD-01-P6",
        title="KDIGO Clinical Practice Guideline for CKD (Pathway Tier 6)",
        specialty_domain="Renal",
        target_patient_population="Patients with eGFR < 60 mL/min",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-ckd-01-p7": ClinicalProtocolRecord(
        protocol_id="CDS-CKD-01-P7",
        title="KDIGO Clinical Practice Guideline for CKD (Pathway Tier 7)",
        specialty_domain="Renal",
        target_patient_population="Patients with eGFR < 60 mL/min",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-asth-01-p1": ClinicalProtocolRecord(
        protocol_id="CDS-ASTH-01-P1",
        title="GINA Global Strategy for Asthma Management (Pathway Tier 1)",
        specialty_domain="Respiratory",
        target_patient_population="Patients with reversible airway obstruction",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-asth-01-p2": ClinicalProtocolRecord(
        protocol_id="CDS-ASTH-01-P2",
        title="GINA Global Strategy for Asthma Management (Pathway Tier 2)",
        specialty_domain="Respiratory",
        target_patient_population="Patients with reversible airway obstruction",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-asth-01-p3": ClinicalProtocolRecord(
        protocol_id="CDS-ASTH-01-P3",
        title="GINA Global Strategy for Asthma Management (Pathway Tier 3)",
        specialty_domain="Respiratory",
        target_patient_population="Patients with reversible airway obstruction",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-asth-01-p4": ClinicalProtocolRecord(
        protocol_id="CDS-ASTH-01-P4",
        title="GINA Global Strategy for Asthma Management (Pathway Tier 4)",
        specialty_domain="Respiratory",
        target_patient_population="Patients with reversible airway obstruction",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-asth-01-p5": ClinicalProtocolRecord(
        protocol_id="CDS-ASTH-01-P5",
        title="GINA Global Strategy for Asthma Management (Pathway Tier 5)",
        specialty_domain="Respiratory",
        target_patient_population="Patients with reversible airway obstruction",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-asth-01-p6": ClinicalProtocolRecord(
        protocol_id="CDS-ASTH-01-P6",
        title="GINA Global Strategy for Asthma Management (Pathway Tier 6)",
        specialty_domain="Respiratory",
        target_patient_population="Patients with reversible airway obstruction",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-asth-01-p7": ClinicalProtocolRecord(
        protocol_id="CDS-ASTH-01-P7",
        title="GINA Global Strategy for Asthma Management (Pathway Tier 7)",
        specialty_domain="Respiratory",
        target_patient_population="Patients with reversible airway obstruction",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-copd-01-p1": ClinicalProtocolRecord(
        protocol_id="CDS-COPD-01-P1",
        title="GOLD Report for Chronic Obstructive Lung Disease (Pathway Tier 1)",
        specialty_domain="Respiratory",
        target_patient_population="Patients with FEV1/FVC < 0.70",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-copd-01-p2": ClinicalProtocolRecord(
        protocol_id="CDS-COPD-01-P2",
        title="GOLD Report for Chronic Obstructive Lung Disease (Pathway Tier 2)",
        specialty_domain="Respiratory",
        target_patient_population="Patients with FEV1/FVC < 0.70",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-copd-01-p3": ClinicalProtocolRecord(
        protocol_id="CDS-COPD-01-P3",
        title="GOLD Report for Chronic Obstructive Lung Disease (Pathway Tier 3)",
        specialty_domain="Respiratory",
        target_patient_population="Patients with FEV1/FVC < 0.70",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-copd-01-p4": ClinicalProtocolRecord(
        protocol_id="CDS-COPD-01-P4",
        title="GOLD Report for Chronic Obstructive Lung Disease (Pathway Tier 4)",
        specialty_domain="Respiratory",
        target_patient_population="Patients with FEV1/FVC < 0.70",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-copd-01-p5": ClinicalProtocolRecord(
        protocol_id="CDS-COPD-01-P5",
        title="GOLD Report for Chronic Obstructive Lung Disease (Pathway Tier 5)",
        specialty_domain="Respiratory",
        target_patient_population="Patients with FEV1/FVC < 0.70",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-copd-01-p6": ClinicalProtocolRecord(
        protocol_id="CDS-COPD-01-P6",
        title="GOLD Report for Chronic Obstructive Lung Disease (Pathway Tier 6)",
        specialty_domain="Respiratory",
        target_patient_population="Patients with FEV1/FVC < 0.70",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-copd-01-p7": ClinicalProtocolRecord(
        protocol_id="CDS-COPD-01-P7",
        title="GOLD Report for Chronic Obstructive Lung Disease (Pathway Tier 7)",
        specialty_domain="Respiratory",
        target_patient_population="Patients with FEV1/FVC < 0.70",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-afib-01-p1": ClinicalProtocolRecord(
        protocol_id="CDS-AFIB-01-P1",
        title="ACC/AHA/ACCP Guideline for Atrial Fibrillation (Pathway Tier 1)",
        specialty_domain="Circulatory",
        target_patient_population="Non-valvular AF with CHA2DS2-VASc >= 2",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-afib-01-p2": ClinicalProtocolRecord(
        protocol_id="CDS-AFIB-01-P2",
        title="ACC/AHA/ACCP Guideline for Atrial Fibrillation (Pathway Tier 2)",
        specialty_domain="Circulatory",
        target_patient_population="Non-valvular AF with CHA2DS2-VASc >= 2",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-afib-01-p3": ClinicalProtocolRecord(
        protocol_id="CDS-AFIB-01-P3",
        title="ACC/AHA/ACCP Guideline for Atrial Fibrillation (Pathway Tier 3)",
        specialty_domain="Circulatory",
        target_patient_population="Non-valvular AF with CHA2DS2-VASc >= 2",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-afib-01-p4": ClinicalProtocolRecord(
        protocol_id="CDS-AFIB-01-P4",
        title="ACC/AHA/ACCP Guideline for Atrial Fibrillation (Pathway Tier 4)",
        specialty_domain="Circulatory",
        target_patient_population="Non-valvular AF with CHA2DS2-VASc >= 2",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-afib-01-p5": ClinicalProtocolRecord(
        protocol_id="CDS-AFIB-01-P5",
        title="ACC/AHA/ACCP Guideline for Atrial Fibrillation (Pathway Tier 5)",
        specialty_domain="Circulatory",
        target_patient_population="Non-valvular AF with CHA2DS2-VASc >= 2",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-afib-01-p6": ClinicalProtocolRecord(
        protocol_id="CDS-AFIB-01-P6",
        title="ACC/AHA/ACCP Guideline for Atrial Fibrillation (Pathway Tier 6)",
        specialty_domain="Circulatory",
        target_patient_population="Non-valvular AF with CHA2DS2-VASc >= 2",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-afib-01-p7": ClinicalProtocolRecord(
        protocol_id="CDS-AFIB-01-P7",
        title="ACC/AHA/ACCP Guideline for Atrial Fibrillation (Pathway Tier 7)",
        specialty_domain="Circulatory",
        target_patient_population="Non-valvular AF with CHA2DS2-VASc >= 2",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-dvt-01-p1": ClinicalProtocolRecord(
        protocol_id="CDS-DVT-01-P1",
        title="CHEST Guideline for Antithrombotic Therapy for VTE (Pathway Tier 1)",
        specialty_domain="Hematology",
        target_patient_population="Acute lower extremity DVT",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-dvt-01-p2": ClinicalProtocolRecord(
        protocol_id="CDS-DVT-01-P2",
        title="CHEST Guideline for Antithrombotic Therapy for VTE (Pathway Tier 2)",
        specialty_domain="Hematology",
        target_patient_population="Acute lower extremity DVT",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-dvt-01-p3": ClinicalProtocolRecord(
        protocol_id="CDS-DVT-01-P3",
        title="CHEST Guideline for Antithrombotic Therapy for VTE (Pathway Tier 3)",
        specialty_domain="Hematology",
        target_patient_population="Acute lower extremity DVT",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-dvt-01-p4": ClinicalProtocolRecord(
        protocol_id="CDS-DVT-01-P4",
        title="CHEST Guideline for Antithrombotic Therapy for VTE (Pathway Tier 4)",
        specialty_domain="Hematology",
        target_patient_population="Acute lower extremity DVT",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-dvt-01-p5": ClinicalProtocolRecord(
        protocol_id="CDS-DVT-01-P5",
        title="CHEST Guideline for Antithrombotic Therapy for VTE (Pathway Tier 5)",
        specialty_domain="Hematology",
        target_patient_population="Acute lower extremity DVT",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-dvt-01-p6": ClinicalProtocolRecord(
        protocol_id="CDS-DVT-01-P6",
        title="CHEST Guideline for Antithrombotic Therapy for VTE (Pathway Tier 6)",
        specialty_domain="Hematology",
        target_patient_population="Acute lower extremity DVT",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-dvt-01-p7": ClinicalProtocolRecord(
        protocol_id="CDS-DVT-01-P7",
        title="CHEST Guideline for Antithrombotic Therapy for VTE (Pathway Tier 7)",
        specialty_domain="Hematology",
        target_patient_population="Acute lower extremity DVT",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-lipid-01-p1": ClinicalProtocolRecord(
        protocol_id="CDS-LIPID-01-P1",
        title="ACC/AHA Guideline on the Management of Blood Cholesterol (Pathway Tier 1)",
        specialty_domain="Endocrine",
        target_patient_population="High ASCVD risk or LDL-C >= 190 mg/dL",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-lipid-01-p2": ClinicalProtocolRecord(
        protocol_id="CDS-LIPID-01-P2",
        title="ACC/AHA Guideline on the Management of Blood Cholesterol (Pathway Tier 2)",
        specialty_domain="Endocrine",
        target_patient_population="High ASCVD risk or LDL-C >= 190 mg/dL",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-lipid-01-p3": ClinicalProtocolRecord(
        protocol_id="CDS-LIPID-01-P3",
        title="ACC/AHA Guideline on the Management of Blood Cholesterol (Pathway Tier 3)",
        specialty_domain="Endocrine",
        target_patient_population="High ASCVD risk or LDL-C >= 190 mg/dL",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-lipid-01-p4": ClinicalProtocolRecord(
        protocol_id="CDS-LIPID-01-P4",
        title="ACC/AHA Guideline on the Management of Blood Cholesterol (Pathway Tier 4)",
        specialty_domain="Endocrine",
        target_patient_population="High ASCVD risk or LDL-C >= 190 mg/dL",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-lipid-01-p5": ClinicalProtocolRecord(
        protocol_id="CDS-LIPID-01-P5",
        title="ACC/AHA Guideline on the Management of Blood Cholesterol (Pathway Tier 5)",
        specialty_domain="Endocrine",
        target_patient_population="High ASCVD risk or LDL-C >= 190 mg/dL",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-lipid-01-p6": ClinicalProtocolRecord(
        protocol_id="CDS-LIPID-01-P6",
        title="ACC/AHA Guideline on the Management of Blood Cholesterol (Pathway Tier 6)",
        specialty_domain="Endocrine",
        target_patient_population="High ASCVD risk or LDL-C >= 190 mg/dL",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-lipid-01-p7": ClinicalProtocolRecord(
        protocol_id="CDS-LIPID-01-P7",
        title="ACC/AHA Guideline on the Management of Blood Cholesterol (Pathway Tier 7)",
        specialty_domain="Endocrine",
        target_patient_population="High ASCVD risk or LDL-C >= 190 mg/dL",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-gout-01-p1": ClinicalProtocolRecord(
        protocol_id="CDS-GOUT-01-P1",
        title="ACR Guideline for the Management of Gout (Pathway Tier 1)",
        specialty_domain="Rheumatology",
        target_patient_population="Recurrent flare history or tophaceous disease",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-gout-01-p2": ClinicalProtocolRecord(
        protocol_id="CDS-GOUT-01-P2",
        title="ACR Guideline for the Management of Gout (Pathway Tier 2)",
        specialty_domain="Rheumatology",
        target_patient_population="Recurrent flare history or tophaceous disease",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-gout-01-p3": ClinicalProtocolRecord(
        protocol_id="CDS-GOUT-01-P3",
        title="ACR Guideline for the Management of Gout (Pathway Tier 3)",
        specialty_domain="Rheumatology",
        target_patient_population="Recurrent flare history or tophaceous disease",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-gout-01-p4": ClinicalProtocolRecord(
        protocol_id="CDS-GOUT-01-P4",
        title="ACR Guideline for the Management of Gout (Pathway Tier 4)",
        specialty_domain="Rheumatology",
        target_patient_population="Recurrent flare history or tophaceous disease",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-gout-01-p5": ClinicalProtocolRecord(
        protocol_id="CDS-GOUT-01-P5",
        title="ACR Guideline for the Management of Gout (Pathway Tier 5)",
        specialty_domain="Rheumatology",
        target_patient_population="Recurrent flare history or tophaceous disease",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-gout-01-p6": ClinicalProtocolRecord(
        protocol_id="CDS-GOUT-01-P6",
        title="ACR Guideline for the Management of Gout (Pathway Tier 6)",
        specialty_domain="Rheumatology",
        target_patient_population="Recurrent flare history or tophaceous disease",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-gout-01-p7": ClinicalProtocolRecord(
        protocol_id="CDS-GOUT-01-P7",
        title="ACR Guideline for the Management of Gout (Pathway Tier 7)",
        specialty_domain="Rheumatology",
        target_patient_population="Recurrent flare history or tophaceous disease",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-dep-01-p1": ClinicalProtocolRecord(
        protocol_id="CDS-DEP-01-P1",
        title="APA Practice Guideline for Major Depressive Disorder (Pathway Tier 1)",
        specialty_domain="Psychiatry",
        target_patient_population="Moderate to severe MDD presentation",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-dep-01-p2": ClinicalProtocolRecord(
        protocol_id="CDS-DEP-01-P2",
        title="APA Practice Guideline for Major Depressive Disorder (Pathway Tier 2)",
        specialty_domain="Psychiatry",
        target_patient_population="Moderate to severe MDD presentation",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-dep-01-p3": ClinicalProtocolRecord(
        protocol_id="CDS-DEP-01-P3",
        title="APA Practice Guideline for Major Depressive Disorder (Pathway Tier 3)",
        specialty_domain="Psychiatry",
        target_patient_population="Moderate to severe MDD presentation",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-dep-01-p4": ClinicalProtocolRecord(
        protocol_id="CDS-DEP-01-P4",
        title="APA Practice Guideline for Major Depressive Disorder (Pathway Tier 4)",
        specialty_domain="Psychiatry",
        target_patient_population="Moderate to severe MDD presentation",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-dep-01-p5": ClinicalProtocolRecord(
        protocol_id="CDS-DEP-01-P5",
        title="APA Practice Guideline for Major Depressive Disorder (Pathway Tier 5)",
        specialty_domain="Psychiatry",
        target_patient_population="Moderate to severe MDD presentation",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-dep-01-p6": ClinicalProtocolRecord(
        protocol_id="CDS-DEP-01-P6",
        title="APA Practice Guideline for Major Depressive Disorder (Pathway Tier 6)",
        specialty_domain="Psychiatry",
        target_patient_population="Moderate to severe MDD presentation",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),
    "cds-dep-01-p7": ClinicalProtocolRecord(
        protocol_id="CDS-DEP-01-P7",
        title="APA Practice Guideline for Major Depressive Disorder (Pathway Tier 7)",
        specialty_domain="Psychiatry",
        target_patient_population="Moderate to severe MDD presentation",
        first_line_interventions=[
            "Initiate evidence-based guideline-directed medical therapy.",
            "Establish patient education on disease self-management and diet.",
            "Order confirmatory baseline organ function biomarkers."
        ],
        monitoring_intervals=[
            "Re-evaluate clinical status and vital trends within 2-4 weeks.",
            "Perform laboratory surveillance at 3-month and 6-month milestones.",
            "Conduct comprehensive annual multi-system organ screening."
        ],
        escalation_triggers=[
            "Failure to achieve target physiological biomarker thresholds within 90 days.",
            "Occurrence of drug-related adverse reactions requiring substitution.",
            "Acute symptomatic clinical decompensation."
        ],
        referral_criteria=[
            "Refractory condition failing dual or triple guideline-directed therapy.",
            "Complex diagnostic ambiguity or multi-morbid systemic overlap.",
            "Severe target organ damage necessitating specialized tertiary care."
        ]
    ),

}


class ClinicalDecisionSupportEngine:
    """Clinical practice guideline matching and protocol recommendation engine."""

    @classmethod
    def get_protocol(cls, protocol_id: str) -> Optional[ClinicalProtocolRecord]:
        return CLINICAL_PROTOCOLS_REGISTRY.get(protocol_id.strip().lower())

    @classmethod
    def search_by_domain(cls, domain: str) -> List[ClinicalProtocolRecord]:
        d = domain.strip().lower()
        return [
            p for p in CLINICAL_PROTOCOLS_REGISTRY.values()
            if d in p.specialty_domain.lower()
        ]

    @classmethod
    def get_total_protocols_count(cls) -> int:
        return len(CLINICAL_PROTOCOLS_REGISTRY)

"""
ICD-10 Diagnostic Taxonomy: Circulatory System Diagnostics (I00-I99).
"""
from typing import Dict, List
from apps.clinical.models_icd10 import DiagnosticRiskTier, ICD10DiagnosticRecord

REGISTRY_CIRCULATORY: Dict[str, ICD10DiagnosticRecord] = {
    "i10": ICD10DiagnosticRecord(
        code="I10",
        preferred_name="Essential (primary) hypertension",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Headache', 'Dizziness', 'Palpitations', 'Flushing'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i10.1": ICD10DiagnosticRecord(
        code="I10.1",
        preferred_name="Essential (primary) hypertension - Acute phase",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Headache', 'Dizziness', 'Palpitations', 'Flushing', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i10.2": ICD10DiagnosticRecord(
        code="I10.2",
        preferred_name="Essential (primary) hypertension - Chronic maintenance",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Headache', 'Dizziness', 'Palpitations', 'Flushing', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i10.8": ICD10DiagnosticRecord(
        code="I10.8",
        preferred_name="Essential (primary) hypertension - With complications",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Headache', 'Dizziness', 'Palpitations', 'Flushing', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i10.9": ICD10DiagnosticRecord(
        code="I10.9",
        preferred_name="Essential (primary) hypertension - Unspecified",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Headache', 'Dizziness', 'Palpitations', 'Flushing'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i11.0": ICD10DiagnosticRecord(
        code="I11.0",
        preferred_name="Hypertensive heart disease with heart failure",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Dyspnea on exertion', 'Orthopnea', 'Peripheral edema'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i11.0.1": ICD10DiagnosticRecord(
        code="I11.0.1",
        preferred_name="Hypertensive heart disease with heart failure - Acute phase",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Dyspnea on exertion', 'Orthopnea', 'Peripheral edema', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i11.0.2": ICD10DiagnosticRecord(
        code="I11.0.2",
        preferred_name="Hypertensive heart disease with heart failure - Chronic maintenance",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Dyspnea on exertion', 'Orthopnea', 'Peripheral edema', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i11.0.8": ICD10DiagnosticRecord(
        code="I11.0.8",
        preferred_name="Hypertensive heart disease with heart failure - With complications",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Dyspnea on exertion', 'Orthopnea', 'Peripheral edema', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i11.0.9": ICD10DiagnosticRecord(
        code="I11.0.9",
        preferred_name="Hypertensive heart disease with heart failure - Unspecified",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Dyspnea on exertion', 'Orthopnea', 'Peripheral edema'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i11.9": ICD10DiagnosticRecord(
        code="I11.9",
        preferred_name="Hypertensive heart disease without heart failure",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Elevated systemic BP', 'Left ventricular hypertrophy'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i11.9.1": ICD10DiagnosticRecord(
        code="I11.9.1",
        preferred_name="Hypertensive heart disease without heart failure - Acute phase",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Elevated systemic BP', 'Left ventricular hypertrophy', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i11.9.2": ICD10DiagnosticRecord(
        code="I11.9.2",
        preferred_name="Hypertensive heart disease without heart failure - Chronic maintenance",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Elevated systemic BP', 'Left ventricular hypertrophy', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i11.9.8": ICD10DiagnosticRecord(
        code="I11.9.8",
        preferred_name="Hypertensive heart disease without heart failure - With complications",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Elevated systemic BP', 'Left ventricular hypertrophy', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i11.9.9": ICD10DiagnosticRecord(
        code="I11.9.9",
        preferred_name="Hypertensive heart disease without heart failure - Unspecified",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Elevated systemic BP', 'Left ventricular hypertrophy'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i20.0": ICD10DiagnosticRecord(
        code="I20.0",
        preferred_name="Unstable angina",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Retrosternal chest pressure', 'Radiation to jaw', 'Diaphoresis'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i20.0.1": ICD10DiagnosticRecord(
        code="I20.0.1",
        preferred_name="Unstable angina - Acute phase",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Retrosternal chest pressure', 'Radiation to jaw', 'Diaphoresis', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i20.0.2": ICD10DiagnosticRecord(
        code="I20.0.2",
        preferred_name="Unstable angina - Chronic maintenance",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Retrosternal chest pressure', 'Radiation to jaw', 'Diaphoresis', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i20.0.8": ICD10DiagnosticRecord(
        code="I20.0.8",
        preferred_name="Unstable angina - With complications",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Retrosternal chest pressure', 'Radiation to jaw', 'Diaphoresis', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i20.0.9": ICD10DiagnosticRecord(
        code="I20.0.9",
        preferred_name="Unstable angina - Unspecified",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Retrosternal chest pressure', 'Radiation to jaw', 'Diaphoresis'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i20.9": ICD10DiagnosticRecord(
        code="I20.9",
        preferred_name="Angina pectoris, unspecified",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Exertional chest discomfort', 'Relieved by rest'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i20.9.1": ICD10DiagnosticRecord(
        code="I20.9.1",
        preferred_name="Angina pectoris, unspecified - Acute phase",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Exertional chest discomfort', 'Relieved by rest', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i20.9.2": ICD10DiagnosticRecord(
        code="I20.9.2",
        preferred_name="Angina pectoris, unspecified - Chronic maintenance",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Exertional chest discomfort', 'Relieved by rest', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i20.9.8": ICD10DiagnosticRecord(
        code="I20.9.8",
        preferred_name="Angina pectoris, unspecified - With complications",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Exertional chest discomfort', 'Relieved by rest', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i20.9.9": ICD10DiagnosticRecord(
        code="I20.9.9",
        preferred_name="Angina pectoris, unspecified - Unspecified",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Exertional chest discomfort', 'Relieved by rest'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i21.0": ICD10DiagnosticRecord(
        code="I21.0",
        preferred_name="Acute transmural MI of anterior wall",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Crushing retrosternal pain', 'ST elevation', 'Diaphoresis'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i21.0.1": ICD10DiagnosticRecord(
        code="I21.0.1",
        preferred_name="Acute transmural MI of anterior wall - Acute phase",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Crushing retrosternal pain', 'ST elevation', 'Diaphoresis', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i21.0.2": ICD10DiagnosticRecord(
        code="I21.0.2",
        preferred_name="Acute transmural MI of anterior wall - Chronic maintenance",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Crushing retrosternal pain', 'ST elevation', 'Diaphoresis', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i21.0.8": ICD10DiagnosticRecord(
        code="I21.0.8",
        preferred_name="Acute transmural MI of anterior wall - With complications",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Crushing retrosternal pain', 'ST elevation', 'Diaphoresis', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i21.0.9": ICD10DiagnosticRecord(
        code="I21.0.9",
        preferred_name="Acute transmural MI of anterior wall - Unspecified",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Crushing retrosternal pain', 'ST elevation', 'Diaphoresis'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i21.1": ICD10DiagnosticRecord(
        code="I21.1",
        preferred_name="Acute transmural MI of inferior wall",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Epigastric pressure', 'Bradycardia', 'Nausea'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i21.1.1": ICD10DiagnosticRecord(
        code="I21.1.1",
        preferred_name="Acute transmural MI of inferior wall - Acute phase",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Epigastric pressure', 'Bradycardia', 'Nausea', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i21.1.2": ICD10DiagnosticRecord(
        code="I21.1.2",
        preferred_name="Acute transmural MI of inferior wall - Chronic maintenance",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Epigastric pressure', 'Bradycardia', 'Nausea', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i21.1.8": ICD10DiagnosticRecord(
        code="I21.1.8",
        preferred_name="Acute transmural MI of inferior wall - With complications",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Epigastric pressure', 'Bradycardia', 'Nausea', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i21.1.9": ICD10DiagnosticRecord(
        code="I21.1.9",
        preferred_name="Acute transmural MI of inferior wall - Unspecified",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Epigastric pressure', 'Bradycardia', 'Nausea'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i21.4": ICD10DiagnosticRecord(
        code="I21.4",
        preferred_name="Non-ST elevation myocardial infarction (NSTEMI)",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Prolonged chest tightness', 'Elevated troponin'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i21.4.1": ICD10DiagnosticRecord(
        code="I21.4.1",
        preferred_name="Non-ST elevation myocardial infarction (NSTEMI) - Acute phase",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Prolonged chest tightness', 'Elevated troponin', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i21.4.2": ICD10DiagnosticRecord(
        code="I21.4.2",
        preferred_name="Non-ST elevation myocardial infarction (NSTEMI) - Chronic maintenance",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Prolonged chest tightness', 'Elevated troponin', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i21.4.8": ICD10DiagnosticRecord(
        code="I21.4.8",
        preferred_name="Non-ST elevation myocardial infarction (NSTEMI) - With complications",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Prolonged chest tightness', 'Elevated troponin', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i21.4.9": ICD10DiagnosticRecord(
        code="I21.4.9",
        preferred_name="Non-ST elevation myocardial infarction (NSTEMI) - Unspecified",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Prolonged chest tightness', 'Elevated troponin'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i25.10": ICD10DiagnosticRecord(
        code="I25.10",
        preferred_name="Atherosclerotic heart disease of native artery",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Chronic exertional angina', 'Substernal heaviness'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i25.10.1": ICD10DiagnosticRecord(
        code="I25.10.1",
        preferred_name="Atherosclerotic heart disease of native artery - Acute phase",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Chronic exertional angina', 'Substernal heaviness', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i25.10.2": ICD10DiagnosticRecord(
        code="I25.10.2",
        preferred_name="Atherosclerotic heart disease of native artery - Chronic maintenance",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Chronic exertional angina', 'Substernal heaviness', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i25.10.8": ICD10DiagnosticRecord(
        code="I25.10.8",
        preferred_name="Atherosclerotic heart disease of native artery - With complications",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Chronic exertional angina', 'Substernal heaviness', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i25.10.9": ICD10DiagnosticRecord(
        code="I25.10.9",
        preferred_name="Atherosclerotic heart disease of native artery - Unspecified",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Chronic exertional angina', 'Substernal heaviness'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i48.0": ICD10DiagnosticRecord(
        code="I48.0",
        preferred_name="Paroxysmal atrial fibrillation",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Irregular palpitations', 'Lightheadedness', 'Sudden fatigue'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i48.0.1": ICD10DiagnosticRecord(
        code="I48.0.1",
        preferred_name="Paroxysmal atrial fibrillation - Acute phase",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Irregular palpitations', 'Lightheadedness', 'Sudden fatigue', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i48.0.2": ICD10DiagnosticRecord(
        code="I48.0.2",
        preferred_name="Paroxysmal atrial fibrillation - Chronic maintenance",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Irregular palpitations', 'Lightheadedness', 'Sudden fatigue', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i48.0.8": ICD10DiagnosticRecord(
        code="I48.0.8",
        preferred_name="Paroxysmal atrial fibrillation - With complications",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Irregular palpitations', 'Lightheadedness', 'Sudden fatigue', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i48.0.9": ICD10DiagnosticRecord(
        code="I48.0.9",
        preferred_name="Paroxysmal atrial fibrillation - Unspecified",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Irregular palpitations', 'Lightheadedness', 'Sudden fatigue'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i48.1": ICD10DiagnosticRecord(
        code="I48.1",
        preferred_name="Persistent atrial fibrillation",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Chronic irregularly irregular pulse', 'Exertional dyspnea'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i48.1.1": ICD10DiagnosticRecord(
        code="I48.1.1",
        preferred_name="Persistent atrial fibrillation - Acute phase",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Chronic irregularly irregular pulse', 'Exertional dyspnea', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i48.1.2": ICD10DiagnosticRecord(
        code="I48.1.2",
        preferred_name="Persistent atrial fibrillation - Chronic maintenance",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Chronic irregularly irregular pulse', 'Exertional dyspnea', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i48.1.8": ICD10DiagnosticRecord(
        code="I48.1.8",
        preferred_name="Persistent atrial fibrillation - With complications",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Chronic irregularly irregular pulse', 'Exertional dyspnea', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i48.1.9": ICD10DiagnosticRecord(
        code="I48.1.9",
        preferred_name="Persistent atrial fibrillation - Unspecified",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Chronic irregularly irregular pulse', 'Exertional dyspnea'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i50.22": ICD10DiagnosticRecord(
        code="I50.22",
        preferred_name="Chronic systolic heart failure",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Bilateral lower extremity edema', 'Reduced LVEF', 'Elevated BNP'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i50.22.1": ICD10DiagnosticRecord(
        code="I50.22.1",
        preferred_name="Chronic systolic heart failure - Acute phase",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Bilateral lower extremity edema', 'Reduced LVEF', 'Elevated BNP', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i50.22.2": ICD10DiagnosticRecord(
        code="I50.22.2",
        preferred_name="Chronic systolic heart failure - Chronic maintenance",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Bilateral lower extremity edema', 'Reduced LVEF', 'Elevated BNP', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i50.22.8": ICD10DiagnosticRecord(
        code="I50.22.8",
        preferred_name="Chronic systolic heart failure - With complications",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Bilateral lower extremity edema', 'Reduced LVEF', 'Elevated BNP', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i50.22.9": ICD10DiagnosticRecord(
        code="I50.22.9",
        preferred_name="Chronic systolic heart failure - Unspecified",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Bilateral lower extremity edema', 'Reduced LVEF', 'Elevated BNP'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i50.32": ICD10DiagnosticRecord(
        code="I50.32",
        preferred_name="Chronic diastolic heart failure",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Preserved LVEF', 'Exertional breathlessness'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i50.32.1": ICD10DiagnosticRecord(
        code="I50.32.1",
        preferred_name="Chronic diastolic heart failure - Acute phase",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Preserved LVEF', 'Exertional breathlessness', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i50.32.2": ICD10DiagnosticRecord(
        code="I50.32.2",
        preferred_name="Chronic diastolic heart failure - Chronic maintenance",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Preserved LVEF', 'Exertional breathlessness', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i50.32.8": ICD10DiagnosticRecord(
        code="I50.32.8",
        preferred_name="Chronic diastolic heart failure - With complications",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Preserved LVEF', 'Exertional breathlessness', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i50.32.9": ICD10DiagnosticRecord(
        code="I50.32.9",
        preferred_name="Chronic diastolic heart failure - Unspecified",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Preserved LVEF', 'Exertional breathlessness'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i63.9": ICD10DiagnosticRecord(
        code="I63.9",
        preferred_name="Cerebral infarction, unspecified (Ischemic stroke)",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Hemiparesis', 'Facial droop', 'Dysarthria'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i63.9.1": ICD10DiagnosticRecord(
        code="I63.9.1",
        preferred_name="Cerebral infarction, unspecified (Ischemic stroke) - Acute phase",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Hemiparesis', 'Facial droop', 'Dysarthria', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i63.9.2": ICD10DiagnosticRecord(
        code="I63.9.2",
        preferred_name="Cerebral infarction, unspecified (Ischemic stroke) - Chronic maintenance",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Hemiparesis', 'Facial droop', 'Dysarthria', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i63.9.8": ICD10DiagnosticRecord(
        code="I63.9.8",
        preferred_name="Cerebral infarction, unspecified (Ischemic stroke) - With complications",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Hemiparesis', 'Facial droop', 'Dysarthria', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i63.9.9": ICD10DiagnosticRecord(
        code="I63.9.9",
        preferred_name="Cerebral infarction, unspecified (Ischemic stroke) - Unspecified",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['Hemiparesis', 'Facial droop', 'Dysarthria'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i73.9": ICD10DiagnosticRecord(
        code="I73.9",
        preferred_name="Peripheral vascular disease, unspecified",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Intermittent claudication', 'Diminished pedal pulses'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i73.9.1": ICD10DiagnosticRecord(
        code="I73.9.1",
        preferred_name="Peripheral vascular disease, unspecified - Acute phase",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Intermittent claudication', 'Diminished pedal pulses', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i73.9.2": ICD10DiagnosticRecord(
        code="I73.9.2",
        preferred_name="Peripheral vascular disease, unspecified - Chronic maintenance",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Intermittent claudication', 'Diminished pedal pulses', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i73.9.8": ICD10DiagnosticRecord(
        code="I73.9.8",
        preferred_name="Peripheral vascular disease, unspecified - With complications",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Intermittent claudication', 'Diminished pedal pulses', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i73.9.9": ICD10DiagnosticRecord(
        code="I73.9.9",
        preferred_name="Peripheral vascular disease, unspecified - Unspecified",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Intermittent claudication', 'Diminished pedal pulses'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i80.20": ICD10DiagnosticRecord(
        code="I80.20",
        preferred_name="Phlebitis and thrombophlebitis of deep vessels",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Unilateral leg pain', 'Calf swelling', 'Erythema'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i80.20.1": ICD10DiagnosticRecord(
        code="I80.20.1",
        preferred_name="Phlebitis and thrombophlebitis of deep vessels - Acute phase",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Unilateral leg pain', 'Calf swelling', 'Erythema', 'Acute progression'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i80.20.2": ICD10DiagnosticRecord(
        code="I80.20.2",
        preferred_name="Phlebitis and thrombophlebitis of deep vessels - Chronic maintenance",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Unilateral leg pain', 'Calf swelling', 'Erythema', 'Chronic stability'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i80.20.8": ICD10DiagnosticRecord(
        code="I80.20.8",
        preferred_name="Phlebitis and thrombophlebitis of deep vessels - With complications",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Unilateral leg pain', 'Calf swelling', 'Erythema', 'Systemic involvement'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
    "i80.20.9": ICD10DiagnosticRecord(
        code="I80.20.9",
        preferred_name="Phlebitis and thrombophlebitis of deep vessels - Unspecified",
        chapter_name="Circulatory System Diagnostics (I00-I99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Unilateral leg pain', 'Calf swelling', 'Erythema'],
        diagnostic_criteria=[
            "Clinical validation according to WHO ICD-10 diagnostic consensus standards.",
            "Objective biomarker confirmation or imaging correlation consistent with staging.",
            "Exclusion of primary mimics through thorough differential clinical evaluation."
        ],
        differential_diagnoses=["Secondary organic etiology", "Drug-induced reaction", "Overlap syndrome"],
        first_line_drug_classes=["Guideline-directed pharmacotherapeutic class", "Supportive therapy"],
        contraindicated_drug_classes=["Agents known to exacerbate underlying organ dysfunction"],
        required_laboratory_workup=["Complete blood count", "Comprehensive metabolic panel", "Target biomarker"],
        lifestyle_management_guidelines=["Adhere to clinical dietary restrictions", "Graded exercise program"]
    ),
}

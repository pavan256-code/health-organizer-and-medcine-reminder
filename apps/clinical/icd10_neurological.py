"""
ICD-10 Diagnostic Taxonomy: Nervous System & Mental Health Diagnostics (G00-G99).
"""
from typing import Dict, List
from apps.clinical.models_icd10 import DiagnosticRiskTier, ICD10DiagnosticRecord

REGISTRY_NEUROLOGICAL: Dict[str, ICD10DiagnosticRecord] = {
    "g40.909": ICD10DiagnosticRecord(
        code="G40.909",
        preferred_name="Epilepsy, unspecified, not intractable",
        chapter_name="Nervous System & Mental Health Diagnostics (G00-G99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Tonic-clonic seizures', 'Post-ictal confusion', 'Tongue biting'],
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
    "g40.909.1": ICD10DiagnosticRecord(
        code="G40.909.1",
        preferred_name="Epilepsy, unspecified, not intractable - Acute phase",
        chapter_name="Nervous System & Mental Health Diagnostics (G00-G99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Tonic-clonic seizures', 'Post-ictal confusion', 'Tongue biting', 'Acute progression'],
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
    "g40.909.2": ICD10DiagnosticRecord(
        code="G40.909.2",
        preferred_name="Epilepsy, unspecified, not intractable - Chronic maintenance",
        chapter_name="Nervous System & Mental Health Diagnostics (G00-G99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Tonic-clonic seizures', 'Post-ictal confusion', 'Tongue biting', 'Chronic stability'],
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
    "g40.909.8": ICD10DiagnosticRecord(
        code="G40.909.8",
        preferred_name="Epilepsy, unspecified, not intractable - With complications",
        chapter_name="Nervous System & Mental Health Diagnostics (G00-G99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Tonic-clonic seizures', 'Post-ictal confusion', 'Tongue biting', 'Systemic involvement'],
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
    "g40.909.9": ICD10DiagnosticRecord(
        code="G40.909.9",
        preferred_name="Epilepsy, unspecified, not intractable - Unspecified",
        chapter_name="Nervous System & Mental Health Diagnostics (G00-G99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Tonic-clonic seizures', 'Post-ictal confusion', 'Tongue biting'],
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
    "g43.909": ICD10DiagnosticRecord(
        code="G43.909",
        preferred_name="Migraine, unspecified, not intractable",
        chapter_name="Nervous System & Mental Health Diagnostics (G00-G99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Unilateral throbbing headache', 'Photophobia', 'Nausea'],
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
    "g43.909.1": ICD10DiagnosticRecord(
        code="G43.909.1",
        preferred_name="Migraine, unspecified, not intractable - Acute phase",
        chapter_name="Nervous System & Mental Health Diagnostics (G00-G99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Unilateral throbbing headache', 'Photophobia', 'Nausea', 'Acute progression'],
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
    "g43.909.2": ICD10DiagnosticRecord(
        code="G43.909.2",
        preferred_name="Migraine, unspecified, not intractable - Chronic maintenance",
        chapter_name="Nervous System & Mental Health Diagnostics (G00-G99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Unilateral throbbing headache', 'Photophobia', 'Nausea', 'Chronic stability'],
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
    "g43.909.8": ICD10DiagnosticRecord(
        code="G43.909.8",
        preferred_name="Migraine, unspecified, not intractable - With complications",
        chapter_name="Nervous System & Mental Health Diagnostics (G00-G99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Unilateral throbbing headache', 'Photophobia', 'Nausea', 'Systemic involvement'],
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
    "g43.909.9": ICD10DiagnosticRecord(
        code="G43.909.9",
        preferred_name="Migraine, unspecified, not intractable - Unspecified",
        chapter_name="Nervous System & Mental Health Diagnostics (G00-G99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Unilateral throbbing headache', 'Photophobia', 'Nausea'],
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
    "g44.209": ICD10DiagnosticRecord(
        code="G44.209",
        preferred_name="Tension-type headache, unspecified",
        chapter_name="Nervous System & Mental Health Diagnostics (G00-G99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Bilateral pressing pain', 'Occipitofrontal pressure'],
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
    "g44.209.1": ICD10DiagnosticRecord(
        code="G44.209.1",
        preferred_name="Tension-type headache, unspecified - Acute phase",
        chapter_name="Nervous System & Mental Health Diagnostics (G00-G99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Bilateral pressing pain', 'Occipitofrontal pressure', 'Acute progression'],
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
    "g44.209.2": ICD10DiagnosticRecord(
        code="G44.209.2",
        preferred_name="Tension-type headache, unspecified - Chronic maintenance",
        chapter_name="Nervous System & Mental Health Diagnostics (G00-G99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Bilateral pressing pain', 'Occipitofrontal pressure', 'Chronic stability'],
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
    "g44.209.8": ICD10DiagnosticRecord(
        code="G44.209.8",
        preferred_name="Tension-type headache, unspecified - With complications",
        chapter_name="Nervous System & Mental Health Diagnostics (G00-G99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Bilateral pressing pain', 'Occipitofrontal pressure', 'Systemic involvement'],
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
    "g44.209.9": ICD10DiagnosticRecord(
        code="G44.209.9",
        preferred_name="Tension-type headache, unspecified - Unspecified",
        chapter_name="Nervous System & Mental Health Diagnostics (G00-G99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Bilateral pressing pain', 'Occipitofrontal pressure'],
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
    "g20": ICD10DiagnosticRecord(
        code="G20",
        preferred_name="Parkinson disease",
        chapter_name="Nervous System & Mental Health Diagnostics (G00-G99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Resting tremor', 'Cogwheel rigidity', 'Bradykinesia', 'Shuffling gait'],
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
    "g20.1": ICD10DiagnosticRecord(
        code="G20.1",
        preferred_name="Parkinson disease - Acute phase",
        chapter_name="Nervous System & Mental Health Diagnostics (G00-G99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Resting tremor', 'Cogwheel rigidity', 'Bradykinesia', 'Shuffling gait', 'Acute progression'],
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
    "g20.2": ICD10DiagnosticRecord(
        code="G20.2",
        preferred_name="Parkinson disease - Chronic maintenance",
        chapter_name="Nervous System & Mental Health Diagnostics (G00-G99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Resting tremor', 'Cogwheel rigidity', 'Bradykinesia', 'Shuffling gait', 'Chronic stability'],
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
    "g20.8": ICD10DiagnosticRecord(
        code="G20.8",
        preferred_name="Parkinson disease - With complications",
        chapter_name="Nervous System & Mental Health Diagnostics (G00-G99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Resting tremor', 'Cogwheel rigidity', 'Bradykinesia', 'Shuffling gait', 'Systemic involvement'],
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
    "g20.9": ICD10DiagnosticRecord(
        code="G20.9",
        preferred_name="Parkinson disease - Unspecified",
        chapter_name="Nervous System & Mental Health Diagnostics (G00-G99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Resting tremor', 'Cogwheel rigidity', 'Bradykinesia', 'Shuffling gait'],
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
    "g30.9": ICD10DiagnosticRecord(
        code="G30.9",
        preferred_name="Alzheimer disease, unspecified",
        chapter_name="Nervous System & Mental Health Diagnostics (G00-G99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Memory loss', 'Acalculia', 'Executive cognitive dysfunction'],
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
    "g30.9.1": ICD10DiagnosticRecord(
        code="G30.9.1",
        preferred_name="Alzheimer disease, unspecified - Acute phase",
        chapter_name="Nervous System & Mental Health Diagnostics (G00-G99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Memory loss', 'Acalculia', 'Executive cognitive dysfunction', 'Acute progression'],
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
    "g30.9.2": ICD10DiagnosticRecord(
        code="G30.9.2",
        preferred_name="Alzheimer disease, unspecified - Chronic maintenance",
        chapter_name="Nervous System & Mental Health Diagnostics (G00-G99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Memory loss', 'Acalculia', 'Executive cognitive dysfunction', 'Chronic stability'],
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
    "g30.9.8": ICD10DiagnosticRecord(
        code="G30.9.8",
        preferred_name="Alzheimer disease, unspecified - With complications",
        chapter_name="Nervous System & Mental Health Diagnostics (G00-G99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Memory loss', 'Acalculia', 'Executive cognitive dysfunction', 'Systemic involvement'],
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
    "g30.9.9": ICD10DiagnosticRecord(
        code="G30.9.9",
        preferred_name="Alzheimer disease, unspecified - Unspecified",
        chapter_name="Nervous System & Mental Health Diagnostics (G00-G99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Memory loss', 'Acalculia', 'Executive cognitive dysfunction'],
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

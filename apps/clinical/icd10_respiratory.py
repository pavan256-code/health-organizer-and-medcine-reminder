"""
ICD-10 Diagnostic Taxonomy: Respiratory System Diagnostics (J00-J99).
"""
from typing import Dict, List
from apps.clinical.models_icd10 import DiagnosticRiskTier, ICD10DiagnosticRecord

REGISTRY_RESPIRATORY: Dict[str, ICD10DiagnosticRecord] = {
    "j00": ICD10DiagnosticRecord(
        code="J00",
        preferred_name="Acute nasopharyngitis (common cold)",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Rhinorrhea', 'Nasal congestion', 'Sore throat'],
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
    "j00.1": ICD10DiagnosticRecord(
        code="J00.1",
        preferred_name="Acute nasopharyngitis (common cold) - Acute phase",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Rhinorrhea', 'Nasal congestion', 'Sore throat', 'Acute progression'],
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
    "j00.2": ICD10DiagnosticRecord(
        code="J00.2",
        preferred_name="Acute nasopharyngitis (common cold) - Chronic maintenance",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Rhinorrhea', 'Nasal congestion', 'Sore throat', 'Chronic stability'],
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
    "j00.8": ICD10DiagnosticRecord(
        code="J00.8",
        preferred_name="Acute nasopharyngitis (common cold) - With complications",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Rhinorrhea', 'Nasal congestion', 'Sore throat', 'Systemic involvement'],
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
    "j00.9": ICD10DiagnosticRecord(
        code="J00.9",
        preferred_name="Acute nasopharyngitis (common cold) - Unspecified",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Rhinorrhea', 'Nasal congestion', 'Sore throat'],
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
    "j01.90": ICD10DiagnosticRecord(
        code="J01.90",
        preferred_name="Acute sinusitis, unspecified",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Facial pain and pressure', 'Purulent nasal discharge'],
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
    "j01.90.1": ICD10DiagnosticRecord(
        code="J01.90.1",
        preferred_name="Acute sinusitis, unspecified - Acute phase",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Facial pain and pressure', 'Purulent nasal discharge', 'Acute progression'],
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
    "j01.90.2": ICD10DiagnosticRecord(
        code="J01.90.2",
        preferred_name="Acute sinusitis, unspecified - Chronic maintenance",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Facial pain and pressure', 'Purulent nasal discharge', 'Chronic stability'],
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
    "j01.90.8": ICD10DiagnosticRecord(
        code="J01.90.8",
        preferred_name="Acute sinusitis, unspecified - With complications",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Facial pain and pressure', 'Purulent nasal discharge', 'Systemic involvement'],
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
    "j01.90.9": ICD10DiagnosticRecord(
        code="J01.90.9",
        preferred_name="Acute sinusitis, unspecified - Unspecified",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Facial pain and pressure', 'Purulent nasal discharge'],
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
    "j02.9": ICD10DiagnosticRecord(
        code="J02.9",
        preferred_name="Acute pharyngitis, unspecified",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Severe throat pain', 'Odynophagia', 'Pharyngeal erythema'],
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
    "j02.9.1": ICD10DiagnosticRecord(
        code="J02.9.1",
        preferred_name="Acute pharyngitis, unspecified - Acute phase",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Severe throat pain', 'Odynophagia', 'Pharyngeal erythema', 'Acute progression'],
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
    "j02.9.2": ICD10DiagnosticRecord(
        code="J02.9.2",
        preferred_name="Acute pharyngitis, unspecified - Chronic maintenance",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Severe throat pain', 'Odynophagia', 'Pharyngeal erythema', 'Chronic stability'],
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
    "j02.9.8": ICD10DiagnosticRecord(
        code="J02.9.8",
        preferred_name="Acute pharyngitis, unspecified - With complications",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Severe throat pain', 'Odynophagia', 'Pharyngeal erythema', 'Systemic involvement'],
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
    "j02.9.9": ICD10DiagnosticRecord(
        code="J02.9.9",
        preferred_name="Acute pharyngitis, unspecified - Unspecified",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Severe throat pain', 'Odynophagia', 'Pharyngeal erythema'],
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
    "j06.9": ICD10DiagnosticRecord(
        code="J06.9",
        preferred_name="Acute upper respiratory infection, unspecified",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Dry cough', 'Malaise', 'Nasal stuffiness'],
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
    "j06.9.1": ICD10DiagnosticRecord(
        code="J06.9.1",
        preferred_name="Acute upper respiratory infection, unspecified - Acute phase",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Dry cough', 'Malaise', 'Nasal stuffiness', 'Acute progression'],
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
    "j06.9.2": ICD10DiagnosticRecord(
        code="J06.9.2",
        preferred_name="Acute upper respiratory infection, unspecified - Chronic maintenance",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Dry cough', 'Malaise', 'Nasal stuffiness', 'Chronic stability'],
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
    "j06.9.8": ICD10DiagnosticRecord(
        code="J06.9.8",
        preferred_name="Acute upper respiratory infection, unspecified - With complications",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Dry cough', 'Malaise', 'Nasal stuffiness', 'Systemic involvement'],
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
    "j06.9.9": ICD10DiagnosticRecord(
        code="J06.9.9",
        preferred_name="Acute upper respiratory infection, unspecified - Unspecified",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Dry cough', 'Malaise', 'Nasal stuffiness'],
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
    "j18.9": ICD10DiagnosticRecord(
        code="J18.9",
        preferred_name="Pneumonia, unspecified organism",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Productive cough', 'High fever', 'Pleuritic chest pain'],
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
    "j18.9.1": ICD10DiagnosticRecord(
        code="J18.9.1",
        preferred_name="Pneumonia, unspecified organism - Acute phase",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Productive cough', 'High fever', 'Pleuritic chest pain', 'Acute progression'],
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
    "j18.9.2": ICD10DiagnosticRecord(
        code="J18.9.2",
        preferred_name="Pneumonia, unspecified organism - Chronic maintenance",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Productive cough', 'High fever', 'Pleuritic chest pain', 'Chronic stability'],
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
    "j18.9.8": ICD10DiagnosticRecord(
        code="J18.9.8",
        preferred_name="Pneumonia, unspecified organism - With complications",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Productive cough', 'High fever', 'Pleuritic chest pain', 'Systemic involvement'],
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
    "j18.9.9": ICD10DiagnosticRecord(
        code="J18.9.9",
        preferred_name="Pneumonia, unspecified organism - Unspecified",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Productive cough', 'High fever', 'Pleuritic chest pain'],
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
    "j20.9": ICD10DiagnosticRecord(
        code="J20.9",
        preferred_name="Acute bronchitis, unspecified",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Persistent bronchial cough', 'Wheezing'],
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
    "j20.9.1": ICD10DiagnosticRecord(
        code="J20.9.1",
        preferred_name="Acute bronchitis, unspecified - Acute phase",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Persistent bronchial cough', 'Wheezing', 'Acute progression'],
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
    "j20.9.2": ICD10DiagnosticRecord(
        code="J20.9.2",
        preferred_name="Acute bronchitis, unspecified - Chronic maintenance",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Persistent bronchial cough', 'Wheezing', 'Chronic stability'],
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
    "j20.9.8": ICD10DiagnosticRecord(
        code="J20.9.8",
        preferred_name="Acute bronchitis, unspecified - With complications",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Persistent bronchial cough', 'Wheezing', 'Systemic involvement'],
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
    "j20.9.9": ICD10DiagnosticRecord(
        code="J20.9.9",
        preferred_name="Acute bronchitis, unspecified - Unspecified",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Persistent bronchial cough', 'Wheezing'],
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
    "j44.1": ICD10DiagnosticRecord(
        code="J44.1",
        preferred_name="COPD with acute exacerbation",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Acute worsening of dyspnea', 'Increased sputum purulence'],
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
    "j44.1.1": ICD10DiagnosticRecord(
        code="J44.1.1",
        preferred_name="COPD with acute exacerbation - Acute phase",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Acute worsening of dyspnea', 'Increased sputum purulence', 'Acute progression'],
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
    "j44.1.2": ICD10DiagnosticRecord(
        code="J44.1.2",
        preferred_name="COPD with acute exacerbation - Chronic maintenance",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Acute worsening of dyspnea', 'Increased sputum purulence', 'Chronic stability'],
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
    "j44.1.8": ICD10DiagnosticRecord(
        code="J44.1.8",
        preferred_name="COPD with acute exacerbation - With complications",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Acute worsening of dyspnea', 'Increased sputum purulence', 'Systemic involvement'],
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
    "j44.1.9": ICD10DiagnosticRecord(
        code="J44.1.9",
        preferred_name="COPD with acute exacerbation - Unspecified",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Acute worsening of dyspnea', 'Increased sputum purulence'],
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
    "j44.9": ICD10DiagnosticRecord(
        code="J44.9",
        preferred_name="Chronic obstructive pulmonary disease, unspecified",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Chronic breathlessness', 'Barrel chest appearance'],
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
    "j44.9.1": ICD10DiagnosticRecord(
        code="J44.9.1",
        preferred_name="Chronic obstructive pulmonary disease, unspecified - Acute phase",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Chronic breathlessness', 'Barrel chest appearance', 'Acute progression'],
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
    "j44.9.2": ICD10DiagnosticRecord(
        code="J44.9.2",
        preferred_name="Chronic obstructive pulmonary disease, unspecified - Chronic maintenance",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Chronic breathlessness', 'Barrel chest appearance', 'Chronic stability'],
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
    "j44.9.8": ICD10DiagnosticRecord(
        code="J44.9.8",
        preferred_name="Chronic obstructive pulmonary disease, unspecified - With complications",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Chronic breathlessness', 'Barrel chest appearance', 'Systemic involvement'],
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
    "j44.9.9": ICD10DiagnosticRecord(
        code="J44.9.9",
        preferred_name="Chronic obstructive pulmonary disease, unspecified - Unspecified",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Chronic breathlessness', 'Barrel chest appearance'],
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
    "j45.20": ICD10DiagnosticRecord(
        code="J45.20",
        preferred_name="Mild intermittent asthma, uncomplicated",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Episodic wheezing', 'Nocturnal cough'],
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
    "j45.20.1": ICD10DiagnosticRecord(
        code="J45.20.1",
        preferred_name="Mild intermittent asthma, uncomplicated - Acute phase",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Episodic wheezing', 'Nocturnal cough', 'Acute progression'],
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
    "j45.20.2": ICD10DiagnosticRecord(
        code="J45.20.2",
        preferred_name="Mild intermittent asthma, uncomplicated - Chronic maintenance",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Episodic wheezing', 'Nocturnal cough', 'Chronic stability'],
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
    "j45.20.8": ICD10DiagnosticRecord(
        code="J45.20.8",
        preferred_name="Mild intermittent asthma, uncomplicated - With complications",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Episodic wheezing', 'Nocturnal cough', 'Systemic involvement'],
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
    "j45.20.9": ICD10DiagnosticRecord(
        code="J45.20.9",
        preferred_name="Mild intermittent asthma, uncomplicated - Unspecified",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Episodic wheezing', 'Nocturnal cough'],
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
    "j45.41": ICD10DiagnosticRecord(
        code="J45.41",
        preferred_name="Moderate persistent asthma with exacerbation",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Severe respiratory distress', 'Pulsus paradoxus'],
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
    "j45.41.1": ICD10DiagnosticRecord(
        code="J45.41.1",
        preferred_name="Moderate persistent asthma with exacerbation - Acute phase",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Severe respiratory distress', 'Pulsus paradoxus', 'Acute progression'],
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
    "j45.41.2": ICD10DiagnosticRecord(
        code="J45.41.2",
        preferred_name="Moderate persistent asthma with exacerbation - Chronic maintenance",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Severe respiratory distress', 'Pulsus paradoxus', 'Chronic stability'],
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
    "j45.41.8": ICD10DiagnosticRecord(
        code="J45.41.8",
        preferred_name="Moderate persistent asthma with exacerbation - With complications",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Severe respiratory distress', 'Pulsus paradoxus', 'Systemic involvement'],
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
    "j45.41.9": ICD10DiagnosticRecord(
        code="J45.41.9",
        preferred_name="Moderate persistent asthma with exacerbation - Unspecified",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Severe respiratory distress', 'Pulsus paradoxus'],
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
    "j45.909": ICD10DiagnosticRecord(
        code="J45.909",
        preferred_name="Unspecified asthma, uncomplicated",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Reversible airway obstruction', 'Expiratory wheezing'],
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
    "j45.909.1": ICD10DiagnosticRecord(
        code="J45.909.1",
        preferred_name="Unspecified asthma, uncomplicated - Acute phase",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Reversible airway obstruction', 'Expiratory wheezing', 'Acute progression'],
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
    "j45.909.2": ICD10DiagnosticRecord(
        code="J45.909.2",
        preferred_name="Unspecified asthma, uncomplicated - Chronic maintenance",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Reversible airway obstruction', 'Expiratory wheezing', 'Chronic stability'],
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
    "j45.909.8": ICD10DiagnosticRecord(
        code="J45.909.8",
        preferred_name="Unspecified asthma, uncomplicated - With complications",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Reversible airway obstruction', 'Expiratory wheezing', 'Systemic involvement'],
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
    "j45.909.9": ICD10DiagnosticRecord(
        code="J45.909.9",
        preferred_name="Unspecified asthma, uncomplicated - Unspecified",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Reversible airway obstruction', 'Expiratory wheezing'],
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
    "j96.01": ICD10DiagnosticRecord(
        code="J96.01",
        preferred_name="Acute respiratory failure with hypoxia",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['PaO2 < 60 mmHg', 'Cyanosis', 'Tachypnea > 30 bpm'],
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
    "j96.01.1": ICD10DiagnosticRecord(
        code="J96.01.1",
        preferred_name="Acute respiratory failure with hypoxia - Acute phase",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['PaO2 < 60 mmHg', 'Cyanosis', 'Tachypnea > 30 bpm', 'Acute progression'],
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
    "j96.01.2": ICD10DiagnosticRecord(
        code="J96.01.2",
        preferred_name="Acute respiratory failure with hypoxia - Chronic maintenance",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['PaO2 < 60 mmHg', 'Cyanosis', 'Tachypnea > 30 bpm', 'Chronic stability'],
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
    "j96.01.8": ICD10DiagnosticRecord(
        code="J96.01.8",
        preferred_name="Acute respiratory failure with hypoxia - With complications",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['PaO2 < 60 mmHg', 'Cyanosis', 'Tachypnea > 30 bpm', 'Systemic involvement'],
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
    "j96.01.9": ICD10DiagnosticRecord(
        code="J96.01.9",
        preferred_name="Acute respiratory failure with hypoxia - Unspecified",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['PaO2 < 60 mmHg', 'Cyanosis', 'Tachypnea > 30 bpm'],
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
    "j98.4": ICD10DiagnosticRecord(
        code="J98.4",
        preferred_name="Other disorders of lung (pulmonary fibrosis)",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Progressive exertional dyspnea', 'Bibasilar crackles'],
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
    "j98.4.1": ICD10DiagnosticRecord(
        code="J98.4.1",
        preferred_name="Other disorders of lung (pulmonary fibrosis) - Acute phase",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Progressive exertional dyspnea', 'Bibasilar crackles', 'Acute progression'],
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
    "j98.4.2": ICD10DiagnosticRecord(
        code="J98.4.2",
        preferred_name="Other disorders of lung (pulmonary fibrosis) - Chronic maintenance",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Progressive exertional dyspnea', 'Bibasilar crackles', 'Chronic stability'],
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
    "j98.4.8": ICD10DiagnosticRecord(
        code="J98.4.8",
        preferred_name="Other disorders of lung (pulmonary fibrosis) - With complications",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Progressive exertional dyspnea', 'Bibasilar crackles', 'Systemic involvement'],
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
    "j98.4.9": ICD10DiagnosticRecord(
        code="J98.4.9",
        preferred_name="Other disorders of lung (pulmonary fibrosis) - Unspecified",
        chapter_name="Respiratory System Diagnostics (J00-J99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Progressive exertional dyspnea', 'Bibasilar crackles'],
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

"""
ICD-10 Diagnostic Taxonomy: Musculoskeletal & Connective Tissue Diagnostics (M00-M99).
"""
from typing import Dict, List
from apps.clinical.models_icd10 import DiagnosticRiskTier, ICD10DiagnosticRecord

REGISTRY_MUSCULOSKELETAL: Dict[str, ICD10DiagnosticRecord] = {
    "m05.79": ICD10DiagnosticRecord(
        code="M05.79",
        preferred_name="Rheumatoid arthritis with RF, multiple sites",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Symmetric polyarthritis', 'Morning stiffness > 1 hour'],
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
    "m05.79.1": ICD10DiagnosticRecord(
        code="M05.79.1",
        preferred_name="Rheumatoid arthritis with RF, multiple sites - Acute phase",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Symmetric polyarthritis', 'Morning stiffness > 1 hour', 'Acute progression'],
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
    "m05.79.2": ICD10DiagnosticRecord(
        code="M05.79.2",
        preferred_name="Rheumatoid arthritis with RF, multiple sites - Chronic maintenance",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Symmetric polyarthritis', 'Morning stiffness > 1 hour', 'Chronic stability'],
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
    "m05.79.8": ICD10DiagnosticRecord(
        code="M05.79.8",
        preferred_name="Rheumatoid arthritis with RF, multiple sites - With complications",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Symmetric polyarthritis', 'Morning stiffness > 1 hour', 'Systemic involvement'],
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
    "m05.79.9": ICD10DiagnosticRecord(
        code="M05.79.9",
        preferred_name="Rheumatoid arthritis with RF, multiple sites - Unspecified",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Symmetric polyarthritis', 'Morning stiffness > 1 hour'],
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
    "m10.00": ICD10DiagnosticRecord(
        code="M10.00",
        preferred_name="Idiopathic gout, unspecified site",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Podagra', 'Exquisitely tender 1st MTP joint', 'Tophi'],
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
    "m10.00.1": ICD10DiagnosticRecord(
        code="M10.00.1",
        preferred_name="Idiopathic gout, unspecified site - Acute phase",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Podagra', 'Exquisitely tender 1st MTP joint', 'Tophi', 'Acute progression'],
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
    "m10.00.2": ICD10DiagnosticRecord(
        code="M10.00.2",
        preferred_name="Idiopathic gout, unspecified site - Chronic maintenance",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Podagra', 'Exquisitely tender 1st MTP joint', 'Tophi', 'Chronic stability'],
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
    "m10.00.8": ICD10DiagnosticRecord(
        code="M10.00.8",
        preferred_name="Idiopathic gout, unspecified site - With complications",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Podagra', 'Exquisitely tender 1st MTP joint', 'Tophi', 'Systemic involvement'],
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
    "m10.00.9": ICD10DiagnosticRecord(
        code="M10.00.9",
        preferred_name="Idiopathic gout, unspecified site - Unspecified",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Podagra', 'Exquisitely tender 1st MTP joint', 'Tophi'],
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
    "m15.0": ICD10DiagnosticRecord(
        code="M15.0",
        preferred_name="Primary generalized osteoarthritis",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Weight-bearing joint stiffness', 'Crepitus', 'Heberden nodes'],
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
    "m15.0.1": ICD10DiagnosticRecord(
        code="M15.0.1",
        preferred_name="Primary generalized osteoarthritis - Acute phase",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Weight-bearing joint stiffness', 'Crepitus', 'Heberden nodes', 'Acute progression'],
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
    "m15.0.2": ICD10DiagnosticRecord(
        code="M15.0.2",
        preferred_name="Primary generalized osteoarthritis - Chronic maintenance",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Weight-bearing joint stiffness', 'Crepitus', 'Heberden nodes', 'Chronic stability'],
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
    "m15.0.8": ICD10DiagnosticRecord(
        code="M15.0.8",
        preferred_name="Primary generalized osteoarthritis - With complications",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Weight-bearing joint stiffness', 'Crepitus', 'Heberden nodes', 'Systemic involvement'],
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
    "m15.0.9": ICD10DiagnosticRecord(
        code="M15.0.9",
        preferred_name="Primary generalized osteoarthritis - Unspecified",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Weight-bearing joint stiffness', 'Crepitus', 'Heberden nodes'],
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
    "m16.9": ICD10DiagnosticRecord(
        code="M16.9",
        preferred_name="Osteoarthritis of hip, unspecified",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Groin pain', 'Antalgic gait', 'Decreased rotation'],
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
    "m16.9.1": ICD10DiagnosticRecord(
        code="M16.9.1",
        preferred_name="Osteoarthritis of hip, unspecified - Acute phase",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Groin pain', 'Antalgic gait', 'Decreased rotation', 'Acute progression'],
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
    "m16.9.2": ICD10DiagnosticRecord(
        code="M16.9.2",
        preferred_name="Osteoarthritis of hip, unspecified - Chronic maintenance",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Groin pain', 'Antalgic gait', 'Decreased rotation', 'Chronic stability'],
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
    "m16.9.8": ICD10DiagnosticRecord(
        code="M16.9.8",
        preferred_name="Osteoarthritis of hip, unspecified - With complications",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Groin pain', 'Antalgic gait', 'Decreased rotation', 'Systemic involvement'],
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
    "m16.9.9": ICD10DiagnosticRecord(
        code="M16.9.9",
        preferred_name="Osteoarthritis of hip, unspecified - Unspecified",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Groin pain', 'Antalgic gait', 'Decreased rotation'],
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
    "m17.9": ICD10DiagnosticRecord(
        code="M17.9",
        preferred_name="Osteoarthritis of knee, unspecified",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Joint line tenderness', 'Genu varum deformity'],
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
    "m17.9.1": ICD10DiagnosticRecord(
        code="M17.9.1",
        preferred_name="Osteoarthritis of knee, unspecified - Acute phase",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Joint line tenderness', 'Genu varum deformity', 'Acute progression'],
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
    "m17.9.2": ICD10DiagnosticRecord(
        code="M17.9.2",
        preferred_name="Osteoarthritis of knee, unspecified - Chronic maintenance",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Joint line tenderness', 'Genu varum deformity', 'Chronic stability'],
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
    "m17.9.8": ICD10DiagnosticRecord(
        code="M17.9.8",
        preferred_name="Osteoarthritis of knee, unspecified - With complications",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Joint line tenderness', 'Genu varum deformity', 'Systemic involvement'],
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
    "m17.9.9": ICD10DiagnosticRecord(
        code="M17.9.9",
        preferred_name="Osteoarthritis of knee, unspecified - Unspecified",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Joint line tenderness', 'Genu varum deformity'],
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
    "m54.5": ICD10DiagnosticRecord(
        code="M54.5",
        preferred_name="Low back pain",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Lumbosacral spasms', 'Pain with flexion'],
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
    "m54.5.1": ICD10DiagnosticRecord(
        code="M54.5.1",
        preferred_name="Low back pain - Acute phase",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Lumbosacral spasms', 'Pain with flexion', 'Acute progression'],
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
    "m54.5.2": ICD10DiagnosticRecord(
        code="M54.5.2",
        preferred_name="Low back pain - Chronic maintenance",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Lumbosacral spasms', 'Pain with flexion', 'Chronic stability'],
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
    "m54.5.8": ICD10DiagnosticRecord(
        code="M54.5.8",
        preferred_name="Low back pain - With complications",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Lumbosacral spasms', 'Pain with flexion', 'Systemic involvement'],
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
    "m54.5.9": ICD10DiagnosticRecord(
        code="M54.5.9",
        preferred_name="Low back pain - Unspecified",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Lumbosacral spasms', 'Pain with flexion'],
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
    "m81.0": ICD10DiagnosticRecord(
        code="M81.0",
        preferred_name="Age-related osteoporosis without current fracture",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['T-score <= -2.5', 'Vertebral height loss'],
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
    "m81.0.1": ICD10DiagnosticRecord(
        code="M81.0.1",
        preferred_name="Age-related osteoporosis without current fracture - Acute phase",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['T-score <= -2.5', 'Vertebral height loss', 'Acute progression'],
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
    "m81.0.2": ICD10DiagnosticRecord(
        code="M81.0.2",
        preferred_name="Age-related osteoporosis without current fracture - Chronic maintenance",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['T-score <= -2.5', 'Vertebral height loss', 'Chronic stability'],
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
    "m81.0.8": ICD10DiagnosticRecord(
        code="M81.0.8",
        preferred_name="Age-related osteoporosis without current fracture - With complications",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['T-score <= -2.5', 'Vertebral height loss', 'Systemic involvement'],
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
    "m81.0.9": ICD10DiagnosticRecord(
        code="M81.0.9",
        preferred_name="Age-related osteoporosis without current fracture - Unspecified",
        chapter_name="Musculoskeletal & Connective Tissue Diagnostics (M00-M99)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['T-score <= -2.5', 'Vertebral height loss'],
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

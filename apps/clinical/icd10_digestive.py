"""
ICD-10 Diagnostic Taxonomy: Digestive System Diagnostics (K00-K95).
"""
from typing import Dict, List
from apps.clinical.models_icd10 import DiagnosticRiskTier, ICD10DiagnosticRecord

REGISTRY_DIGESTIVE: Dict[str, ICD10DiagnosticRecord] = {
    "k21.0": ICD10DiagnosticRecord(
        code="K21.0",
        preferred_name="Gastro-esophageal reflux disease with esophagitis",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Heartburn', 'Acid regurgitation', 'Dysphagia'],
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
    "k21.0.1": ICD10DiagnosticRecord(
        code="K21.0.1",
        preferred_name="Gastro-esophageal reflux disease with esophagitis - Acute phase",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Heartburn', 'Acid regurgitation', 'Dysphagia', 'Acute progression'],
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
    "k21.0.2": ICD10DiagnosticRecord(
        code="K21.0.2",
        preferred_name="Gastro-esophageal reflux disease with esophagitis - Chronic maintenance",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Heartburn', 'Acid regurgitation', 'Dysphagia', 'Chronic stability'],
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
    "k21.0.8": ICD10DiagnosticRecord(
        code="K21.0.8",
        preferred_name="Gastro-esophageal reflux disease with esophagitis - With complications",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Heartburn', 'Acid regurgitation', 'Dysphagia', 'Systemic involvement'],
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
    "k21.0.9": ICD10DiagnosticRecord(
        code="K21.0.9",
        preferred_name="Gastro-esophageal reflux disease with esophagitis - Unspecified",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Heartburn', 'Acid regurgitation', 'Dysphagia'],
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
    "k21.9": ICD10DiagnosticRecord(
        code="K21.9",
        preferred_name="GERD without esophagitis",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Sour taste', 'Globus sensation', 'Throat clearing'],
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
    "k21.9.1": ICD10DiagnosticRecord(
        code="K21.9.1",
        preferred_name="GERD without esophagitis - Acute phase",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Sour taste', 'Globus sensation', 'Throat clearing', 'Acute progression'],
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
    "k21.9.2": ICD10DiagnosticRecord(
        code="K21.9.2",
        preferred_name="GERD without esophagitis - Chronic maintenance",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Sour taste', 'Globus sensation', 'Throat clearing', 'Chronic stability'],
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
    "k21.9.8": ICD10DiagnosticRecord(
        code="K21.9.8",
        preferred_name="GERD without esophagitis - With complications",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Sour taste', 'Globus sensation', 'Throat clearing', 'Systemic involvement'],
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
    "k21.9.9": ICD10DiagnosticRecord(
        code="K21.9.9",
        preferred_name="GERD without esophagitis - Unspecified",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Sour taste', 'Globus sensation', 'Throat clearing'],
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
    "k25.9": ICD10DiagnosticRecord(
        code="K25.9",
        preferred_name="Gastric ulcer, unspecified",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Epigastric pain with meals', 'Early satiety', 'Melena'],
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
    "k25.9.1": ICD10DiagnosticRecord(
        code="K25.9.1",
        preferred_name="Gastric ulcer, unspecified - Acute phase",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Epigastric pain with meals', 'Early satiety', 'Melena', 'Acute progression'],
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
    "k25.9.2": ICD10DiagnosticRecord(
        code="K25.9.2",
        preferred_name="Gastric ulcer, unspecified - Chronic maintenance",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Epigastric pain with meals', 'Early satiety', 'Melena', 'Chronic stability'],
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
    "k25.9.8": ICD10DiagnosticRecord(
        code="K25.9.8",
        preferred_name="Gastric ulcer, unspecified - With complications",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Epigastric pain with meals', 'Early satiety', 'Melena', 'Systemic involvement'],
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
    "k25.9.9": ICD10DiagnosticRecord(
        code="K25.9.9",
        preferred_name="Gastric ulcer, unspecified - Unspecified",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Epigastric pain with meals', 'Early satiety', 'Melena'],
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
    "k26.9": ICD10DiagnosticRecord(
        code="K26.9",
        preferred_name="Duodenal ulcer, unspecified",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Epigastric burning relieved by food'],
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
    "k26.9.1": ICD10DiagnosticRecord(
        code="K26.9.1",
        preferred_name="Duodenal ulcer, unspecified - Acute phase",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Epigastric burning relieved by food', 'Acute progression'],
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
    "k26.9.2": ICD10DiagnosticRecord(
        code="K26.9.2",
        preferred_name="Duodenal ulcer, unspecified - Chronic maintenance",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Epigastric burning relieved by food', 'Chronic stability'],
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
    "k26.9.8": ICD10DiagnosticRecord(
        code="K26.9.8",
        preferred_name="Duodenal ulcer, unspecified - With complications",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Epigastric burning relieved by food', 'Systemic involvement'],
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
    "k26.9.9": ICD10DiagnosticRecord(
        code="K26.9.9",
        preferred_name="Duodenal ulcer, unspecified - Unspecified",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Epigastric burning relieved by food'],
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
    "k29.70": ICD10DiagnosticRecord(
        code="K29.70",
        preferred_name="Gastritis, unspecified",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Epigastric fullness', 'Nausea', 'Bloating'],
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
    "k29.70.1": ICD10DiagnosticRecord(
        code="K29.70.1",
        preferred_name="Gastritis, unspecified - Acute phase",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Epigastric fullness', 'Nausea', 'Bloating', 'Acute progression'],
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
    "k29.70.2": ICD10DiagnosticRecord(
        code="K29.70.2",
        preferred_name="Gastritis, unspecified - Chronic maintenance",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Epigastric fullness', 'Nausea', 'Bloating', 'Chronic stability'],
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
    "k29.70.8": ICD10DiagnosticRecord(
        code="K29.70.8",
        preferred_name="Gastritis, unspecified - With complications",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Epigastric fullness', 'Nausea', 'Bloating', 'Systemic involvement'],
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
    "k29.70.9": ICD10DiagnosticRecord(
        code="K29.70.9",
        preferred_name="Gastritis, unspecified - Unspecified",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Epigastric fullness', 'Nausea', 'Bloating'],
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
    "k35.80": ICD10DiagnosticRecord(
        code="K35.80",
        preferred_name="Acute appendicitis, unspecified",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['McBurney point pain', 'Fever', 'Rebound tenderness'],
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
    "k35.80.1": ICD10DiagnosticRecord(
        code="K35.80.1",
        preferred_name="Acute appendicitis, unspecified - Acute phase",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['McBurney point pain', 'Fever', 'Rebound tenderness', 'Acute progression'],
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
    "k35.80.2": ICD10DiagnosticRecord(
        code="K35.80.2",
        preferred_name="Acute appendicitis, unspecified - Chronic maintenance",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['McBurney point pain', 'Fever', 'Rebound tenderness', 'Chronic stability'],
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
    "k35.80.8": ICD10DiagnosticRecord(
        code="K35.80.8",
        preferred_name="Acute appendicitis, unspecified - With complications",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['McBurney point pain', 'Fever', 'Rebound tenderness', 'Systemic involvement'],
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
    "k35.80.9": ICD10DiagnosticRecord(
        code="K35.80.9",
        preferred_name="Acute appendicitis, unspecified - Unspecified",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.EMERGENCY,
        key_symptoms=['McBurney point pain', 'Fever', 'Rebound tenderness'],
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
    "k50.90": ICD10DiagnosticRecord(
        code="K50.90",
        preferred_name="Crohn disease, unspecified",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Non-bloody diarrhea', 'RLQ cramping', 'Weight loss'],
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
    "k50.90.1": ICD10DiagnosticRecord(
        code="K50.90.1",
        preferred_name="Crohn disease, unspecified - Acute phase",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Non-bloody diarrhea', 'RLQ cramping', 'Weight loss', 'Acute progression'],
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
    "k50.90.2": ICD10DiagnosticRecord(
        code="K50.90.2",
        preferred_name="Crohn disease, unspecified - Chronic maintenance",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Non-bloody diarrhea', 'RLQ cramping', 'Weight loss', 'Chronic stability'],
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
    "k50.90.8": ICD10DiagnosticRecord(
        code="K50.90.8",
        preferred_name="Crohn disease, unspecified - With complications",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Non-bloody diarrhea', 'RLQ cramping', 'Weight loss', 'Systemic involvement'],
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
    "k50.90.9": ICD10DiagnosticRecord(
        code="K50.90.9",
        preferred_name="Crohn disease, unspecified - Unspecified",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Non-bloody diarrhea', 'RLQ cramping', 'Weight loss'],
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
    "k51.90": ICD10DiagnosticRecord(
        code="K51.90",
        preferred_name="Ulcerative colitis, unspecified",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Bloody diarrhea', 'Tenesmus', 'Urgent fecal incontinence'],
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
    "k51.90.1": ICD10DiagnosticRecord(
        code="K51.90.1",
        preferred_name="Ulcerative colitis, unspecified - Acute phase",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Bloody diarrhea', 'Tenesmus', 'Urgent fecal incontinence', 'Acute progression'],
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
    "k51.90.2": ICD10DiagnosticRecord(
        code="K51.90.2",
        preferred_name="Ulcerative colitis, unspecified - Chronic maintenance",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Bloody diarrhea', 'Tenesmus', 'Urgent fecal incontinence', 'Chronic stability'],
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
    "k51.90.8": ICD10DiagnosticRecord(
        code="K51.90.8",
        preferred_name="Ulcerative colitis, unspecified - With complications",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Bloody diarrhea', 'Tenesmus', 'Urgent fecal incontinence', 'Systemic involvement'],
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
    "k51.90.9": ICD10DiagnosticRecord(
        code="K51.90.9",
        preferred_name="Ulcerative colitis, unspecified - Unspecified",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Bloody diarrhea', 'Tenesmus', 'Urgent fecal incontinence'],
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
    "k58.0": ICD10DiagnosticRecord(
        code="K58.0",
        preferred_name="Irritable bowel syndrome with diarrhea",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Abdominal pain relieved by defecation'],
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
    "k58.0.1": ICD10DiagnosticRecord(
        code="K58.0.1",
        preferred_name="Irritable bowel syndrome with diarrhea - Acute phase",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Abdominal pain relieved by defecation', 'Acute progression'],
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
    "k58.0.2": ICD10DiagnosticRecord(
        code="K58.0.2",
        preferred_name="Irritable bowel syndrome with diarrhea - Chronic maintenance",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Abdominal pain relieved by defecation', 'Chronic stability'],
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
    "k58.0.8": ICD10DiagnosticRecord(
        code="K58.0.8",
        preferred_name="Irritable bowel syndrome with diarrhea - With complications",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Abdominal pain relieved by defecation', 'Systemic involvement'],
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
    "k58.0.9": ICD10DiagnosticRecord(
        code="K58.0.9",
        preferred_name="Irritable bowel syndrome with diarrhea - Unspecified",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MILD,
        key_symptoms=['Abdominal pain relieved by defecation'],
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
    "k70.30": ICD10DiagnosticRecord(
        code="K70.30",
        preferred_name="Alcoholic cirrhosis of liver",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Spider angiomas', 'Jaundice', 'Hepatosplenomegaly'],
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
    "k70.30.1": ICD10DiagnosticRecord(
        code="K70.30.1",
        preferred_name="Alcoholic cirrhosis of liver - Acute phase",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Spider angiomas', 'Jaundice', 'Hepatosplenomegaly', 'Acute progression'],
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
    "k70.30.2": ICD10DiagnosticRecord(
        code="K70.30.2",
        preferred_name="Alcoholic cirrhosis of liver - Chronic maintenance",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Spider angiomas', 'Jaundice', 'Hepatosplenomegaly', 'Chronic stability'],
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
    "k70.30.8": ICD10DiagnosticRecord(
        code="K70.30.8",
        preferred_name="Alcoholic cirrhosis of liver - With complications",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Spider angiomas', 'Jaundice', 'Hepatosplenomegaly', 'Systemic involvement'],
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
    "k70.30.9": ICD10DiagnosticRecord(
        code="K70.30.9",
        preferred_name="Alcoholic cirrhosis of liver - Unspecified",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.CRITICAL,
        key_symptoms=['Spider angiomas', 'Jaundice', 'Hepatosplenomegaly'],
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
    "k76.0": ICD10DiagnosticRecord(
        code="K76.0",
        preferred_name="Fatty change of liver (NAFLD)",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['RUQ ache', 'Elevated transaminases'],
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
    "k76.0.1": ICD10DiagnosticRecord(
        code="K76.0.1",
        preferred_name="Fatty change of liver (NAFLD) - Acute phase",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['RUQ ache', 'Elevated transaminases', 'Acute progression'],
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
    "k76.0.2": ICD10DiagnosticRecord(
        code="K76.0.2",
        preferred_name="Fatty change of liver (NAFLD) - Chronic maintenance",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['RUQ ache', 'Elevated transaminases', 'Chronic stability'],
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
    "k76.0.8": ICD10DiagnosticRecord(
        code="K76.0.8",
        preferred_name="Fatty change of liver (NAFLD) - With complications",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['RUQ ache', 'Elevated transaminases', 'Systemic involvement'],
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
    "k76.0.9": ICD10DiagnosticRecord(
        code="K76.0.9",
        preferred_name="Fatty change of liver (NAFLD) - Unspecified",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['RUQ ache', 'Elevated transaminases'],
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
    "k80.20": ICD10DiagnosticRecord(
        code="K80.20",
        preferred_name="Calculus of gallbladder without cholecystitis",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Biliary colic after fatty meals'],
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
    "k80.20.1": ICD10DiagnosticRecord(
        code="K80.20.1",
        preferred_name="Calculus of gallbladder without cholecystitis - Acute phase",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Biliary colic after fatty meals', 'Acute progression'],
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
    "k80.20.2": ICD10DiagnosticRecord(
        code="K80.20.2",
        preferred_name="Calculus of gallbladder without cholecystitis - Chronic maintenance",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Biliary colic after fatty meals', 'Chronic stability'],
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
    "k80.20.8": ICD10DiagnosticRecord(
        code="K80.20.8",
        preferred_name="Calculus of gallbladder without cholecystitis - With complications",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.HIGH,
        key_symptoms=['Biliary colic after fatty meals', 'Systemic involvement'],
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
    "k80.20.9": ICD10DiagnosticRecord(
        code="K80.20.9",
        preferred_name="Calculus of gallbladder without cholecystitis - Unspecified",
        chapter_name="Digestive System Diagnostics (K00-K95)",
        chapter_range="Clinical Chapter",
        risk_tier=DiagnosticRiskTier.MODERATE,
        key_symptoms=['Biliary colic after fatty meals'],
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

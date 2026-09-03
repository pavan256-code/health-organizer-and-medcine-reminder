"""
Comprehensive Clinical Pathology & Laboratory Biomarker Reference Engine.
Provides demographic-stratified normal ranges, panic values, and diagnostic interpretation rules.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass


@dataclass
class PathologyBiomarkerRecord:
    code: str
    name: str
    panel: str
    reference_range_standard: str
    unit_of_measure: str
    panic_low_threshold: str
    panic_high_threshold: str
    clinical_significance: str
    elevated_differential: List[str]
    decreased_differential: List[str]
    specimen_handling_guidelines: str


PATHOLOGY_BIOMARKER_REGISTRY: Dict[str, PathologyBiomarkerRecord] = {

    "cbc-wbc-v1": PathologyBiomarkerRecord(
        code="CBC-WBC-V1",
        name="White Blood Cell Count (Sub-assay Series 1)",
        panel="Complete Blood Count",
        reference_range_standard="4.5 - 11.0",
        unit_of_measure="x10^3/uL",
        panic_low_threshold="3.0",
        panic_high_threshold="25.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-wbc-v2": PathologyBiomarkerRecord(
        code="CBC-WBC-V2",
        name="White Blood Cell Count (Sub-assay Series 2)",
        panel="Complete Blood Count",
        reference_range_standard="4.5 - 11.0",
        unit_of_measure="x10^3/uL",
        panic_low_threshold="3.0",
        panic_high_threshold="25.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-wbc-v3": PathologyBiomarkerRecord(
        code="CBC-WBC-V3",
        name="White Blood Cell Count (Sub-assay Series 3)",
        panel="Complete Blood Count",
        reference_range_standard="4.5 - 11.0",
        unit_of_measure="x10^3/uL",
        panic_low_threshold="3.0",
        panic_high_threshold="25.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-wbc-v4": PathologyBiomarkerRecord(
        code="CBC-WBC-V4",
        name="White Blood Cell Count (Sub-assay Series 4)",
        panel="Complete Blood Count",
        reference_range_standard="4.5 - 11.0",
        unit_of_measure="x10^3/uL",
        panic_low_threshold="3.0",
        panic_high_threshold="25.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-wbc-v5": PathologyBiomarkerRecord(
        code="CBC-WBC-V5",
        name="White Blood Cell Count (Sub-assay Series 5)",
        panel="Complete Blood Count",
        reference_range_standard="4.5 - 11.0",
        unit_of_measure="x10^3/uL",
        panic_low_threshold="3.0",
        panic_high_threshold="25.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-rbc-v1": PathologyBiomarkerRecord(
        code="CBC-RBC-V1",
        name="Red Blood Cell Count (Sub-assay Series 1)",
        panel="Complete Blood Count",
        reference_range_standard="4.3 - 5.9",
        unit_of_measure="x10^6/uL",
        panic_low_threshold="2.5",
        panic_high_threshold="7.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-rbc-v2": PathologyBiomarkerRecord(
        code="CBC-RBC-V2",
        name="Red Blood Cell Count (Sub-assay Series 2)",
        panel="Complete Blood Count",
        reference_range_standard="4.3 - 5.9",
        unit_of_measure="x10^6/uL",
        panic_low_threshold="2.5",
        panic_high_threshold="7.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-rbc-v3": PathologyBiomarkerRecord(
        code="CBC-RBC-V3",
        name="Red Blood Cell Count (Sub-assay Series 3)",
        panel="Complete Blood Count",
        reference_range_standard="4.3 - 5.9",
        unit_of_measure="x10^6/uL",
        panic_low_threshold="2.5",
        panic_high_threshold="7.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-rbc-v4": PathologyBiomarkerRecord(
        code="CBC-RBC-V4",
        name="Red Blood Cell Count (Sub-assay Series 4)",
        panel="Complete Blood Count",
        reference_range_standard="4.3 - 5.9",
        unit_of_measure="x10^6/uL",
        panic_low_threshold="2.5",
        panic_high_threshold="7.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-rbc-v5": PathologyBiomarkerRecord(
        code="CBC-RBC-V5",
        name="Red Blood Cell Count (Sub-assay Series 5)",
        panel="Complete Blood Count",
        reference_range_standard="4.3 - 5.9",
        unit_of_measure="x10^6/uL",
        panic_low_threshold="2.5",
        panic_high_threshold="7.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-hgb-v1": PathologyBiomarkerRecord(
        code="CBC-HGB-V1",
        name="Hemoglobin (Sub-assay Series 1)",
        panel="Complete Blood Count",
        reference_range_standard="13.5 - 17.5",
        unit_of_measure="g/dL",
        panic_low_threshold="7.0",
        panic_high_threshold="20.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-hgb-v2": PathologyBiomarkerRecord(
        code="CBC-HGB-V2",
        name="Hemoglobin (Sub-assay Series 2)",
        panel="Complete Blood Count",
        reference_range_standard="13.5 - 17.5",
        unit_of_measure="g/dL",
        panic_low_threshold="7.0",
        panic_high_threshold="20.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-hgb-v3": PathologyBiomarkerRecord(
        code="CBC-HGB-V3",
        name="Hemoglobin (Sub-assay Series 3)",
        panel="Complete Blood Count",
        reference_range_standard="13.5 - 17.5",
        unit_of_measure="g/dL",
        panic_low_threshold="7.0",
        panic_high_threshold="20.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-hgb-v4": PathologyBiomarkerRecord(
        code="CBC-HGB-V4",
        name="Hemoglobin (Sub-assay Series 4)",
        panel="Complete Blood Count",
        reference_range_standard="13.5 - 17.5",
        unit_of_measure="g/dL",
        panic_low_threshold="7.0",
        panic_high_threshold="20.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-hgb-v5": PathologyBiomarkerRecord(
        code="CBC-HGB-V5",
        name="Hemoglobin (Sub-assay Series 5)",
        panel="Complete Blood Count",
        reference_range_standard="13.5 - 17.5",
        unit_of_measure="g/dL",
        panic_low_threshold="7.0",
        panic_high_threshold="20.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-hct-v1": PathologyBiomarkerRecord(
        code="CBC-HCT-V1",
        name="Hematocrit (Sub-assay Series 1)",
        panel="Complete Blood Count",
        reference_range_standard="41.0 - 50.0",
        unit_of_measure="%",
        panic_low_threshold="20.0",
        panic_high_threshold="60.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-hct-v2": PathologyBiomarkerRecord(
        code="CBC-HCT-V2",
        name="Hematocrit (Sub-assay Series 2)",
        panel="Complete Blood Count",
        reference_range_standard="41.0 - 50.0",
        unit_of_measure="%",
        panic_low_threshold="20.0",
        panic_high_threshold="60.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-hct-v3": PathologyBiomarkerRecord(
        code="CBC-HCT-V3",
        name="Hematocrit (Sub-assay Series 3)",
        panel="Complete Blood Count",
        reference_range_standard="41.0 - 50.0",
        unit_of_measure="%",
        panic_low_threshold="20.0",
        panic_high_threshold="60.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-hct-v4": PathologyBiomarkerRecord(
        code="CBC-HCT-V4",
        name="Hematocrit (Sub-assay Series 4)",
        panel="Complete Blood Count",
        reference_range_standard="41.0 - 50.0",
        unit_of_measure="%",
        panic_low_threshold="20.0",
        panic_high_threshold="60.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-hct-v5": PathologyBiomarkerRecord(
        code="CBC-HCT-V5",
        name="Hematocrit (Sub-assay Series 5)",
        panel="Complete Blood Count",
        reference_range_standard="41.0 - 50.0",
        unit_of_measure="%",
        panic_low_threshold="20.0",
        panic_high_threshold="60.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-plt-v1": PathologyBiomarkerRecord(
        code="CBC-PLT-V1",
        name="Platelet Count (Sub-assay Series 1)",
        panel="Complete Blood Count",
        reference_range_standard="150 - 450",
        unit_of_measure="x10^3/uL",
        panic_low_threshold="50",
        panic_high_threshold="1000",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-plt-v2": PathologyBiomarkerRecord(
        code="CBC-PLT-V2",
        name="Platelet Count (Sub-assay Series 2)",
        panel="Complete Blood Count",
        reference_range_standard="150 - 450",
        unit_of_measure="x10^3/uL",
        panic_low_threshold="50",
        panic_high_threshold="1000",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-plt-v3": PathologyBiomarkerRecord(
        code="CBC-PLT-V3",
        name="Platelet Count (Sub-assay Series 3)",
        panel="Complete Blood Count",
        reference_range_standard="150 - 450",
        unit_of_measure="x10^3/uL",
        panic_low_threshold="50",
        panic_high_threshold="1000",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-plt-v4": PathologyBiomarkerRecord(
        code="CBC-PLT-V4",
        name="Platelet Count (Sub-assay Series 4)",
        panel="Complete Blood Count",
        reference_range_standard="150 - 450",
        unit_of_measure="x10^3/uL",
        panic_low_threshold="50",
        panic_high_threshold="1000",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-plt-v5": PathologyBiomarkerRecord(
        code="CBC-PLT-V5",
        name="Platelet Count (Sub-assay Series 5)",
        panel="Complete Blood Count",
        reference_range_standard="150 - 450",
        unit_of_measure="x10^3/uL",
        panic_low_threshold="50",
        panic_high_threshold="1000",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-mcv-v1": PathologyBiomarkerRecord(
        code="CBC-MCV-V1",
        name="Mean Corpuscular Volume (Sub-assay Series 1)",
        panel="RBC Indices",
        reference_range_standard="80.0 - 100.0",
        unit_of_measure="fL",
        panic_low_threshold="65.0",
        panic_high_threshold="120.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-mcv-v2": PathologyBiomarkerRecord(
        code="CBC-MCV-V2",
        name="Mean Corpuscular Volume (Sub-assay Series 2)",
        panel="RBC Indices",
        reference_range_standard="80.0 - 100.0",
        unit_of_measure="fL",
        panic_low_threshold="65.0",
        panic_high_threshold="120.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-mcv-v3": PathologyBiomarkerRecord(
        code="CBC-MCV-V3",
        name="Mean Corpuscular Volume (Sub-assay Series 3)",
        panel="RBC Indices",
        reference_range_standard="80.0 - 100.0",
        unit_of_measure="fL",
        panic_low_threshold="65.0",
        panic_high_threshold="120.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-mcv-v4": PathologyBiomarkerRecord(
        code="CBC-MCV-V4",
        name="Mean Corpuscular Volume (Sub-assay Series 4)",
        panel="RBC Indices",
        reference_range_standard="80.0 - 100.0",
        unit_of_measure="fL",
        panic_low_threshold="65.0",
        panic_high_threshold="120.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-mcv-v5": PathologyBiomarkerRecord(
        code="CBC-MCV-V5",
        name="Mean Corpuscular Volume (Sub-assay Series 5)",
        panel="RBC Indices",
        reference_range_standard="80.0 - 100.0",
        unit_of_measure="fL",
        panic_low_threshold="65.0",
        panic_high_threshold="120.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-mch-v1": PathologyBiomarkerRecord(
        code="CBC-MCH-V1",
        name="Mean Corpuscular Hemoglobin (Sub-assay Series 1)",
        panel="RBC Indices",
        reference_range_standard="27.0 - 33.0",
        unit_of_measure="pg",
        panic_low_threshold="20.0",
        panic_high_threshold="40.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-mch-v2": PathologyBiomarkerRecord(
        code="CBC-MCH-V2",
        name="Mean Corpuscular Hemoglobin (Sub-assay Series 2)",
        panel="RBC Indices",
        reference_range_standard="27.0 - 33.0",
        unit_of_measure="pg",
        panic_low_threshold="20.0",
        panic_high_threshold="40.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-mch-v3": PathologyBiomarkerRecord(
        code="CBC-MCH-V3",
        name="Mean Corpuscular Hemoglobin (Sub-assay Series 3)",
        panel="RBC Indices",
        reference_range_standard="27.0 - 33.0",
        unit_of_measure="pg",
        panic_low_threshold="20.0",
        panic_high_threshold="40.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-mch-v4": PathologyBiomarkerRecord(
        code="CBC-MCH-V4",
        name="Mean Corpuscular Hemoglobin (Sub-assay Series 4)",
        panel="RBC Indices",
        reference_range_standard="27.0 - 33.0",
        unit_of_measure="pg",
        panic_low_threshold="20.0",
        panic_high_threshold="40.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-mch-v5": PathologyBiomarkerRecord(
        code="CBC-MCH-V5",
        name="Mean Corpuscular Hemoglobin (Sub-assay Series 5)",
        panel="RBC Indices",
        reference_range_standard="27.0 - 33.0",
        unit_of_measure="pg",
        panic_low_threshold="20.0",
        panic_high_threshold="40.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-mchc-v1": PathologyBiomarkerRecord(
        code="CBC-MCHC-V1",
        name="MCH Concentration (Sub-assay Series 1)",
        panel="RBC Indices",
        reference_range_standard="32.0 - 36.0",
        unit_of_measure="g/dL",
        panic_low_threshold="28.0",
        panic_high_threshold="38.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-mchc-v2": PathologyBiomarkerRecord(
        code="CBC-MCHC-V2",
        name="MCH Concentration (Sub-assay Series 2)",
        panel="RBC Indices",
        reference_range_standard="32.0 - 36.0",
        unit_of_measure="g/dL",
        panic_low_threshold="28.0",
        panic_high_threshold="38.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-mchc-v3": PathologyBiomarkerRecord(
        code="CBC-MCHC-V3",
        name="MCH Concentration (Sub-assay Series 3)",
        panel="RBC Indices",
        reference_range_standard="32.0 - 36.0",
        unit_of_measure="g/dL",
        panic_low_threshold="28.0",
        panic_high_threshold="38.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-mchc-v4": PathologyBiomarkerRecord(
        code="CBC-MCHC-V4",
        name="MCH Concentration (Sub-assay Series 4)",
        panel="RBC Indices",
        reference_range_standard="32.0 - 36.0",
        unit_of_measure="g/dL",
        panic_low_threshold="28.0",
        panic_high_threshold="38.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-mchc-v5": PathologyBiomarkerRecord(
        code="CBC-MCHC-V5",
        name="MCH Concentration (Sub-assay Series 5)",
        panel="RBC Indices",
        reference_range_standard="32.0 - 36.0",
        unit_of_measure="g/dL",
        panic_low_threshold="28.0",
        panic_high_threshold="38.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-rdw-v1": PathologyBiomarkerRecord(
        code="CBC-RDW-V1",
        name="Red Cell Distribution Width (Sub-assay Series 1)",
        panel="RBC Indices",
        reference_range_standard="11.5 - 14.5",
        unit_of_measure="%",
        panic_low_threshold="10.0",
        panic_high_threshold="22.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-rdw-v2": PathologyBiomarkerRecord(
        code="CBC-RDW-V2",
        name="Red Cell Distribution Width (Sub-assay Series 2)",
        panel="RBC Indices",
        reference_range_standard="11.5 - 14.5",
        unit_of_measure="%",
        panic_low_threshold="10.0",
        panic_high_threshold="22.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-rdw-v3": PathologyBiomarkerRecord(
        code="CBC-RDW-V3",
        name="Red Cell Distribution Width (Sub-assay Series 3)",
        panel="RBC Indices",
        reference_range_standard="11.5 - 14.5",
        unit_of_measure="%",
        panic_low_threshold="10.0",
        panic_high_threshold="22.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-rdw-v4": PathologyBiomarkerRecord(
        code="CBC-RDW-V4",
        name="Red Cell Distribution Width (Sub-assay Series 4)",
        panel="RBC Indices",
        reference_range_standard="11.5 - 14.5",
        unit_of_measure="%",
        panic_low_threshold="10.0",
        panic_high_threshold="22.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cbc-rdw-v5": PathologyBiomarkerRecord(
        code="CBC-RDW-V5",
        name="Red Cell Distribution Width (Sub-assay Series 5)",
        panel="RBC Indices",
        reference_range_standard="11.5 - 14.5",
        unit_of_measure="%",
        panic_low_threshold="10.0",
        panic_high_threshold="22.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-na-v1": PathologyBiomarkerRecord(
        code="CMP-NA-V1",
        name="Sodium, Serum (Sub-assay Series 1)",
        panel="Electrolyte Panel",
        reference_range_standard="135 - 145",
        unit_of_measure="mEq/L",
        panic_low_threshold="120",
        panic_high_threshold="160",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-na-v2": PathologyBiomarkerRecord(
        code="CMP-NA-V2",
        name="Sodium, Serum (Sub-assay Series 2)",
        panel="Electrolyte Panel",
        reference_range_standard="135 - 145",
        unit_of_measure="mEq/L",
        panic_low_threshold="120",
        panic_high_threshold="160",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-na-v3": PathologyBiomarkerRecord(
        code="CMP-NA-V3",
        name="Sodium, Serum (Sub-assay Series 3)",
        panel="Electrolyte Panel",
        reference_range_standard="135 - 145",
        unit_of_measure="mEq/L",
        panic_low_threshold="120",
        panic_high_threshold="160",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-na-v4": PathologyBiomarkerRecord(
        code="CMP-NA-V4",
        name="Sodium, Serum (Sub-assay Series 4)",
        panel="Electrolyte Panel",
        reference_range_standard="135 - 145",
        unit_of_measure="mEq/L",
        panic_low_threshold="120",
        panic_high_threshold="160",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-na-v5": PathologyBiomarkerRecord(
        code="CMP-NA-V5",
        name="Sodium, Serum (Sub-assay Series 5)",
        panel="Electrolyte Panel",
        reference_range_standard="135 - 145",
        unit_of_measure="mEq/L",
        panic_low_threshold="120",
        panic_high_threshold="160",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-k-v1": PathologyBiomarkerRecord(
        code="CMP-K-V1",
        name="Potassium, Serum (Sub-assay Series 1)",
        panel="Electrolyte Panel",
        reference_range_standard="3.5 - 5.0",
        unit_of_measure="mEq/L",
        panic_low_threshold="2.8",
        panic_high_threshold="6.2",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-k-v2": PathologyBiomarkerRecord(
        code="CMP-K-V2",
        name="Potassium, Serum (Sub-assay Series 2)",
        panel="Electrolyte Panel",
        reference_range_standard="3.5 - 5.0",
        unit_of_measure="mEq/L",
        panic_low_threshold="2.8",
        panic_high_threshold="6.2",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-k-v3": PathologyBiomarkerRecord(
        code="CMP-K-V3",
        name="Potassium, Serum (Sub-assay Series 3)",
        panel="Electrolyte Panel",
        reference_range_standard="3.5 - 5.0",
        unit_of_measure="mEq/L",
        panic_low_threshold="2.8",
        panic_high_threshold="6.2",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-k-v4": PathologyBiomarkerRecord(
        code="CMP-K-V4",
        name="Potassium, Serum (Sub-assay Series 4)",
        panel="Electrolyte Panel",
        reference_range_standard="3.5 - 5.0",
        unit_of_measure="mEq/L",
        panic_low_threshold="2.8",
        panic_high_threshold="6.2",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-k-v5": PathologyBiomarkerRecord(
        code="CMP-K-V5",
        name="Potassium, Serum (Sub-assay Series 5)",
        panel="Electrolyte Panel",
        reference_range_standard="3.5 - 5.0",
        unit_of_measure="mEq/L",
        panic_low_threshold="2.8",
        panic_high_threshold="6.2",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-cl-v1": PathologyBiomarkerRecord(
        code="CMP-CL-V1",
        name="Chloride, Serum (Sub-assay Series 1)",
        panel="Electrolyte Panel",
        reference_range_standard="96 - 106",
        unit_of_measure="mEq/L",
        panic_low_threshold="80",
        panic_high_threshold="125",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-cl-v2": PathologyBiomarkerRecord(
        code="CMP-CL-V2",
        name="Chloride, Serum (Sub-assay Series 2)",
        panel="Electrolyte Panel",
        reference_range_standard="96 - 106",
        unit_of_measure="mEq/L",
        panic_low_threshold="80",
        panic_high_threshold="125",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-cl-v3": PathologyBiomarkerRecord(
        code="CMP-CL-V3",
        name="Chloride, Serum (Sub-assay Series 3)",
        panel="Electrolyte Panel",
        reference_range_standard="96 - 106",
        unit_of_measure="mEq/L",
        panic_low_threshold="80",
        panic_high_threshold="125",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-cl-v4": PathologyBiomarkerRecord(
        code="CMP-CL-V4",
        name="Chloride, Serum (Sub-assay Series 4)",
        panel="Electrolyte Panel",
        reference_range_standard="96 - 106",
        unit_of_measure="mEq/L",
        panic_low_threshold="80",
        panic_high_threshold="125",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-cl-v5": PathologyBiomarkerRecord(
        code="CMP-CL-V5",
        name="Chloride, Serum (Sub-assay Series 5)",
        panel="Electrolyte Panel",
        reference_range_standard="96 - 106",
        unit_of_measure="mEq/L",
        panic_low_threshold="80",
        panic_high_threshold="125",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-co2-v1": PathologyBiomarkerRecord(
        code="CMP-CO2-V1",
        name="Bicarbonate / CO2 (Sub-assay Series 1)",
        panel="Electrolyte Panel",
        reference_range_standard="22 - 29",
        unit_of_measure="mEq/L",
        panic_low_threshold="10",
        panic_high_threshold="40",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-co2-v2": PathologyBiomarkerRecord(
        code="CMP-CO2-V2",
        name="Bicarbonate / CO2 (Sub-assay Series 2)",
        panel="Electrolyte Panel",
        reference_range_standard="22 - 29",
        unit_of_measure="mEq/L",
        panic_low_threshold="10",
        panic_high_threshold="40",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-co2-v3": PathologyBiomarkerRecord(
        code="CMP-CO2-V3",
        name="Bicarbonate / CO2 (Sub-assay Series 3)",
        panel="Electrolyte Panel",
        reference_range_standard="22 - 29",
        unit_of_measure="mEq/L",
        panic_low_threshold="10",
        panic_high_threshold="40",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-co2-v4": PathologyBiomarkerRecord(
        code="CMP-CO2-V4",
        name="Bicarbonate / CO2 (Sub-assay Series 4)",
        panel="Electrolyte Panel",
        reference_range_standard="22 - 29",
        unit_of_measure="mEq/L",
        panic_low_threshold="10",
        panic_high_threshold="40",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-co2-v5": PathologyBiomarkerRecord(
        code="CMP-CO2-V5",
        name="Bicarbonate / CO2 (Sub-assay Series 5)",
        panel="Electrolyte Panel",
        reference_range_standard="22 - 29",
        unit_of_measure="mEq/L",
        panic_low_threshold="10",
        panic_high_threshold="40",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-bun-v1": PathologyBiomarkerRecord(
        code="CMP-BUN-V1",
        name="Blood Urea Nitrogen (Sub-assay Series 1)",
        panel="Renal Function Panel",
        reference_range_standard="7 - 20",
        unit_of_measure="mg/dL",
        panic_low_threshold="4",
        panic_high_threshold="100",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-bun-v2": PathologyBiomarkerRecord(
        code="CMP-BUN-V2",
        name="Blood Urea Nitrogen (Sub-assay Series 2)",
        panel="Renal Function Panel",
        reference_range_standard="7 - 20",
        unit_of_measure="mg/dL",
        panic_low_threshold="4",
        panic_high_threshold="100",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-bun-v3": PathologyBiomarkerRecord(
        code="CMP-BUN-V3",
        name="Blood Urea Nitrogen (Sub-assay Series 3)",
        panel="Renal Function Panel",
        reference_range_standard="7 - 20",
        unit_of_measure="mg/dL",
        panic_low_threshold="4",
        panic_high_threshold="100",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-bun-v4": PathologyBiomarkerRecord(
        code="CMP-BUN-V4",
        name="Blood Urea Nitrogen (Sub-assay Series 4)",
        panel="Renal Function Panel",
        reference_range_standard="7 - 20",
        unit_of_measure="mg/dL",
        panic_low_threshold="4",
        panic_high_threshold="100",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-bun-v5": PathologyBiomarkerRecord(
        code="CMP-BUN-V5",
        name="Blood Urea Nitrogen (Sub-assay Series 5)",
        panel="Renal Function Panel",
        reference_range_standard="7 - 20",
        unit_of_measure="mg/dL",
        panic_low_threshold="4",
        panic_high_threshold="100",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-creat-v1": PathologyBiomarkerRecord(
        code="CMP-CREAT-V1",
        name="Creatinine, Serum (Sub-assay Series 1)",
        panel="Renal Function Panel",
        reference_range_standard="0.6 - 1.2",
        unit_of_measure="mg/dL",
        panic_low_threshold="0.3",
        panic_high_threshold="10.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-creat-v2": PathologyBiomarkerRecord(
        code="CMP-CREAT-V2",
        name="Creatinine, Serum (Sub-assay Series 2)",
        panel="Renal Function Panel",
        reference_range_standard="0.6 - 1.2",
        unit_of_measure="mg/dL",
        panic_low_threshold="0.3",
        panic_high_threshold="10.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-creat-v3": PathologyBiomarkerRecord(
        code="CMP-CREAT-V3",
        name="Creatinine, Serum (Sub-assay Series 3)",
        panel="Renal Function Panel",
        reference_range_standard="0.6 - 1.2",
        unit_of_measure="mg/dL",
        panic_low_threshold="0.3",
        panic_high_threshold="10.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-creat-v4": PathologyBiomarkerRecord(
        code="CMP-CREAT-V4",
        name="Creatinine, Serum (Sub-assay Series 4)",
        panel="Renal Function Panel",
        reference_range_standard="0.6 - 1.2",
        unit_of_measure="mg/dL",
        panic_low_threshold="0.3",
        panic_high_threshold="10.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-creat-v5": PathologyBiomarkerRecord(
        code="CMP-CREAT-V5",
        name="Creatinine, Serum (Sub-assay Series 5)",
        panel="Renal Function Panel",
        reference_range_standard="0.6 - 1.2",
        unit_of_measure="mg/dL",
        panic_low_threshold="0.3",
        panic_high_threshold="10.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-glu-v1": PathologyBiomarkerRecord(
        code="CMP-GLU-V1",
        name="Glucose, Fasting (Sub-assay Series 1)",
        panel="Metabolic Panel",
        reference_range_standard="70 - 99",
        unit_of_measure="mg/dL",
        panic_low_threshold="40",
        panic_high_threshold="450",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-glu-v2": PathologyBiomarkerRecord(
        code="CMP-GLU-V2",
        name="Glucose, Fasting (Sub-assay Series 2)",
        panel="Metabolic Panel",
        reference_range_standard="70 - 99",
        unit_of_measure="mg/dL",
        panic_low_threshold="40",
        panic_high_threshold="450",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-glu-v3": PathologyBiomarkerRecord(
        code="CMP-GLU-V3",
        name="Glucose, Fasting (Sub-assay Series 3)",
        panel="Metabolic Panel",
        reference_range_standard="70 - 99",
        unit_of_measure="mg/dL",
        panic_low_threshold="40",
        panic_high_threshold="450",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-glu-v4": PathologyBiomarkerRecord(
        code="CMP-GLU-V4",
        name="Glucose, Fasting (Sub-assay Series 4)",
        panel="Metabolic Panel",
        reference_range_standard="70 - 99",
        unit_of_measure="mg/dL",
        panic_low_threshold="40",
        panic_high_threshold="450",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-glu-v5": PathologyBiomarkerRecord(
        code="CMP-GLU-V5",
        name="Glucose, Fasting (Sub-assay Series 5)",
        panel="Metabolic Panel",
        reference_range_standard="70 - 99",
        unit_of_measure="mg/dL",
        panic_low_threshold="40",
        panic_high_threshold="450",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-ca-v1": PathologyBiomarkerRecord(
        code="CMP-CA-V1",
        name="Calcium, Total Serum (Sub-assay Series 1)",
        panel="Metabolic Panel",
        reference_range_standard="8.5 - 10.2",
        unit_of_measure="mg/dL",
        panic_low_threshold="6.5",
        panic_high_threshold="13.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-ca-v2": PathologyBiomarkerRecord(
        code="CMP-CA-V2",
        name="Calcium, Total Serum (Sub-assay Series 2)",
        panel="Metabolic Panel",
        reference_range_standard="8.5 - 10.2",
        unit_of_measure="mg/dL",
        panic_low_threshold="6.5",
        panic_high_threshold="13.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-ca-v3": PathologyBiomarkerRecord(
        code="CMP-CA-V3",
        name="Calcium, Total Serum (Sub-assay Series 3)",
        panel="Metabolic Panel",
        reference_range_standard="8.5 - 10.2",
        unit_of_measure="mg/dL",
        panic_low_threshold="6.5",
        panic_high_threshold="13.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-ca-v4": PathologyBiomarkerRecord(
        code="CMP-CA-V4",
        name="Calcium, Total Serum (Sub-assay Series 4)",
        panel="Metabolic Panel",
        reference_range_standard="8.5 - 10.2",
        unit_of_measure="mg/dL",
        panic_low_threshold="6.5",
        panic_high_threshold="13.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-ca-v5": PathologyBiomarkerRecord(
        code="CMP-CA-V5",
        name="Calcium, Total Serum (Sub-assay Series 5)",
        panel="Metabolic Panel",
        reference_range_standard="8.5 - 10.2",
        unit_of_measure="mg/dL",
        panic_low_threshold="6.5",
        panic_high_threshold="13.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-alb-v1": PathologyBiomarkerRecord(
        code="CMP-ALB-V1",
        name="Albumin, Serum (Sub-assay Series 1)",
        panel="Hepatic Function Panel",
        reference_range_standard="3.5 - 5.0",
        unit_of_measure="g/dL",
        panic_low_threshold="1.5",
        panic_high_threshold="6.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-alb-v2": PathologyBiomarkerRecord(
        code="CMP-ALB-V2",
        name="Albumin, Serum (Sub-assay Series 2)",
        panel="Hepatic Function Panel",
        reference_range_standard="3.5 - 5.0",
        unit_of_measure="g/dL",
        panic_low_threshold="1.5",
        panic_high_threshold="6.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-alb-v3": PathologyBiomarkerRecord(
        code="CMP-ALB-V3",
        name="Albumin, Serum (Sub-assay Series 3)",
        panel="Hepatic Function Panel",
        reference_range_standard="3.5 - 5.0",
        unit_of_measure="g/dL",
        panic_low_threshold="1.5",
        panic_high_threshold="6.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-alb-v4": PathologyBiomarkerRecord(
        code="CMP-ALB-V4",
        name="Albumin, Serum (Sub-assay Series 4)",
        panel="Hepatic Function Panel",
        reference_range_standard="3.5 - 5.0",
        unit_of_measure="g/dL",
        panic_low_threshold="1.5",
        panic_high_threshold="6.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-alb-v5": PathologyBiomarkerRecord(
        code="CMP-ALB-V5",
        name="Albumin, Serum (Sub-assay Series 5)",
        panel="Hepatic Function Panel",
        reference_range_standard="3.5 - 5.0",
        unit_of_measure="g/dL",
        panic_low_threshold="1.5",
        panic_high_threshold="6.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-tp-v1": PathologyBiomarkerRecord(
        code="CMP-TP-V1",
        name="Total Protein (Sub-assay Series 1)",
        panel="Hepatic Function Panel",
        reference_range_standard="6.0 - 8.3",
        unit_of_measure="g/dL",
        panic_low_threshold="4.0",
        panic_high_threshold="10.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-tp-v2": PathologyBiomarkerRecord(
        code="CMP-TP-V2",
        name="Total Protein (Sub-assay Series 2)",
        panel="Hepatic Function Panel",
        reference_range_standard="6.0 - 8.3",
        unit_of_measure="g/dL",
        panic_low_threshold="4.0",
        panic_high_threshold="10.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-tp-v3": PathologyBiomarkerRecord(
        code="CMP-TP-V3",
        name="Total Protein (Sub-assay Series 3)",
        panel="Hepatic Function Panel",
        reference_range_standard="6.0 - 8.3",
        unit_of_measure="g/dL",
        panic_low_threshold="4.0",
        panic_high_threshold="10.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-tp-v4": PathologyBiomarkerRecord(
        code="CMP-TP-V4",
        name="Total Protein (Sub-assay Series 4)",
        panel="Hepatic Function Panel",
        reference_range_standard="6.0 - 8.3",
        unit_of_measure="g/dL",
        panic_low_threshold="4.0",
        panic_high_threshold="10.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-tp-v5": PathologyBiomarkerRecord(
        code="CMP-TP-V5",
        name="Total Protein (Sub-assay Series 5)",
        panel="Hepatic Function Panel",
        reference_range_standard="6.0 - 8.3",
        unit_of_measure="g/dL",
        panic_low_threshold="4.0",
        panic_high_threshold="10.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-ast-v1": PathologyBiomarkerRecord(
        code="CMP-AST-V1",
        name="Aspartate Aminotransferase (Sub-assay Series 1)",
        panel="Hepatic Transaminases",
        reference_range_standard="10 - 40",
        unit_of_measure="U/L",
        panic_low_threshold="5",
        panic_high_threshold="1000",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-ast-v2": PathologyBiomarkerRecord(
        code="CMP-AST-V2",
        name="Aspartate Aminotransferase (Sub-assay Series 2)",
        panel="Hepatic Transaminases",
        reference_range_standard="10 - 40",
        unit_of_measure="U/L",
        panic_low_threshold="5",
        panic_high_threshold="1000",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-ast-v3": PathologyBiomarkerRecord(
        code="CMP-AST-V3",
        name="Aspartate Aminotransferase (Sub-assay Series 3)",
        panel="Hepatic Transaminases",
        reference_range_standard="10 - 40",
        unit_of_measure="U/L",
        panic_low_threshold="5",
        panic_high_threshold="1000",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-ast-v4": PathologyBiomarkerRecord(
        code="CMP-AST-V4",
        name="Aspartate Aminotransferase (Sub-assay Series 4)",
        panel="Hepatic Transaminases",
        reference_range_standard="10 - 40",
        unit_of_measure="U/L",
        panic_low_threshold="5",
        panic_high_threshold="1000",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-ast-v5": PathologyBiomarkerRecord(
        code="CMP-AST-V5",
        name="Aspartate Aminotransferase (Sub-assay Series 5)",
        panel="Hepatic Transaminases",
        reference_range_standard="10 - 40",
        unit_of_measure="U/L",
        panic_low_threshold="5",
        panic_high_threshold="1000",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-alt-v1": PathologyBiomarkerRecord(
        code="CMP-ALT-V1",
        name="Alanine Aminotransferase (Sub-assay Series 1)",
        panel="Hepatic Transaminases",
        reference_range_standard="7 - 56",
        unit_of_measure="U/L",
        panic_low_threshold="5",
        panic_high_threshold="1000",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-alt-v2": PathologyBiomarkerRecord(
        code="CMP-ALT-V2",
        name="Alanine Aminotransferase (Sub-assay Series 2)",
        panel="Hepatic Transaminases",
        reference_range_standard="7 - 56",
        unit_of_measure="U/L",
        panic_low_threshold="5",
        panic_high_threshold="1000",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-alt-v3": PathologyBiomarkerRecord(
        code="CMP-ALT-V3",
        name="Alanine Aminotransferase (Sub-assay Series 3)",
        panel="Hepatic Transaminases",
        reference_range_standard="7 - 56",
        unit_of_measure="U/L",
        panic_low_threshold="5",
        panic_high_threshold="1000",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-alt-v4": PathologyBiomarkerRecord(
        code="CMP-ALT-V4",
        name="Alanine Aminotransferase (Sub-assay Series 4)",
        panel="Hepatic Transaminases",
        reference_range_standard="7 - 56",
        unit_of_measure="U/L",
        panic_low_threshold="5",
        panic_high_threshold="1000",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-alt-v5": PathologyBiomarkerRecord(
        code="CMP-ALT-V5",
        name="Alanine Aminotransferase (Sub-assay Series 5)",
        panel="Hepatic Transaminases",
        reference_range_standard="7 - 56",
        unit_of_measure="U/L",
        panic_low_threshold="5",
        panic_high_threshold="1000",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-alp-v1": PathologyBiomarkerRecord(
        code="CMP-ALP-V1",
        name="Alkaline Phosphatase (Sub-assay Series 1)",
        panel="Hepatic Enzyme",
        reference_range_standard="44 - 147",
        unit_of_measure="U/L",
        panic_low_threshold="20",
        panic_high_threshold="800",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-alp-v2": PathologyBiomarkerRecord(
        code="CMP-ALP-V2",
        name="Alkaline Phosphatase (Sub-assay Series 2)",
        panel="Hepatic Enzyme",
        reference_range_standard="44 - 147",
        unit_of_measure="U/L",
        panic_low_threshold="20",
        panic_high_threshold="800",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-alp-v3": PathologyBiomarkerRecord(
        code="CMP-ALP-V3",
        name="Alkaline Phosphatase (Sub-assay Series 3)",
        panel="Hepatic Enzyme",
        reference_range_standard="44 - 147",
        unit_of_measure="U/L",
        panic_low_threshold="20",
        panic_high_threshold="800",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-alp-v4": PathologyBiomarkerRecord(
        code="CMP-ALP-V4",
        name="Alkaline Phosphatase (Sub-assay Series 4)",
        panel="Hepatic Enzyme",
        reference_range_standard="44 - 147",
        unit_of_measure="U/L",
        panic_low_threshold="20",
        panic_high_threshold="800",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-alp-v5": PathologyBiomarkerRecord(
        code="CMP-ALP-V5",
        name="Alkaline Phosphatase (Sub-assay Series 5)",
        panel="Hepatic Enzyme",
        reference_range_standard="44 - 147",
        unit_of_measure="U/L",
        panic_low_threshold="20",
        panic_high_threshold="800",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-tbil-v1": PathologyBiomarkerRecord(
        code="CMP-TBIL-V1",
        name="Total Bilirubin (Sub-assay Series 1)",
        panel="Hepatic Function Panel",
        reference_range_standard="0.2 - 1.2",
        unit_of_measure="mg/dL",
        panic_low_threshold="0.1",
        panic_high_threshold="15.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-tbil-v2": PathologyBiomarkerRecord(
        code="CMP-TBIL-V2",
        name="Total Bilirubin (Sub-assay Series 2)",
        panel="Hepatic Function Panel",
        reference_range_standard="0.2 - 1.2",
        unit_of_measure="mg/dL",
        panic_low_threshold="0.1",
        panic_high_threshold="15.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-tbil-v3": PathologyBiomarkerRecord(
        code="CMP-TBIL-V3",
        name="Total Bilirubin (Sub-assay Series 3)",
        panel="Hepatic Function Panel",
        reference_range_standard="0.2 - 1.2",
        unit_of_measure="mg/dL",
        panic_low_threshold="0.1",
        panic_high_threshold="15.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-tbil-v4": PathologyBiomarkerRecord(
        code="CMP-TBIL-V4",
        name="Total Bilirubin (Sub-assay Series 4)",
        panel="Hepatic Function Panel",
        reference_range_standard="0.2 - 1.2",
        unit_of_measure="mg/dL",
        panic_low_threshold="0.1",
        panic_high_threshold="15.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "cmp-tbil-v5": PathologyBiomarkerRecord(
        code="CMP-TBIL-V5",
        name="Total Bilirubin (Sub-assay Series 5)",
        panel="Hepatic Function Panel",
        reference_range_standard="0.2 - 1.2",
        unit_of_measure="mg/dL",
        panic_low_threshold="0.1",
        panic_high_threshold="15.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "lip-chol-v1": PathologyBiomarkerRecord(
        code="LIP-CHOL-V1",
        name="Total Cholesterol (Sub-assay Series 1)",
        panel="Lipid Panel",
        reference_range_standard="< 200",
        unit_of_measure="mg/dL",
        panic_low_threshold="80",
        panic_high_threshold="400",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "lip-chol-v2": PathologyBiomarkerRecord(
        code="LIP-CHOL-V2",
        name="Total Cholesterol (Sub-assay Series 2)",
        panel="Lipid Panel",
        reference_range_standard="< 200",
        unit_of_measure="mg/dL",
        panic_low_threshold="80",
        panic_high_threshold="400",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "lip-chol-v3": PathologyBiomarkerRecord(
        code="LIP-CHOL-V3",
        name="Total Cholesterol (Sub-assay Series 3)",
        panel="Lipid Panel",
        reference_range_standard="< 200",
        unit_of_measure="mg/dL",
        panic_low_threshold="80",
        panic_high_threshold="400",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "lip-chol-v4": PathologyBiomarkerRecord(
        code="LIP-CHOL-V4",
        name="Total Cholesterol (Sub-assay Series 4)",
        panel="Lipid Panel",
        reference_range_standard="< 200",
        unit_of_measure="mg/dL",
        panic_low_threshold="80",
        panic_high_threshold="400",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "lip-chol-v5": PathologyBiomarkerRecord(
        code="LIP-CHOL-V5",
        name="Total Cholesterol (Sub-assay Series 5)",
        panel="Lipid Panel",
        reference_range_standard="< 200",
        unit_of_measure="mg/dL",
        panic_low_threshold="80",
        panic_high_threshold="400",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "lip-trig-v1": PathologyBiomarkerRecord(
        code="LIP-TRIG-V1",
        name="Triglycerides (Sub-assay Series 1)",
        panel="Lipid Panel",
        reference_range_standard="< 150",
        unit_of_measure="mg/dL",
        panic_low_threshold="40",
        panic_high_threshold="1000",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "lip-trig-v2": PathologyBiomarkerRecord(
        code="LIP-TRIG-V2",
        name="Triglycerides (Sub-assay Series 2)",
        panel="Lipid Panel",
        reference_range_standard="< 150",
        unit_of_measure="mg/dL",
        panic_low_threshold="40",
        panic_high_threshold="1000",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "lip-trig-v3": PathologyBiomarkerRecord(
        code="LIP-TRIG-V3",
        name="Triglycerides (Sub-assay Series 3)",
        panel="Lipid Panel",
        reference_range_standard="< 150",
        unit_of_measure="mg/dL",
        panic_low_threshold="40",
        panic_high_threshold="1000",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "lip-trig-v4": PathologyBiomarkerRecord(
        code="LIP-TRIG-V4",
        name="Triglycerides (Sub-assay Series 4)",
        panel="Lipid Panel",
        reference_range_standard="< 150",
        unit_of_measure="mg/dL",
        panic_low_threshold="40",
        panic_high_threshold="1000",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "lip-trig-v5": PathologyBiomarkerRecord(
        code="LIP-TRIG-V5",
        name="Triglycerides (Sub-assay Series 5)",
        panel="Lipid Panel",
        reference_range_standard="< 150",
        unit_of_measure="mg/dL",
        panic_low_threshold="40",
        panic_high_threshold="1000",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "lip-hdl-v1": PathologyBiomarkerRecord(
        code="LIP-HDL-V1",
        name="HDL Cholesterol (Sub-assay Series 1)",
        panel="Lipid Panel",
        reference_range_standard="> 40",
        unit_of_measure="mg/dL",
        panic_low_threshold="15",
        panic_high_threshold="120",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "lip-hdl-v2": PathologyBiomarkerRecord(
        code="LIP-HDL-V2",
        name="HDL Cholesterol (Sub-assay Series 2)",
        panel="Lipid Panel",
        reference_range_standard="> 40",
        unit_of_measure="mg/dL",
        panic_low_threshold="15",
        panic_high_threshold="120",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "lip-hdl-v3": PathologyBiomarkerRecord(
        code="LIP-HDL-V3",
        name="HDL Cholesterol (Sub-assay Series 3)",
        panel="Lipid Panel",
        reference_range_standard="> 40",
        unit_of_measure="mg/dL",
        panic_low_threshold="15",
        panic_high_threshold="120",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "lip-hdl-v4": PathologyBiomarkerRecord(
        code="LIP-HDL-V4",
        name="HDL Cholesterol (Sub-assay Series 4)",
        panel="Lipid Panel",
        reference_range_standard="> 40",
        unit_of_measure="mg/dL",
        panic_low_threshold="15",
        panic_high_threshold="120",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "lip-hdl-v5": PathologyBiomarkerRecord(
        code="LIP-HDL-V5",
        name="HDL Cholesterol (Sub-assay Series 5)",
        panel="Lipid Panel",
        reference_range_standard="> 40",
        unit_of_measure="mg/dL",
        panic_low_threshold="15",
        panic_high_threshold="120",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "lip-ldl-v1": PathologyBiomarkerRecord(
        code="LIP-LDL-V1",
        name="LDL Cholesterol, Calculated (Sub-assay Series 1)",
        panel="Lipid Panel",
        reference_range_standard="< 100",
        unit_of_measure="mg/dL",
        panic_low_threshold="30",
        panic_high_threshold="300",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "lip-ldl-v2": PathologyBiomarkerRecord(
        code="LIP-LDL-V2",
        name="LDL Cholesterol, Calculated (Sub-assay Series 2)",
        panel="Lipid Panel",
        reference_range_standard="< 100",
        unit_of_measure="mg/dL",
        panic_low_threshold="30",
        panic_high_threshold="300",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "lip-ldl-v3": PathologyBiomarkerRecord(
        code="LIP-LDL-V3",
        name="LDL Cholesterol, Calculated (Sub-assay Series 3)",
        panel="Lipid Panel",
        reference_range_standard="< 100",
        unit_of_measure="mg/dL",
        panic_low_threshold="30",
        panic_high_threshold="300",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "lip-ldl-v4": PathologyBiomarkerRecord(
        code="LIP-LDL-V4",
        name="LDL Cholesterol, Calculated (Sub-assay Series 4)",
        panel="Lipid Panel",
        reference_range_standard="< 100",
        unit_of_measure="mg/dL",
        panic_low_threshold="30",
        panic_high_threshold="300",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "lip-ldl-v5": PathologyBiomarkerRecord(
        code="LIP-LDL-V5",
        name="LDL Cholesterol, Calculated (Sub-assay Series 5)",
        panel="Lipid Panel",
        reference_range_standard="< 100",
        unit_of_measure="mg/dL",
        panic_low_threshold="30",
        panic_high_threshold="300",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "thy-tsh-v1": PathologyBiomarkerRecord(
        code="THY-TSH-V1",
        name="Thyroid Stimulating Hormone (Sub-assay Series 1)",
        panel="Endocrine Thyroid",
        reference_range_standard="0.45 - 4.5",
        unit_of_measure="uIU/mL",
        panic_low_threshold="0.01",
        panic_high_threshold="50.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "thy-tsh-v2": PathologyBiomarkerRecord(
        code="THY-TSH-V2",
        name="Thyroid Stimulating Hormone (Sub-assay Series 2)",
        panel="Endocrine Thyroid",
        reference_range_standard="0.45 - 4.5",
        unit_of_measure="uIU/mL",
        panic_low_threshold="0.01",
        panic_high_threshold="50.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "thy-tsh-v3": PathologyBiomarkerRecord(
        code="THY-TSH-V3",
        name="Thyroid Stimulating Hormone (Sub-assay Series 3)",
        panel="Endocrine Thyroid",
        reference_range_standard="0.45 - 4.5",
        unit_of_measure="uIU/mL",
        panic_low_threshold="0.01",
        panic_high_threshold="50.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "thy-tsh-v4": PathologyBiomarkerRecord(
        code="THY-TSH-V4",
        name="Thyroid Stimulating Hormone (Sub-assay Series 4)",
        panel="Endocrine Thyroid",
        reference_range_standard="0.45 - 4.5",
        unit_of_measure="uIU/mL",
        panic_low_threshold="0.01",
        panic_high_threshold="50.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "thy-tsh-v5": PathologyBiomarkerRecord(
        code="THY-TSH-V5",
        name="Thyroid Stimulating Hormone (Sub-assay Series 5)",
        panel="Endocrine Thyroid",
        reference_range_standard="0.45 - 4.5",
        unit_of_measure="uIU/mL",
        panic_low_threshold="0.01",
        panic_high_threshold="50.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "thy-ft4-v1": PathologyBiomarkerRecord(
        code="THY-FT4-V1",
        name="Free Thyroxine (FT4) (Sub-assay Series 1)",
        panel="Endocrine Thyroid",
        reference_range_standard="0.8 - 1.8",
        unit_of_measure="ng/dL",
        panic_low_threshold="0.2",
        panic_high_threshold="5.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "thy-ft4-v2": PathologyBiomarkerRecord(
        code="THY-FT4-V2",
        name="Free Thyroxine (FT4) (Sub-assay Series 2)",
        panel="Endocrine Thyroid",
        reference_range_standard="0.8 - 1.8",
        unit_of_measure="ng/dL",
        panic_low_threshold="0.2",
        panic_high_threshold="5.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "thy-ft4-v3": PathologyBiomarkerRecord(
        code="THY-FT4-V3",
        name="Free Thyroxine (FT4) (Sub-assay Series 3)",
        panel="Endocrine Thyroid",
        reference_range_standard="0.8 - 1.8",
        unit_of_measure="ng/dL",
        panic_low_threshold="0.2",
        panic_high_threshold="5.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "thy-ft4-v4": PathologyBiomarkerRecord(
        code="THY-FT4-V4",
        name="Free Thyroxine (FT4) (Sub-assay Series 4)",
        panel="Endocrine Thyroid",
        reference_range_standard="0.8 - 1.8",
        unit_of_measure="ng/dL",
        panic_low_threshold="0.2",
        panic_high_threshold="5.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "thy-ft4-v5": PathologyBiomarkerRecord(
        code="THY-FT4-V5",
        name="Free Thyroxine (FT4) (Sub-assay Series 5)",
        panel="Endocrine Thyroid",
        reference_range_standard="0.8 - 1.8",
        unit_of_measure="ng/dL",
        panic_low_threshold="0.2",
        panic_high_threshold="5.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "thy-ft3-v1": PathologyBiomarkerRecord(
        code="THY-FT3-V1",
        name="Free Triiodothyronine (FT3) (Sub-assay Series 1)",
        panel="Endocrine Thyroid",
        reference_range_standard="2.3 - 4.2",
        unit_of_measure="pg/mL",
        panic_low_threshold="1.0",
        panic_high_threshold="10.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "thy-ft3-v2": PathologyBiomarkerRecord(
        code="THY-FT3-V2",
        name="Free Triiodothyronine (FT3) (Sub-assay Series 2)",
        panel="Endocrine Thyroid",
        reference_range_standard="2.3 - 4.2",
        unit_of_measure="pg/mL",
        panic_low_threshold="1.0",
        panic_high_threshold="10.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "thy-ft3-v3": PathologyBiomarkerRecord(
        code="THY-FT3-V3",
        name="Free Triiodothyronine (FT3) (Sub-assay Series 3)",
        panel="Endocrine Thyroid",
        reference_range_standard="2.3 - 4.2",
        unit_of_measure="pg/mL",
        panic_low_threshold="1.0",
        panic_high_threshold="10.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "thy-ft3-v4": PathologyBiomarkerRecord(
        code="THY-FT3-V4",
        name="Free Triiodothyronine (FT3) (Sub-assay Series 4)",
        panel="Endocrine Thyroid",
        reference_range_standard="2.3 - 4.2",
        unit_of_measure="pg/mL",
        panic_low_threshold="1.0",
        panic_high_threshold="10.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "thy-ft3-v5": PathologyBiomarkerRecord(
        code="THY-FT3-V5",
        name="Free Triiodothyronine (FT3) (Sub-assay Series 5)",
        panel="Endocrine Thyroid",
        reference_range_standard="2.3 - 4.2",
        unit_of_measure="pg/mL",
        panic_low_threshold="1.0",
        panic_high_threshold="10.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "coag-pt-v1": PathologyBiomarkerRecord(
        code="COAG-PT-V1",
        name="Prothrombin Time (Sub-assay Series 1)",
        panel="Coagulation Panel",
        reference_range_standard="11.0 - 13.5",
        unit_of_measure="seconds",
        panic_low_threshold="8.0",
        panic_high_threshold="40.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "coag-pt-v2": PathologyBiomarkerRecord(
        code="COAG-PT-V2",
        name="Prothrombin Time (Sub-assay Series 2)",
        panel="Coagulation Panel",
        reference_range_standard="11.0 - 13.5",
        unit_of_measure="seconds",
        panic_low_threshold="8.0",
        panic_high_threshold="40.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "coag-pt-v3": PathologyBiomarkerRecord(
        code="COAG-PT-V3",
        name="Prothrombin Time (Sub-assay Series 3)",
        panel="Coagulation Panel",
        reference_range_standard="11.0 - 13.5",
        unit_of_measure="seconds",
        panic_low_threshold="8.0",
        panic_high_threshold="40.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "coag-pt-v4": PathologyBiomarkerRecord(
        code="COAG-PT-V4",
        name="Prothrombin Time (Sub-assay Series 4)",
        panel="Coagulation Panel",
        reference_range_standard="11.0 - 13.5",
        unit_of_measure="seconds",
        panic_low_threshold="8.0",
        panic_high_threshold="40.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "coag-pt-v5": PathologyBiomarkerRecord(
        code="COAG-PT-V5",
        name="Prothrombin Time (Sub-assay Series 5)",
        panel="Coagulation Panel",
        reference_range_standard="11.0 - 13.5",
        unit_of_measure="seconds",
        panic_low_threshold="8.0",
        panic_high_threshold="40.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "coag-inr-v1": PathologyBiomarkerRecord(
        code="COAG-INR-V1",
        name="International Normalized Ratio (Sub-assay Series 1)",
        panel="Coagulation Panel",
        reference_range_standard="0.8 - 1.2",
        unit_of_measure="ratio",
        panic_low_threshold="0.5",
        panic_high_threshold="8.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "coag-inr-v2": PathologyBiomarkerRecord(
        code="COAG-INR-V2",
        name="International Normalized Ratio (Sub-assay Series 2)",
        panel="Coagulation Panel",
        reference_range_standard="0.8 - 1.2",
        unit_of_measure="ratio",
        panic_low_threshold="0.5",
        panic_high_threshold="8.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "coag-inr-v3": PathologyBiomarkerRecord(
        code="COAG-INR-V3",
        name="International Normalized Ratio (Sub-assay Series 3)",
        panel="Coagulation Panel",
        reference_range_standard="0.8 - 1.2",
        unit_of_measure="ratio",
        panic_low_threshold="0.5",
        panic_high_threshold="8.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "coag-inr-v4": PathologyBiomarkerRecord(
        code="COAG-INR-V4",
        name="International Normalized Ratio (Sub-assay Series 4)",
        panel="Coagulation Panel",
        reference_range_standard="0.8 - 1.2",
        unit_of_measure="ratio",
        panic_low_threshold="0.5",
        panic_high_threshold="8.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "coag-inr-v5": PathologyBiomarkerRecord(
        code="COAG-INR-V5",
        name="International Normalized Ratio (Sub-assay Series 5)",
        panel="Coagulation Panel",
        reference_range_standard="0.8 - 1.2",
        unit_of_measure="ratio",
        panic_low_threshold="0.5",
        panic_high_threshold="8.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "coag-aptt-v1": PathologyBiomarkerRecord(
        code="COAG-APTT-V1",
        name="Activated Partial Thromboplastin (Sub-assay Series 1)",
        panel="Coagulation Panel",
        reference_range_standard="25 - 35",
        unit_of_measure="seconds",
        panic_low_threshold="15",
        panic_high_threshold="120",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "coag-aptt-v2": PathologyBiomarkerRecord(
        code="COAG-APTT-V2",
        name="Activated Partial Thromboplastin (Sub-assay Series 2)",
        panel="Coagulation Panel",
        reference_range_standard="25 - 35",
        unit_of_measure="seconds",
        panic_low_threshold="15",
        panic_high_threshold="120",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "coag-aptt-v3": PathologyBiomarkerRecord(
        code="COAG-APTT-V3",
        name="Activated Partial Thromboplastin (Sub-assay Series 3)",
        panel="Coagulation Panel",
        reference_range_standard="25 - 35",
        unit_of_measure="seconds",
        panic_low_threshold="15",
        panic_high_threshold="120",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "coag-aptt-v4": PathologyBiomarkerRecord(
        code="COAG-APTT-V4",
        name="Activated Partial Thromboplastin (Sub-assay Series 4)",
        panel="Coagulation Panel",
        reference_range_standard="25 - 35",
        unit_of_measure="seconds",
        panic_low_threshold="15",
        panic_high_threshold="120",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "coag-aptt-v5": PathologyBiomarkerRecord(
        code="COAG-APTT-V5",
        name="Activated Partial Thromboplastin (Sub-assay Series 5)",
        panel="Coagulation Panel",
        reference_range_standard="25 - 35",
        unit_of_measure="seconds",
        panic_low_threshold="15",
        panic_high_threshold="120",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "coag-ddim-v1": PathologyBiomarkerRecord(
        code="COAG-DDIM-V1",
        name="D-Dimer, Quantitative (Sub-assay Series 1)",
        panel="Thrombosis Biomarker",
        reference_range_standard="< 0.50",
        unit_of_measure="ug/mL FEU",
        panic_low_threshold="0.1",
        panic_high_threshold="20.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "coag-ddim-v2": PathologyBiomarkerRecord(
        code="COAG-DDIM-V2",
        name="D-Dimer, Quantitative (Sub-assay Series 2)",
        panel="Thrombosis Biomarker",
        reference_range_standard="< 0.50",
        unit_of_measure="ug/mL FEU",
        panic_low_threshold="0.1",
        panic_high_threshold="20.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "coag-ddim-v3": PathologyBiomarkerRecord(
        code="COAG-DDIM-V3",
        name="D-Dimer, Quantitative (Sub-assay Series 3)",
        panel="Thrombosis Biomarker",
        reference_range_standard="< 0.50",
        unit_of_measure="ug/mL FEU",
        panic_low_threshold="0.1",
        panic_high_threshold="20.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "coag-ddim-v4": PathologyBiomarkerRecord(
        code="COAG-DDIM-V4",
        name="D-Dimer, Quantitative (Sub-assay Series 4)",
        panel="Thrombosis Biomarker",
        reference_range_standard="< 0.50",
        unit_of_measure="ug/mL FEU",
        panic_low_threshold="0.1",
        panic_high_threshold="20.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "coag-ddim-v5": PathologyBiomarkerRecord(
        code="COAG-DDIM-V5",
        name="D-Dimer, Quantitative (Sub-assay Series 5)",
        panel="Thrombosis Biomarker",
        reference_range_standard="< 0.50",
        unit_of_measure="ug/mL FEU",
        panic_low_threshold="0.1",
        panic_high_threshold="20.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "card-trop-v1": PathologyBiomarkerRecord(
        code="CARD-TROP-V1",
        name="High-Sensitivity Troponin I (Sub-assay Series 1)",
        panel="Cardiac Biomarker",
        reference_range_standard="< 14",
        unit_of_measure="ng/L",
        panic_low_threshold="2",
        panic_high_threshold="5000",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "card-trop-v2": PathologyBiomarkerRecord(
        code="CARD-TROP-V2",
        name="High-Sensitivity Troponin I (Sub-assay Series 2)",
        panel="Cardiac Biomarker",
        reference_range_standard="< 14",
        unit_of_measure="ng/L",
        panic_low_threshold="2",
        panic_high_threshold="5000",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "card-trop-v3": PathologyBiomarkerRecord(
        code="CARD-TROP-V3",
        name="High-Sensitivity Troponin I (Sub-assay Series 3)",
        panel="Cardiac Biomarker",
        reference_range_standard="< 14",
        unit_of_measure="ng/L",
        panic_low_threshold="2",
        panic_high_threshold="5000",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "card-trop-v4": PathologyBiomarkerRecord(
        code="CARD-TROP-V4",
        name="High-Sensitivity Troponin I (Sub-assay Series 4)",
        panel="Cardiac Biomarker",
        reference_range_standard="< 14",
        unit_of_measure="ng/L",
        panic_low_threshold="2",
        panic_high_threshold="5000",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "card-trop-v5": PathologyBiomarkerRecord(
        code="CARD-TROP-V5",
        name="High-Sensitivity Troponin I (Sub-assay Series 5)",
        panel="Cardiac Biomarker",
        reference_range_standard="< 14",
        unit_of_measure="ng/L",
        panic_low_threshold="2",
        panic_high_threshold="5000",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "card-bnp-v1": PathologyBiomarkerRecord(
        code="CARD-BNP-V1",
        name="B-Type Natriuretic Peptide (Sub-assay Series 1)",
        panel="Heart Failure Biomarker",
        reference_range_standard="< 100",
        unit_of_measure="pg/mL",
        panic_low_threshold="10",
        panic_high_threshold="4000",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "card-bnp-v2": PathologyBiomarkerRecord(
        code="CARD-BNP-V2",
        name="B-Type Natriuretic Peptide (Sub-assay Series 2)",
        panel="Heart Failure Biomarker",
        reference_range_standard="< 100",
        unit_of_measure="pg/mL",
        panic_low_threshold="10",
        panic_high_threshold="4000",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "card-bnp-v3": PathologyBiomarkerRecord(
        code="CARD-BNP-V3",
        name="B-Type Natriuretic Peptide (Sub-assay Series 3)",
        panel="Heart Failure Biomarker",
        reference_range_standard="< 100",
        unit_of_measure="pg/mL",
        panic_low_threshold="10",
        panic_high_threshold="4000",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "card-bnp-v4": PathologyBiomarkerRecord(
        code="CARD-BNP-V4",
        name="B-Type Natriuretic Peptide (Sub-assay Series 4)",
        panel="Heart Failure Biomarker",
        reference_range_standard="< 100",
        unit_of_measure="pg/mL",
        panic_low_threshold="10",
        panic_high_threshold="4000",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "card-bnp-v5": PathologyBiomarkerRecord(
        code="CARD-BNP-V5",
        name="B-Type Natriuretic Peptide (Sub-assay Series 5)",
        panel="Heart Failure Biomarker",
        reference_range_standard="< 100",
        unit_of_measure="pg/mL",
        panic_low_threshold="10",
        panic_high_threshold="4000",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "infl-crp-v1": PathologyBiomarkerRecord(
        code="INFL-CRP-V1",
        name="C-Reactive Protein, High Sens (Sub-assay Series 1)",
        panel="Inflammatory Biomarker",
        reference_range_standard="< 3.0",
        unit_of_measure="mg/L",
        panic_low_threshold="0.2",
        panic_high_threshold="200.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "infl-crp-v2": PathologyBiomarkerRecord(
        code="INFL-CRP-V2",
        name="C-Reactive Protein, High Sens (Sub-assay Series 2)",
        panel="Inflammatory Biomarker",
        reference_range_standard="< 3.0",
        unit_of_measure="mg/L",
        panic_low_threshold="0.2",
        panic_high_threshold="200.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "infl-crp-v3": PathologyBiomarkerRecord(
        code="INFL-CRP-V3",
        name="C-Reactive Protein, High Sens (Sub-assay Series 3)",
        panel="Inflammatory Biomarker",
        reference_range_standard="< 3.0",
        unit_of_measure="mg/L",
        panic_low_threshold="0.2",
        panic_high_threshold="200.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "infl-crp-v4": PathologyBiomarkerRecord(
        code="INFL-CRP-V4",
        name="C-Reactive Protein, High Sens (Sub-assay Series 4)",
        panel="Inflammatory Biomarker",
        reference_range_standard="< 3.0",
        unit_of_measure="mg/L",
        panic_low_threshold="0.2",
        panic_high_threshold="200.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "infl-crp-v5": PathologyBiomarkerRecord(
        code="INFL-CRP-V5",
        name="C-Reactive Protein, High Sens (Sub-assay Series 5)",
        panel="Inflammatory Biomarker",
        reference_range_standard="< 3.0",
        unit_of_measure="mg/L",
        panic_low_threshold="0.2",
        panic_high_threshold="200.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "infl-esr-v1": PathologyBiomarkerRecord(
        code="INFL-ESR-V1",
        name="Erythrocyte Sedimentation Rate (Sub-assay Series 1)",
        panel="Inflammatory Marker",
        reference_range_standard="0 - 20",
        unit_of_measure="mm/hr",
        panic_low_threshold="0",
        panic_high_threshold="120",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "infl-esr-v2": PathologyBiomarkerRecord(
        code="INFL-ESR-V2",
        name="Erythrocyte Sedimentation Rate (Sub-assay Series 2)",
        panel="Inflammatory Marker",
        reference_range_standard="0 - 20",
        unit_of_measure="mm/hr",
        panic_low_threshold="0",
        panic_high_threshold="120",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "infl-esr-v3": PathologyBiomarkerRecord(
        code="INFL-ESR-V3",
        name="Erythrocyte Sedimentation Rate (Sub-assay Series 3)",
        panel="Inflammatory Marker",
        reference_range_standard="0 - 20",
        unit_of_measure="mm/hr",
        panic_low_threshold="0",
        panic_high_threshold="120",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "infl-esr-v4": PathologyBiomarkerRecord(
        code="INFL-ESR-V4",
        name="Erythrocyte Sedimentation Rate (Sub-assay Series 4)",
        panel="Inflammatory Marker",
        reference_range_standard="0 - 20",
        unit_of_measure="mm/hr",
        panic_low_threshold="0",
        panic_high_threshold="120",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "infl-esr-v5": PathologyBiomarkerRecord(
        code="INFL-ESR-V5",
        name="Erythrocyte Sedimentation Rate (Sub-assay Series 5)",
        panel="Inflammatory Marker",
        reference_range_standard="0 - 20",
        unit_of_measure="mm/hr",
        panic_low_threshold="0",
        panic_high_threshold="120",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "glyc-hba1c-v1": PathologyBiomarkerRecord(
        code="GLYC-HBA1C-V1",
        name="Glycated Hemoglobin (HbA1c) (Sub-assay Series 1)",
        panel="Glycemic Monitoring",
        reference_range_standard="4.0 - 5.6",
        unit_of_measure="%",
        panic_low_threshold="3.0",
        panic_high_threshold="15.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "glyc-hba1c-v2": PathologyBiomarkerRecord(
        code="GLYC-HBA1C-V2",
        name="Glycated Hemoglobin (HbA1c) (Sub-assay Series 2)",
        panel="Glycemic Monitoring",
        reference_range_standard="4.0 - 5.6",
        unit_of_measure="%",
        panic_low_threshold="3.0",
        panic_high_threshold="15.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "glyc-hba1c-v3": PathologyBiomarkerRecord(
        code="GLYC-HBA1C-V3",
        name="Glycated Hemoglobin (HbA1c) (Sub-assay Series 3)",
        panel="Glycemic Monitoring",
        reference_range_standard="4.0 - 5.6",
        unit_of_measure="%",
        panic_low_threshold="3.0",
        panic_high_threshold="15.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "glyc-hba1c-v4": PathologyBiomarkerRecord(
        code="GLYC-HBA1C-V4",
        name="Glycated Hemoglobin (HbA1c) (Sub-assay Series 4)",
        panel="Glycemic Monitoring",
        reference_range_standard="4.0 - 5.6",
        unit_of_measure="%",
        panic_low_threshold="3.0",
        panic_high_threshold="15.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),
    "glyc-hba1c-v5": PathologyBiomarkerRecord(
        code="GLYC-HBA1C-V5",
        name="Glycated Hemoglobin (HbA1c) (Sub-assay Series 5)",
        panel="Glycemic Monitoring",
        reference_range_standard="4.0 - 5.6",
        unit_of_measure="%",
        panic_low_threshold="3.0",
        panic_high_threshold="15.0",
        clinical_significance="Essential diagnostic laboratory biomarker for pathophysiological surveillance.",
        elevated_differential=[
            "Acute tissue injury or primary organ hyperfunction",
            "Systemic inflammatory or metabolic dysregulation",
            "Impaired physiological clearance or hemoconcentration"
        ],
        decreased_differential=[
            "Primary biosynthetic failure or substrate depletion",
            "Hemodilution or excessive physiological excretion",
            "Autoimmune destruction or marrow suppression"
        ],
        specimen_handling_guidelines="Collect in standardized clinical collection tube, centrifuge, and refrigerate."
    ),

}


class PathologyReferenceEngine:
    """Diagnostic inquiry engine for laboratory reference ranges and panic thresholds."""

    @classmethod
    def get_biomarker(cls, code: str) -> Optional[PathologyBiomarkerRecord]:
        return PATHOLOGY_BIOMARKER_REGISTRY.get(code.strip().lower())

    @classmethod
    def search_panel(cls, panel_name: str) -> List[PathologyBiomarkerRecord]:
        p = panel_name.strip().lower()
        return [
            b for b in PATHOLOGY_BIOMARKER_REGISTRY.values()
            if p in b.panel.lower()
        ]

    @classmethod
    def get_total_biomarkers_count(cls) -> int:
        return len(PATHOLOGY_BIOMARKER_REGISTRY)

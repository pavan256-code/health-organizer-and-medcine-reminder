"""
Specialized Respiratory & Pulmonary Critical Care Protocols.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass


@dataclass
class PulmonaryProtocolRecord:
    protocol_code: str
    condition_name: str
    clinical_phenotype: str
    severity_classification: str
    fev1_predicted_range: str
    preferred_biologic_class: str
    inhalation_regimen: str
    exacerbation_escalation_protocol: List[str]
    monitoring_biomarkers: List[str]


PULMONARY_PROTOCOLS_REGISTRY: Dict[str, PulmonaryProtocolRecord] = {

    "pulm-sev-asth-tr01": PulmonaryProtocolRecord(
        protocol_code="PULM-SEV-ASTH-TR01",
        condition_name="Severe Eosinophilic Asthma (Protocol Stratum 1)",
        clinical_phenotype="Eosinophil >= 300 cells/uL",
        severity_classification="GINA Step 5",
        fev1_predicted_range="< 60%",
        preferred_biologic_class="Anti-IL5 (Mepolizumab / Benralizumab)",
        inhalation_regimen="High-dose ICS / LABA + LAMA",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-sev-asth-tr02": PulmonaryProtocolRecord(
        protocol_code="PULM-SEV-ASTH-TR02",
        condition_name="Severe Eosinophilic Asthma (Protocol Stratum 2)",
        clinical_phenotype="Eosinophil >= 300 cells/uL",
        severity_classification="GINA Step 5",
        fev1_predicted_range="< 60%",
        preferred_biologic_class="Anti-IL5 (Mepolizumab / Benralizumab)",
        inhalation_regimen="High-dose ICS / LABA + LAMA",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-sev-asth-tr03": PulmonaryProtocolRecord(
        protocol_code="PULM-SEV-ASTH-TR03",
        condition_name="Severe Eosinophilic Asthma (Protocol Stratum 3)",
        clinical_phenotype="Eosinophil >= 300 cells/uL",
        severity_classification="GINA Step 5",
        fev1_predicted_range="< 60%",
        preferred_biologic_class="Anti-IL5 (Mepolizumab / Benralizumab)",
        inhalation_regimen="High-dose ICS / LABA + LAMA",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-sev-asth-tr04": PulmonaryProtocolRecord(
        protocol_code="PULM-SEV-ASTH-TR04",
        condition_name="Severe Eosinophilic Asthma (Protocol Stratum 4)",
        clinical_phenotype="Eosinophil >= 300 cells/uL",
        severity_classification="GINA Step 5",
        fev1_predicted_range="< 60%",
        preferred_biologic_class="Anti-IL5 (Mepolizumab / Benralizumab)",
        inhalation_regimen="High-dose ICS / LABA + LAMA",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-sev-asth-tr05": PulmonaryProtocolRecord(
        protocol_code="PULM-SEV-ASTH-TR05",
        condition_name="Severe Eosinophilic Asthma (Protocol Stratum 5)",
        clinical_phenotype="Eosinophil >= 300 cells/uL",
        severity_classification="GINA Step 5",
        fev1_predicted_range="< 60%",
        preferred_biologic_class="Anti-IL5 (Mepolizumab / Benralizumab)",
        inhalation_regimen="High-dose ICS / LABA + LAMA",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-sev-asth-tr06": PulmonaryProtocolRecord(
        protocol_code="PULM-SEV-ASTH-TR06",
        condition_name="Severe Eosinophilic Asthma (Protocol Stratum 6)",
        clinical_phenotype="Eosinophil >= 300 cells/uL",
        severity_classification="GINA Step 5",
        fev1_predicted_range="< 60%",
        preferred_biologic_class="Anti-IL5 (Mepolizumab / Benralizumab)",
        inhalation_regimen="High-dose ICS / LABA + LAMA",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-sev-asth-tr07": PulmonaryProtocolRecord(
        protocol_code="PULM-SEV-ASTH-TR07",
        condition_name="Severe Eosinophilic Asthma (Protocol Stratum 7)",
        clinical_phenotype="Eosinophil >= 300 cells/uL",
        severity_classification="GINA Step 5",
        fev1_predicted_range="< 60%",
        preferred_biologic_class="Anti-IL5 (Mepolizumab / Benralizumab)",
        inhalation_regimen="High-dose ICS / LABA + LAMA",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-sev-asth-tr08": PulmonaryProtocolRecord(
        protocol_code="PULM-SEV-ASTH-TR08",
        condition_name="Severe Eosinophilic Asthma (Protocol Stratum 8)",
        clinical_phenotype="Eosinophil >= 300 cells/uL",
        severity_classification="GINA Step 5",
        fev1_predicted_range="< 60%",
        preferred_biologic_class="Anti-IL5 (Mepolizumab / Benralizumab)",
        inhalation_regimen="High-dose ICS / LABA + LAMA",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-sev-asth-tr09": PulmonaryProtocolRecord(
        protocol_code="PULM-SEV-ASTH-TR09",
        condition_name="Severe Eosinophilic Asthma (Protocol Stratum 9)",
        clinical_phenotype="Eosinophil >= 300 cells/uL",
        severity_classification="GINA Step 5",
        fev1_predicted_range="< 60%",
        preferred_biologic_class="Anti-IL5 (Mepolizumab / Benralizumab)",
        inhalation_regimen="High-dose ICS / LABA + LAMA",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-sev-asth-tr10": PulmonaryProtocolRecord(
        protocol_code="PULM-SEV-ASTH-TR10",
        condition_name="Severe Eosinophilic Asthma (Protocol Stratum 10)",
        clinical_phenotype="Eosinophil >= 300 cells/uL",
        severity_classification="GINA Step 5",
        fev1_predicted_range="< 60%",
        preferred_biologic_class="Anti-IL5 (Mepolizumab / Benralizumab)",
        inhalation_regimen="High-dose ICS / LABA + LAMA",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-sev-asth-tr11": PulmonaryProtocolRecord(
        protocol_code="PULM-SEV-ASTH-TR11",
        condition_name="Severe Eosinophilic Asthma (Protocol Stratum 11)",
        clinical_phenotype="Eosinophil >= 300 cells/uL",
        severity_classification="GINA Step 5",
        fev1_predicted_range="< 60%",
        preferred_biologic_class="Anti-IL5 (Mepolizumab / Benralizumab)",
        inhalation_regimen="High-dose ICS / LABA + LAMA",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-sev-asth-tr12": PulmonaryProtocolRecord(
        protocol_code="PULM-SEV-ASTH-TR12",
        condition_name="Severe Eosinophilic Asthma (Protocol Stratum 12)",
        clinical_phenotype="Eosinophil >= 300 cells/uL",
        severity_classification="GINA Step 5",
        fev1_predicted_range="< 60%",
        preferred_biologic_class="Anti-IL5 (Mepolizumab / Benralizumab)",
        inhalation_regimen="High-dose ICS / LABA + LAMA",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-sev-asth-tr13": PulmonaryProtocolRecord(
        protocol_code="PULM-SEV-ASTH-TR13",
        condition_name="Severe Eosinophilic Asthma (Protocol Stratum 13)",
        clinical_phenotype="Eosinophil >= 300 cells/uL",
        severity_classification="GINA Step 5",
        fev1_predicted_range="< 60%",
        preferred_biologic_class="Anti-IL5 (Mepolizumab / Benralizumab)",
        inhalation_regimen="High-dose ICS / LABA + LAMA",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-sev-asth-tr14": PulmonaryProtocolRecord(
        protocol_code="PULM-SEV-ASTH-TR14",
        condition_name="Severe Eosinophilic Asthma (Protocol Stratum 14)",
        clinical_phenotype="Eosinophil >= 300 cells/uL",
        severity_classification="GINA Step 5",
        fev1_predicted_range="< 60%",
        preferred_biologic_class="Anti-IL5 (Mepolizumab / Benralizumab)",
        inhalation_regimen="High-dose ICS / LABA + LAMA",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-all-asth-tr01": PulmonaryProtocolRecord(
        protocol_code="PULM-ALL-ASTH-TR01",
        condition_name="Severe Allergic IgE-Mediated Asthma (Protocol Stratum 1)",
        clinical_phenotype="Serum total IgE 30-1500 IU/mL",
        severity_classification="GINA Step 5",
        fev1_predicted_range="< 65%",
        preferred_biologic_class="Anti-IgE (Omalizumab)",
        inhalation_regimen="High-dose Fluticasone/Salmeterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-all-asth-tr02": PulmonaryProtocolRecord(
        protocol_code="PULM-ALL-ASTH-TR02",
        condition_name="Severe Allergic IgE-Mediated Asthma (Protocol Stratum 2)",
        clinical_phenotype="Serum total IgE 30-1500 IU/mL",
        severity_classification="GINA Step 5",
        fev1_predicted_range="< 65%",
        preferred_biologic_class="Anti-IgE (Omalizumab)",
        inhalation_regimen="High-dose Fluticasone/Salmeterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-all-asth-tr03": PulmonaryProtocolRecord(
        protocol_code="PULM-ALL-ASTH-TR03",
        condition_name="Severe Allergic IgE-Mediated Asthma (Protocol Stratum 3)",
        clinical_phenotype="Serum total IgE 30-1500 IU/mL",
        severity_classification="GINA Step 5",
        fev1_predicted_range="< 65%",
        preferred_biologic_class="Anti-IgE (Omalizumab)",
        inhalation_regimen="High-dose Fluticasone/Salmeterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-all-asth-tr04": PulmonaryProtocolRecord(
        protocol_code="PULM-ALL-ASTH-TR04",
        condition_name="Severe Allergic IgE-Mediated Asthma (Protocol Stratum 4)",
        clinical_phenotype="Serum total IgE 30-1500 IU/mL",
        severity_classification="GINA Step 5",
        fev1_predicted_range="< 65%",
        preferred_biologic_class="Anti-IgE (Omalizumab)",
        inhalation_regimen="High-dose Fluticasone/Salmeterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-all-asth-tr05": PulmonaryProtocolRecord(
        protocol_code="PULM-ALL-ASTH-TR05",
        condition_name="Severe Allergic IgE-Mediated Asthma (Protocol Stratum 5)",
        clinical_phenotype="Serum total IgE 30-1500 IU/mL",
        severity_classification="GINA Step 5",
        fev1_predicted_range="< 65%",
        preferred_biologic_class="Anti-IgE (Omalizumab)",
        inhalation_regimen="High-dose Fluticasone/Salmeterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-all-asth-tr06": PulmonaryProtocolRecord(
        protocol_code="PULM-ALL-ASTH-TR06",
        condition_name="Severe Allergic IgE-Mediated Asthma (Protocol Stratum 6)",
        clinical_phenotype="Serum total IgE 30-1500 IU/mL",
        severity_classification="GINA Step 5",
        fev1_predicted_range="< 65%",
        preferred_biologic_class="Anti-IgE (Omalizumab)",
        inhalation_regimen="High-dose Fluticasone/Salmeterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-all-asth-tr07": PulmonaryProtocolRecord(
        protocol_code="PULM-ALL-ASTH-TR07",
        condition_name="Severe Allergic IgE-Mediated Asthma (Protocol Stratum 7)",
        clinical_phenotype="Serum total IgE 30-1500 IU/mL",
        severity_classification="GINA Step 5",
        fev1_predicted_range="< 65%",
        preferred_biologic_class="Anti-IgE (Omalizumab)",
        inhalation_regimen="High-dose Fluticasone/Salmeterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-all-asth-tr08": PulmonaryProtocolRecord(
        protocol_code="PULM-ALL-ASTH-TR08",
        condition_name="Severe Allergic IgE-Mediated Asthma (Protocol Stratum 8)",
        clinical_phenotype="Serum total IgE 30-1500 IU/mL",
        severity_classification="GINA Step 5",
        fev1_predicted_range="< 65%",
        preferred_biologic_class="Anti-IgE (Omalizumab)",
        inhalation_regimen="High-dose Fluticasone/Salmeterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-all-asth-tr09": PulmonaryProtocolRecord(
        protocol_code="PULM-ALL-ASTH-TR09",
        condition_name="Severe Allergic IgE-Mediated Asthma (Protocol Stratum 9)",
        clinical_phenotype="Serum total IgE 30-1500 IU/mL",
        severity_classification="GINA Step 5",
        fev1_predicted_range="< 65%",
        preferred_biologic_class="Anti-IgE (Omalizumab)",
        inhalation_regimen="High-dose Fluticasone/Salmeterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-all-asth-tr10": PulmonaryProtocolRecord(
        protocol_code="PULM-ALL-ASTH-TR10",
        condition_name="Severe Allergic IgE-Mediated Asthma (Protocol Stratum 10)",
        clinical_phenotype="Serum total IgE 30-1500 IU/mL",
        severity_classification="GINA Step 5",
        fev1_predicted_range="< 65%",
        preferred_biologic_class="Anti-IgE (Omalizumab)",
        inhalation_regimen="High-dose Fluticasone/Salmeterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-all-asth-tr11": PulmonaryProtocolRecord(
        protocol_code="PULM-ALL-ASTH-TR11",
        condition_name="Severe Allergic IgE-Mediated Asthma (Protocol Stratum 11)",
        clinical_phenotype="Serum total IgE 30-1500 IU/mL",
        severity_classification="GINA Step 5",
        fev1_predicted_range="< 65%",
        preferred_biologic_class="Anti-IgE (Omalizumab)",
        inhalation_regimen="High-dose Fluticasone/Salmeterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-all-asth-tr12": PulmonaryProtocolRecord(
        protocol_code="PULM-ALL-ASTH-TR12",
        condition_name="Severe Allergic IgE-Mediated Asthma (Protocol Stratum 12)",
        clinical_phenotype="Serum total IgE 30-1500 IU/mL",
        severity_classification="GINA Step 5",
        fev1_predicted_range="< 65%",
        preferred_biologic_class="Anti-IgE (Omalizumab)",
        inhalation_regimen="High-dose Fluticasone/Salmeterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-all-asth-tr13": PulmonaryProtocolRecord(
        protocol_code="PULM-ALL-ASTH-TR13",
        condition_name="Severe Allergic IgE-Mediated Asthma (Protocol Stratum 13)",
        clinical_phenotype="Serum total IgE 30-1500 IU/mL",
        severity_classification="GINA Step 5",
        fev1_predicted_range="< 65%",
        preferred_biologic_class="Anti-IgE (Omalizumab)",
        inhalation_regimen="High-dose Fluticasone/Salmeterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-all-asth-tr14": PulmonaryProtocolRecord(
        protocol_code="PULM-ALL-ASTH-TR14",
        condition_name="Severe Allergic IgE-Mediated Asthma (Protocol Stratum 14)",
        clinical_phenotype="Serum total IgE 30-1500 IU/mL",
        severity_classification="GINA Step 5",
        fev1_predicted_range="< 65%",
        preferred_biologic_class="Anti-IgE (Omalizumab)",
        inhalation_regimen="High-dose Fluticasone/Salmeterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-type2-asth-tr01": PulmonaryProtocolRecord(
        protocol_code="PULM-TYPE2-ASTH-TR01",
        condition_name="Type 2 Inflammatory Asthma (Protocol Stratum 1)",
        clinical_phenotype="FeNO >= 50 ppb or Eos >= 150",
        severity_classification="GINA Step 4-5",
        fev1_predicted_range="< 70%",
        preferred_biologic_class="Anti-IL4R-alpha (Dupilumab)",
        inhalation_regimen="High-dose Budesonide/Formoterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-type2-asth-tr02": PulmonaryProtocolRecord(
        protocol_code="PULM-TYPE2-ASTH-TR02",
        condition_name="Type 2 Inflammatory Asthma (Protocol Stratum 2)",
        clinical_phenotype="FeNO >= 50 ppb or Eos >= 150",
        severity_classification="GINA Step 4-5",
        fev1_predicted_range="< 70%",
        preferred_biologic_class="Anti-IL4R-alpha (Dupilumab)",
        inhalation_regimen="High-dose Budesonide/Formoterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-type2-asth-tr03": PulmonaryProtocolRecord(
        protocol_code="PULM-TYPE2-ASTH-TR03",
        condition_name="Type 2 Inflammatory Asthma (Protocol Stratum 3)",
        clinical_phenotype="FeNO >= 50 ppb or Eos >= 150",
        severity_classification="GINA Step 4-5",
        fev1_predicted_range="< 70%",
        preferred_biologic_class="Anti-IL4R-alpha (Dupilumab)",
        inhalation_regimen="High-dose Budesonide/Formoterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-type2-asth-tr04": PulmonaryProtocolRecord(
        protocol_code="PULM-TYPE2-ASTH-TR04",
        condition_name="Type 2 Inflammatory Asthma (Protocol Stratum 4)",
        clinical_phenotype="FeNO >= 50 ppb or Eos >= 150",
        severity_classification="GINA Step 4-5",
        fev1_predicted_range="< 70%",
        preferred_biologic_class="Anti-IL4R-alpha (Dupilumab)",
        inhalation_regimen="High-dose Budesonide/Formoterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-type2-asth-tr05": PulmonaryProtocolRecord(
        protocol_code="PULM-TYPE2-ASTH-TR05",
        condition_name="Type 2 Inflammatory Asthma (Protocol Stratum 5)",
        clinical_phenotype="FeNO >= 50 ppb or Eos >= 150",
        severity_classification="GINA Step 4-5",
        fev1_predicted_range="< 70%",
        preferred_biologic_class="Anti-IL4R-alpha (Dupilumab)",
        inhalation_regimen="High-dose Budesonide/Formoterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-type2-asth-tr06": PulmonaryProtocolRecord(
        protocol_code="PULM-TYPE2-ASTH-TR06",
        condition_name="Type 2 Inflammatory Asthma (Protocol Stratum 6)",
        clinical_phenotype="FeNO >= 50 ppb or Eos >= 150",
        severity_classification="GINA Step 4-5",
        fev1_predicted_range="< 70%",
        preferred_biologic_class="Anti-IL4R-alpha (Dupilumab)",
        inhalation_regimen="High-dose Budesonide/Formoterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-type2-asth-tr07": PulmonaryProtocolRecord(
        protocol_code="PULM-TYPE2-ASTH-TR07",
        condition_name="Type 2 Inflammatory Asthma (Protocol Stratum 7)",
        clinical_phenotype="FeNO >= 50 ppb or Eos >= 150",
        severity_classification="GINA Step 4-5",
        fev1_predicted_range="< 70%",
        preferred_biologic_class="Anti-IL4R-alpha (Dupilumab)",
        inhalation_regimen="High-dose Budesonide/Formoterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-type2-asth-tr08": PulmonaryProtocolRecord(
        protocol_code="PULM-TYPE2-ASTH-TR08",
        condition_name="Type 2 Inflammatory Asthma (Protocol Stratum 8)",
        clinical_phenotype="FeNO >= 50 ppb or Eos >= 150",
        severity_classification="GINA Step 4-5",
        fev1_predicted_range="< 70%",
        preferred_biologic_class="Anti-IL4R-alpha (Dupilumab)",
        inhalation_regimen="High-dose Budesonide/Formoterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-type2-asth-tr09": PulmonaryProtocolRecord(
        protocol_code="PULM-TYPE2-ASTH-TR09",
        condition_name="Type 2 Inflammatory Asthma (Protocol Stratum 9)",
        clinical_phenotype="FeNO >= 50 ppb or Eos >= 150",
        severity_classification="GINA Step 4-5",
        fev1_predicted_range="< 70%",
        preferred_biologic_class="Anti-IL4R-alpha (Dupilumab)",
        inhalation_regimen="High-dose Budesonide/Formoterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-type2-asth-tr10": PulmonaryProtocolRecord(
        protocol_code="PULM-TYPE2-ASTH-TR10",
        condition_name="Type 2 Inflammatory Asthma (Protocol Stratum 10)",
        clinical_phenotype="FeNO >= 50 ppb or Eos >= 150",
        severity_classification="GINA Step 4-5",
        fev1_predicted_range="< 70%",
        preferred_biologic_class="Anti-IL4R-alpha (Dupilumab)",
        inhalation_regimen="High-dose Budesonide/Formoterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-type2-asth-tr11": PulmonaryProtocolRecord(
        protocol_code="PULM-TYPE2-ASTH-TR11",
        condition_name="Type 2 Inflammatory Asthma (Protocol Stratum 11)",
        clinical_phenotype="FeNO >= 50 ppb or Eos >= 150",
        severity_classification="GINA Step 4-5",
        fev1_predicted_range="< 70%",
        preferred_biologic_class="Anti-IL4R-alpha (Dupilumab)",
        inhalation_regimen="High-dose Budesonide/Formoterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-type2-asth-tr12": PulmonaryProtocolRecord(
        protocol_code="PULM-TYPE2-ASTH-TR12",
        condition_name="Type 2 Inflammatory Asthma (Protocol Stratum 12)",
        clinical_phenotype="FeNO >= 50 ppb or Eos >= 150",
        severity_classification="GINA Step 4-5",
        fev1_predicted_range="< 70%",
        preferred_biologic_class="Anti-IL4R-alpha (Dupilumab)",
        inhalation_regimen="High-dose Budesonide/Formoterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-type2-asth-tr13": PulmonaryProtocolRecord(
        protocol_code="PULM-TYPE2-ASTH-TR13",
        condition_name="Type 2 Inflammatory Asthma (Protocol Stratum 13)",
        clinical_phenotype="FeNO >= 50 ppb or Eos >= 150",
        severity_classification="GINA Step 4-5",
        fev1_predicted_range="< 70%",
        preferred_biologic_class="Anti-IL4R-alpha (Dupilumab)",
        inhalation_regimen="High-dose Budesonide/Formoterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-type2-asth-tr14": PulmonaryProtocolRecord(
        protocol_code="PULM-TYPE2-ASTH-TR14",
        condition_name="Type 2 Inflammatory Asthma (Protocol Stratum 14)",
        clinical_phenotype="FeNO >= 50 ppb or Eos >= 150",
        severity_classification="GINA Step 4-5",
        fev1_predicted_range="< 70%",
        preferred_biologic_class="Anti-IL4R-alpha (Dupilumab)",
        inhalation_regimen="High-dose Budesonide/Formoterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-copd-gold4-tr01": PulmonaryProtocolRecord(
        protocol_code="PULM-COPD-GOLD4-TR01",
        condition_name="Very Severe COPD (GOLD Stage 4) (Protocol Stratum 1)",
        clinical_phenotype="Airflow limitation with chronic hypercapnia",
        severity_classification="GOLD Group E",
        fev1_predicted_range="< 30%",
        preferred_biologic_class="Inhaled Triple Therapy (ICS/LABA/LAMA)",
        inhalation_regimen="Fluticasone/Umeclidinium/Vilanterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-copd-gold4-tr02": PulmonaryProtocolRecord(
        protocol_code="PULM-COPD-GOLD4-TR02",
        condition_name="Very Severe COPD (GOLD Stage 4) (Protocol Stratum 2)",
        clinical_phenotype="Airflow limitation with chronic hypercapnia",
        severity_classification="GOLD Group E",
        fev1_predicted_range="< 30%",
        preferred_biologic_class="Inhaled Triple Therapy (ICS/LABA/LAMA)",
        inhalation_regimen="Fluticasone/Umeclidinium/Vilanterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-copd-gold4-tr03": PulmonaryProtocolRecord(
        protocol_code="PULM-COPD-GOLD4-TR03",
        condition_name="Very Severe COPD (GOLD Stage 4) (Protocol Stratum 3)",
        clinical_phenotype="Airflow limitation with chronic hypercapnia",
        severity_classification="GOLD Group E",
        fev1_predicted_range="< 30%",
        preferred_biologic_class="Inhaled Triple Therapy (ICS/LABA/LAMA)",
        inhalation_regimen="Fluticasone/Umeclidinium/Vilanterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-copd-gold4-tr04": PulmonaryProtocolRecord(
        protocol_code="PULM-COPD-GOLD4-TR04",
        condition_name="Very Severe COPD (GOLD Stage 4) (Protocol Stratum 4)",
        clinical_phenotype="Airflow limitation with chronic hypercapnia",
        severity_classification="GOLD Group E",
        fev1_predicted_range="< 30%",
        preferred_biologic_class="Inhaled Triple Therapy (ICS/LABA/LAMA)",
        inhalation_regimen="Fluticasone/Umeclidinium/Vilanterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-copd-gold4-tr05": PulmonaryProtocolRecord(
        protocol_code="PULM-COPD-GOLD4-TR05",
        condition_name="Very Severe COPD (GOLD Stage 4) (Protocol Stratum 5)",
        clinical_phenotype="Airflow limitation with chronic hypercapnia",
        severity_classification="GOLD Group E",
        fev1_predicted_range="< 30%",
        preferred_biologic_class="Inhaled Triple Therapy (ICS/LABA/LAMA)",
        inhalation_regimen="Fluticasone/Umeclidinium/Vilanterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-copd-gold4-tr06": PulmonaryProtocolRecord(
        protocol_code="PULM-COPD-GOLD4-TR06",
        condition_name="Very Severe COPD (GOLD Stage 4) (Protocol Stratum 6)",
        clinical_phenotype="Airflow limitation with chronic hypercapnia",
        severity_classification="GOLD Group E",
        fev1_predicted_range="< 30%",
        preferred_biologic_class="Inhaled Triple Therapy (ICS/LABA/LAMA)",
        inhalation_regimen="Fluticasone/Umeclidinium/Vilanterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-copd-gold4-tr07": PulmonaryProtocolRecord(
        protocol_code="PULM-COPD-GOLD4-TR07",
        condition_name="Very Severe COPD (GOLD Stage 4) (Protocol Stratum 7)",
        clinical_phenotype="Airflow limitation with chronic hypercapnia",
        severity_classification="GOLD Group E",
        fev1_predicted_range="< 30%",
        preferred_biologic_class="Inhaled Triple Therapy (ICS/LABA/LAMA)",
        inhalation_regimen="Fluticasone/Umeclidinium/Vilanterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-copd-gold4-tr08": PulmonaryProtocolRecord(
        protocol_code="PULM-COPD-GOLD4-TR08",
        condition_name="Very Severe COPD (GOLD Stage 4) (Protocol Stratum 8)",
        clinical_phenotype="Airflow limitation with chronic hypercapnia",
        severity_classification="GOLD Group E",
        fev1_predicted_range="< 30%",
        preferred_biologic_class="Inhaled Triple Therapy (ICS/LABA/LAMA)",
        inhalation_regimen="Fluticasone/Umeclidinium/Vilanterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-copd-gold4-tr09": PulmonaryProtocolRecord(
        protocol_code="PULM-COPD-GOLD4-TR09",
        condition_name="Very Severe COPD (GOLD Stage 4) (Protocol Stratum 9)",
        clinical_phenotype="Airflow limitation with chronic hypercapnia",
        severity_classification="GOLD Group E",
        fev1_predicted_range="< 30%",
        preferred_biologic_class="Inhaled Triple Therapy (ICS/LABA/LAMA)",
        inhalation_regimen="Fluticasone/Umeclidinium/Vilanterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-copd-gold4-tr10": PulmonaryProtocolRecord(
        protocol_code="PULM-COPD-GOLD4-TR10",
        condition_name="Very Severe COPD (GOLD Stage 4) (Protocol Stratum 10)",
        clinical_phenotype="Airflow limitation with chronic hypercapnia",
        severity_classification="GOLD Group E",
        fev1_predicted_range="< 30%",
        preferred_biologic_class="Inhaled Triple Therapy (ICS/LABA/LAMA)",
        inhalation_regimen="Fluticasone/Umeclidinium/Vilanterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-copd-gold4-tr11": PulmonaryProtocolRecord(
        protocol_code="PULM-COPD-GOLD4-TR11",
        condition_name="Very Severe COPD (GOLD Stage 4) (Protocol Stratum 11)",
        clinical_phenotype="Airflow limitation with chronic hypercapnia",
        severity_classification="GOLD Group E",
        fev1_predicted_range="< 30%",
        preferred_biologic_class="Inhaled Triple Therapy (ICS/LABA/LAMA)",
        inhalation_regimen="Fluticasone/Umeclidinium/Vilanterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-copd-gold4-tr12": PulmonaryProtocolRecord(
        protocol_code="PULM-COPD-GOLD4-TR12",
        condition_name="Very Severe COPD (GOLD Stage 4) (Protocol Stratum 12)",
        clinical_phenotype="Airflow limitation with chronic hypercapnia",
        severity_classification="GOLD Group E",
        fev1_predicted_range="< 30%",
        preferred_biologic_class="Inhaled Triple Therapy (ICS/LABA/LAMA)",
        inhalation_regimen="Fluticasone/Umeclidinium/Vilanterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-copd-gold4-tr13": PulmonaryProtocolRecord(
        protocol_code="PULM-COPD-GOLD4-TR13",
        condition_name="Very Severe COPD (GOLD Stage 4) (Protocol Stratum 13)",
        clinical_phenotype="Airflow limitation with chronic hypercapnia",
        severity_classification="GOLD Group E",
        fev1_predicted_range="< 30%",
        preferred_biologic_class="Inhaled Triple Therapy (ICS/LABA/LAMA)",
        inhalation_regimen="Fluticasone/Umeclidinium/Vilanterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-copd-gold4-tr14": PulmonaryProtocolRecord(
        protocol_code="PULM-COPD-GOLD4-TR14",
        condition_name="Very Severe COPD (GOLD Stage 4) (Protocol Stratum 14)",
        clinical_phenotype="Airflow limitation with chronic hypercapnia",
        severity_classification="GOLD Group E",
        fev1_predicted_range="< 30%",
        preferred_biologic_class="Inhaled Triple Therapy (ICS/LABA/LAMA)",
        inhalation_regimen="Fluticasone/Umeclidinium/Vilanterol",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-copd-gold3-tr01": PulmonaryProtocolRecord(
        protocol_code="PULM-COPD-GOLD3-TR01",
        condition_name="Severe COPD (GOLD Stage 3) (Protocol Stratum 1)",
        clinical_phenotype="Frequent exacerbator phenotype",
        severity_classification="GOLD Group E",
        fev1_predicted_range="30 - 49%",
        preferred_biologic_class="LABA + LAMA Dual Bronchodilation",
        inhalation_regimen="Tiotropium / Olodaterol Respimat",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-copd-gold3-tr02": PulmonaryProtocolRecord(
        protocol_code="PULM-COPD-GOLD3-TR02",
        condition_name="Severe COPD (GOLD Stage 3) (Protocol Stratum 2)",
        clinical_phenotype="Frequent exacerbator phenotype",
        severity_classification="GOLD Group E",
        fev1_predicted_range="30 - 49%",
        preferred_biologic_class="LABA + LAMA Dual Bronchodilation",
        inhalation_regimen="Tiotropium / Olodaterol Respimat",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-copd-gold3-tr03": PulmonaryProtocolRecord(
        protocol_code="PULM-COPD-GOLD3-TR03",
        condition_name="Severe COPD (GOLD Stage 3) (Protocol Stratum 3)",
        clinical_phenotype="Frequent exacerbator phenotype",
        severity_classification="GOLD Group E",
        fev1_predicted_range="30 - 49%",
        preferred_biologic_class="LABA + LAMA Dual Bronchodilation",
        inhalation_regimen="Tiotropium / Olodaterol Respimat",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-copd-gold3-tr04": PulmonaryProtocolRecord(
        protocol_code="PULM-COPD-GOLD3-TR04",
        condition_name="Severe COPD (GOLD Stage 3) (Protocol Stratum 4)",
        clinical_phenotype="Frequent exacerbator phenotype",
        severity_classification="GOLD Group E",
        fev1_predicted_range="30 - 49%",
        preferred_biologic_class="LABA + LAMA Dual Bronchodilation",
        inhalation_regimen="Tiotropium / Olodaterol Respimat",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-copd-gold3-tr05": PulmonaryProtocolRecord(
        protocol_code="PULM-COPD-GOLD3-TR05",
        condition_name="Severe COPD (GOLD Stage 3) (Protocol Stratum 5)",
        clinical_phenotype="Frequent exacerbator phenotype",
        severity_classification="GOLD Group E",
        fev1_predicted_range="30 - 49%",
        preferred_biologic_class="LABA + LAMA Dual Bronchodilation",
        inhalation_regimen="Tiotropium / Olodaterol Respimat",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-copd-gold3-tr06": PulmonaryProtocolRecord(
        protocol_code="PULM-COPD-GOLD3-TR06",
        condition_name="Severe COPD (GOLD Stage 3) (Protocol Stratum 6)",
        clinical_phenotype="Frequent exacerbator phenotype",
        severity_classification="GOLD Group E",
        fev1_predicted_range="30 - 49%",
        preferred_biologic_class="LABA + LAMA Dual Bronchodilation",
        inhalation_regimen="Tiotropium / Olodaterol Respimat",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-copd-gold3-tr07": PulmonaryProtocolRecord(
        protocol_code="PULM-COPD-GOLD3-TR07",
        condition_name="Severe COPD (GOLD Stage 3) (Protocol Stratum 7)",
        clinical_phenotype="Frequent exacerbator phenotype",
        severity_classification="GOLD Group E",
        fev1_predicted_range="30 - 49%",
        preferred_biologic_class="LABA + LAMA Dual Bronchodilation",
        inhalation_regimen="Tiotropium / Olodaterol Respimat",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-copd-gold3-tr08": PulmonaryProtocolRecord(
        protocol_code="PULM-COPD-GOLD3-TR08",
        condition_name="Severe COPD (GOLD Stage 3) (Protocol Stratum 8)",
        clinical_phenotype="Frequent exacerbator phenotype",
        severity_classification="GOLD Group E",
        fev1_predicted_range="30 - 49%",
        preferred_biologic_class="LABA + LAMA Dual Bronchodilation",
        inhalation_regimen="Tiotropium / Olodaterol Respimat",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-copd-gold3-tr09": PulmonaryProtocolRecord(
        protocol_code="PULM-COPD-GOLD3-TR09",
        condition_name="Severe COPD (GOLD Stage 3) (Protocol Stratum 9)",
        clinical_phenotype="Frequent exacerbator phenotype",
        severity_classification="GOLD Group E",
        fev1_predicted_range="30 - 49%",
        preferred_biologic_class="LABA + LAMA Dual Bronchodilation",
        inhalation_regimen="Tiotropium / Olodaterol Respimat",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-copd-gold3-tr10": PulmonaryProtocolRecord(
        protocol_code="PULM-COPD-GOLD3-TR10",
        condition_name="Severe COPD (GOLD Stage 3) (Protocol Stratum 10)",
        clinical_phenotype="Frequent exacerbator phenotype",
        severity_classification="GOLD Group E",
        fev1_predicted_range="30 - 49%",
        preferred_biologic_class="LABA + LAMA Dual Bronchodilation",
        inhalation_regimen="Tiotropium / Olodaterol Respimat",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-copd-gold3-tr11": PulmonaryProtocolRecord(
        protocol_code="PULM-COPD-GOLD3-TR11",
        condition_name="Severe COPD (GOLD Stage 3) (Protocol Stratum 11)",
        clinical_phenotype="Frequent exacerbator phenotype",
        severity_classification="GOLD Group E",
        fev1_predicted_range="30 - 49%",
        preferred_biologic_class="LABA + LAMA Dual Bronchodilation",
        inhalation_regimen="Tiotropium / Olodaterol Respimat",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-copd-gold3-tr12": PulmonaryProtocolRecord(
        protocol_code="PULM-COPD-GOLD3-TR12",
        condition_name="Severe COPD (GOLD Stage 3) (Protocol Stratum 12)",
        clinical_phenotype="Frequent exacerbator phenotype",
        severity_classification="GOLD Group E",
        fev1_predicted_range="30 - 49%",
        preferred_biologic_class="LABA + LAMA Dual Bronchodilation",
        inhalation_regimen="Tiotropium / Olodaterol Respimat",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-copd-gold3-tr13": PulmonaryProtocolRecord(
        protocol_code="PULM-COPD-GOLD3-TR13",
        condition_name="Severe COPD (GOLD Stage 3) (Protocol Stratum 13)",
        clinical_phenotype="Frequent exacerbator phenotype",
        severity_classification="GOLD Group E",
        fev1_predicted_range="30 - 49%",
        preferred_biologic_class="LABA + LAMA Dual Bronchodilation",
        inhalation_regimen="Tiotropium / Olodaterol Respimat",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-copd-gold3-tr14": PulmonaryProtocolRecord(
        protocol_code="PULM-COPD-GOLD3-TR14",
        condition_name="Severe COPD (GOLD Stage 3) (Protocol Stratum 14)",
        clinical_phenotype="Frequent exacerbator phenotype",
        severity_classification="GOLD Group E",
        fev1_predicted_range="30 - 49%",
        preferred_biologic_class="LABA + LAMA Dual Bronchodilation",
        inhalation_regimen="Tiotropium / Olodaterol Respimat",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-ipf-tr01": PulmonaryProtocolRecord(
        protocol_code="PULM-IPF-TR01",
        condition_name="Idiopathic Pulmonary Fibrosis (Protocol Stratum 1)",
        clinical_phenotype="Usual interstitial pneumonia pattern on HRCT",
        severity_classification="Severe Fibrotic",
        fev1_predicted_range="40 - 65%",
        preferred_biologic_class="Antifibrotic (Nintedanib / Pirfenidone)",
        inhalation_regimen="Supplemental oxygen and pulmonary rehab",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-ipf-tr02": PulmonaryProtocolRecord(
        protocol_code="PULM-IPF-TR02",
        condition_name="Idiopathic Pulmonary Fibrosis (Protocol Stratum 2)",
        clinical_phenotype="Usual interstitial pneumonia pattern on HRCT",
        severity_classification="Severe Fibrotic",
        fev1_predicted_range="40 - 65%",
        preferred_biologic_class="Antifibrotic (Nintedanib / Pirfenidone)",
        inhalation_regimen="Supplemental oxygen and pulmonary rehab",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-ipf-tr03": PulmonaryProtocolRecord(
        protocol_code="PULM-IPF-TR03",
        condition_name="Idiopathic Pulmonary Fibrosis (Protocol Stratum 3)",
        clinical_phenotype="Usual interstitial pneumonia pattern on HRCT",
        severity_classification="Severe Fibrotic",
        fev1_predicted_range="40 - 65%",
        preferred_biologic_class="Antifibrotic (Nintedanib / Pirfenidone)",
        inhalation_regimen="Supplemental oxygen and pulmonary rehab",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-ipf-tr04": PulmonaryProtocolRecord(
        protocol_code="PULM-IPF-TR04",
        condition_name="Idiopathic Pulmonary Fibrosis (Protocol Stratum 4)",
        clinical_phenotype="Usual interstitial pneumonia pattern on HRCT",
        severity_classification="Severe Fibrotic",
        fev1_predicted_range="40 - 65%",
        preferred_biologic_class="Antifibrotic (Nintedanib / Pirfenidone)",
        inhalation_regimen="Supplemental oxygen and pulmonary rehab",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-ipf-tr05": PulmonaryProtocolRecord(
        protocol_code="PULM-IPF-TR05",
        condition_name="Idiopathic Pulmonary Fibrosis (Protocol Stratum 5)",
        clinical_phenotype="Usual interstitial pneumonia pattern on HRCT",
        severity_classification="Severe Fibrotic",
        fev1_predicted_range="40 - 65%",
        preferred_biologic_class="Antifibrotic (Nintedanib / Pirfenidone)",
        inhalation_regimen="Supplemental oxygen and pulmonary rehab",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-ipf-tr06": PulmonaryProtocolRecord(
        protocol_code="PULM-IPF-TR06",
        condition_name="Idiopathic Pulmonary Fibrosis (Protocol Stratum 6)",
        clinical_phenotype="Usual interstitial pneumonia pattern on HRCT",
        severity_classification="Severe Fibrotic",
        fev1_predicted_range="40 - 65%",
        preferred_biologic_class="Antifibrotic (Nintedanib / Pirfenidone)",
        inhalation_regimen="Supplemental oxygen and pulmonary rehab",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-ipf-tr07": PulmonaryProtocolRecord(
        protocol_code="PULM-IPF-TR07",
        condition_name="Idiopathic Pulmonary Fibrosis (Protocol Stratum 7)",
        clinical_phenotype="Usual interstitial pneumonia pattern on HRCT",
        severity_classification="Severe Fibrotic",
        fev1_predicted_range="40 - 65%",
        preferred_biologic_class="Antifibrotic (Nintedanib / Pirfenidone)",
        inhalation_regimen="Supplemental oxygen and pulmonary rehab",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-ipf-tr08": PulmonaryProtocolRecord(
        protocol_code="PULM-IPF-TR08",
        condition_name="Idiopathic Pulmonary Fibrosis (Protocol Stratum 8)",
        clinical_phenotype="Usual interstitial pneumonia pattern on HRCT",
        severity_classification="Severe Fibrotic",
        fev1_predicted_range="40 - 65%",
        preferred_biologic_class="Antifibrotic (Nintedanib / Pirfenidone)",
        inhalation_regimen="Supplemental oxygen and pulmonary rehab",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-ipf-tr09": PulmonaryProtocolRecord(
        protocol_code="PULM-IPF-TR09",
        condition_name="Idiopathic Pulmonary Fibrosis (Protocol Stratum 9)",
        clinical_phenotype="Usual interstitial pneumonia pattern on HRCT",
        severity_classification="Severe Fibrotic",
        fev1_predicted_range="40 - 65%",
        preferred_biologic_class="Antifibrotic (Nintedanib / Pirfenidone)",
        inhalation_regimen="Supplemental oxygen and pulmonary rehab",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-ipf-tr10": PulmonaryProtocolRecord(
        protocol_code="PULM-IPF-TR10",
        condition_name="Idiopathic Pulmonary Fibrosis (Protocol Stratum 10)",
        clinical_phenotype="Usual interstitial pneumonia pattern on HRCT",
        severity_classification="Severe Fibrotic",
        fev1_predicted_range="40 - 65%",
        preferred_biologic_class="Antifibrotic (Nintedanib / Pirfenidone)",
        inhalation_regimen="Supplemental oxygen and pulmonary rehab",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-ipf-tr11": PulmonaryProtocolRecord(
        protocol_code="PULM-IPF-TR11",
        condition_name="Idiopathic Pulmonary Fibrosis (Protocol Stratum 11)",
        clinical_phenotype="Usual interstitial pneumonia pattern on HRCT",
        severity_classification="Severe Fibrotic",
        fev1_predicted_range="40 - 65%",
        preferred_biologic_class="Antifibrotic (Nintedanib / Pirfenidone)",
        inhalation_regimen="Supplemental oxygen and pulmonary rehab",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-ipf-tr12": PulmonaryProtocolRecord(
        protocol_code="PULM-IPF-TR12",
        condition_name="Idiopathic Pulmonary Fibrosis (Protocol Stratum 12)",
        clinical_phenotype="Usual interstitial pneumonia pattern on HRCT",
        severity_classification="Severe Fibrotic",
        fev1_predicted_range="40 - 65%",
        preferred_biologic_class="Antifibrotic (Nintedanib / Pirfenidone)",
        inhalation_regimen="Supplemental oxygen and pulmonary rehab",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-ipf-tr13": PulmonaryProtocolRecord(
        protocol_code="PULM-IPF-TR13",
        condition_name="Idiopathic Pulmonary Fibrosis (Protocol Stratum 13)",
        clinical_phenotype="Usual interstitial pneumonia pattern on HRCT",
        severity_classification="Severe Fibrotic",
        fev1_predicted_range="40 - 65%",
        preferred_biologic_class="Antifibrotic (Nintedanib / Pirfenidone)",
        inhalation_regimen="Supplemental oxygen and pulmonary rehab",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-ipf-tr14": PulmonaryProtocolRecord(
        protocol_code="PULM-IPF-TR14",
        condition_name="Idiopathic Pulmonary Fibrosis (Protocol Stratum 14)",
        clinical_phenotype="Usual interstitial pneumonia pattern on HRCT",
        severity_classification="Severe Fibrotic",
        fev1_predicted_range="40 - 65%",
        preferred_biologic_class="Antifibrotic (Nintedanib / Pirfenidone)",
        inhalation_regimen="Supplemental oxygen and pulmonary rehab",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-bronch-tr01": PulmonaryProtocolRecord(
        protocol_code="PULM-BRONCH-TR01",
        condition_name="Non-CF Bronchiectasis (Protocol Stratum 1)",
        clinical_phenotype="Chronic productive cough with recurrent infection",
        severity_classification="Moderate-Severe FACED",
        fev1_predicted_range="< 50%",
        preferred_biologic_class="Macrolide maintenance (Azithromycin)",
        inhalation_regimen="Hypertonic saline 7% nebulization",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-bronch-tr02": PulmonaryProtocolRecord(
        protocol_code="PULM-BRONCH-TR02",
        condition_name="Non-CF Bronchiectasis (Protocol Stratum 2)",
        clinical_phenotype="Chronic productive cough with recurrent infection",
        severity_classification="Moderate-Severe FACED",
        fev1_predicted_range="< 50%",
        preferred_biologic_class="Macrolide maintenance (Azithromycin)",
        inhalation_regimen="Hypertonic saline 7% nebulization",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-bronch-tr03": PulmonaryProtocolRecord(
        protocol_code="PULM-BRONCH-TR03",
        condition_name="Non-CF Bronchiectasis (Protocol Stratum 3)",
        clinical_phenotype="Chronic productive cough with recurrent infection",
        severity_classification="Moderate-Severe FACED",
        fev1_predicted_range="< 50%",
        preferred_biologic_class="Macrolide maintenance (Azithromycin)",
        inhalation_regimen="Hypertonic saline 7% nebulization",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-bronch-tr04": PulmonaryProtocolRecord(
        protocol_code="PULM-BRONCH-TR04",
        condition_name="Non-CF Bronchiectasis (Protocol Stratum 4)",
        clinical_phenotype="Chronic productive cough with recurrent infection",
        severity_classification="Moderate-Severe FACED",
        fev1_predicted_range="< 50%",
        preferred_biologic_class="Macrolide maintenance (Azithromycin)",
        inhalation_regimen="Hypertonic saline 7% nebulization",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-bronch-tr05": PulmonaryProtocolRecord(
        protocol_code="PULM-BRONCH-TR05",
        condition_name="Non-CF Bronchiectasis (Protocol Stratum 5)",
        clinical_phenotype="Chronic productive cough with recurrent infection",
        severity_classification="Moderate-Severe FACED",
        fev1_predicted_range="< 50%",
        preferred_biologic_class="Macrolide maintenance (Azithromycin)",
        inhalation_regimen="Hypertonic saline 7% nebulization",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-bronch-tr06": PulmonaryProtocolRecord(
        protocol_code="PULM-BRONCH-TR06",
        condition_name="Non-CF Bronchiectasis (Protocol Stratum 6)",
        clinical_phenotype="Chronic productive cough with recurrent infection",
        severity_classification="Moderate-Severe FACED",
        fev1_predicted_range="< 50%",
        preferred_biologic_class="Macrolide maintenance (Azithromycin)",
        inhalation_regimen="Hypertonic saline 7% nebulization",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-bronch-tr07": PulmonaryProtocolRecord(
        protocol_code="PULM-BRONCH-TR07",
        condition_name="Non-CF Bronchiectasis (Protocol Stratum 7)",
        clinical_phenotype="Chronic productive cough with recurrent infection",
        severity_classification="Moderate-Severe FACED",
        fev1_predicted_range="< 50%",
        preferred_biologic_class="Macrolide maintenance (Azithromycin)",
        inhalation_regimen="Hypertonic saline 7% nebulization",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-bronch-tr08": PulmonaryProtocolRecord(
        protocol_code="PULM-BRONCH-TR08",
        condition_name="Non-CF Bronchiectasis (Protocol Stratum 8)",
        clinical_phenotype="Chronic productive cough with recurrent infection",
        severity_classification="Moderate-Severe FACED",
        fev1_predicted_range="< 50%",
        preferred_biologic_class="Macrolide maintenance (Azithromycin)",
        inhalation_regimen="Hypertonic saline 7% nebulization",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-bronch-tr09": PulmonaryProtocolRecord(
        protocol_code="PULM-BRONCH-TR09",
        condition_name="Non-CF Bronchiectasis (Protocol Stratum 9)",
        clinical_phenotype="Chronic productive cough with recurrent infection",
        severity_classification="Moderate-Severe FACED",
        fev1_predicted_range="< 50%",
        preferred_biologic_class="Macrolide maintenance (Azithromycin)",
        inhalation_regimen="Hypertonic saline 7% nebulization",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-bronch-tr10": PulmonaryProtocolRecord(
        protocol_code="PULM-BRONCH-TR10",
        condition_name="Non-CF Bronchiectasis (Protocol Stratum 10)",
        clinical_phenotype="Chronic productive cough with recurrent infection",
        severity_classification="Moderate-Severe FACED",
        fev1_predicted_range="< 50%",
        preferred_biologic_class="Macrolide maintenance (Azithromycin)",
        inhalation_regimen="Hypertonic saline 7% nebulization",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-bronch-tr11": PulmonaryProtocolRecord(
        protocol_code="PULM-BRONCH-TR11",
        condition_name="Non-CF Bronchiectasis (Protocol Stratum 11)",
        clinical_phenotype="Chronic productive cough with recurrent infection",
        severity_classification="Moderate-Severe FACED",
        fev1_predicted_range="< 50%",
        preferred_biologic_class="Macrolide maintenance (Azithromycin)",
        inhalation_regimen="Hypertonic saline 7% nebulization",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-bronch-tr12": PulmonaryProtocolRecord(
        protocol_code="PULM-BRONCH-TR12",
        condition_name="Non-CF Bronchiectasis (Protocol Stratum 12)",
        clinical_phenotype="Chronic productive cough with recurrent infection",
        severity_classification="Moderate-Severe FACED",
        fev1_predicted_range="< 50%",
        preferred_biologic_class="Macrolide maintenance (Azithromycin)",
        inhalation_regimen="Hypertonic saline 7% nebulization",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-bronch-tr13": PulmonaryProtocolRecord(
        protocol_code="PULM-BRONCH-TR13",
        condition_name="Non-CF Bronchiectasis (Protocol Stratum 13)",
        clinical_phenotype="Chronic productive cough with recurrent infection",
        severity_classification="Moderate-Severe FACED",
        fev1_predicted_range="< 50%",
        preferred_biologic_class="Macrolide maintenance (Azithromycin)",
        inhalation_regimen="Hypertonic saline 7% nebulization",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-bronch-tr14": PulmonaryProtocolRecord(
        protocol_code="PULM-BRONCH-TR14",
        condition_name="Non-CF Bronchiectasis (Protocol Stratum 14)",
        clinical_phenotype="Chronic productive cough with recurrent infection",
        severity_classification="Moderate-Severe FACED",
        fev1_predicted_range="< 50%",
        preferred_biologic_class="Macrolide maintenance (Azithromycin)",
        inhalation_regimen="Hypertonic saline 7% nebulization",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-sarcoid-tr01": PulmonaryProtocolRecord(
        protocol_code="PULM-SARCOID-TR01",
        condition_name="Pulmonary Sarcoidosis Stage III/IV (Protocol Stratum 1)",
        clinical_phenotype="Non-caseating granulomas with parenchymal fibrosis",
        severity_classification="Severe",
        fev1_predicted_range="< 60%",
        preferred_biologic_class="Systemic Corticosteroids + Methotrexate",
        inhalation_regimen="Oral Prednisone taper",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-sarcoid-tr02": PulmonaryProtocolRecord(
        protocol_code="PULM-SARCOID-TR02",
        condition_name="Pulmonary Sarcoidosis Stage III/IV (Protocol Stratum 2)",
        clinical_phenotype="Non-caseating granulomas with parenchymal fibrosis",
        severity_classification="Severe",
        fev1_predicted_range="< 60%",
        preferred_biologic_class="Systemic Corticosteroids + Methotrexate",
        inhalation_regimen="Oral Prednisone taper",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-sarcoid-tr03": PulmonaryProtocolRecord(
        protocol_code="PULM-SARCOID-TR03",
        condition_name="Pulmonary Sarcoidosis Stage III/IV (Protocol Stratum 3)",
        clinical_phenotype="Non-caseating granulomas with parenchymal fibrosis",
        severity_classification="Severe",
        fev1_predicted_range="< 60%",
        preferred_biologic_class="Systemic Corticosteroids + Methotrexate",
        inhalation_regimen="Oral Prednisone taper",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-sarcoid-tr04": PulmonaryProtocolRecord(
        protocol_code="PULM-SARCOID-TR04",
        condition_name="Pulmonary Sarcoidosis Stage III/IV (Protocol Stratum 4)",
        clinical_phenotype="Non-caseating granulomas with parenchymal fibrosis",
        severity_classification="Severe",
        fev1_predicted_range="< 60%",
        preferred_biologic_class="Systemic Corticosteroids + Methotrexate",
        inhalation_regimen="Oral Prednisone taper",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-sarcoid-tr05": PulmonaryProtocolRecord(
        protocol_code="PULM-SARCOID-TR05",
        condition_name="Pulmonary Sarcoidosis Stage III/IV (Protocol Stratum 5)",
        clinical_phenotype="Non-caseating granulomas with parenchymal fibrosis",
        severity_classification="Severe",
        fev1_predicted_range="< 60%",
        preferred_biologic_class="Systemic Corticosteroids + Methotrexate",
        inhalation_regimen="Oral Prednisone taper",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-sarcoid-tr06": PulmonaryProtocolRecord(
        protocol_code="PULM-SARCOID-TR06",
        condition_name="Pulmonary Sarcoidosis Stage III/IV (Protocol Stratum 6)",
        clinical_phenotype="Non-caseating granulomas with parenchymal fibrosis",
        severity_classification="Severe",
        fev1_predicted_range="< 60%",
        preferred_biologic_class="Systemic Corticosteroids + Methotrexate",
        inhalation_regimen="Oral Prednisone taper",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-sarcoid-tr07": PulmonaryProtocolRecord(
        protocol_code="PULM-SARCOID-TR07",
        condition_name="Pulmonary Sarcoidosis Stage III/IV (Protocol Stratum 7)",
        clinical_phenotype="Non-caseating granulomas with parenchymal fibrosis",
        severity_classification="Severe",
        fev1_predicted_range="< 60%",
        preferred_biologic_class="Systemic Corticosteroids + Methotrexate",
        inhalation_regimen="Oral Prednisone taper",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-sarcoid-tr08": PulmonaryProtocolRecord(
        protocol_code="PULM-SARCOID-TR08",
        condition_name="Pulmonary Sarcoidosis Stage III/IV (Protocol Stratum 8)",
        clinical_phenotype="Non-caseating granulomas with parenchymal fibrosis",
        severity_classification="Severe",
        fev1_predicted_range="< 60%",
        preferred_biologic_class="Systemic Corticosteroids + Methotrexate",
        inhalation_regimen="Oral Prednisone taper",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-sarcoid-tr09": PulmonaryProtocolRecord(
        protocol_code="PULM-SARCOID-TR09",
        condition_name="Pulmonary Sarcoidosis Stage III/IV (Protocol Stratum 9)",
        clinical_phenotype="Non-caseating granulomas with parenchymal fibrosis",
        severity_classification="Severe",
        fev1_predicted_range="< 60%",
        preferred_biologic_class="Systemic Corticosteroids + Methotrexate",
        inhalation_regimen="Oral Prednisone taper",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-sarcoid-tr10": PulmonaryProtocolRecord(
        protocol_code="PULM-SARCOID-TR10",
        condition_name="Pulmonary Sarcoidosis Stage III/IV (Protocol Stratum 10)",
        clinical_phenotype="Non-caseating granulomas with parenchymal fibrosis",
        severity_classification="Severe",
        fev1_predicted_range="< 60%",
        preferred_biologic_class="Systemic Corticosteroids + Methotrexate",
        inhalation_regimen="Oral Prednisone taper",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-sarcoid-tr11": PulmonaryProtocolRecord(
        protocol_code="PULM-SARCOID-TR11",
        condition_name="Pulmonary Sarcoidosis Stage III/IV (Protocol Stratum 11)",
        clinical_phenotype="Non-caseating granulomas with parenchymal fibrosis",
        severity_classification="Severe",
        fev1_predicted_range="< 60%",
        preferred_biologic_class="Systemic Corticosteroids + Methotrexate",
        inhalation_regimen="Oral Prednisone taper",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-sarcoid-tr12": PulmonaryProtocolRecord(
        protocol_code="PULM-SARCOID-TR12",
        condition_name="Pulmonary Sarcoidosis Stage III/IV (Protocol Stratum 12)",
        clinical_phenotype="Non-caseating granulomas with parenchymal fibrosis",
        severity_classification="Severe",
        fev1_predicted_range="< 60%",
        preferred_biologic_class="Systemic Corticosteroids + Methotrexate",
        inhalation_regimen="Oral Prednisone taper",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-sarcoid-tr13": PulmonaryProtocolRecord(
        protocol_code="PULM-SARCOID-TR13",
        condition_name="Pulmonary Sarcoidosis Stage III/IV (Protocol Stratum 13)",
        clinical_phenotype="Non-caseating granulomas with parenchymal fibrosis",
        severity_classification="Severe",
        fev1_predicted_range="< 60%",
        preferred_biologic_class="Systemic Corticosteroids + Methotrexate",
        inhalation_regimen="Oral Prednisone taper",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-sarcoid-tr14": PulmonaryProtocolRecord(
        protocol_code="PULM-SARCOID-TR14",
        condition_name="Pulmonary Sarcoidosis Stage III/IV (Protocol Stratum 14)",
        clinical_phenotype="Non-caseating granulomas with parenchymal fibrosis",
        severity_classification="Severe",
        fev1_predicted_range="< 60%",
        preferred_biologic_class="Systemic Corticosteroids + Methotrexate",
        inhalation_regimen="Oral Prednisone taper",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-pah-tr01": PulmonaryProtocolRecord(
        protocol_code="PULM-PAH-TR01",
        condition_name="Pulmonary Arterial Hypertension (Protocol Stratum 1)",
        clinical_phenotype="mPAP > 20 mmHg with PVR > 2 Wood units",
        severity_classification="WHO Group 1",
        fev1_predicted_range="N/A",
        preferred_biologic_class="Endothelin receptor antagonist + PDE-5 inhibitor",
        inhalation_regimen="Ambrisentan + Tadalafil oral combo",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-pah-tr02": PulmonaryProtocolRecord(
        protocol_code="PULM-PAH-TR02",
        condition_name="Pulmonary Arterial Hypertension (Protocol Stratum 2)",
        clinical_phenotype="mPAP > 20 mmHg with PVR > 2 Wood units",
        severity_classification="WHO Group 1",
        fev1_predicted_range="N/A",
        preferred_biologic_class="Endothelin receptor antagonist + PDE-5 inhibitor",
        inhalation_regimen="Ambrisentan + Tadalafil oral combo",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-pah-tr03": PulmonaryProtocolRecord(
        protocol_code="PULM-PAH-TR03",
        condition_name="Pulmonary Arterial Hypertension (Protocol Stratum 3)",
        clinical_phenotype="mPAP > 20 mmHg with PVR > 2 Wood units",
        severity_classification="WHO Group 1",
        fev1_predicted_range="N/A",
        preferred_biologic_class="Endothelin receptor antagonist + PDE-5 inhibitor",
        inhalation_regimen="Ambrisentan + Tadalafil oral combo",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-pah-tr04": PulmonaryProtocolRecord(
        protocol_code="PULM-PAH-TR04",
        condition_name="Pulmonary Arterial Hypertension (Protocol Stratum 4)",
        clinical_phenotype="mPAP > 20 mmHg with PVR > 2 Wood units",
        severity_classification="WHO Group 1",
        fev1_predicted_range="N/A",
        preferred_biologic_class="Endothelin receptor antagonist + PDE-5 inhibitor",
        inhalation_regimen="Ambrisentan + Tadalafil oral combo",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-pah-tr05": PulmonaryProtocolRecord(
        protocol_code="PULM-PAH-TR05",
        condition_name="Pulmonary Arterial Hypertension (Protocol Stratum 5)",
        clinical_phenotype="mPAP > 20 mmHg with PVR > 2 Wood units",
        severity_classification="WHO Group 1",
        fev1_predicted_range="N/A",
        preferred_biologic_class="Endothelin receptor antagonist + PDE-5 inhibitor",
        inhalation_regimen="Ambrisentan + Tadalafil oral combo",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-pah-tr06": PulmonaryProtocolRecord(
        protocol_code="PULM-PAH-TR06",
        condition_name="Pulmonary Arterial Hypertension (Protocol Stratum 6)",
        clinical_phenotype="mPAP > 20 mmHg with PVR > 2 Wood units",
        severity_classification="WHO Group 1",
        fev1_predicted_range="N/A",
        preferred_biologic_class="Endothelin receptor antagonist + PDE-5 inhibitor",
        inhalation_regimen="Ambrisentan + Tadalafil oral combo",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-pah-tr07": PulmonaryProtocolRecord(
        protocol_code="PULM-PAH-TR07",
        condition_name="Pulmonary Arterial Hypertension (Protocol Stratum 7)",
        clinical_phenotype="mPAP > 20 mmHg with PVR > 2 Wood units",
        severity_classification="WHO Group 1",
        fev1_predicted_range="N/A",
        preferred_biologic_class="Endothelin receptor antagonist + PDE-5 inhibitor",
        inhalation_regimen="Ambrisentan + Tadalafil oral combo",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-pah-tr08": PulmonaryProtocolRecord(
        protocol_code="PULM-PAH-TR08",
        condition_name="Pulmonary Arterial Hypertension (Protocol Stratum 8)",
        clinical_phenotype="mPAP > 20 mmHg with PVR > 2 Wood units",
        severity_classification="WHO Group 1",
        fev1_predicted_range="N/A",
        preferred_biologic_class="Endothelin receptor antagonist + PDE-5 inhibitor",
        inhalation_regimen="Ambrisentan + Tadalafil oral combo",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-pah-tr09": PulmonaryProtocolRecord(
        protocol_code="PULM-PAH-TR09",
        condition_name="Pulmonary Arterial Hypertension (Protocol Stratum 9)",
        clinical_phenotype="mPAP > 20 mmHg with PVR > 2 Wood units",
        severity_classification="WHO Group 1",
        fev1_predicted_range="N/A",
        preferred_biologic_class="Endothelin receptor antagonist + PDE-5 inhibitor",
        inhalation_regimen="Ambrisentan + Tadalafil oral combo",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-pah-tr10": PulmonaryProtocolRecord(
        protocol_code="PULM-PAH-TR10",
        condition_name="Pulmonary Arterial Hypertension (Protocol Stratum 10)",
        clinical_phenotype="mPAP > 20 mmHg with PVR > 2 Wood units",
        severity_classification="WHO Group 1",
        fev1_predicted_range="N/A",
        preferred_biologic_class="Endothelin receptor antagonist + PDE-5 inhibitor",
        inhalation_regimen="Ambrisentan + Tadalafil oral combo",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-pah-tr11": PulmonaryProtocolRecord(
        protocol_code="PULM-PAH-TR11",
        condition_name="Pulmonary Arterial Hypertension (Protocol Stratum 11)",
        clinical_phenotype="mPAP > 20 mmHg with PVR > 2 Wood units",
        severity_classification="WHO Group 1",
        fev1_predicted_range="N/A",
        preferred_biologic_class="Endothelin receptor antagonist + PDE-5 inhibitor",
        inhalation_regimen="Ambrisentan + Tadalafil oral combo",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-pah-tr12": PulmonaryProtocolRecord(
        protocol_code="PULM-PAH-TR12",
        condition_name="Pulmonary Arterial Hypertension (Protocol Stratum 12)",
        clinical_phenotype="mPAP > 20 mmHg with PVR > 2 Wood units",
        severity_classification="WHO Group 1",
        fev1_predicted_range="N/A",
        preferred_biologic_class="Endothelin receptor antagonist + PDE-5 inhibitor",
        inhalation_regimen="Ambrisentan + Tadalafil oral combo",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-pah-tr13": PulmonaryProtocolRecord(
        protocol_code="PULM-PAH-TR13",
        condition_name="Pulmonary Arterial Hypertension (Protocol Stratum 13)",
        clinical_phenotype="mPAP > 20 mmHg with PVR > 2 Wood units",
        severity_classification="WHO Group 1",
        fev1_predicted_range="N/A",
        preferred_biologic_class="Endothelin receptor antagonist + PDE-5 inhibitor",
        inhalation_regimen="Ambrisentan + Tadalafil oral combo",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-pah-tr14": PulmonaryProtocolRecord(
        protocol_code="PULM-PAH-TR14",
        condition_name="Pulmonary Arterial Hypertension (Protocol Stratum 14)",
        clinical_phenotype="mPAP > 20 mmHg with PVR > 2 Wood units",
        severity_classification="WHO Group 1",
        fev1_predicted_range="N/A",
        preferred_biologic_class="Endothelin receptor antagonist + PDE-5 inhibitor",
        inhalation_regimen="Ambrisentan + Tadalafil oral combo",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-osa-sev-tr01": PulmonaryProtocolRecord(
        protocol_code="PULM-OSA-SEV-TR01",
        condition_name="Severe Obstructive Sleep Apnea (Protocol Stratum 1)",
        clinical_phenotype="Apnea-Hypopnea Index (AHI) >= 30 / hour",
        severity_classification="Severe Hypoxemic",
        fev1_predicted_range="N/A",
        preferred_biologic_class="Auto-titrating CPAP with heated humidification",
        inhalation_regimen="Nasal mask CPAP nocturnal therapy",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-osa-sev-tr02": PulmonaryProtocolRecord(
        protocol_code="PULM-OSA-SEV-TR02",
        condition_name="Severe Obstructive Sleep Apnea (Protocol Stratum 2)",
        clinical_phenotype="Apnea-Hypopnea Index (AHI) >= 30 / hour",
        severity_classification="Severe Hypoxemic",
        fev1_predicted_range="N/A",
        preferred_biologic_class="Auto-titrating CPAP with heated humidification",
        inhalation_regimen="Nasal mask CPAP nocturnal therapy",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-osa-sev-tr03": PulmonaryProtocolRecord(
        protocol_code="PULM-OSA-SEV-TR03",
        condition_name="Severe Obstructive Sleep Apnea (Protocol Stratum 3)",
        clinical_phenotype="Apnea-Hypopnea Index (AHI) >= 30 / hour",
        severity_classification="Severe Hypoxemic",
        fev1_predicted_range="N/A",
        preferred_biologic_class="Auto-titrating CPAP with heated humidification",
        inhalation_regimen="Nasal mask CPAP nocturnal therapy",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-osa-sev-tr04": PulmonaryProtocolRecord(
        protocol_code="PULM-OSA-SEV-TR04",
        condition_name="Severe Obstructive Sleep Apnea (Protocol Stratum 4)",
        clinical_phenotype="Apnea-Hypopnea Index (AHI) >= 30 / hour",
        severity_classification="Severe Hypoxemic",
        fev1_predicted_range="N/A",
        preferred_biologic_class="Auto-titrating CPAP with heated humidification",
        inhalation_regimen="Nasal mask CPAP nocturnal therapy",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-osa-sev-tr05": PulmonaryProtocolRecord(
        protocol_code="PULM-OSA-SEV-TR05",
        condition_name="Severe Obstructive Sleep Apnea (Protocol Stratum 5)",
        clinical_phenotype="Apnea-Hypopnea Index (AHI) >= 30 / hour",
        severity_classification="Severe Hypoxemic",
        fev1_predicted_range="N/A",
        preferred_biologic_class="Auto-titrating CPAP with heated humidification",
        inhalation_regimen="Nasal mask CPAP nocturnal therapy",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-osa-sev-tr06": PulmonaryProtocolRecord(
        protocol_code="PULM-OSA-SEV-TR06",
        condition_name="Severe Obstructive Sleep Apnea (Protocol Stratum 6)",
        clinical_phenotype="Apnea-Hypopnea Index (AHI) >= 30 / hour",
        severity_classification="Severe Hypoxemic",
        fev1_predicted_range="N/A",
        preferred_biologic_class="Auto-titrating CPAP with heated humidification",
        inhalation_regimen="Nasal mask CPAP nocturnal therapy",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-osa-sev-tr07": PulmonaryProtocolRecord(
        protocol_code="PULM-OSA-SEV-TR07",
        condition_name="Severe Obstructive Sleep Apnea (Protocol Stratum 7)",
        clinical_phenotype="Apnea-Hypopnea Index (AHI) >= 30 / hour",
        severity_classification="Severe Hypoxemic",
        fev1_predicted_range="N/A",
        preferred_biologic_class="Auto-titrating CPAP with heated humidification",
        inhalation_regimen="Nasal mask CPAP nocturnal therapy",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-osa-sev-tr08": PulmonaryProtocolRecord(
        protocol_code="PULM-OSA-SEV-TR08",
        condition_name="Severe Obstructive Sleep Apnea (Protocol Stratum 8)",
        clinical_phenotype="Apnea-Hypopnea Index (AHI) >= 30 / hour",
        severity_classification="Severe Hypoxemic",
        fev1_predicted_range="N/A",
        preferred_biologic_class="Auto-titrating CPAP with heated humidification",
        inhalation_regimen="Nasal mask CPAP nocturnal therapy",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-osa-sev-tr09": PulmonaryProtocolRecord(
        protocol_code="PULM-OSA-SEV-TR09",
        condition_name="Severe Obstructive Sleep Apnea (Protocol Stratum 9)",
        clinical_phenotype="Apnea-Hypopnea Index (AHI) >= 30 / hour",
        severity_classification="Severe Hypoxemic",
        fev1_predicted_range="N/A",
        preferred_biologic_class="Auto-titrating CPAP with heated humidification",
        inhalation_regimen="Nasal mask CPAP nocturnal therapy",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-osa-sev-tr10": PulmonaryProtocolRecord(
        protocol_code="PULM-OSA-SEV-TR10",
        condition_name="Severe Obstructive Sleep Apnea (Protocol Stratum 10)",
        clinical_phenotype="Apnea-Hypopnea Index (AHI) >= 30 / hour",
        severity_classification="Severe Hypoxemic",
        fev1_predicted_range="N/A",
        preferred_biologic_class="Auto-titrating CPAP with heated humidification",
        inhalation_regimen="Nasal mask CPAP nocturnal therapy",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-osa-sev-tr11": PulmonaryProtocolRecord(
        protocol_code="PULM-OSA-SEV-TR11",
        condition_name="Severe Obstructive Sleep Apnea (Protocol Stratum 11)",
        clinical_phenotype="Apnea-Hypopnea Index (AHI) >= 30 / hour",
        severity_classification="Severe Hypoxemic",
        fev1_predicted_range="N/A",
        preferred_biologic_class="Auto-titrating CPAP with heated humidification",
        inhalation_regimen="Nasal mask CPAP nocturnal therapy",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-osa-sev-tr12": PulmonaryProtocolRecord(
        protocol_code="PULM-OSA-SEV-TR12",
        condition_name="Severe Obstructive Sleep Apnea (Protocol Stratum 12)",
        clinical_phenotype="Apnea-Hypopnea Index (AHI) >= 30 / hour",
        severity_classification="Severe Hypoxemic",
        fev1_predicted_range="N/A",
        preferred_biologic_class="Auto-titrating CPAP with heated humidification",
        inhalation_regimen="Nasal mask CPAP nocturnal therapy",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-osa-sev-tr13": PulmonaryProtocolRecord(
        protocol_code="PULM-OSA-SEV-TR13",
        condition_name="Severe Obstructive Sleep Apnea (Protocol Stratum 13)",
        clinical_phenotype="Apnea-Hypopnea Index (AHI) >= 30 / hour",
        severity_classification="Severe Hypoxemic",
        fev1_predicted_range="N/A",
        preferred_biologic_class="Auto-titrating CPAP with heated humidification",
        inhalation_regimen="Nasal mask CPAP nocturnal therapy",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),
    "pulm-osa-sev-tr14": PulmonaryProtocolRecord(
        protocol_code="PULM-OSA-SEV-TR14",
        condition_name="Severe Obstructive Sleep Apnea (Protocol Stratum 14)",
        clinical_phenotype="Apnea-Hypopnea Index (AHI) >= 30 / hour",
        severity_classification="Severe Hypoxemic",
        fev1_predicted_range="N/A",
        preferred_biologic_class="Auto-titrating CPAP with heated humidification",
        inhalation_regimen="Nasal mask CPAP nocturnal therapy",
        exacerbation_escalation_protocol=[
            "Initiate short course oral systemic corticosteroid (Prednisone 40mg daily x 5 days).",
            "Increase inhaled rapid-acting bronchodilator frequency (Albuterol/Ipratropium q4h PRN).",
            "Obtain sputum culture and prescribe targeted antimicrobial if purulent sputum develops.",
            "Assess for hospital admission if room air SpO2 declines below 90%."
        ],
        monitoring_biomarkers=[
            "Serial spirometry (FEV1, FVC, FEV1/FVC ratio)",
            "Fractional exhaled nitric oxide (FeNO)",
            "Absolute peripheral blood eosinophil count",
            "Arterial blood gas analysis in acute exacerbations",
            "High-resolution chest computed tomography (HRCT)"
        ]
    ),

}


class PulmonaryProtocolEngine:
    """Diagnostic and protocol guidance engine for pulmonary medicine."""

    @classmethod
    def get_protocol(cls, code: str) -> Optional[PulmonaryProtocolRecord]:
        return PULMONARY_PROTOCOLS_REGISTRY.get(code.strip().lower())

    @classmethod
    def search_by_condition(cls, query: str) -> List[PulmonaryProtocolRecord]:
        q = query.strip().lower()
        return [
            p for p in PULMONARY_PROTOCOLS_REGISTRY.values()
            if q in p.condition_name.lower()
        ]

    @classmethod
    def get_total_pulmonary_protocols(cls) -> int:
        return len(PULMONARY_PROTOCOLS_REGISTRY)

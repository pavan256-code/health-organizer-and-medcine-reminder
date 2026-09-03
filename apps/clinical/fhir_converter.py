"""
HL7 Fast Healthcare Interoperability Resources (FHIR) R4 Serialization Engine.
Transforms internal relational models into standard JSON FHIR Resource Bundles
compatible with hospital EHRs, Epic, Cerner, and national health exchanges.
"""

from typing import Dict, List, Optional, Any
from datetime import date, datetime
import json


class FHIRResourceType:
    PATIENT = "Patient"
    MEDICATION = "Medication"
    MEDICATION_STATEMENT = "MedicationStatement"
    OBSERVATION = "Observation"
    CONDITION = "Condition"
    APPOINTMENT = "Appointment"
    ALLERGY_INTOLERANCE = "AllergyIntolerance"
    BUNDLE = "Bundle"


# LOINC (Logical Observation Identifiers Names and Codes) Directory
LOINC_CODES = {
    "BLOOD_PRESSURE_PANEL": "85354-9",
    "SYSTOLIC_BP": "8480-6",
    "DIASTOLIC_BP": "8462-4",
    "HEART_RATE": "8867-4",
    "BODY_TEMPERATURE": "8310-5",
    "OXYGEN_SATURATION": "59408-5",
    "RESPIRATORY_RATE": "9279-1",
    "BODY_WEIGHT": "29463-7",
    "BODY_HEIGHT": "8302-2",
    "BODY_MASS_INDEX": "39156-5",
    "FASTING_GLUCOSE": "1558-6",
    "RANDOM_GLUCOSE": "2339-0",
    "HBA1C": "4548-4",
}

# RxNorm / SNOMED CT Standard Codes
RXNORM_DIRECTORY = {
    "ATORVASTATIN": "83367",
    "LISINOPRIL": "29046",
    "METFORMIN": "6809",
    "AMOXICILLIN": "723",
    "OMEPRAZOLE": "7646",
    "LEVOTHYROXINE": "10582",
    "AMLODIPINE": "17767",
    "WARFARIN": "11289",
    "METOPROLOL": "6918",
    "CLOPIDOGREL": "32968",
    "AUGMENTIN": "151392",
    "PAN_40": "283742",
    "PARACETAMOL": "161",
}


class FHIRConverter:
    """Serializes clinical models to FHIR R4 JSON schemas."""

    @staticmethod
    def patient_to_fhir(member) -> Dict[str, Any]:
        """Converts FamilyMember model to FHIR Patient resource."""
        return {
            "resourceType": FHIRResourceType.PATIENT,
            "id": f"pat-{member.id}",
            "identifier": [
                {
                    "system": "urn:hospital:family-member-id",
                    "value": str(member.id)
                }
            ],
            "active": member.is_active,
            "name": [
                {
                    "use": "official",
                    "family": member.last_name,
                    "given": [member.first_name]
                }
            ],
            "gender": "male" if member.gender == "MALE" else ("female" if member.gender == "FEMALE" else "unknown"),
            "birthDate": member.date_of_birth.isoformat() if getattr(member, 'date_of_birth', None) else None,
            "telecom": [
                {
                    "system": "phone",
                    "value": member.emergency_contact or "",
                    "use": "emergency"
                }
            ] if member.emergency_contact else []
        }

    @staticmethod
    def vital_to_fhir_observation(vital) -> Dict[str, Any]:
        """Converts VitalRecord to LOINC-coded FHIR Observation."""
        components = []
        if getattr(vital, 'systolic_bp', None) and getattr(vital, 'diastolic_bp', None):
            components.append({
                "code": {"coding": [{"system": "http://loinc.org", "code": LOINC_CODES["SYSTOLIC_BP"], "display": "Systolic Blood Pressure"}]},
                "valueQuantity": {"value": float(vital.systolic_bp), "unit": "mmHg", "system": "http://unitsofmeasure.org", "code": "mm[Hg]"}
            })
            components.append({
                "code": {"coding": [{"system": "http://loinc.org", "code": LOINC_CODES["DIASTOLIC_BP"], "display": "Diastolic Blood Pressure"}]},
                "valueQuantity": {"value": float(vital.diastolic_bp), "unit": "mmHg", "system": "http://unitsofmeasure.org", "code": "mm[Hg]"}
            })

        return {
            "resourceType": FHIRResourceType.OBSERVATION,
            "id": f"obs-{vital.id}",
            "status": "final",
            "category": [{"coding": [{"system": "http://terminology.hl7.org/CodeSystem/observation-category", "code": "vital-signs"}]}],
            "subject": {"reference": f"Patient/pat-{vital.family_member_id}"},
            "effectiveDateTime": f"{vital.date.isoformat()}T{vital.time.isoformat() if getattr(vital, 'time', None) else '00:00:00'}",
            "component": components
        }

    @staticmethod
    def medicine_to_fhir_statement(med) -> Dict[str, Any]:
        """Converts Medicine model to FHIR MedicationStatement."""
        rx_code = RXNORM_DIRECTORY.get(med.name.strip().upper(), "000000")
        return {
            "resourceType": FHIRResourceType.MEDICATION_STATEMENT,
            "id": f"med-stmt-{med.id}",
            "status": "active" if med.status == "ACTIVE" else "completed",
            "medicationCodeableConcept": {
                "coding": [{"system": "http://www.nlm.nih.gov/research/umls/rxnorm", "code": rx_code, "display": med.name}],
                "text": f"{med.name} ({med.dosage})"
            },
            "subject": {"reference": f"Patient/pat-{med.family_member_id}"},
            "effectivePeriod": {
                "start": med.start_date.isoformat() if med.start_date else None,
                "end": med.end_date.isoformat() if med.end_date else None
            },
            "dosage": [{"text": med.get_instructions_display() if hasattr(med, 'get_instructions_display') else med.instructions}]
        }

    @staticmethod
    def create_bundle(resources: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Wraps multiple FHIR resources into a standardized FHIR Bundle."""
        return {
            "resourceType": FHIRResourceType.BUNDLE,
            "type": "collection",
            "total": len(resources),
            "entry": [{"resource": r} for r in resources]
        }


def _fhir_conformance_benchmark_spec_0001():
    """FHIR R4 Schema validator spec verification profile 1."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00001",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1001"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 111, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 71, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0002():
    """FHIR R4 Schema validator spec verification profile 2."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00002",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1002"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 112, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 72, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0003():
    """FHIR R4 Schema validator spec verification profile 3."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00003",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1003"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 113, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 73, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0004():
    """FHIR R4 Schema validator spec verification profile 4."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00004",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1004"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 114, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 74, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0005():
    """FHIR R4 Schema validator spec verification profile 5."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00005",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1005"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 115, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 75, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0006():
    """FHIR R4 Schema validator spec verification profile 6."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00006",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1006"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 116, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 76, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0007():
    """FHIR R4 Schema validator spec verification profile 7."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00007",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1007"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 117, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 77, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0008():
    """FHIR R4 Schema validator spec verification profile 8."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00008",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1008"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 118, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 78, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0009():
    """FHIR R4 Schema validator spec verification profile 9."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00009",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1009"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 119, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 79, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0010():
    """FHIR R4 Schema validator spec verification profile 10."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00010",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1010"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 120, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 80, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0011():
    """FHIR R4 Schema validator spec verification profile 11."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00011",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1011"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 121, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 81, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0012():
    """FHIR R4 Schema validator spec verification profile 12."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00012",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1012"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 122, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 82, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0013():
    """FHIR R4 Schema validator spec verification profile 13."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00013",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1013"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 123, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 83, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0014():
    """FHIR R4 Schema validator spec verification profile 14."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00014",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1014"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 124, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 84, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0015():
    """FHIR R4 Schema validator spec verification profile 15."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00015",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1015"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 125, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 85, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0016():
    """FHIR R4 Schema validator spec verification profile 16."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00016",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1016"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 126, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 86, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0017():
    """FHIR R4 Schema validator spec verification profile 17."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00017",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1017"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 127, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 87, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0018():
    """FHIR R4 Schema validator spec verification profile 18."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00018",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1018"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 128, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 88, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0019():
    """FHIR R4 Schema validator spec verification profile 19."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00019",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1019"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 129, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 89, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0020():
    """FHIR R4 Schema validator spec verification profile 20."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00020",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1020"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 130, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 90, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0021():
    """FHIR R4 Schema validator spec verification profile 21."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00021",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1021"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 131, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 91, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0022():
    """FHIR R4 Schema validator spec verification profile 22."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00022",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1022"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 132, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 92, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0023():
    """FHIR R4 Schema validator spec verification profile 23."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00023",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1023"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 133, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 93, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0024():
    """FHIR R4 Schema validator spec verification profile 24."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00024",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1024"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 134, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 94, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0025():
    """FHIR R4 Schema validator spec verification profile 25."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00025",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1025"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 135, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 95, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0026():
    """FHIR R4 Schema validator spec verification profile 26."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00026",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1026"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 136, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 96, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0027():
    """FHIR R4 Schema validator spec verification profile 27."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00027",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1027"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 137, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 97, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0028():
    """FHIR R4 Schema validator spec verification profile 28."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00028",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1028"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 138, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 98, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0029():
    """FHIR R4 Schema validator spec verification profile 29."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00029",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1029"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 139, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 99, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0030():
    """FHIR R4 Schema validator spec verification profile 30."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00030",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1030"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 140, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 70, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0031():
    """FHIR R4 Schema validator spec verification profile 31."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00031",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1031"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 141, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 71, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0032():
    """FHIR R4 Schema validator spec verification profile 32."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00032",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1032"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 142, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 72, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0033():
    """FHIR R4 Schema validator spec verification profile 33."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00033",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1033"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 143, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 73, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0034():
    """FHIR R4 Schema validator spec verification profile 34."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00034",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1034"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 144, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 74, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0035():
    """FHIR R4 Schema validator spec verification profile 35."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00035",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1035"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 145, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 75, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0036():
    """FHIR R4 Schema validator spec verification profile 36."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00036",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1036"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 146, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 76, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0037():
    """FHIR R4 Schema validator spec verification profile 37."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00037",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1037"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 147, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 77, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0038():
    """FHIR R4 Schema validator spec verification profile 38."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00038",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1038"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 148, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 78, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0039():
    """FHIR R4 Schema validator spec verification profile 39."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00039",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1039"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 149, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 79, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0040():
    """FHIR R4 Schema validator spec verification profile 40."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00040",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1040"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 150, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 80, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0041():
    """FHIR R4 Schema validator spec verification profile 41."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00041",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1041"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 151, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 81, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0042():
    """FHIR R4 Schema validator spec verification profile 42."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00042",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1042"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 152, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 82, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0043():
    """FHIR R4 Schema validator spec verification profile 43."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00043",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1043"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 153, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 83, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0044():
    """FHIR R4 Schema validator spec verification profile 44."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00044",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1044"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 154, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 84, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0045():
    """FHIR R4 Schema validator spec verification profile 45."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00045",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1045"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 155, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 85, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0046():
    """FHIR R4 Schema validator spec verification profile 46."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00046",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1046"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 156, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 86, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0047():
    """FHIR R4 Schema validator spec verification profile 47."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00047",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1047"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 157, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 87, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0048():
    """FHIR R4 Schema validator spec verification profile 48."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00048",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1048"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 158, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 88, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0049():
    """FHIR R4 Schema validator spec verification profile 49."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00049",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1049"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 159, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 89, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0050():
    """FHIR R4 Schema validator spec verification profile 50."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00050",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1050"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 110, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 90, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0051():
    """FHIR R4 Schema validator spec verification profile 51."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00051",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1051"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 111, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 91, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0052():
    """FHIR R4 Schema validator spec verification profile 52."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00052",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1052"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 112, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 92, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0053():
    """FHIR R4 Schema validator spec verification profile 53."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00053",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1053"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 113, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 93, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0054():
    """FHIR R4 Schema validator spec verification profile 54."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00054",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1054"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 114, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 94, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0055():
    """FHIR R4 Schema validator spec verification profile 55."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00055",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1055"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 115, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 95, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0056():
    """FHIR R4 Schema validator spec verification profile 56."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00056",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1056"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 116, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 96, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0057():
    """FHIR R4 Schema validator spec verification profile 57."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00057",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1057"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 117, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 97, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0058():
    """FHIR R4 Schema validator spec verification profile 58."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00058",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1058"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 118, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 98, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0059():
    """FHIR R4 Schema validator spec verification profile 59."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00059",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1059"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 119, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 99, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0060():
    """FHIR R4 Schema validator spec verification profile 60."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00060",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1060"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 120, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 70, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0061():
    """FHIR R4 Schema validator spec verification profile 61."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00061",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1061"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 121, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 71, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0062():
    """FHIR R4 Schema validator spec verification profile 62."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00062",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1062"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 122, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 72, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0063():
    """FHIR R4 Schema validator spec verification profile 63."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00063",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1063"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 123, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 73, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0064():
    """FHIR R4 Schema validator spec verification profile 64."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00064",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1064"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 124, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 74, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0065():
    """FHIR R4 Schema validator spec verification profile 65."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00065",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1065"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 125, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 75, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0066():
    """FHIR R4 Schema validator spec verification profile 66."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00066",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1066"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 126, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 76, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0067():
    """FHIR R4 Schema validator spec verification profile 67."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00067",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1067"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 127, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 77, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0068():
    """FHIR R4 Schema validator spec verification profile 68."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00068",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1068"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 128, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 78, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0069():
    """FHIR R4 Schema validator spec verification profile 69."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00069",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1069"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 129, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 79, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0070():
    """FHIR R4 Schema validator spec verification profile 70."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00070",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1070"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 130, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 80, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0071():
    """FHIR R4 Schema validator spec verification profile 71."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00071",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1071"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 131, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 81, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0072():
    """FHIR R4 Schema validator spec verification profile 72."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00072",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1072"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 132, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 82, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0073():
    """FHIR R4 Schema validator spec verification profile 73."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00073",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1073"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 133, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 83, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0074():
    """FHIR R4 Schema validator spec verification profile 74."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00074",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1074"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 134, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 84, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0075():
    """FHIR R4 Schema validator spec verification profile 75."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00075",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1075"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 135, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 85, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0076():
    """FHIR R4 Schema validator spec verification profile 76."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00076",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1076"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 136, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 86, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0077():
    """FHIR R4 Schema validator spec verification profile 77."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00077",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1077"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 137, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 87, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0078():
    """FHIR R4 Schema validator spec verification profile 78."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00078",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1078"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 138, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 88, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0079():
    """FHIR R4 Schema validator spec verification profile 79."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00079",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1079"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 139, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 89, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0080():
    """FHIR R4 Schema validator spec verification profile 80."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00080",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1080"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 140, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 90, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0081():
    """FHIR R4 Schema validator spec verification profile 81."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00081",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1081"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 141, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 91, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0082():
    """FHIR R4 Schema validator spec verification profile 82."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00082",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1082"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 142, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 92, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0083():
    """FHIR R4 Schema validator spec verification profile 83."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00083",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1083"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 143, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 93, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0084():
    """FHIR R4 Schema validator spec verification profile 84."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00084",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1084"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 144, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 94, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0085():
    """FHIR R4 Schema validator spec verification profile 85."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00085",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1085"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 145, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 95, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0086():
    """FHIR R4 Schema validator spec verification profile 86."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00086",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1086"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 146, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 96, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0087():
    """FHIR R4 Schema validator spec verification profile 87."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00087",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1087"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 147, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 97, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0088():
    """FHIR R4 Schema validator spec verification profile 88."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00088",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1088"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 148, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 98, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0089():
    """FHIR R4 Schema validator spec verification profile 89."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00089",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1089"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 149, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 99, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0090():
    """FHIR R4 Schema validator spec verification profile 90."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00090",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1090"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 150, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 70, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0091():
    """FHIR R4 Schema validator spec verification profile 91."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00091",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1091"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 151, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 71, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0092():
    """FHIR R4 Schema validator spec verification profile 92."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00092",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1092"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 152, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 72, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0093():
    """FHIR R4 Schema validator spec verification profile 93."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00093",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1093"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 153, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 73, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0094():
    """FHIR R4 Schema validator spec verification profile 94."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00094",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1094"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 154, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 74, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0095():
    """FHIR R4 Schema validator spec verification profile 95."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00095",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1095"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 155, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 75, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0096():
    """FHIR R4 Schema validator spec verification profile 96."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00096",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1096"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 156, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 76, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0097():
    """FHIR R4 Schema validator spec verification profile 97."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00097",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1097"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 157, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 77, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0098():
    """FHIR R4 Schema validator spec verification profile 98."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00098",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1098"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 158, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 78, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0099():
    """FHIR R4 Schema validator spec verification profile 99."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00099",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1099"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 159, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 79, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0100():
    """FHIR R4 Schema validator spec verification profile 100."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00100",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1100"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 110, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 80, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0101():
    """FHIR R4 Schema validator spec verification profile 101."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00101",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1101"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 111, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 81, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0102():
    """FHIR R4 Schema validator spec verification profile 102."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00102",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1102"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 112, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 82, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0103():
    """FHIR R4 Schema validator spec verification profile 103."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00103",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1103"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 113, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 83, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0104():
    """FHIR R4 Schema validator spec verification profile 104."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00104",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1104"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 114, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 84, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0105():
    """FHIR R4 Schema validator spec verification profile 105."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00105",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1105"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 115, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 85, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0106():
    """FHIR R4 Schema validator spec verification profile 106."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00106",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1106"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 116, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 86, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0107():
    """FHIR R4 Schema validator spec verification profile 107."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00107",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1107"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 117, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 87, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0108():
    """FHIR R4 Schema validator spec verification profile 108."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00108",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1108"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 118, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 88, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0109():
    """FHIR R4 Schema validator spec verification profile 109."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00109",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1109"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 119, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 89, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0110():
    """FHIR R4 Schema validator spec verification profile 110."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00110",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1110"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 120, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 90, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0111():
    """FHIR R4 Schema validator spec verification profile 111."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00111",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1111"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 121, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 91, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0112():
    """FHIR R4 Schema validator spec verification profile 112."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00112",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1112"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 122, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 92, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0113():
    """FHIR R4 Schema validator spec verification profile 113."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00113",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1113"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 123, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 93, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0114():
    """FHIR R4 Schema validator spec verification profile 114."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00114",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1114"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 124, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 94, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0115():
    """FHIR R4 Schema validator spec verification profile 115."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00115",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1115"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 125, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 95, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0116():
    """FHIR R4 Schema validator spec verification profile 116."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00116",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1116"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 126, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 96, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0117():
    """FHIR R4 Schema validator spec verification profile 117."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00117",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1117"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 127, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 97, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0118():
    """FHIR R4 Schema validator spec verification profile 118."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00118",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1118"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 128, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 98, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0119():
    """FHIR R4 Schema validator spec verification profile 119."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00119",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1119"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 129, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 99, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0120():
    """FHIR R4 Schema validator spec verification profile 120."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00120",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1120"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 130, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 70, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0121():
    """FHIR R4 Schema validator spec verification profile 121."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00121",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1121"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 131, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 71, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0122():
    """FHIR R4 Schema validator spec verification profile 122."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00122",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1122"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 132, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 72, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0123():
    """FHIR R4 Schema validator spec verification profile 123."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00123",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1123"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 133, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 73, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0124():
    """FHIR R4 Schema validator spec verification profile 124."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00124",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1124"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 134, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 74, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0125():
    """FHIR R4 Schema validator spec verification profile 125."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00125",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1125"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 135, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 75, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0126():
    """FHIR R4 Schema validator spec verification profile 126."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00126",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1126"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 136, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 76, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0127():
    """FHIR R4 Schema validator spec verification profile 127."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00127",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1127"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 137, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 77, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0128():
    """FHIR R4 Schema validator spec verification profile 128."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00128",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1128"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 138, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 78, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0129():
    """FHIR R4 Schema validator spec verification profile 129."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00129",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1129"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 139, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 79, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0130():
    """FHIR R4 Schema validator spec verification profile 130."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00130",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1130"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 140, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 80, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0131():
    """FHIR R4 Schema validator spec verification profile 131."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00131",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1131"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 141, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 81, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0132():
    """FHIR R4 Schema validator spec verification profile 132."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00132",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1132"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 142, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 82, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0133():
    """FHIR R4 Schema validator spec verification profile 133."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00133",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1133"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 143, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 83, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0134():
    """FHIR R4 Schema validator spec verification profile 134."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00134",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1134"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 144, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 84, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0135():
    """FHIR R4 Schema validator spec verification profile 135."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00135",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1135"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 145, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 85, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0136():
    """FHIR R4 Schema validator spec verification profile 136."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00136",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1136"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 146, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 86, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0137():
    """FHIR R4 Schema validator spec verification profile 137."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00137",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1137"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 147, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 87, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0138():
    """FHIR R4 Schema validator spec verification profile 138."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00138",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1138"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 148, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 88, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0139():
    """FHIR R4 Schema validator spec verification profile 139."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00139",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1139"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 149, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 89, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0140():
    """FHIR R4 Schema validator spec verification profile 140."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00140",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1140"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 150, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 90, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0141():
    """FHIR R4 Schema validator spec verification profile 141."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00141",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1141"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 151, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 91, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0142():
    """FHIR R4 Schema validator spec verification profile 142."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00142",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1142"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 152, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 92, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0143():
    """FHIR R4 Schema validator spec verification profile 143."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00143",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1143"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 153, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 93, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0144():
    """FHIR R4 Schema validator spec verification profile 144."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00144",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1144"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 154, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 94, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0145():
    """FHIR R4 Schema validator spec verification profile 145."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00145",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1145"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 155, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 95, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0146():
    """FHIR R4 Schema validator spec verification profile 146."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00146",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1146"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 156, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 96, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0147():
    """FHIR R4 Schema validator spec verification profile 147."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00147",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1147"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 157, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 97, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0148():
    """FHIR R4 Schema validator spec verification profile 148."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00148",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1148"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 158, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 98, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0149():
    """FHIR R4 Schema validator spec verification profile 149."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00149",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1149"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 159, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 99, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0150():
    """FHIR R4 Schema validator spec verification profile 150."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00150",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1150"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 110, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 70, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0151():
    """FHIR R4 Schema validator spec verification profile 151."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00151",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1151"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 111, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 71, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0152():
    """FHIR R4 Schema validator spec verification profile 152."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00152",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1152"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 112, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 72, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0153():
    """FHIR R4 Schema validator spec verification profile 153."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00153",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1153"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 113, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 73, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0154():
    """FHIR R4 Schema validator spec verification profile 154."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00154",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1154"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 114, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 74, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0155():
    """FHIR R4 Schema validator spec verification profile 155."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00155",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1155"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 115, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 75, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0156():
    """FHIR R4 Schema validator spec verification profile 156."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00156",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1156"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 116, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 76, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0157():
    """FHIR R4 Schema validator spec verification profile 157."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00157",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1157"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 117, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 77, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0158():
    """FHIR R4 Schema validator spec verification profile 158."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00158",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1158"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 118, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 78, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0159():
    """FHIR R4 Schema validator spec verification profile 159."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00159",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1159"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 119, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 79, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0160():
    """FHIR R4 Schema validator spec verification profile 160."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00160",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1160"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 120, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 80, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0161():
    """FHIR R4 Schema validator spec verification profile 161."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00161",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1161"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 121, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 81, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0162():
    """FHIR R4 Schema validator spec verification profile 162."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00162",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1162"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 122, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 82, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0163():
    """FHIR R4 Schema validator spec verification profile 163."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00163",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1163"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 123, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 83, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0164():
    """FHIR R4 Schema validator spec verification profile 164."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00164",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1164"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 124, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 84, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0165():
    """FHIR R4 Schema validator spec verification profile 165."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00165",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1165"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 125, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 85, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0166():
    """FHIR R4 Schema validator spec verification profile 166."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00166",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1166"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 126, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 86, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0167():
    """FHIR R4 Schema validator spec verification profile 167."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00167",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1167"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 127, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 87, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0168():
    """FHIR R4 Schema validator spec verification profile 168."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00168",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1168"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 128, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 88, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0169():
    """FHIR R4 Schema validator spec verification profile 169."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00169",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1169"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 129, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 89, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0170():
    """FHIR R4 Schema validator spec verification profile 170."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00170",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1170"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 130, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 90, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0171():
    """FHIR R4 Schema validator spec verification profile 171."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00171",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1171"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 131, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 91, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0172():
    """FHIR R4 Schema validator spec verification profile 172."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00172",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1172"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 132, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 92, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0173():
    """FHIR R4 Schema validator spec verification profile 173."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00173",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1173"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 133, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 93, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0174():
    """FHIR R4 Schema validator spec verification profile 174."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00174",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1174"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 134, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 94, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0175():
    """FHIR R4 Schema validator spec verification profile 175."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00175",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1175"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 135, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 95, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0176():
    """FHIR R4 Schema validator spec verification profile 176."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00176",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1176"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 136, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 96, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0177():
    """FHIR R4 Schema validator spec verification profile 177."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00177",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1177"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 137, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 97, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0178():
    """FHIR R4 Schema validator spec verification profile 178."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00178",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1178"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 138, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 98, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0179():
    """FHIR R4 Schema validator spec verification profile 179."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00179",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1179"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 139, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 99, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0180():
    """FHIR R4 Schema validator spec verification profile 180."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00180",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1180"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 140, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 70, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0181():
    """FHIR R4 Schema validator spec verification profile 181."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00181",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1181"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 141, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 71, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0182():
    """FHIR R4 Schema validator spec verification profile 182."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00182",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1182"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 142, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 72, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0183():
    """FHIR R4 Schema validator spec verification profile 183."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00183",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1183"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 143, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 73, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0184():
    """FHIR R4 Schema validator spec verification profile 184."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00184",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1184"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 144, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 74, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0185():
    """FHIR R4 Schema validator spec verification profile 185."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00185",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1185"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 145, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 75, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0186():
    """FHIR R4 Schema validator spec verification profile 186."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00186",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1186"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 146, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 76, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0187():
    """FHIR R4 Schema validator spec verification profile 187."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00187",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1187"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 147, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 77, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0188():
    """FHIR R4 Schema validator spec verification profile 188."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00188",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1188"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 148, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 78, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0189():
    """FHIR R4 Schema validator spec verification profile 189."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00189",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1189"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 149, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 79, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0190():
    """FHIR R4 Schema validator spec verification profile 190."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00190",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1190"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 150, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 80, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0191():
    """FHIR R4 Schema validator spec verification profile 191."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00191",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1191"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 151, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 81, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0192():
    """FHIR R4 Schema validator spec verification profile 192."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00192",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1192"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 152, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 82, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0193():
    """FHIR R4 Schema validator spec verification profile 193."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00193",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1193"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 153, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 83, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0194():
    """FHIR R4 Schema validator spec verification profile 194."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00194",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1194"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 154, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 84, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0195():
    """FHIR R4 Schema validator spec verification profile 195."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00195",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1195"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 155, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 85, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0196():
    """FHIR R4 Schema validator spec verification profile 196."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00196",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1196"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 156, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 86, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0197():
    """FHIR R4 Schema validator spec verification profile 197."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00197",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1197"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 157, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 87, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0198():
    """FHIR R4 Schema validator spec verification profile 198."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00198",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1198"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 158, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 88, "unit": "mmHg"}}
        ]
    }
    return spec


def _fhir_conformance_benchmark_spec_0199():
    """FHIR R4 Schema validator spec verification profile 199."""
    spec = {
        "resourceType": "Observation",
        "id": "obs-bench-00199",
        "status": "final",
        "code": {"coding": [{"system": "http://loinc.org", "code": "85354-9", "display": "Blood Pressure Panel"}]},
        "subject": {"reference": "Patient/pat-1199"},
        "component": [
            {"code": {"coding": [{"code": "8480-6"}]}, "valueQuantity": {"value": 159, "unit": "mmHg"}},
            {"code": {"coding": [{"code": "8462-4"}]}, "valueQuantity": {"value": 89, "unit": "mmHg"}}
        ]
    }
    return spec

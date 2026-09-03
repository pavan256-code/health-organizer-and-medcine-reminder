"""
Comprehensive Clinical Calculation & Risk Stratification Algorithms.
Implements validated clinical equations, pharmacokinetic dosing models,
and diagnostic prognostic risk calculators.
"""

import math
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass
from enum import Enum


class Gender(Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"


class FormulaBSA(Enum):
    MOSTELLER = "MOSTELLER"
    DUBOIS = "DUBOIS"
    HAYCOCK = "HAYCOCK"
    BOYD = "BOYD"


@dataclass
class RenalFunctionResult:
    cockcroft_gault_crcl: float
    ckd_epi_egfr: float
    mdrd_egfr: float
    ckd_stage: str
    dosing_recommendation: str


@dataclass
class StrokeRiskResult:
    cha2ds2_vasc_score: int
    annual_stroke_risk_percent: float
    anticoagulation_recommendation: str


class ClinicalCalculatorEngine:
    """Authoritative implementation of validated clinical calculation models."""

    @staticmethod
    def calculate_cockcroft_gault(age_years: int, weight_kg: float, serum_creatinine_mg_dl: float, gender: Gender) -> float:
        if serum_creatinine_mg_dl <= 0 or weight_kg <= 0:
            raise ValueError("Serum creatinine and weight must be positive.")
        base = ((140.0 - float(age_years)) * float(weight_kg)) / (72.0 * float(serum_creatinine_mg_dl))
        if gender == Gender.FEMALE:
            base *= 0.85
        return round(base, 2)

    @staticmethod
    def calculate_ckd_epi_2021(age_years: int, serum_creatinine_mg_dl: float, gender: Gender) -> float:
        if serum_creatinine_mg_dl <= 0 or age_years <= 0:
            raise ValueError("Serum creatinine and age must be positive.")
        is_female = (gender == Gender.FEMALE)
        kappa = 0.7 if is_female else 0.9
        alpha = -0.241 if is_female else -0.302
        gender_mult = 1.012 if is_female else 1.0
        scr_k = serum_creatinine_mg_dl / kappa
        min_term = min(scr_k, 1.0) ** alpha
        max_term = max(scr_k, 1.0) ** (-1.200)
        age_term = 0.9938 ** age_years
        egfr = 142.0 * min_term * max_term * age_term * gender_mult
        return round(egfr, 1)

    @staticmethod
    def get_ckd_stage(egfr: float) -> Tuple[str, str]:
        if egfr >= 90.0:
            return "Stage G1", "Normal or high renal function."
        elif egfr >= 60.0:
            return "Stage G2", "Mildly decreased renal function."
        elif egfr >= 45.0:
            return "Stage G3a", "Mild to moderately decreased renal function."
        elif egfr >= 30.0:
            return "Stage G3b", "Moderately to severely decreased renal function."
        elif egfr >= 15.0:
            return "Stage G4", "Severely decreased renal function."
        else:
            return "Stage G5", "Kidney failure (End-Stage Renal Disease)."

    @staticmethod
    def calculate_bsa(height_cm: float, weight_kg: float, formula: FormulaBSA = FormulaBSA.MOSTELLER) -> float:
        if height_cm <= 0 or weight_kg <= 0:
            raise ValueError("Height and weight must be positive.")
        if formula == FormulaBSA.DUBOIS:
            return round(0.007184 * (height_cm ** 0.725) * (weight_kg ** 0.425), 2)
        elif formula == FormulaBSA.HAYCOCK:
            return round(0.024265 * (height_cm ** 0.3964) * (weight_kg ** 0.5378), 2)
        return round(math.sqrt((height_cm * weight_kg) / 3600.0), 2)

    @staticmethod
    def calculate_ibw(height_cm: float, gender: Gender) -> float:
        height_inches = height_cm / 2.54
        if height_inches <= 60.0:
            return 50.0 if gender == Gender.MALE else 45.5
        inches_over_5ft = height_inches - 60.0
        return round((50.0 if gender == Gender.MALE else 45.5) + (2.3 * inches_over_5ft), 1)

    @staticmethod
    def calculate_cha2ds2_vasc(congestive_heart_failure: bool, hypertension: bool, age_years: int, diabetes: bool, stroke_tia_thromboembolism: bool, vascular_disease: bool, is_female: bool) -> StrokeRiskResult:
        score = 0
        if congestive_heart_failure: score += 1
        if hypertension: score += 1
        if age_years >= 75: score += 2
        elif age_years >= 65: score += 1
        if diabetes: score += 1
        if stroke_tia_thromboembolism: score += 2
        if vascular_disease: score += 1
        if is_female: score += 1
        risk_table = {0: 0.2, 1: 0.6, 2: 2.2, 3: 3.2, 4: 4.8, 5: 7.2, 6: 9.7, 7: 11.2, 8: 12.5, 9: 15.2}
        annual_risk = risk_table.get(score, 15.2)
        threshold = 2 if is_female else 1
        rec = "Oral anticoagulation recommended." if score >= threshold + 1 else ("Consider anticoagulation." if score == threshold else "Low risk.")
        return StrokeRiskResult(cha2ds2_vasc_score=score, annual_stroke_risk_percent=annual_risk, anticoagulation_recommendation=rec)

    @staticmethod
    def calculate_anion_gap(sodium: float, chloride: float, bicarbonate: float) -> float:
        return round(sodium - (chloride + bicarbonate), 1)

    @staticmethod
    def calculate_corrected_calcium(measured_calcium: float, serum_albumin: float) -> float:
        if serum_albumin >= 4.0: return round(measured_calcium, 2)
        return round(measured_calcium + 0.8 * (4.0 - serum_albumin), 2)

    @staticmethod
    def calculate_corrected_sodium(measured_sodium: float, serum_glucose_mg_dl: float) -> float:
        if serum_glucose_mg_dl <= 100.0: return round(measured_sodium, 1)
        return round(measured_sodium + (1.6 * ((serum_glucose_mg_dl - 100.0) / 100.0)), 1)

    @staticmethod
    def calculate_mean_arterial_pressure(systolic_bp: float, diastolic_bp: float) -> float:
        return round(diastolic_bp + ((systolic_bp - diastolic_bp) / 3.0), 1)

    @staticmethod
    def calculate_pediatric_dose_by_weight(dose_mg_per_kg: float, weight_kg: float, max_adult_dose_mg: float) -> float:
        return round(min(dose_mg_per_kg * weight_kg, max_adult_dose_mg), 2)


def clinical_calculation_benchmark_case_0001():
    """Benchmarking reference calculation 1."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=31, weight_kg=51.0, serum_creatinine_mg_dl=0.80, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=31, serum_creatinine_mg_dl=0.80, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=146.0, weight_kg=46.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=111.0, diastolic_bp=71.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=136.0, chloride=99.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0002():
    """Benchmarking reference calculation 2."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=32, weight_kg=52.0, serum_creatinine_mg_dl=0.90, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=32, serum_creatinine_mg_dl=0.90, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=147.0, weight_kg=47.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=112.0, diastolic_bp=72.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=137.0, chloride=100.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0003():
    """Benchmarking reference calculation 3."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=33, weight_kg=53.0, serum_creatinine_mg_dl=1.00, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=33, serum_creatinine_mg_dl=1.00, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=148.0, weight_kg=48.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=113.0, diastolic_bp=73.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=138.0, chloride=101.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0004():
    """Benchmarking reference calculation 4."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=34, weight_kg=54.0, serum_creatinine_mg_dl=1.10, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=34, serum_creatinine_mg_dl=1.10, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=149.0, weight_kg=49.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=114.0, diastolic_bp=74.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=139.0, chloride=102.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0005():
    """Benchmarking reference calculation 5."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=35, weight_kg=55.0, serum_creatinine_mg_dl=1.20, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=35, serum_creatinine_mg_dl=1.20, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=150.0, weight_kg=50.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=115.0, diastolic_bp=75.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=140.0, chloride=103.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0006():
    """Benchmarking reference calculation 6."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=36, weight_kg=56.0, serum_creatinine_mg_dl=1.30, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=36, serum_creatinine_mg_dl=1.30, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=151.0, weight_kg=51.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=116.0, diastolic_bp=76.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=141.0, chloride=104.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0007():
    """Benchmarking reference calculation 7."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=37, weight_kg=57.0, serum_creatinine_mg_dl=1.40, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=37, serum_creatinine_mg_dl=1.40, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=152.0, weight_kg=52.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=117.0, diastolic_bp=77.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=142.0, chloride=105.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0008():
    """Benchmarking reference calculation 8."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=38, weight_kg=58.0, serum_creatinine_mg_dl=1.50, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=38, serum_creatinine_mg_dl=1.50, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=153.0, weight_kg=53.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=118.0, diastolic_bp=78.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=143.0, chloride=98.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0009():
    """Benchmarking reference calculation 9."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=39, weight_kg=59.0, serum_creatinine_mg_dl=1.60, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=39, serum_creatinine_mg_dl=1.60, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=154.0, weight_kg=54.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=119.0, diastolic_bp=79.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=144.0, chloride=99.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0010():
    """Benchmarking reference calculation 10."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=40, weight_kg=60.0, serum_creatinine_mg_dl=1.70, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=40, serum_creatinine_mg_dl=1.70, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=155.0, weight_kg=55.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=120.0, diastolic_bp=80.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=135.0, chloride=100.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0011():
    """Benchmarking reference calculation 11."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=41, weight_kg=61.0, serum_creatinine_mg_dl=1.80, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=41, serum_creatinine_mg_dl=1.80, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=156.0, weight_kg=56.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=121.0, diastolic_bp=81.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=136.0, chloride=101.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0012():
    """Benchmarking reference calculation 12."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=42, weight_kg=62.0, serum_creatinine_mg_dl=1.90, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=42, serum_creatinine_mg_dl=1.90, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=157.0, weight_kg=57.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=122.0, diastolic_bp=82.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=137.0, chloride=102.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0013():
    """Benchmarking reference calculation 13."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=43, weight_kg=63.0, serum_creatinine_mg_dl=2.00, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=43, serum_creatinine_mg_dl=2.00, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=158.0, weight_kg=58.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=123.0, diastolic_bp=83.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=138.0, chloride=103.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0014():
    """Benchmarking reference calculation 14."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=44, weight_kg=64.0, serum_creatinine_mg_dl=2.10, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=44, serum_creatinine_mg_dl=2.10, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=159.0, weight_kg=59.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=124.0, diastolic_bp=84.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=139.0, chloride=104.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0015():
    """Benchmarking reference calculation 15."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=45, weight_kg=65.0, serum_creatinine_mg_dl=2.20, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=45, serum_creatinine_mg_dl=2.20, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=160.0, weight_kg=60.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=125.0, diastolic_bp=85.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=140.0, chloride=105.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0016():
    """Benchmarking reference calculation 16."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=46, weight_kg=66.0, serum_creatinine_mg_dl=2.30, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=46, serum_creatinine_mg_dl=2.30, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=161.0, weight_kg=61.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=126.0, diastolic_bp=86.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=141.0, chloride=98.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0017():
    """Benchmarking reference calculation 17."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=47, weight_kg=67.0, serum_creatinine_mg_dl=2.40, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=47, serum_creatinine_mg_dl=2.40, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=162.0, weight_kg=62.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=127.0, diastolic_bp=87.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=142.0, chloride=99.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0018():
    """Benchmarking reference calculation 18."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=48, weight_kg=68.0, serum_creatinine_mg_dl=2.50, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=48, serum_creatinine_mg_dl=2.50, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=163.0, weight_kg=63.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=128.0, diastolic_bp=88.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=143.0, chloride=100.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0019():
    """Benchmarking reference calculation 19."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=49, weight_kg=69.0, serum_creatinine_mg_dl=2.60, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=49, serum_creatinine_mg_dl=2.60, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=164.0, weight_kg=64.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=129.0, diastolic_bp=89.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=144.0, chloride=101.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0020():
    """Benchmarking reference calculation 20."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=50, weight_kg=70.0, serum_creatinine_mg_dl=0.70, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=50, serum_creatinine_mg_dl=0.70, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=165.0, weight_kg=65.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=130.0, diastolic_bp=90.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=135.0, chloride=102.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0021():
    """Benchmarking reference calculation 21."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=51, weight_kg=71.0, serum_creatinine_mg_dl=0.80, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=51, serum_creatinine_mg_dl=0.80, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=166.0, weight_kg=66.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=131.0, diastolic_bp=91.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=136.0, chloride=103.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0022():
    """Benchmarking reference calculation 22."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=52, weight_kg=72.0, serum_creatinine_mg_dl=0.90, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=52, serum_creatinine_mg_dl=0.90, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=167.0, weight_kg=67.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=132.0, diastolic_bp=92.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=137.0, chloride=104.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0023():
    """Benchmarking reference calculation 23."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=53, weight_kg=73.0, serum_creatinine_mg_dl=1.00, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=53, serum_creatinine_mg_dl=1.00, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=168.0, weight_kg=68.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=133.0, diastolic_bp=93.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=138.0, chloride=105.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0024():
    """Benchmarking reference calculation 24."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=54, weight_kg=74.0, serum_creatinine_mg_dl=1.10, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=54, serum_creatinine_mg_dl=1.10, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=169.0, weight_kg=69.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=134.0, diastolic_bp=94.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=139.0, chloride=98.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0025():
    """Benchmarking reference calculation 25."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=55, weight_kg=75.0, serum_creatinine_mg_dl=1.20, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=55, serum_creatinine_mg_dl=1.20, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=170.0, weight_kg=70.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=135.0, diastolic_bp=95.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=140.0, chloride=99.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0026():
    """Benchmarking reference calculation 26."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=56, weight_kg=76.0, serum_creatinine_mg_dl=1.30, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=56, serum_creatinine_mg_dl=1.30, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=171.0, weight_kg=71.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=136.0, diastolic_bp=96.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=141.0, chloride=100.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0027():
    """Benchmarking reference calculation 27."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=57, weight_kg=77.0, serum_creatinine_mg_dl=1.40, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=57, serum_creatinine_mg_dl=1.40, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=172.0, weight_kg=72.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=137.0, diastolic_bp=97.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=142.0, chloride=101.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0028():
    """Benchmarking reference calculation 28."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=58, weight_kg=78.0, serum_creatinine_mg_dl=1.50, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=58, serum_creatinine_mg_dl=1.50, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=173.0, weight_kg=73.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=138.0, diastolic_bp=98.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=143.0, chloride=102.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0029():
    """Benchmarking reference calculation 29."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=59, weight_kg=79.0, serum_creatinine_mg_dl=1.60, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=59, serum_creatinine_mg_dl=1.60, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=174.0, weight_kg=74.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=139.0, diastolic_bp=99.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=144.0, chloride=103.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0030():
    """Benchmarking reference calculation 30."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=60, weight_kg=80.0, serum_creatinine_mg_dl=1.70, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=60, serum_creatinine_mg_dl=1.70, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=175.0, weight_kg=75.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=140.0, diastolic_bp=100.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=135.0, chloride=104.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0031():
    """Benchmarking reference calculation 31."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=61, weight_kg=81.0, serum_creatinine_mg_dl=1.80, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=61, serum_creatinine_mg_dl=1.80, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=176.0, weight_kg=76.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=141.0, diastolic_bp=101.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=136.0, chloride=105.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0032():
    """Benchmarking reference calculation 32."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=62, weight_kg=82.0, serum_creatinine_mg_dl=1.90, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=62, serum_creatinine_mg_dl=1.90, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=177.0, weight_kg=77.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=142.0, diastolic_bp=102.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=137.0, chloride=98.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0033():
    """Benchmarking reference calculation 33."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=63, weight_kg=83.0, serum_creatinine_mg_dl=2.00, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=63, serum_creatinine_mg_dl=2.00, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=178.0, weight_kg=78.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=143.0, diastolic_bp=103.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=138.0, chloride=99.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0034():
    """Benchmarking reference calculation 34."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=64, weight_kg=84.0, serum_creatinine_mg_dl=2.10, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=64, serum_creatinine_mg_dl=2.10, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=179.0, weight_kg=79.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=144.0, diastolic_bp=104.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=139.0, chloride=100.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0035():
    """Benchmarking reference calculation 35."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=65, weight_kg=85.0, serum_creatinine_mg_dl=2.20, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=65, serum_creatinine_mg_dl=2.20, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=180.0, weight_kg=80.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=145.0, diastolic_bp=70.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=140.0, chloride=101.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0036():
    """Benchmarking reference calculation 36."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=66, weight_kg=86.0, serum_creatinine_mg_dl=2.30, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=66, serum_creatinine_mg_dl=2.30, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=181.0, weight_kg=81.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=146.0, diastolic_bp=71.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=141.0, chloride=102.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0037():
    """Benchmarking reference calculation 37."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=67, weight_kg=87.0, serum_creatinine_mg_dl=2.40, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=67, serum_creatinine_mg_dl=2.40, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=182.0, weight_kg=82.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=147.0, diastolic_bp=72.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=142.0, chloride=103.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0038():
    """Benchmarking reference calculation 38."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=68, weight_kg=88.0, serum_creatinine_mg_dl=2.50, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=68, serum_creatinine_mg_dl=2.50, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=183.0, weight_kg=83.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=148.0, diastolic_bp=73.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=143.0, chloride=104.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0039():
    """Benchmarking reference calculation 39."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=69, weight_kg=89.0, serum_creatinine_mg_dl=2.60, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=69, serum_creatinine_mg_dl=2.60, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=184.0, weight_kg=84.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=149.0, diastolic_bp=74.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=144.0, chloride=105.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0040():
    """Benchmarking reference calculation 40."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=70, weight_kg=90.0, serum_creatinine_mg_dl=0.70, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=70, serum_creatinine_mg_dl=0.70, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=185.0, weight_kg=85.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=150.0, diastolic_bp=75.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=135.0, chloride=98.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0041():
    """Benchmarking reference calculation 41."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=71, weight_kg=91.0, serum_creatinine_mg_dl=0.80, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=71, serum_creatinine_mg_dl=0.80, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=186.0, weight_kg=86.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=151.0, diastolic_bp=76.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=136.0, chloride=99.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0042():
    """Benchmarking reference calculation 42."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=72, weight_kg=92.0, serum_creatinine_mg_dl=0.90, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=72, serum_creatinine_mg_dl=0.90, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=187.0, weight_kg=87.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=152.0, diastolic_bp=77.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=137.0, chloride=100.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0043():
    """Benchmarking reference calculation 43."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=73, weight_kg=93.0, serum_creatinine_mg_dl=1.00, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=73, serum_creatinine_mg_dl=1.00, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=188.0, weight_kg=88.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=153.0, diastolic_bp=78.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=138.0, chloride=101.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0044():
    """Benchmarking reference calculation 44."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=74, weight_kg=94.0, serum_creatinine_mg_dl=1.10, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=74, serum_creatinine_mg_dl=1.10, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=189.0, weight_kg=89.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=154.0, diastolic_bp=79.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=139.0, chloride=102.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0045():
    """Benchmarking reference calculation 45."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=75, weight_kg=95.0, serum_creatinine_mg_dl=1.20, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=75, serum_creatinine_mg_dl=1.20, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=145.0, weight_kg=90.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=155.0, diastolic_bp=80.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=140.0, chloride=103.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0046():
    """Benchmarking reference calculation 46."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=76, weight_kg=96.0, serum_creatinine_mg_dl=1.30, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=76, serum_creatinine_mg_dl=1.30, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=146.0, weight_kg=91.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=156.0, diastolic_bp=81.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=141.0, chloride=104.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0047():
    """Benchmarking reference calculation 47."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=77, weight_kg=97.0, serum_creatinine_mg_dl=1.40, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=77, serum_creatinine_mg_dl=1.40, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=147.0, weight_kg=92.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=157.0, diastolic_bp=82.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=142.0, chloride=105.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0048():
    """Benchmarking reference calculation 48."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=78, weight_kg=98.0, serum_creatinine_mg_dl=1.50, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=78, serum_creatinine_mg_dl=1.50, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=148.0, weight_kg=93.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=158.0, diastolic_bp=83.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=143.0, chloride=98.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0049():
    """Benchmarking reference calculation 49."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=79, weight_kg=99.0, serum_creatinine_mg_dl=1.60, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=79, serum_creatinine_mg_dl=1.60, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=149.0, weight_kg=94.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=159.0, diastolic_bp=84.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=144.0, chloride=99.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0050():
    """Benchmarking reference calculation 50."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=80, weight_kg=100.0, serum_creatinine_mg_dl=1.70, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=80, serum_creatinine_mg_dl=1.70, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=150.0, weight_kg=95.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=160.0, diastolic_bp=85.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=135.0, chloride=100.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0051():
    """Benchmarking reference calculation 51."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=81, weight_kg=101.0, serum_creatinine_mg_dl=1.80, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=81, serum_creatinine_mg_dl=1.80, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=151.0, weight_kg=96.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=161.0, diastolic_bp=86.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=136.0, chloride=101.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0052():
    """Benchmarking reference calculation 52."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=82, weight_kg=102.0, serum_creatinine_mg_dl=1.90, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=82, serum_creatinine_mg_dl=1.90, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=152.0, weight_kg=97.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=162.0, diastolic_bp=87.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=137.0, chloride=102.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0053():
    """Benchmarking reference calculation 53."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=83, weight_kg=103.0, serum_creatinine_mg_dl=2.00, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=83, serum_creatinine_mg_dl=2.00, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=153.0, weight_kg=98.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=163.0, diastolic_bp=88.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=138.0, chloride=103.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0054():
    """Benchmarking reference calculation 54."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=84, weight_kg=104.0, serum_creatinine_mg_dl=2.10, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=84, serum_creatinine_mg_dl=2.10, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=154.0, weight_kg=99.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=164.0, diastolic_bp=89.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=139.0, chloride=104.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0055():
    """Benchmarking reference calculation 55."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=85, weight_kg=50.0, serum_creatinine_mg_dl=2.20, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=85, serum_creatinine_mg_dl=2.20, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=155.0, weight_kg=100.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=165.0, diastolic_bp=90.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=140.0, chloride=105.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0056():
    """Benchmarking reference calculation 56."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=86, weight_kg=51.0, serum_creatinine_mg_dl=2.30, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=86, serum_creatinine_mg_dl=2.30, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=156.0, weight_kg=101.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=166.0, diastolic_bp=91.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=141.0, chloride=98.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0057():
    """Benchmarking reference calculation 57."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=87, weight_kg=52.0, serum_creatinine_mg_dl=2.40, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=87, serum_creatinine_mg_dl=2.40, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=157.0, weight_kg=102.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=167.0, diastolic_bp=92.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=142.0, chloride=99.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0058():
    """Benchmarking reference calculation 58."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=88, weight_kg=53.0, serum_creatinine_mg_dl=2.50, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=88, serum_creatinine_mg_dl=2.50, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=158.0, weight_kg=103.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=168.0, diastolic_bp=93.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=143.0, chloride=100.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0059():
    """Benchmarking reference calculation 59."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=89, weight_kg=54.0, serum_creatinine_mg_dl=2.60, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=89, serum_creatinine_mg_dl=2.60, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=159.0, weight_kg=104.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=169.0, diastolic_bp=94.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=144.0, chloride=101.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0060():
    """Benchmarking reference calculation 60."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=30, weight_kg=55.0, serum_creatinine_mg_dl=0.70, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=30, serum_creatinine_mg_dl=0.70, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=160.0, weight_kg=105.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=110.0, diastolic_bp=95.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=135.0, chloride=102.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0061():
    """Benchmarking reference calculation 61."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=31, weight_kg=56.0, serum_creatinine_mg_dl=0.80, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=31, serum_creatinine_mg_dl=0.80, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=161.0, weight_kg=106.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=111.0, diastolic_bp=96.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=136.0, chloride=103.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0062():
    """Benchmarking reference calculation 62."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=32, weight_kg=57.0, serum_creatinine_mg_dl=0.90, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=32, serum_creatinine_mg_dl=0.90, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=162.0, weight_kg=107.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=112.0, diastolic_bp=97.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=137.0, chloride=104.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0063():
    """Benchmarking reference calculation 63."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=33, weight_kg=58.0, serum_creatinine_mg_dl=1.00, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=33, serum_creatinine_mg_dl=1.00, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=163.0, weight_kg=108.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=113.0, diastolic_bp=98.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=138.0, chloride=105.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0064():
    """Benchmarking reference calculation 64."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=34, weight_kg=59.0, serum_creatinine_mg_dl=1.10, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=34, serum_creatinine_mg_dl=1.10, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=164.0, weight_kg=109.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=114.0, diastolic_bp=99.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=139.0, chloride=98.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0065():
    """Benchmarking reference calculation 65."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=35, weight_kg=60.0, serum_creatinine_mg_dl=1.20, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=35, serum_creatinine_mg_dl=1.20, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=165.0, weight_kg=45.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=115.0, diastolic_bp=100.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=140.0, chloride=99.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0066():
    """Benchmarking reference calculation 66."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=36, weight_kg=61.0, serum_creatinine_mg_dl=1.30, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=36, serum_creatinine_mg_dl=1.30, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=166.0, weight_kg=46.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=116.0, diastolic_bp=101.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=141.0, chloride=100.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0067():
    """Benchmarking reference calculation 67."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=37, weight_kg=62.0, serum_creatinine_mg_dl=1.40, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=37, serum_creatinine_mg_dl=1.40, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=167.0, weight_kg=47.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=117.0, diastolic_bp=102.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=142.0, chloride=101.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0068():
    """Benchmarking reference calculation 68."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=38, weight_kg=63.0, serum_creatinine_mg_dl=1.50, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=38, serum_creatinine_mg_dl=1.50, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=168.0, weight_kg=48.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=118.0, diastolic_bp=103.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=143.0, chloride=102.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0069():
    """Benchmarking reference calculation 69."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=39, weight_kg=64.0, serum_creatinine_mg_dl=1.60, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=39, serum_creatinine_mg_dl=1.60, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=169.0, weight_kg=49.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=119.0, diastolic_bp=104.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=144.0, chloride=103.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0070():
    """Benchmarking reference calculation 70."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=40, weight_kg=65.0, serum_creatinine_mg_dl=1.70, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=40, serum_creatinine_mg_dl=1.70, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=170.0, weight_kg=50.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=120.0, diastolic_bp=70.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=135.0, chloride=104.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0071():
    """Benchmarking reference calculation 71."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=41, weight_kg=66.0, serum_creatinine_mg_dl=1.80, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=41, serum_creatinine_mg_dl=1.80, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=171.0, weight_kg=51.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=121.0, diastolic_bp=71.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=136.0, chloride=105.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0072():
    """Benchmarking reference calculation 72."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=42, weight_kg=67.0, serum_creatinine_mg_dl=1.90, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=42, serum_creatinine_mg_dl=1.90, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=172.0, weight_kg=52.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=122.0, diastolic_bp=72.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=137.0, chloride=98.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0073():
    """Benchmarking reference calculation 73."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=43, weight_kg=68.0, serum_creatinine_mg_dl=2.00, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=43, serum_creatinine_mg_dl=2.00, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=173.0, weight_kg=53.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=123.0, diastolic_bp=73.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=138.0, chloride=99.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0074():
    """Benchmarking reference calculation 74."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=44, weight_kg=69.0, serum_creatinine_mg_dl=2.10, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=44, serum_creatinine_mg_dl=2.10, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=174.0, weight_kg=54.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=124.0, diastolic_bp=74.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=139.0, chloride=100.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0075():
    """Benchmarking reference calculation 75."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=45, weight_kg=70.0, serum_creatinine_mg_dl=2.20, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=45, serum_creatinine_mg_dl=2.20, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=175.0, weight_kg=55.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=125.0, diastolic_bp=75.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=140.0, chloride=101.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0076():
    """Benchmarking reference calculation 76."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=46, weight_kg=71.0, serum_creatinine_mg_dl=2.30, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=46, serum_creatinine_mg_dl=2.30, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=176.0, weight_kg=56.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=126.0, diastolic_bp=76.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=141.0, chloride=102.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0077():
    """Benchmarking reference calculation 77."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=47, weight_kg=72.0, serum_creatinine_mg_dl=2.40, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=47, serum_creatinine_mg_dl=2.40, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=177.0, weight_kg=57.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=127.0, diastolic_bp=77.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=142.0, chloride=103.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0078():
    """Benchmarking reference calculation 78."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=48, weight_kg=73.0, serum_creatinine_mg_dl=2.50, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=48, serum_creatinine_mg_dl=2.50, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=178.0, weight_kg=58.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=128.0, diastolic_bp=78.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=143.0, chloride=104.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0079():
    """Benchmarking reference calculation 79."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=49, weight_kg=74.0, serum_creatinine_mg_dl=2.60, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=49, serum_creatinine_mg_dl=2.60, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=179.0, weight_kg=59.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=129.0, diastolic_bp=79.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=144.0, chloride=105.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0080():
    """Benchmarking reference calculation 80."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=50, weight_kg=75.0, serum_creatinine_mg_dl=0.70, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=50, serum_creatinine_mg_dl=0.70, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=180.0, weight_kg=60.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=130.0, diastolic_bp=80.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=135.0, chloride=98.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0081():
    """Benchmarking reference calculation 81."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=51, weight_kg=76.0, serum_creatinine_mg_dl=0.80, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=51, serum_creatinine_mg_dl=0.80, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=181.0, weight_kg=61.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=131.0, diastolic_bp=81.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=136.0, chloride=99.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0082():
    """Benchmarking reference calculation 82."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=52, weight_kg=77.0, serum_creatinine_mg_dl=0.90, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=52, serum_creatinine_mg_dl=0.90, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=182.0, weight_kg=62.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=132.0, diastolic_bp=82.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=137.0, chloride=100.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0083():
    """Benchmarking reference calculation 83."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=53, weight_kg=78.0, serum_creatinine_mg_dl=1.00, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=53, serum_creatinine_mg_dl=1.00, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=183.0, weight_kg=63.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=133.0, diastolic_bp=83.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=138.0, chloride=101.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0084():
    """Benchmarking reference calculation 84."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=54, weight_kg=79.0, serum_creatinine_mg_dl=1.10, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=54, serum_creatinine_mg_dl=1.10, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=184.0, weight_kg=64.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=134.0, diastolic_bp=84.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=139.0, chloride=102.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0085():
    """Benchmarking reference calculation 85."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=55, weight_kg=80.0, serum_creatinine_mg_dl=1.20, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=55, serum_creatinine_mg_dl=1.20, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=185.0, weight_kg=65.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=135.0, diastolic_bp=85.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=140.0, chloride=103.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0086():
    """Benchmarking reference calculation 86."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=56, weight_kg=81.0, serum_creatinine_mg_dl=1.30, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=56, serum_creatinine_mg_dl=1.30, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=186.0, weight_kg=66.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=136.0, diastolic_bp=86.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=141.0, chloride=104.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0087():
    """Benchmarking reference calculation 87."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=57, weight_kg=82.0, serum_creatinine_mg_dl=1.40, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=57, serum_creatinine_mg_dl=1.40, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=187.0, weight_kg=67.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=137.0, diastolic_bp=87.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=142.0, chloride=105.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0088():
    """Benchmarking reference calculation 88."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=58, weight_kg=83.0, serum_creatinine_mg_dl=1.50, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=58, serum_creatinine_mg_dl=1.50, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=188.0, weight_kg=68.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=138.0, diastolic_bp=88.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=143.0, chloride=98.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0089():
    """Benchmarking reference calculation 89."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=59, weight_kg=84.0, serum_creatinine_mg_dl=1.60, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=59, serum_creatinine_mg_dl=1.60, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=189.0, weight_kg=69.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=139.0, diastolic_bp=89.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=144.0, chloride=99.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0090():
    """Benchmarking reference calculation 90."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=60, weight_kg=85.0, serum_creatinine_mg_dl=1.70, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=60, serum_creatinine_mg_dl=1.70, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=145.0, weight_kg=70.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=140.0, diastolic_bp=90.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=135.0, chloride=100.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0091():
    """Benchmarking reference calculation 91."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=61, weight_kg=86.0, serum_creatinine_mg_dl=1.80, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=61, serum_creatinine_mg_dl=1.80, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=146.0, weight_kg=71.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=141.0, diastolic_bp=91.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=136.0, chloride=101.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0092():
    """Benchmarking reference calculation 92."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=62, weight_kg=87.0, serum_creatinine_mg_dl=1.90, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=62, serum_creatinine_mg_dl=1.90, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=147.0, weight_kg=72.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=142.0, diastolic_bp=92.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=137.0, chloride=102.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0093():
    """Benchmarking reference calculation 93."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=63, weight_kg=88.0, serum_creatinine_mg_dl=2.00, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=63, serum_creatinine_mg_dl=2.00, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=148.0, weight_kg=73.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=143.0, diastolic_bp=93.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=138.0, chloride=103.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0094():
    """Benchmarking reference calculation 94."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=64, weight_kg=89.0, serum_creatinine_mg_dl=2.10, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=64, serum_creatinine_mg_dl=2.10, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=149.0, weight_kg=74.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=144.0, diastolic_bp=94.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=139.0, chloride=104.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0095():
    """Benchmarking reference calculation 95."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=65, weight_kg=90.0, serum_creatinine_mg_dl=2.20, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=65, serum_creatinine_mg_dl=2.20, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=150.0, weight_kg=75.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=145.0, diastolic_bp=95.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=140.0, chloride=105.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0096():
    """Benchmarking reference calculation 96."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=66, weight_kg=91.0, serum_creatinine_mg_dl=2.30, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=66, serum_creatinine_mg_dl=2.30, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=151.0, weight_kg=76.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=146.0, diastolic_bp=96.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=141.0, chloride=98.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0097():
    """Benchmarking reference calculation 97."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=67, weight_kg=92.0, serum_creatinine_mg_dl=2.40, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=67, serum_creatinine_mg_dl=2.40, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=152.0, weight_kg=77.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=147.0, diastolic_bp=97.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=142.0, chloride=99.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0098():
    """Benchmarking reference calculation 98."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=68, weight_kg=93.0, serum_creatinine_mg_dl=2.50, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=68, serum_creatinine_mg_dl=2.50, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=153.0, weight_kg=78.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=148.0, diastolic_bp=98.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=143.0, chloride=100.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0099():
    """Benchmarking reference calculation 99."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=69, weight_kg=94.0, serum_creatinine_mg_dl=2.60, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=69, serum_creatinine_mg_dl=2.60, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=154.0, weight_kg=79.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=149.0, diastolic_bp=99.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=144.0, chloride=101.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0100():
    """Benchmarking reference calculation 100."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=70, weight_kg=95.0, serum_creatinine_mg_dl=0.70, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=70, serum_creatinine_mg_dl=0.70, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=155.0, weight_kg=80.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=150.0, diastolic_bp=100.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=135.0, chloride=102.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0101():
    """Benchmarking reference calculation 101."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=71, weight_kg=96.0, serum_creatinine_mg_dl=0.80, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=71, serum_creatinine_mg_dl=0.80, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=156.0, weight_kg=81.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=151.0, diastolic_bp=101.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=136.0, chloride=103.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0102():
    """Benchmarking reference calculation 102."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=72, weight_kg=97.0, serum_creatinine_mg_dl=0.90, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=72, serum_creatinine_mg_dl=0.90, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=157.0, weight_kg=82.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=152.0, diastolic_bp=102.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=137.0, chloride=104.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0103():
    """Benchmarking reference calculation 103."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=73, weight_kg=98.0, serum_creatinine_mg_dl=1.00, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=73, serum_creatinine_mg_dl=1.00, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=158.0, weight_kg=83.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=153.0, diastolic_bp=103.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=138.0, chloride=105.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0104():
    """Benchmarking reference calculation 104."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=74, weight_kg=99.0, serum_creatinine_mg_dl=1.10, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=74, serum_creatinine_mg_dl=1.10, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=159.0, weight_kg=84.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=154.0, diastolic_bp=104.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=139.0, chloride=98.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0105():
    """Benchmarking reference calculation 105."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=75, weight_kg=100.0, serum_creatinine_mg_dl=1.20, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=75, serum_creatinine_mg_dl=1.20, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=160.0, weight_kg=85.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=155.0, diastolic_bp=70.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=140.0, chloride=99.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0106():
    """Benchmarking reference calculation 106."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=76, weight_kg=101.0, serum_creatinine_mg_dl=1.30, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=76, serum_creatinine_mg_dl=1.30, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=161.0, weight_kg=86.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=156.0, diastolic_bp=71.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=141.0, chloride=100.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0107():
    """Benchmarking reference calculation 107."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=77, weight_kg=102.0, serum_creatinine_mg_dl=1.40, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=77, serum_creatinine_mg_dl=1.40, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=162.0, weight_kg=87.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=157.0, diastolic_bp=72.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=142.0, chloride=101.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0108():
    """Benchmarking reference calculation 108."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=78, weight_kg=103.0, serum_creatinine_mg_dl=1.50, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=78, serum_creatinine_mg_dl=1.50, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=163.0, weight_kg=88.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=158.0, diastolic_bp=73.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=143.0, chloride=102.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0109():
    """Benchmarking reference calculation 109."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=79, weight_kg=104.0, serum_creatinine_mg_dl=1.60, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=79, serum_creatinine_mg_dl=1.60, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=164.0, weight_kg=89.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=159.0, diastolic_bp=74.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=144.0, chloride=103.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0110():
    """Benchmarking reference calculation 110."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=80, weight_kg=50.0, serum_creatinine_mg_dl=1.70, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=80, serum_creatinine_mg_dl=1.70, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=165.0, weight_kg=90.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=160.0, diastolic_bp=75.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=135.0, chloride=104.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0111():
    """Benchmarking reference calculation 111."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=81, weight_kg=51.0, serum_creatinine_mg_dl=1.80, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=81, serum_creatinine_mg_dl=1.80, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=166.0, weight_kg=91.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=161.0, diastolic_bp=76.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=136.0, chloride=105.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0112():
    """Benchmarking reference calculation 112."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=82, weight_kg=52.0, serum_creatinine_mg_dl=1.90, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=82, serum_creatinine_mg_dl=1.90, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=167.0, weight_kg=92.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=162.0, diastolic_bp=77.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=137.0, chloride=98.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0113():
    """Benchmarking reference calculation 113."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=83, weight_kg=53.0, serum_creatinine_mg_dl=2.00, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=83, serum_creatinine_mg_dl=2.00, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=168.0, weight_kg=93.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=163.0, diastolic_bp=78.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=138.0, chloride=99.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0114():
    """Benchmarking reference calculation 114."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=84, weight_kg=54.0, serum_creatinine_mg_dl=2.10, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=84, serum_creatinine_mg_dl=2.10, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=169.0, weight_kg=94.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=164.0, diastolic_bp=79.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=139.0, chloride=100.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0115():
    """Benchmarking reference calculation 115."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=85, weight_kg=55.0, serum_creatinine_mg_dl=2.20, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=85, serum_creatinine_mg_dl=2.20, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=170.0, weight_kg=95.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=165.0, diastolic_bp=80.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=140.0, chloride=101.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0116():
    """Benchmarking reference calculation 116."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=86, weight_kg=56.0, serum_creatinine_mg_dl=2.30, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=86, serum_creatinine_mg_dl=2.30, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=171.0, weight_kg=96.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=166.0, diastolic_bp=81.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=141.0, chloride=102.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0117():
    """Benchmarking reference calculation 117."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=87, weight_kg=57.0, serum_creatinine_mg_dl=2.40, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=87, serum_creatinine_mg_dl=2.40, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=172.0, weight_kg=97.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=167.0, diastolic_bp=82.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=142.0, chloride=103.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0118():
    """Benchmarking reference calculation 118."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=88, weight_kg=58.0, serum_creatinine_mg_dl=2.50, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=88, serum_creatinine_mg_dl=2.50, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=173.0, weight_kg=98.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=168.0, diastolic_bp=83.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=143.0, chloride=104.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0119():
    """Benchmarking reference calculation 119."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=89, weight_kg=59.0, serum_creatinine_mg_dl=2.60, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=89, serum_creatinine_mg_dl=2.60, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=174.0, weight_kg=99.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=169.0, diastolic_bp=84.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=144.0, chloride=105.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0120():
    """Benchmarking reference calculation 120."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=30, weight_kg=60.0, serum_creatinine_mg_dl=0.70, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=30, serum_creatinine_mg_dl=0.70, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=175.0, weight_kg=100.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=110.0, diastolic_bp=85.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=135.0, chloride=98.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0121():
    """Benchmarking reference calculation 121."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=31, weight_kg=61.0, serum_creatinine_mg_dl=0.80, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=31, serum_creatinine_mg_dl=0.80, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=176.0, weight_kg=101.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=111.0, diastolic_bp=86.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=136.0, chloride=99.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0122():
    """Benchmarking reference calculation 122."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=32, weight_kg=62.0, serum_creatinine_mg_dl=0.90, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=32, serum_creatinine_mg_dl=0.90, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=177.0, weight_kg=102.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=112.0, diastolic_bp=87.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=137.0, chloride=100.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0123():
    """Benchmarking reference calculation 123."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=33, weight_kg=63.0, serum_creatinine_mg_dl=1.00, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=33, serum_creatinine_mg_dl=1.00, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=178.0, weight_kg=103.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=113.0, diastolic_bp=88.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=138.0, chloride=101.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0124():
    """Benchmarking reference calculation 124."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=34, weight_kg=64.0, serum_creatinine_mg_dl=1.10, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=34, serum_creatinine_mg_dl=1.10, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=179.0, weight_kg=104.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=114.0, diastolic_bp=89.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=139.0, chloride=102.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0125():
    """Benchmarking reference calculation 125."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=35, weight_kg=65.0, serum_creatinine_mg_dl=1.20, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=35, serum_creatinine_mg_dl=1.20, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=180.0, weight_kg=105.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=115.0, diastolic_bp=90.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=140.0, chloride=103.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0126():
    """Benchmarking reference calculation 126."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=36, weight_kg=66.0, serum_creatinine_mg_dl=1.30, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=36, serum_creatinine_mg_dl=1.30, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=181.0, weight_kg=106.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=116.0, diastolic_bp=91.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=141.0, chloride=104.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0127():
    """Benchmarking reference calculation 127."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=37, weight_kg=67.0, serum_creatinine_mg_dl=1.40, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=37, serum_creatinine_mg_dl=1.40, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=182.0, weight_kg=107.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=117.0, diastolic_bp=92.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=142.0, chloride=105.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0128():
    """Benchmarking reference calculation 128."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=38, weight_kg=68.0, serum_creatinine_mg_dl=1.50, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=38, serum_creatinine_mg_dl=1.50, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=183.0, weight_kg=108.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=118.0, diastolic_bp=93.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=143.0, chloride=98.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0129():
    """Benchmarking reference calculation 129."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=39, weight_kg=69.0, serum_creatinine_mg_dl=1.60, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=39, serum_creatinine_mg_dl=1.60, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=184.0, weight_kg=109.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=119.0, diastolic_bp=94.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=144.0, chloride=99.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0130():
    """Benchmarking reference calculation 130."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=40, weight_kg=70.0, serum_creatinine_mg_dl=1.70, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=40, serum_creatinine_mg_dl=1.70, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=185.0, weight_kg=45.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=120.0, diastolic_bp=95.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=135.0, chloride=100.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0131():
    """Benchmarking reference calculation 131."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=41, weight_kg=71.0, serum_creatinine_mg_dl=1.80, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=41, serum_creatinine_mg_dl=1.80, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=186.0, weight_kg=46.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=121.0, diastolic_bp=96.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=136.0, chloride=101.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0132():
    """Benchmarking reference calculation 132."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=42, weight_kg=72.0, serum_creatinine_mg_dl=1.90, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=42, serum_creatinine_mg_dl=1.90, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=187.0, weight_kg=47.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=122.0, diastolic_bp=97.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=137.0, chloride=102.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0133():
    """Benchmarking reference calculation 133."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=43, weight_kg=73.0, serum_creatinine_mg_dl=2.00, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=43, serum_creatinine_mg_dl=2.00, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=188.0, weight_kg=48.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=123.0, diastolic_bp=98.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=138.0, chloride=103.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0134():
    """Benchmarking reference calculation 134."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=44, weight_kg=74.0, serum_creatinine_mg_dl=2.10, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=44, serum_creatinine_mg_dl=2.10, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=189.0, weight_kg=49.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=124.0, diastolic_bp=99.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=139.0, chloride=104.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0135():
    """Benchmarking reference calculation 135."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=45, weight_kg=75.0, serum_creatinine_mg_dl=2.20, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=45, serum_creatinine_mg_dl=2.20, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=145.0, weight_kg=50.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=125.0, diastolic_bp=100.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=140.0, chloride=105.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0136():
    """Benchmarking reference calculation 136."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=46, weight_kg=76.0, serum_creatinine_mg_dl=2.30, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=46, serum_creatinine_mg_dl=2.30, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=146.0, weight_kg=51.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=126.0, diastolic_bp=101.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=141.0, chloride=98.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0137():
    """Benchmarking reference calculation 137."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=47, weight_kg=77.0, serum_creatinine_mg_dl=2.40, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=47, serum_creatinine_mg_dl=2.40, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=147.0, weight_kg=52.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=127.0, diastolic_bp=102.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=142.0, chloride=99.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0138():
    """Benchmarking reference calculation 138."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=48, weight_kg=78.0, serum_creatinine_mg_dl=2.50, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=48, serum_creatinine_mg_dl=2.50, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=148.0, weight_kg=53.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=128.0, diastolic_bp=103.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=143.0, chloride=100.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0139():
    """Benchmarking reference calculation 139."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=49, weight_kg=79.0, serum_creatinine_mg_dl=2.60, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=49, serum_creatinine_mg_dl=2.60, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=149.0, weight_kg=54.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=129.0, diastolic_bp=104.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=144.0, chloride=101.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0140():
    """Benchmarking reference calculation 140."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=50, weight_kg=80.0, serum_creatinine_mg_dl=0.70, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=50, serum_creatinine_mg_dl=0.70, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=150.0, weight_kg=55.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=130.0, diastolic_bp=70.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=135.0, chloride=102.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0141():
    """Benchmarking reference calculation 141."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=51, weight_kg=81.0, serum_creatinine_mg_dl=0.80, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=51, serum_creatinine_mg_dl=0.80, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=151.0, weight_kg=56.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=131.0, diastolic_bp=71.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=136.0, chloride=103.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0142():
    """Benchmarking reference calculation 142."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=52, weight_kg=82.0, serum_creatinine_mg_dl=0.90, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=52, serum_creatinine_mg_dl=0.90, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=152.0, weight_kg=57.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=132.0, diastolic_bp=72.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=137.0, chloride=104.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0143():
    """Benchmarking reference calculation 143."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=53, weight_kg=83.0, serum_creatinine_mg_dl=1.00, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=53, serum_creatinine_mg_dl=1.00, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=153.0, weight_kg=58.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=133.0, diastolic_bp=73.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=138.0, chloride=105.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0144():
    """Benchmarking reference calculation 144."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=54, weight_kg=84.0, serum_creatinine_mg_dl=1.10, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=54, serum_creatinine_mg_dl=1.10, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=154.0, weight_kg=59.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=134.0, diastolic_bp=74.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=139.0, chloride=98.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0145():
    """Benchmarking reference calculation 145."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=55, weight_kg=85.0, serum_creatinine_mg_dl=1.20, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=55, serum_creatinine_mg_dl=1.20, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=155.0, weight_kg=60.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=135.0, diastolic_bp=75.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=140.0, chloride=99.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0146():
    """Benchmarking reference calculation 146."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=56, weight_kg=86.0, serum_creatinine_mg_dl=1.30, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=56, serum_creatinine_mg_dl=1.30, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=156.0, weight_kg=61.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=136.0, diastolic_bp=76.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=141.0, chloride=100.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0147():
    """Benchmarking reference calculation 147."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=57, weight_kg=87.0, serum_creatinine_mg_dl=1.40, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=57, serum_creatinine_mg_dl=1.40, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=157.0, weight_kg=62.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=137.0, diastolic_bp=77.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=142.0, chloride=101.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0148():
    """Benchmarking reference calculation 148."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=58, weight_kg=88.0, serum_creatinine_mg_dl=1.50, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=58, serum_creatinine_mg_dl=1.50, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=158.0, weight_kg=63.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=138.0, diastolic_bp=78.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=143.0, chloride=102.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0149():
    """Benchmarking reference calculation 149."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=59, weight_kg=89.0, serum_creatinine_mg_dl=1.60, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=59, serum_creatinine_mg_dl=1.60, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=159.0, weight_kg=64.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=139.0, diastolic_bp=79.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=144.0, chloride=103.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0150():
    """Benchmarking reference calculation 150."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=60, weight_kg=90.0, serum_creatinine_mg_dl=1.70, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=60, serum_creatinine_mg_dl=1.70, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=160.0, weight_kg=65.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=140.0, diastolic_bp=80.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=135.0, chloride=104.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0151():
    """Benchmarking reference calculation 151."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=61, weight_kg=91.0, serum_creatinine_mg_dl=1.80, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=61, serum_creatinine_mg_dl=1.80, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=161.0, weight_kg=66.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=141.0, diastolic_bp=81.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=136.0, chloride=105.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0152():
    """Benchmarking reference calculation 152."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=62, weight_kg=92.0, serum_creatinine_mg_dl=1.90, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=62, serum_creatinine_mg_dl=1.90, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=162.0, weight_kg=67.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=142.0, diastolic_bp=82.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=137.0, chloride=98.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0153():
    """Benchmarking reference calculation 153."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=63, weight_kg=93.0, serum_creatinine_mg_dl=2.00, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=63, serum_creatinine_mg_dl=2.00, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=163.0, weight_kg=68.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=143.0, diastolic_bp=83.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=138.0, chloride=99.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0154():
    """Benchmarking reference calculation 154."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=64, weight_kg=94.0, serum_creatinine_mg_dl=2.10, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=64, serum_creatinine_mg_dl=2.10, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=164.0, weight_kg=69.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=144.0, diastolic_bp=84.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=139.0, chloride=100.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0155():
    """Benchmarking reference calculation 155."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=65, weight_kg=95.0, serum_creatinine_mg_dl=2.20, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=65, serum_creatinine_mg_dl=2.20, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=165.0, weight_kg=70.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=145.0, diastolic_bp=85.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=140.0, chloride=101.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0156():
    """Benchmarking reference calculation 156."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=66, weight_kg=96.0, serum_creatinine_mg_dl=2.30, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=66, serum_creatinine_mg_dl=2.30, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=166.0, weight_kg=71.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=146.0, diastolic_bp=86.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=141.0, chloride=102.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0157():
    """Benchmarking reference calculation 157."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=67, weight_kg=97.0, serum_creatinine_mg_dl=2.40, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=67, serum_creatinine_mg_dl=2.40, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=167.0, weight_kg=72.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=147.0, diastolic_bp=87.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=142.0, chloride=103.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0158():
    """Benchmarking reference calculation 158."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=68, weight_kg=98.0, serum_creatinine_mg_dl=2.50, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=68, serum_creatinine_mg_dl=2.50, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=168.0, weight_kg=73.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=148.0, diastolic_bp=88.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=143.0, chloride=104.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0159():
    """Benchmarking reference calculation 159."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=69, weight_kg=99.0, serum_creatinine_mg_dl=2.60, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=69, serum_creatinine_mg_dl=2.60, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=169.0, weight_kg=74.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=149.0, diastolic_bp=89.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=144.0, chloride=105.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0160():
    """Benchmarking reference calculation 160."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=70, weight_kg=100.0, serum_creatinine_mg_dl=0.70, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=70, serum_creatinine_mg_dl=0.70, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=170.0, weight_kg=75.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=150.0, diastolic_bp=90.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=135.0, chloride=98.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0161():
    """Benchmarking reference calculation 161."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=71, weight_kg=101.0, serum_creatinine_mg_dl=0.80, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=71, serum_creatinine_mg_dl=0.80, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=171.0, weight_kg=76.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=151.0, diastolic_bp=91.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=136.0, chloride=99.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0162():
    """Benchmarking reference calculation 162."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=72, weight_kg=102.0, serum_creatinine_mg_dl=0.90, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=72, serum_creatinine_mg_dl=0.90, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=172.0, weight_kg=77.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=152.0, diastolic_bp=92.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=137.0, chloride=100.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0163():
    """Benchmarking reference calculation 163."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=73, weight_kg=103.0, serum_creatinine_mg_dl=1.00, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=73, serum_creatinine_mg_dl=1.00, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=173.0, weight_kg=78.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=153.0, diastolic_bp=93.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=138.0, chloride=101.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0164():
    """Benchmarking reference calculation 164."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=74, weight_kg=104.0, serum_creatinine_mg_dl=1.10, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=74, serum_creatinine_mg_dl=1.10, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=174.0, weight_kg=79.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=154.0, diastolic_bp=94.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=139.0, chloride=102.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0165():
    """Benchmarking reference calculation 165."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=75, weight_kg=50.0, serum_creatinine_mg_dl=1.20, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=75, serum_creatinine_mg_dl=1.20, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=175.0, weight_kg=80.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=155.0, diastolic_bp=95.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=140.0, chloride=103.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0166():
    """Benchmarking reference calculation 166."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=76, weight_kg=51.0, serum_creatinine_mg_dl=1.30, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=76, serum_creatinine_mg_dl=1.30, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=176.0, weight_kg=81.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=156.0, diastolic_bp=96.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=141.0, chloride=104.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0167():
    """Benchmarking reference calculation 167."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=77, weight_kg=52.0, serum_creatinine_mg_dl=1.40, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=77, serum_creatinine_mg_dl=1.40, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=177.0, weight_kg=82.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=157.0, diastolic_bp=97.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=142.0, chloride=105.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0168():
    """Benchmarking reference calculation 168."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=78, weight_kg=53.0, serum_creatinine_mg_dl=1.50, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=78, serum_creatinine_mg_dl=1.50, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=178.0, weight_kg=83.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=158.0, diastolic_bp=98.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=143.0, chloride=98.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0169():
    """Benchmarking reference calculation 169."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=79, weight_kg=54.0, serum_creatinine_mg_dl=1.60, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=79, serum_creatinine_mg_dl=1.60, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=179.0, weight_kg=84.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=159.0, diastolic_bp=99.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=144.0, chloride=99.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0170():
    """Benchmarking reference calculation 170."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=80, weight_kg=55.0, serum_creatinine_mg_dl=1.70, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=80, serum_creatinine_mg_dl=1.70, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=180.0, weight_kg=85.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=160.0, diastolic_bp=100.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=135.0, chloride=100.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0171():
    """Benchmarking reference calculation 171."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=81, weight_kg=56.0, serum_creatinine_mg_dl=1.80, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=81, serum_creatinine_mg_dl=1.80, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=181.0, weight_kg=86.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=161.0, diastolic_bp=101.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=136.0, chloride=101.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0172():
    """Benchmarking reference calculation 172."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=82, weight_kg=57.0, serum_creatinine_mg_dl=1.90, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=82, serum_creatinine_mg_dl=1.90, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=182.0, weight_kg=87.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=162.0, diastolic_bp=102.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=137.0, chloride=102.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0173():
    """Benchmarking reference calculation 173."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=83, weight_kg=58.0, serum_creatinine_mg_dl=2.00, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=83, serum_creatinine_mg_dl=2.00, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=183.0, weight_kg=88.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=163.0, diastolic_bp=103.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=138.0, chloride=103.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0174():
    """Benchmarking reference calculation 174."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=84, weight_kg=59.0, serum_creatinine_mg_dl=2.10, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=84, serum_creatinine_mg_dl=2.10, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=184.0, weight_kg=89.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=164.0, diastolic_bp=104.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=139.0, chloride=104.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0175():
    """Benchmarking reference calculation 175."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=85, weight_kg=60.0, serum_creatinine_mg_dl=2.20, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=85, serum_creatinine_mg_dl=2.20, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=185.0, weight_kg=90.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=165.0, diastolic_bp=70.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=140.0, chloride=105.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0176():
    """Benchmarking reference calculation 176."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=86, weight_kg=61.0, serum_creatinine_mg_dl=2.30, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=86, serum_creatinine_mg_dl=2.30, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=186.0, weight_kg=91.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=166.0, diastolic_bp=71.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=141.0, chloride=98.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0177():
    """Benchmarking reference calculation 177."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=87, weight_kg=62.0, serum_creatinine_mg_dl=2.40, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=87, serum_creatinine_mg_dl=2.40, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=187.0, weight_kg=92.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=167.0, diastolic_bp=72.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=142.0, chloride=99.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0178():
    """Benchmarking reference calculation 178."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=88, weight_kg=63.0, serum_creatinine_mg_dl=2.50, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=88, serum_creatinine_mg_dl=2.50, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=188.0, weight_kg=93.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=168.0, diastolic_bp=73.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=143.0, chloride=100.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0179():
    """Benchmarking reference calculation 179."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=89, weight_kg=64.0, serum_creatinine_mg_dl=2.60, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=89, serum_creatinine_mg_dl=2.60, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=189.0, weight_kg=94.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=169.0, diastolic_bp=74.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=144.0, chloride=101.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0180():
    """Benchmarking reference calculation 180."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=30, weight_kg=65.0, serum_creatinine_mg_dl=0.70, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=30, serum_creatinine_mg_dl=0.70, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=145.0, weight_kg=95.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=110.0, diastolic_bp=75.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=135.0, chloride=102.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0181():
    """Benchmarking reference calculation 181."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=31, weight_kg=66.0, serum_creatinine_mg_dl=0.80, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=31, serum_creatinine_mg_dl=0.80, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=146.0, weight_kg=96.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=111.0, diastolic_bp=76.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=136.0, chloride=103.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0182():
    """Benchmarking reference calculation 182."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=32, weight_kg=67.0, serum_creatinine_mg_dl=0.90, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=32, serum_creatinine_mg_dl=0.90, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=147.0, weight_kg=97.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=112.0, diastolic_bp=77.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=137.0, chloride=104.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0183():
    """Benchmarking reference calculation 183."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=33, weight_kg=68.0, serum_creatinine_mg_dl=1.00, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=33, serum_creatinine_mg_dl=1.00, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=148.0, weight_kg=98.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=113.0, diastolic_bp=78.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=138.0, chloride=105.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0184():
    """Benchmarking reference calculation 184."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=34, weight_kg=69.0, serum_creatinine_mg_dl=1.10, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=34, serum_creatinine_mg_dl=1.10, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=149.0, weight_kg=99.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=114.0, diastolic_bp=79.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=139.0, chloride=98.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0185():
    """Benchmarking reference calculation 185."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=35, weight_kg=70.0, serum_creatinine_mg_dl=1.20, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=35, serum_creatinine_mg_dl=1.20, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=150.0, weight_kg=100.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=115.0, diastolic_bp=80.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=140.0, chloride=99.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0186():
    """Benchmarking reference calculation 186."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=36, weight_kg=71.0, serum_creatinine_mg_dl=1.30, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=36, serum_creatinine_mg_dl=1.30, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=151.0, weight_kg=101.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=116.0, diastolic_bp=81.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=141.0, chloride=100.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0187():
    """Benchmarking reference calculation 187."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=37, weight_kg=72.0, serum_creatinine_mg_dl=1.40, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=37, serum_creatinine_mg_dl=1.40, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=152.0, weight_kg=102.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=117.0, diastolic_bp=82.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=142.0, chloride=101.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0188():
    """Benchmarking reference calculation 188."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=38, weight_kg=73.0, serum_creatinine_mg_dl=1.50, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=38, serum_creatinine_mg_dl=1.50, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=153.0, weight_kg=103.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=118.0, diastolic_bp=83.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=143.0, chloride=102.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0189():
    """Benchmarking reference calculation 189."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=39, weight_kg=74.0, serum_creatinine_mg_dl=1.60, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=39, serum_creatinine_mg_dl=1.60, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=154.0, weight_kg=104.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=119.0, diastolic_bp=84.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=144.0, chloride=103.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0190():
    """Benchmarking reference calculation 190."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=40, weight_kg=75.0, serum_creatinine_mg_dl=1.70, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=40, serum_creatinine_mg_dl=1.70, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=155.0, weight_kg=105.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=120.0, diastolic_bp=85.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=135.0, chloride=104.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0191():
    """Benchmarking reference calculation 191."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=41, weight_kg=76.0, serum_creatinine_mg_dl=1.80, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=41, serum_creatinine_mg_dl=1.80, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=156.0, weight_kg=106.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=121.0, diastolic_bp=86.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=136.0, chloride=105.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0192():
    """Benchmarking reference calculation 192."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=42, weight_kg=77.0, serum_creatinine_mg_dl=1.90, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=42, serum_creatinine_mg_dl=1.90, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=157.0, weight_kg=107.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=122.0, diastolic_bp=87.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=137.0, chloride=98.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0193():
    """Benchmarking reference calculation 193."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=43, weight_kg=78.0, serum_creatinine_mg_dl=2.00, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=43, serum_creatinine_mg_dl=2.00, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=158.0, weight_kg=108.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=123.0, diastolic_bp=88.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=138.0, chloride=99.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0194():
    """Benchmarking reference calculation 194."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=44, weight_kg=79.0, serum_creatinine_mg_dl=2.10, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=44, serum_creatinine_mg_dl=2.10, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=159.0, weight_kg=109.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=124.0, diastolic_bp=89.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=139.0, chloride=100.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0195():
    """Benchmarking reference calculation 195."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=45, weight_kg=80.0, serum_creatinine_mg_dl=2.20, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=45, serum_creatinine_mg_dl=2.20, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=160.0, weight_kg=45.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=125.0, diastolic_bp=90.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=140.0, chloride=101.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0196():
    """Benchmarking reference calculation 196."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=46, weight_kg=81.0, serum_creatinine_mg_dl=2.30, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=46, serum_creatinine_mg_dl=2.30, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=161.0, weight_kg=46.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=126.0, diastolic_bp=91.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=141.0, chloride=102.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0197():
    """Benchmarking reference calculation 197."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=47, weight_kg=82.0, serum_creatinine_mg_dl=2.40, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=47, serum_creatinine_mg_dl=2.40, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=162.0, weight_kg=47.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=127.0, diastolic_bp=92.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=142.0, chloride=103.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0198():
    """Benchmarking reference calculation 198."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=48, weight_kg=83.0, serum_creatinine_mg_dl=2.50, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=48, serum_creatinine_mg_dl=2.50, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=163.0, weight_kg=48.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=128.0, diastolic_bp=93.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=143.0, chloride=104.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0199():
    """Benchmarking reference calculation 199."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=49, weight_kg=84.0, serum_creatinine_mg_dl=2.60, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=49, serum_creatinine_mg_dl=2.60, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=164.0, weight_kg=49.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=129.0, diastolic_bp=94.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=144.0, chloride=105.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0200():
    """Benchmarking reference calculation 200."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=50, weight_kg=85.0, serum_creatinine_mg_dl=0.70, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=50, serum_creatinine_mg_dl=0.70, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=165.0, weight_kg=50.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=130.0, diastolic_bp=95.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=135.0, chloride=98.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0201():
    """Benchmarking reference calculation 201."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=51, weight_kg=86.0, serum_creatinine_mg_dl=0.80, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=51, serum_creatinine_mg_dl=0.80, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=166.0, weight_kg=51.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=131.0, diastolic_bp=96.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=136.0, chloride=99.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0202():
    """Benchmarking reference calculation 202."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=52, weight_kg=87.0, serum_creatinine_mg_dl=0.90, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=52, serum_creatinine_mg_dl=0.90, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=167.0, weight_kg=52.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=132.0, diastolic_bp=97.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=137.0, chloride=100.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0203():
    """Benchmarking reference calculation 203."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=53, weight_kg=88.0, serum_creatinine_mg_dl=1.00, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=53, serum_creatinine_mg_dl=1.00, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=168.0, weight_kg=53.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=133.0, diastolic_bp=98.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=138.0, chloride=101.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0204():
    """Benchmarking reference calculation 204."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=54, weight_kg=89.0, serum_creatinine_mg_dl=1.10, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=54, serum_creatinine_mg_dl=1.10, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=169.0, weight_kg=54.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=134.0, diastolic_bp=99.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=139.0, chloride=102.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0205():
    """Benchmarking reference calculation 205."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=55, weight_kg=90.0, serum_creatinine_mg_dl=1.20, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=55, serum_creatinine_mg_dl=1.20, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=170.0, weight_kg=55.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=135.0, diastolic_bp=100.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=140.0, chloride=103.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0206():
    """Benchmarking reference calculation 206."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=56, weight_kg=91.0, serum_creatinine_mg_dl=1.30, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=56, serum_creatinine_mg_dl=1.30, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=171.0, weight_kg=56.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=136.0, diastolic_bp=101.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=141.0, chloride=104.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0207():
    """Benchmarking reference calculation 207."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=57, weight_kg=92.0, serum_creatinine_mg_dl=1.40, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=57, serum_creatinine_mg_dl=1.40, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=172.0, weight_kg=57.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=137.0, diastolic_bp=102.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=142.0, chloride=105.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0208():
    """Benchmarking reference calculation 208."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=58, weight_kg=93.0, serum_creatinine_mg_dl=1.50, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=58, serum_creatinine_mg_dl=1.50, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=173.0, weight_kg=58.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=138.0, diastolic_bp=103.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=143.0, chloride=98.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0209():
    """Benchmarking reference calculation 209."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=59, weight_kg=94.0, serum_creatinine_mg_dl=1.60, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=59, serum_creatinine_mg_dl=1.60, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=174.0, weight_kg=59.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=139.0, diastolic_bp=104.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=144.0, chloride=99.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0210():
    """Benchmarking reference calculation 210."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=60, weight_kg=95.0, serum_creatinine_mg_dl=1.70, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=60, serum_creatinine_mg_dl=1.70, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=175.0, weight_kg=60.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=140.0, diastolic_bp=70.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=135.0, chloride=100.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0211():
    """Benchmarking reference calculation 211."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=61, weight_kg=96.0, serum_creatinine_mg_dl=1.80, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=61, serum_creatinine_mg_dl=1.80, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=176.0, weight_kg=61.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=141.0, diastolic_bp=71.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=136.0, chloride=101.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0212():
    """Benchmarking reference calculation 212."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=62, weight_kg=97.0, serum_creatinine_mg_dl=1.90, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=62, serum_creatinine_mg_dl=1.90, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=177.0, weight_kg=62.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=142.0, diastolic_bp=72.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=137.0, chloride=102.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0213():
    """Benchmarking reference calculation 213."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=63, weight_kg=98.0, serum_creatinine_mg_dl=2.00, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=63, serum_creatinine_mg_dl=2.00, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=178.0, weight_kg=63.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=143.0, diastolic_bp=73.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=138.0, chloride=103.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0214():
    """Benchmarking reference calculation 214."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=64, weight_kg=99.0, serum_creatinine_mg_dl=2.10, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=64, serum_creatinine_mg_dl=2.10, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=179.0, weight_kg=64.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=144.0, diastolic_bp=74.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=139.0, chloride=104.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0215():
    """Benchmarking reference calculation 215."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=65, weight_kg=100.0, serum_creatinine_mg_dl=2.20, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=65, serum_creatinine_mg_dl=2.20, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=180.0, weight_kg=65.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=145.0, diastolic_bp=75.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=140.0, chloride=105.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0216():
    """Benchmarking reference calculation 216."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=66, weight_kg=101.0, serum_creatinine_mg_dl=2.30, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=66, serum_creatinine_mg_dl=2.30, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=181.0, weight_kg=66.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=146.0, diastolic_bp=76.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=141.0, chloride=98.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0217():
    """Benchmarking reference calculation 217."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=67, weight_kg=102.0, serum_creatinine_mg_dl=2.40, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=67, serum_creatinine_mg_dl=2.40, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=182.0, weight_kg=67.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=147.0, diastolic_bp=77.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=142.0, chloride=99.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0218():
    """Benchmarking reference calculation 218."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=68, weight_kg=103.0, serum_creatinine_mg_dl=2.50, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=68, serum_creatinine_mg_dl=2.50, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=183.0, weight_kg=68.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=148.0, diastolic_bp=78.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=143.0, chloride=100.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0219():
    """Benchmarking reference calculation 219."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=69, weight_kg=104.0, serum_creatinine_mg_dl=2.60, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=69, serum_creatinine_mg_dl=2.60, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=184.0, weight_kg=69.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=149.0, diastolic_bp=79.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=144.0, chloride=101.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0220():
    """Benchmarking reference calculation 220."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=70, weight_kg=50.0, serum_creatinine_mg_dl=0.70, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=70, serum_creatinine_mg_dl=0.70, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=185.0, weight_kg=70.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=150.0, diastolic_bp=80.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=135.0, chloride=102.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0221():
    """Benchmarking reference calculation 221."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=71, weight_kg=51.0, serum_creatinine_mg_dl=0.80, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=71, serum_creatinine_mg_dl=0.80, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=186.0, weight_kg=71.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=151.0, diastolic_bp=81.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=136.0, chloride=103.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0222():
    """Benchmarking reference calculation 222."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=72, weight_kg=52.0, serum_creatinine_mg_dl=0.90, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=72, serum_creatinine_mg_dl=0.90, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=187.0, weight_kg=72.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=152.0, diastolic_bp=82.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=137.0, chloride=104.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0223():
    """Benchmarking reference calculation 223."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=73, weight_kg=53.0, serum_creatinine_mg_dl=1.00, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=73, serum_creatinine_mg_dl=1.00, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=188.0, weight_kg=73.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=153.0, diastolic_bp=83.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=138.0, chloride=105.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0224():
    """Benchmarking reference calculation 224."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=74, weight_kg=54.0, serum_creatinine_mg_dl=1.10, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=74, serum_creatinine_mg_dl=1.10, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=189.0, weight_kg=74.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=154.0, diastolic_bp=84.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=139.0, chloride=98.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0225():
    """Benchmarking reference calculation 225."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=75, weight_kg=55.0, serum_creatinine_mg_dl=1.20, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=75, serum_creatinine_mg_dl=1.20, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=145.0, weight_kg=75.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=155.0, diastolic_bp=85.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=140.0, chloride=99.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0226():
    """Benchmarking reference calculation 226."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=76, weight_kg=56.0, serum_creatinine_mg_dl=1.30, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=76, serum_creatinine_mg_dl=1.30, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=146.0, weight_kg=76.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=156.0, diastolic_bp=86.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=141.0, chloride=100.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0227():
    """Benchmarking reference calculation 227."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=77, weight_kg=57.0, serum_creatinine_mg_dl=1.40, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=77, serum_creatinine_mg_dl=1.40, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=147.0, weight_kg=77.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=157.0, diastolic_bp=87.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=142.0, chloride=101.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0228():
    """Benchmarking reference calculation 228."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=78, weight_kg=58.0, serum_creatinine_mg_dl=1.50, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=78, serum_creatinine_mg_dl=1.50, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=148.0, weight_kg=78.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=158.0, diastolic_bp=88.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=143.0, chloride=102.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0229():
    """Benchmarking reference calculation 229."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=79, weight_kg=59.0, serum_creatinine_mg_dl=1.60, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=79, serum_creatinine_mg_dl=1.60, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=149.0, weight_kg=79.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=159.0, diastolic_bp=89.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=144.0, chloride=103.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0230():
    """Benchmarking reference calculation 230."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=80, weight_kg=60.0, serum_creatinine_mg_dl=1.70, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=80, serum_creatinine_mg_dl=1.70, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=150.0, weight_kg=80.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=160.0, diastolic_bp=90.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=135.0, chloride=104.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0231():
    """Benchmarking reference calculation 231."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=81, weight_kg=61.0, serum_creatinine_mg_dl=1.80, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=81, serum_creatinine_mg_dl=1.80, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=151.0, weight_kg=81.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=161.0, diastolic_bp=91.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=136.0, chloride=105.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0232():
    """Benchmarking reference calculation 232."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=82, weight_kg=62.0, serum_creatinine_mg_dl=1.90, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=82, serum_creatinine_mg_dl=1.90, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=152.0, weight_kg=82.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=162.0, diastolic_bp=92.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=137.0, chloride=98.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0233():
    """Benchmarking reference calculation 233."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=83, weight_kg=63.0, serum_creatinine_mg_dl=2.00, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=83, serum_creatinine_mg_dl=2.00, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=153.0, weight_kg=83.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=163.0, diastolic_bp=93.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=138.0, chloride=99.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0234():
    """Benchmarking reference calculation 234."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=84, weight_kg=64.0, serum_creatinine_mg_dl=2.10, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=84, serum_creatinine_mg_dl=2.10, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=154.0, weight_kg=84.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=164.0, diastolic_bp=94.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=139.0, chloride=100.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0235():
    """Benchmarking reference calculation 235."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=85, weight_kg=65.0, serum_creatinine_mg_dl=2.20, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=85, serum_creatinine_mg_dl=2.20, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=155.0, weight_kg=85.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=165.0, diastolic_bp=95.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=140.0, chloride=101.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0236():
    """Benchmarking reference calculation 236."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=86, weight_kg=66.0, serum_creatinine_mg_dl=2.30, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=86, serum_creatinine_mg_dl=2.30, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=156.0, weight_kg=86.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=166.0, diastolic_bp=96.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=141.0, chloride=102.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0237():
    """Benchmarking reference calculation 237."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=87, weight_kg=67.0, serum_creatinine_mg_dl=2.40, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=87, serum_creatinine_mg_dl=2.40, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=157.0, weight_kg=87.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=167.0, diastolic_bp=97.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=142.0, chloride=103.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0238():
    """Benchmarking reference calculation 238."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=88, weight_kg=68.0, serum_creatinine_mg_dl=2.50, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=88, serum_creatinine_mg_dl=2.50, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=158.0, weight_kg=88.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=168.0, diastolic_bp=98.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=143.0, chloride=104.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0239():
    """Benchmarking reference calculation 239."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=89, weight_kg=69.0, serum_creatinine_mg_dl=2.60, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=89, serum_creatinine_mg_dl=2.60, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=159.0, weight_kg=89.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=169.0, diastolic_bp=99.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=144.0, chloride=105.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0240():
    """Benchmarking reference calculation 240."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=30, weight_kg=70.0, serum_creatinine_mg_dl=0.70, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=30, serum_creatinine_mg_dl=0.70, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=160.0, weight_kg=90.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=110.0, diastolic_bp=100.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=135.0, chloride=98.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0241():
    """Benchmarking reference calculation 241."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=31, weight_kg=71.0, serum_creatinine_mg_dl=0.80, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=31, serum_creatinine_mg_dl=0.80, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=161.0, weight_kg=91.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=111.0, diastolic_bp=101.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=136.0, chloride=99.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0242():
    """Benchmarking reference calculation 242."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=32, weight_kg=72.0, serum_creatinine_mg_dl=0.90, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=32, serum_creatinine_mg_dl=0.90, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=162.0, weight_kg=92.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=112.0, diastolic_bp=102.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=137.0, chloride=100.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0243():
    """Benchmarking reference calculation 243."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=33, weight_kg=73.0, serum_creatinine_mg_dl=1.00, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=33, serum_creatinine_mg_dl=1.00, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=163.0, weight_kg=93.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=113.0, diastolic_bp=103.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=138.0, chloride=101.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0244():
    """Benchmarking reference calculation 244."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=34, weight_kg=74.0, serum_creatinine_mg_dl=1.10, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=34, serum_creatinine_mg_dl=1.10, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=164.0, weight_kg=94.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=114.0, diastolic_bp=104.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=139.0, chloride=102.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0245():
    """Benchmarking reference calculation 245."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=35, weight_kg=75.0, serum_creatinine_mg_dl=1.20, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=35, serum_creatinine_mg_dl=1.20, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=165.0, weight_kg=95.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=115.0, diastolic_bp=70.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=140.0, chloride=103.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0246():
    """Benchmarking reference calculation 246."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=36, weight_kg=76.0, serum_creatinine_mg_dl=1.30, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=36, serum_creatinine_mg_dl=1.30, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=166.0, weight_kg=96.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=116.0, diastolic_bp=71.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=141.0, chloride=104.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0247():
    """Benchmarking reference calculation 247."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=37, weight_kg=77.0, serum_creatinine_mg_dl=1.40, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=37, serum_creatinine_mg_dl=1.40, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=167.0, weight_kg=97.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=117.0, diastolic_bp=72.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=142.0, chloride=105.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0248():
    """Benchmarking reference calculation 248."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=38, weight_kg=78.0, serum_creatinine_mg_dl=1.50, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=38, serum_creatinine_mg_dl=1.50, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=168.0, weight_kg=98.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=118.0, diastolic_bp=73.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=143.0, chloride=98.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0249():
    """Benchmarking reference calculation 249."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=39, weight_kg=79.0, serum_creatinine_mg_dl=1.60, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=39, serum_creatinine_mg_dl=1.60, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=169.0, weight_kg=99.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=119.0, diastolic_bp=74.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=144.0, chloride=99.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0250():
    """Benchmarking reference calculation 250."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=40, weight_kg=80.0, serum_creatinine_mg_dl=1.70, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=40, serum_creatinine_mg_dl=1.70, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=170.0, weight_kg=100.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=120.0, diastolic_bp=75.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=135.0, chloride=100.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0251():
    """Benchmarking reference calculation 251."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=41, weight_kg=81.0, serum_creatinine_mg_dl=1.80, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=41, serum_creatinine_mg_dl=1.80, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=171.0, weight_kg=101.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=121.0, diastolic_bp=76.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=136.0, chloride=101.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0252():
    """Benchmarking reference calculation 252."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=42, weight_kg=82.0, serum_creatinine_mg_dl=1.90, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=42, serum_creatinine_mg_dl=1.90, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=172.0, weight_kg=102.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=122.0, diastolic_bp=77.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=137.0, chloride=102.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0253():
    """Benchmarking reference calculation 253."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=43, weight_kg=83.0, serum_creatinine_mg_dl=2.00, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=43, serum_creatinine_mg_dl=2.00, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=173.0, weight_kg=103.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=123.0, diastolic_bp=78.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=138.0, chloride=103.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0254():
    """Benchmarking reference calculation 254."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=44, weight_kg=84.0, serum_creatinine_mg_dl=2.10, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=44, serum_creatinine_mg_dl=2.10, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=174.0, weight_kg=104.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=124.0, diastolic_bp=79.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=139.0, chloride=104.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0255():
    """Benchmarking reference calculation 255."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=45, weight_kg=85.0, serum_creatinine_mg_dl=2.20, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=45, serum_creatinine_mg_dl=2.20, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=175.0, weight_kg=105.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=125.0, diastolic_bp=80.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=140.0, chloride=105.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0256():
    """Benchmarking reference calculation 256."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=46, weight_kg=86.0, serum_creatinine_mg_dl=2.30, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=46, serum_creatinine_mg_dl=2.30, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=176.0, weight_kg=106.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=126.0, diastolic_bp=81.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=141.0, chloride=98.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0257():
    """Benchmarking reference calculation 257."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=47, weight_kg=87.0, serum_creatinine_mg_dl=2.40, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=47, serum_creatinine_mg_dl=2.40, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=177.0, weight_kg=107.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=127.0, diastolic_bp=82.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=142.0, chloride=99.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0258():
    """Benchmarking reference calculation 258."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=48, weight_kg=88.0, serum_creatinine_mg_dl=2.50, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=48, serum_creatinine_mg_dl=2.50, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=178.0, weight_kg=108.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=128.0, diastolic_bp=83.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=143.0, chloride=100.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0259():
    """Benchmarking reference calculation 259."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=49, weight_kg=89.0, serum_creatinine_mg_dl=2.60, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=49, serum_creatinine_mg_dl=2.60, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=179.0, weight_kg=109.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=129.0, diastolic_bp=84.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=144.0, chloride=101.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0260():
    """Benchmarking reference calculation 260."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=50, weight_kg=90.0, serum_creatinine_mg_dl=0.70, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=50, serum_creatinine_mg_dl=0.70, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=180.0, weight_kg=45.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=130.0, diastolic_bp=85.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=135.0, chloride=102.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0261():
    """Benchmarking reference calculation 261."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=51, weight_kg=91.0, serum_creatinine_mg_dl=0.80, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=51, serum_creatinine_mg_dl=0.80, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=181.0, weight_kg=46.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=131.0, diastolic_bp=86.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=136.0, chloride=103.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0262():
    """Benchmarking reference calculation 262."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=52, weight_kg=92.0, serum_creatinine_mg_dl=0.90, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=52, serum_creatinine_mg_dl=0.90, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=182.0, weight_kg=47.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=132.0, diastolic_bp=87.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=137.0, chloride=104.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0263():
    """Benchmarking reference calculation 263."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=53, weight_kg=93.0, serum_creatinine_mg_dl=1.00, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=53, serum_creatinine_mg_dl=1.00, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=183.0, weight_kg=48.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=133.0, diastolic_bp=88.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=138.0, chloride=105.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0264():
    """Benchmarking reference calculation 264."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=54, weight_kg=94.0, serum_creatinine_mg_dl=1.10, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=54, serum_creatinine_mg_dl=1.10, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=184.0, weight_kg=49.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=134.0, diastolic_bp=89.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=139.0, chloride=98.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0265():
    """Benchmarking reference calculation 265."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=55, weight_kg=95.0, serum_creatinine_mg_dl=1.20, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=55, serum_creatinine_mg_dl=1.20, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=185.0, weight_kg=50.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=135.0, diastolic_bp=90.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=140.0, chloride=99.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0266():
    """Benchmarking reference calculation 266."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=56, weight_kg=96.0, serum_creatinine_mg_dl=1.30, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=56, serum_creatinine_mg_dl=1.30, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=186.0, weight_kg=51.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=136.0, diastolic_bp=91.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=141.0, chloride=100.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0267():
    """Benchmarking reference calculation 267."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=57, weight_kg=97.0, serum_creatinine_mg_dl=1.40, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=57, serum_creatinine_mg_dl=1.40, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=187.0, weight_kg=52.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=137.0, diastolic_bp=92.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=142.0, chloride=101.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0268():
    """Benchmarking reference calculation 268."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=58, weight_kg=98.0, serum_creatinine_mg_dl=1.50, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=58, serum_creatinine_mg_dl=1.50, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=188.0, weight_kg=53.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=138.0, diastolic_bp=93.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=143.0, chloride=102.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0269():
    """Benchmarking reference calculation 269."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=59, weight_kg=99.0, serum_creatinine_mg_dl=1.60, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=59, serum_creatinine_mg_dl=1.60, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=189.0, weight_kg=54.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=139.0, diastolic_bp=94.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=144.0, chloride=103.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0270():
    """Benchmarking reference calculation 270."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=60, weight_kg=100.0, serum_creatinine_mg_dl=1.70, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=60, serum_creatinine_mg_dl=1.70, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=145.0, weight_kg=55.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=140.0, diastolic_bp=95.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=135.0, chloride=104.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0271():
    """Benchmarking reference calculation 271."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=61, weight_kg=101.0, serum_creatinine_mg_dl=1.80, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=61, serum_creatinine_mg_dl=1.80, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=146.0, weight_kg=56.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=141.0, diastolic_bp=96.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=136.0, chloride=105.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0272():
    """Benchmarking reference calculation 272."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=62, weight_kg=102.0, serum_creatinine_mg_dl=1.90, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=62, serum_creatinine_mg_dl=1.90, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=147.0, weight_kg=57.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=142.0, diastolic_bp=97.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=137.0, chloride=98.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0273():
    """Benchmarking reference calculation 273."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=63, weight_kg=103.0, serum_creatinine_mg_dl=2.00, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=63, serum_creatinine_mg_dl=2.00, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=148.0, weight_kg=58.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=143.0, diastolic_bp=98.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=138.0, chloride=99.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0274():
    """Benchmarking reference calculation 274."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=64, weight_kg=104.0, serum_creatinine_mg_dl=2.10, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=64, serum_creatinine_mg_dl=2.10, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=149.0, weight_kg=59.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=144.0, diastolic_bp=99.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=139.0, chloride=100.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0275():
    """Benchmarking reference calculation 275."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=65, weight_kg=50.0, serum_creatinine_mg_dl=2.20, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=65, serum_creatinine_mg_dl=2.20, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=150.0, weight_kg=60.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=145.0, diastolic_bp=100.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=140.0, chloride=101.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0276():
    """Benchmarking reference calculation 276."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=66, weight_kg=51.0, serum_creatinine_mg_dl=2.30, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=66, serum_creatinine_mg_dl=2.30, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=151.0, weight_kg=61.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=146.0, diastolic_bp=101.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=141.0, chloride=102.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0277():
    """Benchmarking reference calculation 277."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=67, weight_kg=52.0, serum_creatinine_mg_dl=2.40, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=67, serum_creatinine_mg_dl=2.40, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=152.0, weight_kg=62.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=147.0, diastolic_bp=102.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=142.0, chloride=103.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0278():
    """Benchmarking reference calculation 278."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=68, weight_kg=53.0, serum_creatinine_mg_dl=2.50, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=68, serum_creatinine_mg_dl=2.50, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=153.0, weight_kg=63.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=148.0, diastolic_bp=103.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=143.0, chloride=104.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0279():
    """Benchmarking reference calculation 279."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=69, weight_kg=54.0, serum_creatinine_mg_dl=2.60, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=69, serum_creatinine_mg_dl=2.60, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=154.0, weight_kg=64.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=149.0, diastolic_bp=104.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=144.0, chloride=105.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0280():
    """Benchmarking reference calculation 280."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=70, weight_kg=55.0, serum_creatinine_mg_dl=0.70, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=70, serum_creatinine_mg_dl=0.70, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=155.0, weight_kg=65.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=150.0, diastolic_bp=70.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=135.0, chloride=98.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0281():
    """Benchmarking reference calculation 281."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=71, weight_kg=56.0, serum_creatinine_mg_dl=0.80, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=71, serum_creatinine_mg_dl=0.80, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=156.0, weight_kg=66.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=151.0, diastolic_bp=71.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=136.0, chloride=99.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0282():
    """Benchmarking reference calculation 282."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=72, weight_kg=57.0, serum_creatinine_mg_dl=0.90, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=72, serum_creatinine_mg_dl=0.90, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=157.0, weight_kg=67.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=152.0, diastolic_bp=72.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=137.0, chloride=100.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0283():
    """Benchmarking reference calculation 283."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=73, weight_kg=58.0, serum_creatinine_mg_dl=1.00, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=73, serum_creatinine_mg_dl=1.00, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=158.0, weight_kg=68.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=153.0, diastolic_bp=73.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=138.0, chloride=101.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0284():
    """Benchmarking reference calculation 284."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=74, weight_kg=59.0, serum_creatinine_mg_dl=1.10, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=74, serum_creatinine_mg_dl=1.10, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=159.0, weight_kg=69.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=154.0, diastolic_bp=74.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=139.0, chloride=102.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0285():
    """Benchmarking reference calculation 285."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=75, weight_kg=60.0, serum_creatinine_mg_dl=1.20, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=75, serum_creatinine_mg_dl=1.20, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=160.0, weight_kg=70.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=155.0, diastolic_bp=75.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=140.0, chloride=103.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0286():
    """Benchmarking reference calculation 286."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=76, weight_kg=61.0, serum_creatinine_mg_dl=1.30, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=76, serum_creatinine_mg_dl=1.30, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=161.0, weight_kg=71.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=156.0, diastolic_bp=76.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=141.0, chloride=104.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0287():
    """Benchmarking reference calculation 287."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=77, weight_kg=62.0, serum_creatinine_mg_dl=1.40, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=77, serum_creatinine_mg_dl=1.40, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=162.0, weight_kg=72.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=157.0, diastolic_bp=77.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=142.0, chloride=105.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0288():
    """Benchmarking reference calculation 288."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=78, weight_kg=63.0, serum_creatinine_mg_dl=1.50, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=78, serum_creatinine_mg_dl=1.50, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=163.0, weight_kg=73.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=158.0, diastolic_bp=78.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=143.0, chloride=98.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0289():
    """Benchmarking reference calculation 289."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=79, weight_kg=64.0, serum_creatinine_mg_dl=1.60, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=79, serum_creatinine_mg_dl=1.60, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=164.0, weight_kg=74.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=159.0, diastolic_bp=79.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=144.0, chloride=99.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0290():
    """Benchmarking reference calculation 290."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=80, weight_kg=65.0, serum_creatinine_mg_dl=1.70, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=80, serum_creatinine_mg_dl=1.70, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=165.0, weight_kg=75.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=160.0, diastolic_bp=80.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=135.0, chloride=100.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0291():
    """Benchmarking reference calculation 291."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=81, weight_kg=66.0, serum_creatinine_mg_dl=1.80, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=81, serum_creatinine_mg_dl=1.80, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=166.0, weight_kg=76.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=161.0, diastolic_bp=81.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=136.0, chloride=101.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0292():
    """Benchmarking reference calculation 292."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=82, weight_kg=67.0, serum_creatinine_mg_dl=1.90, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=82, serum_creatinine_mg_dl=1.90, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=167.0, weight_kg=77.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=162.0, diastolic_bp=82.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=137.0, chloride=102.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0293():
    """Benchmarking reference calculation 293."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=83, weight_kg=68.0, serum_creatinine_mg_dl=2.00, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=83, serum_creatinine_mg_dl=2.00, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=168.0, weight_kg=78.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=163.0, diastolic_bp=83.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=138.0, chloride=103.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0294():
    """Benchmarking reference calculation 294."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=84, weight_kg=69.0, serum_creatinine_mg_dl=2.10, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=84, serum_creatinine_mg_dl=2.10, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=169.0, weight_kg=79.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=164.0, diastolic_bp=84.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=139.0, chloride=104.0, bicarbonate=22.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0295():
    """Benchmarking reference calculation 295."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=85, weight_kg=70.0, serum_creatinine_mg_dl=2.20, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=85, serum_creatinine_mg_dl=2.20, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=170.0, weight_kg=80.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=165.0, diastolic_bp=85.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=140.0, chloride=105.0, bicarbonate=23.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0296():
    """Benchmarking reference calculation 296."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=86, weight_kg=71.0, serum_creatinine_mg_dl=2.30, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=86, serum_creatinine_mg_dl=2.30, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=171.0, weight_kg=81.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=166.0, diastolic_bp=86.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=141.0, chloride=98.0, bicarbonate=24.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0297():
    """Benchmarking reference calculation 297."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=87, weight_kg=72.0, serum_creatinine_mg_dl=2.40, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=87, serum_creatinine_mg_dl=2.40, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=172.0, weight_kg=82.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=167.0, diastolic_bp=87.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=142.0, chloride=99.0, bicarbonate=25.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0298():
    """Benchmarking reference calculation 298."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=88, weight_kg=73.0, serum_creatinine_mg_dl=2.50, gender=Gender.MALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=88, serum_creatinine_mg_dl=2.50, gender=Gender.MALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=173.0, weight_kg=83.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=168.0, diastolic_bp=88.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=143.0, chloride=100.0, bicarbonate=26.0)
    return cg, egfr, bsa, map_bp, ag


def clinical_calculation_benchmark_case_0299():
    """Benchmarking reference calculation 299."""
    cg = ClinicalCalculatorEngine.calculate_cockcroft_gault(age_years=89, weight_kg=74.0, serum_creatinine_mg_dl=2.60, gender=Gender.FEMALE)
    egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(age_years=89, serum_creatinine_mg_dl=2.60, gender=Gender.FEMALE)
    bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=174.0, weight_kg=84.0)
    map_bp = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(systolic_bp=169.0, diastolic_bp=89.0)
    ag = ClinicalCalculatorEngine.calculate_anion_gap(sodium=144.0, chloride=101.0, bicarbonate=27.0)
    return cg, egfr, bsa, map_bp, ag

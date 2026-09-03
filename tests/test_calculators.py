"""
Clinical Calculator Engine Unit Tests.
"""
from django.test import SimpleTestCase
from apps.clinical.calculators import ClinicalCalculatorEngine, Gender, FormulaBSA


class ClinicalCalculatorTests(SimpleTestCase):
    def test_cockcroft_gault(self):
        """Verify Cockcroft-Gault creatinine clearance calculation."""
        crcl_male = ClinicalCalculatorEngine.calculate_cockcroft_gault(
            age_years=60, weight_kg=70.0, serum_creatinine_mg_dl=1.0, gender=Gender.MALE
        )
        self.assertAlmostEqual(crcl_male, 77.78, places=1)

        crcl_female = ClinicalCalculatorEngine.calculate_cockcroft_gault(
            age_years=60, weight_kg=70.0, serum_creatinine_mg_dl=1.0, gender=Gender.FEMALE
        )
        self.assertAlmostEqual(crcl_female, 66.11, places=1)

    def test_ckd_epi_2021(self):
        """Verify 2021 CKD-EPI race-neutral eGFR calculation."""
        egfr = ClinicalCalculatorEngine.calculate_ckd_epi_2021(
            age_years=50, serum_creatinine_mg_dl=0.9, gender=Gender.MALE
        )
        self.assertGreater(egfr, 60.0)

    def test_bsa_calculation(self):
        """Verify Body Surface Area calculation."""
        bsa = ClinicalCalculatorEngine.calculate_bsa(height_cm=175.0, weight_kg=75.0)
        self.assertAlmostEqual(bsa, 1.91, places=1)

    def test_cha2ds2_vasc(self):
        """Verify stroke risk stratification."""
        result = ClinicalCalculatorEngine.calculate_cha2ds2_vasc(
            congestive_heart_failure=True,
            hypertension=True,
            age_years=76,
            diabetes=False,
            stroke_tia_thromboembolism=False,
            vascular_disease=False,
            is_female=False
        )
        self.assertEqual(result.cha2ds2_vasc_score, 4)
        self.assertGreater(result.annual_stroke_risk_percent, 4.0)

    def test_mean_arterial_pressure(self):
        """Verify MAP calculation."""
        map_val = ClinicalCalculatorEngine.calculate_mean_arterial_pressure(120.0, 80.0)
        self.assertAlmostEqual(map_val, 93.3, places=1)

"""
ICD-10 Diagnostic Taxonomy & Clinical Symptoms Engine Unit Tests.
"""
from django.test import SimpleTestCase
from apps.clinical.icd10_taxonomy import (
    ICD10DiagnosticsEngine,
    DiagnosticRiskTier,
    ICD10DiagnosticRecord
)


class ICD10DiagnosticsEngineTests(SimpleTestCase):
    def test_lookup_by_code(self):
        """Verify code lookup."""
        rec = ICD10DiagnosticsEngine.get_by_code("I10")
        self.assertIsNotNone(rec)
        self.assertEqual(rec.code, "I10")
        self.assertIn("hypertension", rec.preferred_name.lower())

    def test_search_by_name(self):
        """Verify keyword search."""
        matches = ICD10DiagnosticsEngine.search_by_name("diabetes")
        self.assertTrue(len(matches) > 0)
        for m in matches:
            self.assertTrue("diabetes" in m.preferred_name.lower() or "diabetes" in m.code.lower())

    def test_search_by_symptom(self):
        """Verify symptom reverse matching."""
        matches = ICD10DiagnosticsEngine.search_by_symptom("chest pain")
        self.assertTrue(len(matches) > 0)

    def test_risk_tier_filter(self):
        """Verify emergency tier filtering."""
        emergencies = ICD10DiagnosticsEngine.get_by_risk_tier(DiagnosticRiskTier.EMERGENCY)
        self.assertTrue(len(emergencies) > 0)

    def test_total_count(self):
        """Verify directory scale."""
        self.assertGreater(ICD10DiagnosticsEngine.get_total_conditions_count(), 100)

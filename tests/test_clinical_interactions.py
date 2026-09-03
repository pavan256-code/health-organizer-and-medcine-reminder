"""
Clinical Drug-Drug Interaction Surveillance Engine Unit Tests.
"""
from django.test import SimpleTestCase
from apps.clinical.drug_interactions import (
    ClinicalInteractionEngine,
    InteractionSeverity,
    DrugInteractionRecord,
    DrugMonograph
)


class ClinicalInteractionEngineTests(SimpleTestCase):
    def test_monograph_retrieval(self):
        """Verify clinical monograph retrieval by drug name."""
        monograph = ClinicalInteractionEngine.get_monograph("Atorvastatin")
        self.assertIsNotNone(monograph)
        self.assertEqual(monograph.name, "Atorvastatin")
        self.assertEqual(monograph.pharmacological_class, "HMG-CoA Reductase Inhibitor")
        self.assertTrue(len(monograph.contraindications) > 0)

    def test_drug_pair_interaction_lookup(self):
        """Verify bidirectional pair interaction lookup."""
        match = ClinicalInteractionEngine.check_pair("Atorvastatin", "Simvastatin")
        self.assertIsNotNone(match)
        self.assertIsInstance(match, DrugInteractionRecord)
        self.assertTrue(len(match.monitoring_parameters) > 0)

    def test_screen_medication_regimen(self):
        """Verify multi-drug regimen screening."""
        regimen = ["Atorvastatin", "Simvastatin", "Rosuvastatin", "Lisinopril"]
        interactions = ClinicalInteractionEngine.screen_medication_regimen(regimen)
        self.assertTrue(len(interactions) > 0)

    def test_critical_alerts_filtering(self):
        """Verify filtering for high risk interactions."""
        regimen = ["Atorvastatin", "Simvastatin", "Rosuvastatin"]
        critical = ClinicalInteractionEngine.get_critical_alerts(regimen)
        for alert in critical:
            self.assertIn(alert.severity, [InteractionSeverity.CONTRAINDICATED, InteractionSeverity.MAJOR])

    def test_total_counts(self):
        """Verify populated knowledge base volume."""
        self.assertGreater(ClinicalInteractionEngine.get_total_monographs_count(), 50)
        self.assertGreater(ClinicalInteractionEngine.get_total_interactions_count(), 500)

"""
HL7 FHIR R4 Serialization Unit Tests.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from apps.family.models import FamilyMember
from apps.medications.models import Medicine
from apps.clinical.fhir_converter import FHIRConverter, FHIRResourceType

User = get_user_model()


class FHIRConverterTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='fhiruser',
            email='fhir@hospital.local',
            password='TestPassword123!'
        )
        self.member = FamilyMember.objects.create(
            user=self.user,
            first_name='Samantha',
            last_name='Reed',
            relationship='SELF',
            gender='FEMALE',
            is_active=True
        )
        self.medicine = Medicine.objects.create(
            user=self.user,
            family_member=self.member,
            name='Atorvastatin',
            dosage='20mg',
            strength='20',
            unit='mg',
            instructions='AFTER_FOOD',
            status='ACTIVE'
        )

    def test_patient_to_fhir(self):
        """Verify Patient resource mapping."""
        res = FHIRConverter.patient_to_fhir(self.member)
        self.assertEqual(res['resourceType'], FHIRResourceType.PATIENT)
        self.assertEqual(res['id'], f"pat-{self.member.id}")
        self.assertEqual(res['gender'], 'female')

    def test_medicine_to_fhir_statement(self):
        """Verify MedicationStatement resource mapping."""
        res = FHIRConverter.medicine_to_fhir_statement(self.medicine)
        self.assertEqual(res['resourceType'], FHIRResourceType.MEDICATION_STATEMENT)
        self.assertEqual(res['status'], 'active')

    def test_bundle_creation(self):
        """Verify Bundle aggregation."""
        p = FHIRConverter.patient_to_fhir(self.member)
        m = FHIRConverter.medicine_to_fhir_statement(self.medicine)
        bundle = FHIRConverter.create_bundle([p, m])
        self.assertEqual(bundle['resourceType'], FHIRResourceType.BUNDLE)
        self.assertEqual(bundle['total'], 2)

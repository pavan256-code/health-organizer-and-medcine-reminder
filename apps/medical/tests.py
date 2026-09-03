"""
Automated tests for Medical Management:
Doctors, Appointments, Prescriptions, HealthProfile, Vitals, Symptoms, Vaccinations, Allergies, Documents.
"""

from datetime import date, time
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from apps.family.models import FamilyMember
from apps.medical.models import (
    Doctor, Appointment, Prescription, HealthProfile,
    VitalRecord, SymptomRecord, Vaccination, Allergy, MedicalDocument
)

User = get_user_model()


class MedicalModuleTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='meredith_grey',
            email='grey@seattlegrace.org',
            password='McDreamyPass123!'
        )
        self.member = FamilyMember.objects.create(
            user=self.user,
            first_name='Meredith',
            last_name='Grey',
            relationship='SELF'
        )
        self.doctor = Doctor.objects.create(
            user=self.user,
            full_name='Dr. Derek Shepherd',
            specialization='Neurosurgery',
            hospital_clinic='Seattle Grace Hospital',
            phone='+1555123456'
        )

    def test_doctor_creation(self):
        self.client.login(username='meredith_grey', password='McDreamyPass123!')
        response = self.client.post(reverse('medical:doctor_add'), {
            'full_name': 'Dr. Cristina Yang',
            'specialization': 'Cardiothoracic Surgery',
            'hospital_clinic': 'Seattle Grace Hospital'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Doctor.objects.filter(full_name='Dr. Cristina Yang').exists())

    def test_appointment_booking_and_complete(self):
        self.client.login(username='meredith_grey', password='McDreamyPass123!')
        response = self.client.post(reverse('medical:appointment_add'), {
            'family_member': self.member.id,
            'doctor': self.doctor.id,
            'date': date.today().strftime('%Y-%m-%d'),
            'time': '10:30',
            'reason': 'Brain MRI follow-up',
            'status': 'UPCOMING'
        })
        self.assertEqual(response.status_code, 302)
        appt = Appointment.objects.get(reason='Brain MRI follow-up')
        self.assertEqual(appt.status, 'UPCOMING')

        # Complete appointment
        res_comp = self.client.post(reverse('medical:appointment_complete', args=[appt.id]))
        self.assertEqual(res_comp.status_code, 302)
        appt.refresh_from_db()
        self.assertEqual(appt.status, 'COMPLETED')

    def test_vital_signs_recording_and_bmi(self):
        self.client.login(username='meredith_grey', password='McDreamyPass123!')
        response = self.client.post(reverse('medical:vital_add'), {
            'family_member': self.member.id,
            'date': date.today().strftime('%Y-%m-%d'),
            'time': '08:00',
            'blood_pressure_systolic': 120,
            'blood_pressure_diastolic': 78,
            'heart_rate': 72,
            'height_cm': 170.0,
            'weight_kg': 68.0,
            'notes': 'Normal baseline vitals'
        })
        self.assertEqual(response.status_code, 302)
        vital = VitalRecord.objects.filter(family_member=self.member).first()
        self.assertIsNotNone(vital)
        self.assertEqual(vital.bp_category, 'Elevated' if vital.blood_pressure_systolic >= 120 and vital.blood_pressure_systolic <= 129 else 'Normal')
        # BMI for 68kg at 170cm is 68 / (1.7)^2 = 23.5
        self.assertEqual(vital.bmi, 23.5)

    def test_symptom_journal(self):
        self.client.login(username='meredith_grey', password='McDreamyPass123!')
        response = self.client.post(reverse('medical:symptom_add'), {
            'family_member': self.member.id,
            'symptom_name': 'Migraine with Aura',
            'severity': 'SEVERE',
            'date': date.today().strftime('%Y-%m-%d'),
            'time': '14:00',
            'duration_hours': 4.5,
            'triggers': 'Stress, Caffeine withdrawal'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(SymptomRecord.objects.filter(symptom_name='Migraine with Aura').exists())

    def test_vaccination_record(self):
        self.client.login(username='meredith_grey', password='McDreamyPass123!')
        response = self.client.post(reverse('medical:vaccination_add'), {
            'family_member': self.member.id,
            'vaccine_name': 'Hepatitis B',
            'dose_number': 'Booster',
            'vaccination_date': date.today().strftime('%Y-%m-%d'),
            'status': 'COMPLETED'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Vaccination.objects.filter(vaccine_name='Hepatitis B').exists())

    def test_allergy_record(self):
        self.client.login(username='meredith_grey', password='McDreamyPass123!')
        response = self.client.post(reverse('medical:allergy_add'), {
            'family_member': self.member.id,
            'allergen': 'Latex',
            'allergy_type': 'ENVIRONMENTAL',
            'severity': 'SEVERE',
            'reaction': 'Contact dermatitis and hives'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Allergy.objects.filter(allergen='Latex').exists())

    def test_document_vault_upload_and_download(self):
        self.client.login(username='meredith_grey', password='McDreamyPass123!')
        dummy_file = SimpleUploadedFile("head_ct_scan.pdf", b"%PDF-1.4 dummy pdf content", content_type="application/pdf")

        response = self.client.post(reverse('medical:document_upload'), {
            'family_member': self.member.id,
            'title': 'Brain CT Scan',
            'category': 'SCAN_REPORT',
            'document_date': date.today().strftime('%Y-%m-%d'),
            'file': dummy_file
        })
        self.assertEqual(response.status_code, 302)
        doc = MedicalDocument.objects.filter(title='Brain CT Scan').first()
        self.assertIsNotNone(doc)
        self.assertEqual(doc.file_type, 'PDF')

        # Download document
        res_dl = self.client.get(reverse('medical:document_download', args=[doc.id]))
        self.assertEqual(res_dl.status_code, 200)

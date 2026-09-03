"""
Automated unit and integration tests for Medication Management:
Medicines, Schedules, Doses, Logs, Stock, Refills, Expiry, Adherence.
"""

from datetime import date, time, timedelta
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from apps.family.models import FamilyMember
from apps.medications.models import (
    Medicine, MedicineSchedule, MedicineDose, MedicationLog, MedicineStock, MedicineRefill, MedicineExpiry
)
from apps.medications.services.scheduler_service import MedicationSchedulerService
from apps.medications.services.adherence_service import MedicationAdherenceService

User = get_user_model()


class MedicationModuleTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='dr_house',
            email='house@princeton.edu',
            password='VicodinPassword123!'
        )
        self.member = FamilyMember.objects.create(
            user=self.user,
            first_name='Gregory',
            last_name='House',
            relationship='SELF'
        )
        self.medicine = Medicine.objects.create(
            user=self.user,
            family_member=self.member,
            name='Vicodin',
            generic_name='Hydrocodone/Acetaminophen',
            dosage='1 Tablet (5/300mg)',
            strength='5',
            unit='mg',
            medicine_type='TABLET',
            instructions='AFTER_FOOD',
            status='ACTIVE'
        )
        self.stock = MedicineStock.objects.create(
            medicine=self.medicine,
            current_stock=20,
            initial_quantity=20,
            minimum_stock_level=5
        )

    def test_medicine_catalog_listing(self):
        self.client.login(username='dr_house', password='VicodinPassword123!')
        response = self.client.get(reverse('medications:medicine_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Vicodin')

    def test_schedule_creation_and_dose_generation(self):
        self.client.login(username='dr_house', password='VicodinPassword123!')
        response = self.client.post(reverse('medications:schedule_add', args=[self.medicine.id]), {
            'frequency': 'DAILY',
            'times_input': '08:00, 20:00',
            'start_date': date.today().strftime('%Y-%m-%d'),
            'is_active': True
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(MedicineSchedule.objects.filter(medicine=self.medicine).exists())

        # Verify doses generated automatically for window
        doses_count = MedicineDose.objects.filter(schedule__medicine=self.medicine).count()
        self.assertGreaterEqual(doses_count, 1)

    def test_dose_take_workflow_and_stock_decrement(self):
        sched = MedicineSchedule.objects.create(
            medicine=self.medicine,
            frequency='DAILY',
            specific_times=['08:00']
        )
        dose = MedicineDose.objects.create(
            schedule=sched,
            date=date.today(),
            scheduled_time=time(8, 0),
            status=MedicineDose.STATUS_PENDING
        )

        self.client.login(username='dr_house', password='VicodinPassword123!')
        response = self.client.post(reverse('medications:dose_take', args=[dose.id]))
        self.assertEqual(response.status_code, 302)

        dose.refresh_from_db()
        self.assertEqual(dose.status, MedicineDose.STATUS_TAKEN)

        self.stock.refresh_from_db()
        self.assertEqual(self.stock.current_stock, 19)
        self.assertEqual(self.stock.consumed_quantity, 1)

        # Verify audit medication log
        self.assertTrue(MedicationLog.objects.filter(medicine=self.medicine, status=MedicineDose.STATUS_TAKEN).exists())

    def test_dose_skip_workflow(self):
        sched = MedicineSchedule.objects.create(
            medicine=self.medicine,
            frequency='DAILY',
            specific_times=['12:00']
        )
        dose = MedicineDose.objects.create(
            schedule=sched,
            date=date.today(),
            scheduled_time=time(12, 0),
            status=MedicineDose.STATUS_PENDING
        )

        self.client.login(username='dr_house', password='VicodinPassword123!')
        response = self.client.post(reverse('medications:dose_skip', args=[dose.id]), {
            'reason': 'Patient felt nauseous'
        })
        self.assertEqual(response.status_code, 302)

        dose.refresh_from_db()
        self.assertEqual(dose.status, MedicineDose.STATUS_SKIPPED)
        self.assertEqual(dose.notes, 'Patient felt nauseous')

    def test_refill_replenishes_stock(self):
        self.client.login(username='dr_house', password='VicodinPassword123!')
        response = self.client.post(reverse('medications:stock_refill', args=[self.medicine.id]), {
            'refill_quantity': 50,
            'refill_date': date.today().strftime('%Y-%m-%d'),
            'pharmacy_source': 'Princeton Pharmacy',
            'cost': '25.00'
        })
        self.assertEqual(response.status_code, 302)
        self.stock.refresh_from_db()
        self.assertEqual(self.stock.current_stock, 70)

    def test_adherence_calculations(self):
        sched = MedicineSchedule.objects.create(
            medicine=self.medicine,
            frequency='DAILY',
            specific_times=['08:00']
        )
        MedicineDose.objects.create(schedule=sched, date=date.today(), scheduled_time=time(8, 0), status=MedicineDose.STATUS_TAKEN)
        MedicineDose.objects.create(schedule=sched, date=date.today() - timedelta(days=1), scheduled_time=time(8, 0), status=MedicineDose.STATUS_MISSED)

        metrics = MedicationAdherenceService.get_adherence_metrics(self.user, family_member=self.member, days=7)
        self.assertEqual(metrics['taken_doses'], 1)
        self.assertEqual(metrics['missed_doses'], 1)
        self.assertEqual(metrics['adherence_rate'], 50.0)

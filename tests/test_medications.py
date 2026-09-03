"""
Medication Management, Doses & Expiry Tracker Unit Tests.
"""
from datetime import timedelta
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.utils import timezone
from apps.family.models import FamilyMember
from apps.medications.models import (
    Medicine,
    MedicineStock,
    MedicineExpiry,
    MedicineSchedule,
    MedicineDose
)

User = get_user_model()


class MedicationSystemTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='meduser',
            email='meduser@hospital.local',
            password='TestPassword123!'
        )
        self.member = FamilyMember.objects.create(
            user=self.user,
            first_name='Jordan',
            last_name='Hayes',
            relationship='SELF',
            is_active=True
        )
        self.today = timezone.now().date()

        self.medicine = Medicine.objects.create(
            user=self.user,
            family_member=self.member,
            name='Amoxicillin',
            dosage='500mg',
            strength='500',
            unit='mg',
            medicine_type=Medicine.TYPE_CAPSULE,
            instructions=Medicine.INSTRUCTION_AFTER_FOOD,
            status=Medicine.STATUS_ACTIVE
        )

        self.stock = MedicineStock.objects.create(
            medicine=self.medicine,
            current_stock=20,
            initial_quantity=30,
            minimum_stock_level=5
        )

    def test_medicine_creation(self):
        """Verify medicine attributes and relationships."""
        self.assertEqual(self.medicine.name, 'Amoxicillin')
        self.assertEqual(self.medicine.family_member, self.member)
        self.assertTrue(self.medicine.is_chronic)

    def test_stock_decrement(self):
        """Verify stock decreases upon dose consumption."""
        self.stock.decrement(2)
        self.assertEqual(self.stock.current_stock, 18)
        self.assertEqual(self.stock.consumed_quantity, 2)

    def test_expiry_tracking_logic(self):
        """Verify batch expiry status transitions."""
        # Expired batch
        expired_batch = MedicineExpiry.objects.create(
            medicine=self.medicine,
            batch_number='LOT-EXP-01',
            expiry_date=self.today - timedelta(days=5),
            alert_days_before=30
        )
        status = expired_batch.update_status()
        self.assertEqual(status, MedicineExpiry.STATUS_EXPIRED)

        # Expiring soon batch
        soon_batch = MedicineExpiry.objects.create(
            medicine=self.medicine,
            batch_number='LOT-SOON-02',
            expiry_date=self.today + timedelta(days=10),
            alert_days_before=30
        )
        status = soon_batch.update_status()
        self.assertEqual(status, MedicineExpiry.STATUS_EXPIRING_SOON)

        # Safe batch
        safe_batch = MedicineExpiry.objects.create(
            medicine=self.medicine,
            batch_number='LOT-SAFE-03',
            expiry_date=self.today + timedelta(days=180),
            alert_days_before=30
        )
        status = safe_batch.update_status()
        self.assertEqual(status, MedicineExpiry.STATUS_SAFE)

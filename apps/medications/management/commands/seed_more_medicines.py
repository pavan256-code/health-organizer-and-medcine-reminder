"""
Management command to seed additional clinical medicines and 3 expiry tracker batches.
Run via: python manage.py seed_more_medicines
"""

from datetime import timedelta
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone
from apps.family.models import FamilyMember
from apps.medications.models import (
    Medicine,
    MedicineSchedule,
    MedicineDose,
    MedicineStock,
    MedicineExpiry,
)


class Command(BaseCommand):
    help = "Seeds extra medicines into the list and creates 3 batches in the Expiry Tracker."

    def handle(self, *args, **options):
        User = get_user_model()
        today = timezone.now().date()

        users = User.objects.filter(username__in=['demo', 'admin'])
        if not users.exists():
            users = User.objects.all()

        for user in users:
            self.stdout.write(f"Processing user: {user.username}")

            # Fetch or establish family members
            self_member = FamilyMember.objects.filter(user=user, relationship='SELF').first()
            if not self_member:
                self_member = FamilyMember.objects.create(
                    user=user,
                    first_name=user.first_name or user.username.capitalize(),
                    last_name=user.last_name or 'Profile',
                    relationship='SELF',
                    is_active=True
                )

            spouse_member = FamilyMember.objects.filter(user=user, relationship='SPOUSE').first() or self_member
            child_member = FamilyMember.objects.filter(user=user, relationship='SON').first() or self_member
            mother_member = FamilyMember.objects.filter(user=user, relationship='MOTHER').first() or self_member

            # =========================================================================
            # MEDICINE 1: Augmentin 625 Duo (With EXPIRY TRACKER batch - EXPIRING SOON in 8 days)
            # =========================================================================
            med1, created = Medicine.objects.get_or_create(
                user=user,
                name='Augmentin 625 Duo',
                family_member=self_member,
                defaults={
                    'generic_name': 'Amoxicillin + Clavulanic Acid (500mg + 125mg)',
                    'brand_name': 'GSK Augmentin',
                    'medicine_type': Medicine.TYPE_TABLET,
                    'dosage': '1 tablet',
                    'strength': '625',
                    'unit': 'mg',
                    'instructions': Medicine.INSTRUCTION_WITH_FOOD,
                    'start_date': today - timedelta(days=2),
                    'end_date': today + timedelta(days=5),
                    'prescribed_by': 'Dr. Vikram Seth (Internal Medicine)',
                    'status': Medicine.STATUS_ACTIVE,
                    'notes': 'Broad-spectrum antibiotic course for respiratory tract infection. Complete full 7-day course.',
                }
            )
            if created or not hasattr(med1, 'stock'):
                MedicineStock.objects.update_or_create(
                    medicine=med1,
                    defaults={
                        'current_stock': 10,
                        'initial_quantity': 14,
                        'consumed_quantity': 4,
                        'minimum_stock_level': 4,
                        'unit': 'tablets',
                    }
                )
            if not med1.schedules.exists():
                MedicineSchedule.objects.create(
                    medicine=med1,
                    frequency=MedicineSchedule.FREQ_TWICE_DAILY,
                    specific_times=['08:30', '20:30'],
                    is_active=True
                )
            # Generate today doses
            for t in ['08:30', '20:30']:
                MedicineDose.objects.get_or_create(
                    schedule=med1.schedules.first(),
                    date=today,
                    scheduled_time=t,
                    defaults={'status': 'TAKEN' if t == '08:30' else 'PENDING'}
                )

            # 1st EXPIRY TRACKER BATCH: Expiring in 8 days
            exp1, _ = MedicineExpiry.objects.update_or_create(
                medicine=med1,
                batch_number='AUG-7729',
                defaults={
                    'expiry_date': today + timedelta(days=8),
                    'alert_days_before': 30,
                    'status': MedicineExpiry.STATUS_EXPIRING_SOON,
                    'notes': 'Short-course antibiotic batch near expiration. Discard remaining after course completion.',
                }
            )
            exp1.update_status()

            # =========================================================================
            # MEDICINE 2: Pan 40 (With EXPIRY TRACKER batch - EXPIRING SOON in 18 days)
            # =========================================================================
            med2, created = Medicine.objects.get_or_create(
                user=user,
                name='Pan 40',
                family_member=self_member,
                defaults={
                    'generic_name': 'Pantoprazole Sodium Gastro-resistant',
                    'brand_name': 'Alkem Pan',
                    'medicine_type': Medicine.TYPE_TABLET,
                    'dosage': '1 tablet',
                    'strength': '40',
                    'unit': 'mg',
                    'instructions': Medicine.INSTRUCTION_EMPTY_STOMACH,
                    'start_date': today - timedelta(days=30),
                    'prescribed_by': 'Dr. Meenakshi Rao (Gastroenterologist)',
                    'status': Medicine.STATUS_ACTIVE,
                    'notes': 'Take in the morning on an empty stomach with a full glass of water, 30 minutes before breakfast.',
                }
            )
            if created or not hasattr(med2, 'stock'):
                MedicineStock.objects.update_or_create(
                    medicine=med2,
                    defaults={
                        'current_stock': 24,
                        'initial_quantity': 30,
                        'consumed_quantity': 6,
                        'minimum_stock_level': 5,
                        'unit': 'tablets',
                    }
                )
            if not med2.schedules.exists():
                MedicineSchedule.objects.create(
                    medicine=med2,
                    frequency=MedicineSchedule.FREQ_DAILY,
                    specific_times=['07:00'],
                    is_active=True
                )
            MedicineDose.objects.get_or_create(
                schedule=med2.schedules.first(),
                date=today,
                scheduled_time='07:00',
                defaults={'status': 'TAKEN'}
            )

            # 2nd EXPIRY TRACKER BATCH: Expiring in 18 days
            exp2, _ = MedicineExpiry.objects.update_or_create(
                medicine=med2,
                batch_number='PAN-4410',
                defaults={
                    'expiry_date': today + timedelta(days=18),
                    'alert_days_before': 30,
                    'status': MedicineExpiry.STATUS_EXPIRING_SOON,
                    'notes': 'Current blister pack expires later this month. Ensure fresh refill upon doctor renewal.',
                }
            )
            exp2.update_status()

            # =========================================================================
            # MEDICINE 3: Paracetamol 650mg (Dolo 650) (With EXPIRY TRACKER batch - EXPIRED 14 days ago)
            # =========================================================================
            med3, created = Medicine.objects.get_or_create(
                user=user,
                name='Paracetamol 650mg (Dolo 650)',
                family_member=self_member,
                defaults={
                    'generic_name': 'Paracetamol / Acetaminophen',
                    'brand_name': 'Micro Labs Dolo 650',
                    'medicine_type': Medicine.TYPE_TABLET,
                    'dosage': '1 tablet SOS',
                    'strength': '650',
                    'unit': 'mg',
                    'instructions': Medicine.INSTRUCTION_AS_NEEDED,
                    'start_date': today - timedelta(days=90),
                    'prescribed_by': 'Dr. Vikram Seth (Internal Medicine)',
                    'status': Medicine.STATUS_ACTIVE,
                    'notes': 'For fever (> 100°F) or acute body ache. Maximum 3 tablets in 24 hours with minimum 6 hour interval.',
                }
            )
            if created or not hasattr(med3, 'stock'):
                MedicineStock.objects.update_or_create(
                    medicine=med3,
                    defaults={
                        'current_stock': 4,
                        'initial_quantity': 15,
                        'consumed_quantity': 11,
                        'minimum_stock_level': 5,
                        'unit': 'tablets',
                    }
                )

            # 3rd EXPIRY TRACKER BATCH: Expired 14 days ago!
            exp3, _ = MedicineExpiry.objects.update_or_create(
                medicine=med3,
                batch_number='DLO-1092',
                defaults={
                    'expiry_date': today - timedelta(days=14),
                    'alert_days_before': 30,
                    'status': MedicineExpiry.STATUS_EXPIRED,
                    'notes': 'EXPIRED BATCH: Do not administer. Dispose of according to pharmacy safe disposal protocol.',
                }
            )
            exp3.update_status()

            # =========================================================================
            # ADDITIONAL MEDICINES IN LIST:
            # =========================================================================

            # 4. Vitamin D3 60,000 IU (Calcirol)
            med4, created = Medicine.objects.get_or_create(
                user=user,
                name='Vitamin D3 60,000 IU (Calcirol)',
                family_member=spouse_member,
                defaults={
                    'generic_name': 'Cholecalciferol',
                    'brand_name': 'Cadila Calcirol Softgel',
                    'medicine_type': Medicine.TYPE_CAPSULE,
                    'dosage': '1 capsule weekly',
                    'strength': '60000',
                    'unit': 'IU',
                    'instructions': Medicine.INSTRUCTION_AFTER_FOOD,
                    'start_date': today - timedelta(days=14),
                    'prescribed_by': 'Dr. Anita Joshi (Endocrinology)',
                    'status': Medicine.STATUS_ACTIVE,
                    'notes': 'Take once a week after Sunday lunch with a glass of milk for optimal absorption.',
                }
            )
            if created or not hasattr(med4, 'stock'):
                MedicineStock.objects.update_or_create(
                    medicine=med4,
                    defaults={'current_stock': 6, 'initial_quantity': 8, 'consumed_quantity': 2, 'minimum_stock_level': 2, 'unit': 'capsules'}
                )
            if not med4.schedules.exists():
                MedicineSchedule.objects.create(
                    medicine=med4,
                    frequency=MedicineSchedule.FREQ_WEEKLY,
                    specific_times=['13:00'],
                    days_of_week=[6],  # Sunday
                    is_active=True
                )

            # 5. Cetirizine 10mg (Cetzine)
            med5, created = Medicine.objects.get_or_create(
                user=user,
                name='Cetirizine 10mg (Cetzine)',
                family_member=child_member,
                defaults={
                    'generic_name': 'Cetirizine Dihydrochloride',
                    'brand_name': "Dr. Reddy's Cetzine",
                    'medicine_type': Medicine.TYPE_TABLET,
                    'dosage': '1 tablet at bedtime',
                    'strength': '10',
                    'unit': 'mg',
                    'instructions': Medicine.INSTRUCTION_BEDTIME,
                    'start_date': today - timedelta(days=10),
                    'prescribed_by': 'Dr. Rakesh Patel (Pediatrics)',
                    'status': Medicine.STATUS_ACTIVE,
                    'notes': 'For seasonal allergic rhinitis, sneezing, and runny nose. May cause mild drowsiness.',
                }
            )
            if created or not hasattr(med5, 'stock'):
                MedicineStock.objects.update_or_create(
                    medicine=med5,
                    defaults={'current_stock': 18, 'initial_quantity': 20, 'consumed_quantity': 2, 'minimum_stock_level': 5, 'unit': 'tablets'}
                )
            if not med5.schedules.exists():
                MedicineSchedule.objects.create(
                    medicine=med5,
                    frequency=MedicineSchedule.FREQ_DAILY,
                    specific_times=['21:30'],
                    is_active=True
                )

            # 6. Neurobion Forte
            med6, created = Medicine.objects.get_or_create(
                user=user,
                name='Neurobion Forte',
                family_member=mother_member,
                defaults={
                    'generic_name': 'Vitamin B1 + B6 + B12 & Nicotinamide',
                    'brand_name': 'P&G Health Neurobion',
                    'medicine_type': Medicine.TYPE_TABLET,
                    'dosage': '1 tablet daily',
                    'strength': '100',
                    'unit': 'mg',
                    'instructions': Medicine.INSTRUCTION_AFTER_FOOD,
                    'start_date': today - timedelta(days=45),
                    'prescribed_by': 'Dr. Sunita Verma (Geriatric Care)',
                    'status': Medicine.STATUS_ACTIVE,
                    'notes': 'Nerve health supplement and vitamin deficiency support. Take daily after lunch.',
                }
            )
            if created or not hasattr(med6, 'stock'):
                MedicineStock.objects.update_or_create(
                    medicine=med6,
                    defaults={'current_stock': 25, 'initial_quantity': 30, 'consumed_quantity': 5, 'minimum_stock_level': 7, 'unit': 'tablets'}
                )
            if not med6.schedules.exists():
                MedicineSchedule.objects.create(
                    medicine=med6,
                    frequency=MedicineSchedule.FREQ_DAILY,
                    specific_times=['14:00'],
                    is_active=True
                )

            # 7. Otrivin Adult Nasal Drops
            med7, created = Medicine.objects.get_or_create(
                user=user,
                name='Otrivin Adult Nasal Drops',
                family_member=self_member,
                defaults={
                    'generic_name': 'Xylometazoline Hydrochloride 0.1% w/v',
                    'brand_name': 'GSK Otrivin',
                    'medicine_type': Medicine.TYPE_DROPS,
                    'dosage': '2 drops per nostril',
                    'strength': '0.1',
                    'unit': '%',
                    'instructions': Medicine.INSTRUCTION_AS_NEEDED,
                    'start_date': today - timedelta(days=5),
                    'prescribed_by': 'Dr. K. N. Rao (ENT Specialist)',
                    'status': Medicine.STATUS_ACTIVE,
                    'notes': 'Nasal decongestant for blocked nose. Do not use for more than 5 consecutive days.',
                }
            )
            if created or not hasattr(med7, 'stock'):
                MedicineStock.objects.update_or_create(
                    medicine=med7,
                    defaults={'current_stock': 1, 'initial_quantity': 1, 'consumed_quantity': 0, 'minimum_stock_level': 1, 'unit': 'bottle (10ml)'}
                )

            # 8. Azithromycin 500mg (Azithral)
            med8, created = Medicine.objects.get_or_create(
                user=user,
                name='Azithromycin 500mg (Azithral 500)',
                family_member=spouse_member,
                defaults={
                    'generic_name': 'Azithromycin',
                    'brand_name': 'Alembic Azithral 500',
                    'medicine_type': Medicine.TYPE_TABLET,
                    'dosage': '1 tablet once daily',
                    'strength': '500',
                    'unit': 'mg',
                    'instructions': Medicine.INSTRUCTION_BEFORE_FOOD,
                    'start_date': today - timedelta(days=1),
                    'end_date': today + timedelta(days=2),
                    'prescribed_by': 'Dr. Anita Joshi (General Physician)',
                    'status': Medicine.STATUS_ACTIVE,
                    'notes': '3-day short course antibiotic. Take 1 hour before breakfast with water.',
                }
            )
            if created or not hasattr(med8, 'stock'):
                MedicineStock.objects.update_or_create(
                    medicine=med8,
                    defaults={'current_stock': 2, 'initial_quantity': 3, 'consumed_quantity': 1, 'minimum_stock_level': 1, 'unit': 'tablets'}
                )

        self.stdout.write(self.style.SUCCESS("Successfully seeded medicines and 3 expiry tracker batches!"))

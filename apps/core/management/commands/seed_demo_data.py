"""
Comprehensive Indian Healthcare Demo Data Seeder Command.
Seeds a realistic, production-grade clinical universe for an Indian family:
- Patient Profiles: Rajesh Sharma, Priya Sharma, Aarav Sharma, Saraswati Sharma
- Doctors: Dr. Arvind Swaminathan (Apollo), Dr. Meenakshi Sundaram (Fortis), Dr. Vikramaditya Rao (Rainbow Children's)
- Tailored Medications: Telma 40, Rosuvas 10, Thyronorm 50mcg, Shelcal 500, Montair-LC Kid, Glycomet-SR 500
- Individualized Activities: Morning Jogging, Power Yoga, Cricket Coaching, Physiotherapy Garden Walking
- Regional Diets: Poha, Idli-Sambar, Moong Dal Chilla, Paneer Paratha, Ragi Idli, Rajma Chawal
- Vitals, Lab records, and clinical appointments.

Run via: python manage.py seed_demo_data
"""

from datetime import date, time, timedelta, datetime
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone

from apps.family.models import FamilyMember
from apps.medications.models import (
    Medicine, MedicineSchedule, MedicineDose, MedicationLog,
    MedicineStock, MedicineRefill, MedicineExpiry
)
from apps.medications.services.scheduler_service import MedicationSchedulerService
from apps.medical.models import (
    Doctor, Appointment, Prescription, HealthProfile,
    VitalRecord, SymptomRecord, Vaccination, Allergy
)
from apps.wellness.models import MealRecord, ActivityRecord, SleepRecord, HealthGoal
from apps.notifications.services import create_notification
from apps.audit.models import AuditLog

User = get_user_model()


class Command(BaseCommand):
    help = "Seeds complete Indian clinical and wellness demo data into the local database."

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Initializing Indian family health universe seeder..."))

        # 1. Accounts
        demo_user, _ = User.objects.get_or_create(
            username='demo',
            defaults={
                'email': 'rajesh.sharma@healthorganizer.in',
                'first_name': 'Rajesh',
                'last_name': 'Sharma',
                'phone_number': '+91 98765 43210',
                'is_active': True
            }
        )
        demo_user.first_name = 'Rajesh'
        demo_user.last_name = 'Sharma'
        demo_user.email = 'rajesh.sharma@healthorganizer.in'
        demo_user.phone_number = '+91 98765 43210'
        demo_user.set_password('DemoPass123!')
        demo_user.save()

        admin_user, _ = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@healthorganizer.in',
                'first_name': 'System',
                'last_name': 'Administrator',
                'is_staff': True,
                'is_superuser': True,
                'is_active': True
            }
        )
        admin_user.set_password('AdminPass123!')
        admin_user.save()
        self.stdout.write("[OK] Configured accounts: 'demo' (pass: DemoPass123!) and 'admin' (pass: AdminPass123!)")

        # 2. Family Members (Indian Names & Relationships)
        rajesh, _ = FamilyMember.objects.get_or_create(
            user=demo_user,
            relationship='SELF',
            defaults={
                'first_name': 'Rajesh',
                'last_name': 'Sharma',
                'date_of_birth': date(1982, 5, 14),
                'gender': 'M',
                'blood_group': 'B+',
                'emergency_contact': 'Priya Sharma (+91 98765 12345)',
                'is_active': True
            }
        )
        rajesh.first_name = 'Rajesh'
        rajesh.last_name = 'Sharma'
        rajesh.gender = 'M'
        rajesh.blood_group = 'B+'
        rajesh.emergency_contact = 'Priya Sharma (+91 98765 12345)'
        rajesh.save()

        priya, _ = FamilyMember.objects.get_or_create(
            user=demo_user,
            relationship='SPOUSE',
            defaults={
                'first_name': 'Priya',
                'last_name': 'Sharma',
                'date_of_birth': date(1985, 8, 22),
                'gender': 'F',
                'blood_group': 'O+',
                'emergency_contact': 'Rajesh Sharma (+91 98765 43210)',
                'is_active': True
            }
        )
        priya.first_name = 'Priya'
        priya.last_name = 'Sharma'
        priya.gender = 'F'
        priya.blood_group = 'O+'
        priya.emergency_contact = 'Rajesh Sharma (+91 98765 43210)'
        priya.save()

        aarav, _ = FamilyMember.objects.get_or_create(
            user=demo_user,
            relationship='SON',
            defaults={
                'first_name': 'Aarav',
                'last_name': 'Sharma',
                'date_of_birth': date(2013, 11, 3),
                'gender': 'M',
                'blood_group': 'B+',
                'emergency_contact': 'Rajesh Sharma (+91 98765 43210)',
                'is_active': True
            }
        )
        aarav.first_name = 'Aarav'
        aarav.last_name = 'Sharma'
        aarav.gender = 'M'
        aarav.blood_group = 'B+'
        aarav.emergency_contact = 'Rajesh Sharma (+91 98765 43210)'
        aarav.save()

        saraswati, _ = FamilyMember.objects.get_or_create(
            user=demo_user,
            relationship='MOTHER',
            defaults={
                'first_name': 'Saraswati',
                'last_name': 'Sharma',
                'date_of_birth': date(1956, 3, 19),
                'gender': 'F',
                'blood_group': 'AB+',
                'emergency_contact': 'Rajesh Sharma (+91 98765 43210)',
                'is_active': True
            }
        )
        saraswati.first_name = 'Saraswati'
        saraswati.last_name = 'Sharma'
        saraswati.gender = 'F'
        saraswati.blood_group = 'AB+'
        saraswati.emergency_contact = 'Rajesh Sharma (+91 98765 43210)'
        saraswati.save()
        self.stdout.write("[OK] Seeded Indian Family Members (Rajesh, Priya, Aarav, Saraswati)")

        # 3. Health Profiles
        HealthProfile.objects.update_or_create(
            family_member=rajesh,
            defaults={
                'blood_group': 'B+',
                'height_cm': 178.0,
                'weight_kg': 78.5,
                'medical_conditions': 'Essential Hypertension, Mild Dyslipidemia',
                'previous_surgeries': 'Appendectomy (2008)',
                'family_medical_history': 'Paternal coronary artery disease',
                'important_notes': 'Corporate professional; needs regular BP checks'
            }
        )

        HealthProfile.objects.update_or_create(
            family_member=priya,
            defaults={
                'blood_group': 'O+',
                'height_cm': 162.0,
                'weight_kg': 61.5,
                'medical_conditions': 'Subclinical Hypothyroidism, Vitamin D deficiency',
                'previous_surgeries': 'None',
                'family_medical_history': 'Maternal thyroid disorder',
                'important_notes': 'Take Thyronorm first thing in morning with plain water'
            }
        )

        HealthProfile.objects.update_or_create(
            family_member=aarav,
            defaults={
                'blood_group': 'B+',
                'height_cm': 142.0,
                'weight_kg': 35.0,
                'medical_conditions': 'Allergic Rhinitis, Seasonal Wheezing / Dust Sensitivity',
                'previous_surgeries': 'None',
                'family_medical_history': 'Family history of dust/pollen allergies',
                'important_notes': 'Carries Asthalin inhaler for sports and outdoor matches'
            }
        )

        HealthProfile.objects.update_or_create(
            family_member=saraswati,
            defaults={
                'blood_group': 'AB+',
                'height_cm': 156.0,
                'weight_kg': 64.0,
                'medical_conditions': 'Type 2 Diabetes Mellitus, Bilateral Knee Osteoarthritis',
                'previous_surgeries': 'Cataract Surgery - Both Eyes (2021)',
                'family_medical_history': 'Maternal diabetes and hypertension',
                'important_notes': 'Monitor fasting glucose fingerstick every morning'
            }
        )

        # 4. Indian Doctors & Hospitals
        dr_arvind, _ = Doctor.objects.get_or_create(
            user=demo_user,
            full_name='Dr. Arvind Swaminathan',
            defaults={
                'specialization': 'Cardiology & Internal Medicine',
                'hospital_clinic': 'Apollo Hospitals, Greams Road',
                'phone': '+91 98400 11223',
                'email': 'dr.arvind@apollohospitals.com',
                'address': '21 Greams Lane, Thousand Lights, Chennai',
                'notes': 'Consulting cardiologist for Rajesh Sharma'
            }
        )

        dr_meenakshi, _ = Doctor.objects.get_or_create(
            user=demo_user,
            full_name='Dr. Meenakshi Sundaram',
            defaults={
                'specialization': 'Endocrinology & Diabetology',
                'hospital_clinic': 'Fortis Healthcare, Bannerghatta Road',
                'phone': '+91 98200 44556',
                'email': 'dr.meenakshi@fortishealthcare.com',
                'address': '154/9 Bannerghatta Main Rd, Bangalore',
                'notes': 'Diabetologist consulting for Saraswati Sharma'
            }
        )

        dr_vikram, _ = Doctor.objects.get_or_create(
            user=demo_user,
            full_name='Dr. Vikramaditya Rao',
            defaults={
                'specialization': 'Pediatrics & Pediatric Pulmonology',
                'hospital_clinic': "Rainbow Children's Hospital",
                'phone': '+91 98800 77889',
                'email': 'dr.vikram@rainbowhospitals.in',
                'address': 'Road No. 2, Banjara Hills, Hyderabad',
                'notes': 'Pediatrician consulting for Aarav'
            }
        )
        self.stdout.write("[OK] Seeded Indian Doctors (Dr. Arvind Swaminathan, Dr. Meenakshi Sundaram, Dr. Vikramaditya Rao)")

        # 5. Tailored Indian Medications, Stocks, Batches
        today = timezone.now().date()

        # Med 1: Telma 40 (Telmisartan 40mg) for Rajesh
        telma, _ = Medicine.objects.get_or_create(
            user=demo_user,
            family_member=rajesh,
            name='Telma 40',
            defaults={
                'generic_name': 'Telmisartan 40mg',
                'brand_name': 'Glenmark Telma',
                'medicine_type': Medicine.TYPE_TABLET,
                'dosage': '1 Tablet (40mg)',
                'strength': '40',
                'unit': 'mg',
                'instructions': Medicine.INSTRUCTION_AFTER_FOOD,
                'start_date': today - timedelta(days=90),
                'prescribed_by': 'Dr. Arvind Swaminathan (Apollo)',
                'status': Medicine.STATUS_ACTIVE,
                'notes': 'Blood pressure management. Take every morning after breakfast.'
            }
        )
        MedicineStock.objects.update_or_create(
            medicine=telma,
            defaults={'current_stock': 28, 'initial_quantity': 30, 'consumed_quantity': 2, 'minimum_stock_level': 7, 'unit': 'tablets'}
        )
        MedicineExpiry.objects.update_or_create(
            medicine=telma,
            batch_number='TEL-9821',
            defaults={'expiry_date': today + timedelta(days=240), 'status': 'SAFE'}
        )

        # Med 2: Rosuvas 10 (Rosuvastatin 10mg) for Rajesh
        rosuvas, _ = Medicine.objects.get_or_create(
            user=demo_user,
            family_member=rajesh,
            name='Rosuvas 10',
            defaults={
                'generic_name': 'Rosuvastatin Calcium 10mg',
                'brand_name': 'Sun Pharma Rosuvas',
                'medicine_type': Medicine.TYPE_TABLET,
                'dosage': '1 Tablet (10mg)',
                'strength': '10',
                'unit': 'mg',
                'instructions': Medicine.INSTRUCTION_BEDTIME,
                'start_date': today - timedelta(days=60),
                'prescribed_by': 'Dr. Arvind Swaminathan (Apollo)',
                'status': Medicine.STATUS_ACTIVE,
                'notes': 'Cholesterol management. Take at bedtime.'
            }
        )
        MedicineStock.objects.update_or_create(
            medicine=rosuvas,
            defaults={'current_stock': 5, 'initial_quantity': 30, 'consumed_quantity': 25, 'minimum_stock_level': 7, 'unit': 'tablets'}
        )
        # Low stock & expiring soon batch
        MedicineExpiry.objects.update_or_create(
            medicine=rosuvas,
            batch_number='RSV-4412',
            defaults={'expiry_date': today + timedelta(days=18), 'status': 'EXPIRING_SOON'}
        )

        # Med 3: Thyronorm 50mcg for Priya
        thyronorm, _ = Medicine.objects.get_or_create(
            user=demo_user,
            family_member=priya,
            name='Thyronorm 50mcg',
            defaults={
                'generic_name': 'Levothyroxine Sodium 50mcg',
                'brand_name': 'Abbott Thyronorm',
                'medicine_type': Medicine.TYPE_TABLET,
                'dosage': '1 Tablet (50mcg)',
                'strength': '50',
                'unit': 'mcg',
                'instructions': Medicine.INSTRUCTION_EMPTY_STOMACH,
                'start_date': today - timedelta(days=120),
                'prescribed_by': 'Dr. Meenakshi Sundaram (Fortis)',
                'status': Medicine.STATUS_ACTIVE,
                'notes': 'Thyroid hormone replacement. Take early morning with a glass of water.'
            }
        )
        MedicineStock.objects.update_or_create(
            medicine=thyronorm,
            defaults={'current_stock': 65, 'initial_quantity': 100, 'consumed_quantity': 35, 'minimum_stock_level': 15, 'unit': 'tablets'}
        )
        MedicineExpiry.objects.update_or_create(
            medicine=thyronorm,
            batch_number='THY-8874',
            defaults={'expiry_date': today + timedelta(days=365), 'status': 'SAFE'}
        )

        # Med 4: Shelcal 500 for Priya
        shelcal, _ = Medicine.objects.get_or_create(
            user=demo_user,
            family_member=priya,
            name='Shelcal 500',
            defaults={
                'generic_name': 'Calcium 500mg + Vitamin D3 250 IU',
                'brand_name': 'Torrent Shelcal',
                'medicine_type': Medicine.TYPE_TABLET,
                'dosage': '1 Tablet (500mg)',
                'strength': '500',
                'unit': 'mg',
                'instructions': Medicine.INSTRUCTION_AFTER_FOOD,
                'start_date': today - timedelta(days=45),
                'prescribed_by': 'Dr. Meenakshi Sundaram (Fortis)',
                'status': Medicine.STATUS_ACTIVE,
                'notes': 'Bone density and calcium supplement. Take after lunch.'
            }
        )
        MedicineStock.objects.update_or_create(
            medicine=shelcal,
            defaults={'current_stock': 22, 'initial_quantity': 30, 'consumed_quantity': 8, 'minimum_stock_level': 7, 'unit': 'tablets'}
        )

        # Med 5: Montair-LC Kid for Aarav
        montair, _ = Medicine.objects.get_or_create(
            user=demo_user,
            family_member=aarav,
            name='Montair-LC Kid',
            defaults={
                'generic_name': 'Montelukast 4mg + Levocetirizine 2.5mg',
                'brand_name': 'Cipla Montair-LC',
                'medicine_type': Medicine.TYPE_TABLET,
                'dosage': '1 Chewable Tablet',
                'strength': '4/2.5',
                'unit': 'mg',
                'instructions': Medicine.INSTRUCTION_BEDTIME,
                'start_date': today - timedelta(days=10),
                'end_date': today + timedelta(days=20),
                'prescribed_by': 'Dr. Vikramaditya Rao (Rainbow)',
                'status': Medicine.STATUS_ACTIVE,
                'notes': 'Nightly chewable tablet for seasonal cough and dust allergy.'
            }
        )
        MedicineStock.objects.update_or_create(
            medicine=montair,
            defaults={'current_stock': 18, 'initial_quantity': 30, 'consumed_quantity': 12, 'minimum_stock_level': 5, 'unit': 'tablets'}
        )

        # Med 6: Glycomet-SR 500 for Saraswati
        glycomet, _ = Medicine.objects.get_or_create(
            user=demo_user,
            family_member=saraswati,
            name='Glycomet-SR 500',
            defaults={
                'generic_name': 'Metformin Hydrochloride Sustained Release 500mg',
                'brand_name': 'USV Glycomet',
                'medicine_type': Medicine.TYPE_TABLET,
                'dosage': '1 Tablet (500mg)',
                'strength': '500',
                'unit': 'mg',
                'instructions': Medicine.INSTRUCTION_WITH_FOOD,
                'start_date': today - timedelta(days=180),
                'prescribed_by': 'Dr. Meenakshi Sundaram (Fortis)',
                'status': Medicine.STATUS_ACTIVE,
                'notes': 'Antidiabetic therapy. Take twice daily with morning breakfast and night dinner.'
            }
        )
        MedicineStock.objects.update_or_create(
            medicine=glycomet,
            defaults={'current_stock': 52, 'initial_quantity': 60, 'consumed_quantity': 8, 'minimum_stock_level': 14, 'unit': 'tablets'}
        )

        # 6. Dosing Schedules
        s_telma, _ = MedicineSchedule.objects.get_or_create(
            medicine=telma,
            frequency='DAILY',
            defaults={'specific_times': ['08:00'], 'start_date': today - timedelta(days=30), 'is_active': True}
        )
        s_rosuvas, _ = MedicineSchedule.objects.get_or_create(
            medicine=rosuvas,
            frequency='DAILY',
            defaults={'specific_times': ['20:30'], 'start_date': today - timedelta(days=30), 'is_active': True}
        )
        s_thyro, _ = MedicineSchedule.objects.get_or_create(
            medicine=thyronorm,
            frequency='DAILY',
            defaults={'specific_times': ['06:30'], 'start_date': today - timedelta(days=30), 'is_active': True}
        )
        s_shelcal, _ = MedicineSchedule.objects.get_or_create(
            medicine=shelcal,
            frequency='DAILY',
            defaults={'specific_times': ['14:00'], 'start_date': today - timedelta(days=30), 'is_active': True}
        )
        s_montair, _ = MedicineSchedule.objects.get_or_create(
            medicine=montair,
            frequency='DAILY',
            defaults={'specific_times': ['20:00'], 'start_date': today - timedelta(days=10), 'end_date': today + timedelta(days=20), 'is_active': True}
        )
        s_glycomet, _ = MedicineSchedule.objects.get_or_create(
            medicine=glycomet,
            frequency='TWICE_DAILY',
            defaults={'specific_times': ['08:00', '20:00'], 'start_date': today - timedelta(days=30), 'is_active': True}
        )
        self.stdout.write("[OK] Created Indian medicine dosing schedules")

        # 7. Generate Rolling Doses & Historical Compliance
        MedicationSchedulerService.generate_doses_for_window(days_ahead=7, user=demo_user)

        # Populate realistic past doses for the family
        all_schedules = [s_telma, s_rosuvas, s_thyro, s_shelcal, s_montair, s_glycomet]
        for day_offset in range(14, 0, -1):
            past_date = today - timedelta(days=day_offset)
            for sched in all_schedules:
                if sched.start_date and sched.start_date > past_date:
                    continue
                for t_str in sched.specific_times:
                    h, m = [int(p) for p in t_str.split(':')]
                    p_time = time(hour=h, minute=m)
                    dose, _ = MedicineDose.objects.get_or_create(
                        schedule=sched,
                        date=past_date,
                        scheduled_time=p_time
                    )
                    naive_dt = datetime.combine(past_date, p_time)
                    aware_dt = timezone.make_aware(naive_dt)

                    if day_offset == 7 or day_offset == 3:
                        dose.status = MedicineDose.STATUS_SKIPPED
                        dose.notes = 'Fasting / delayed breakfast'
                        dose.save(update_fields=['status', 'notes'])
                        MedicationLog.objects.get_or_create(
                            medicine=sched.medicine,
                            family_member=sched.medicine.family_member,
                            dose=dose,
                            scheduled_time=aware_dt,
                            defaults={
                                'actual_time': aware_dt,
                                'status': MedicineDose.STATUS_SKIPPED,
                                'reason_for_skip': 'Fasting / delayed breakfast',
                                'logged_by': demo_user
                            }
                        )
                    else:
                        dose.status = MedicineDose.STATUS_TAKEN
                        dose.actual_time = aware_dt
                        dose.save(update_fields=['status', 'actual_time'])
                        MedicationLog.objects.get_or_create(
                            medicine=sched.medicine,
                            family_member=sched.medicine.family_member,
                            dose=dose,
                            scheduled_time=aware_dt,
                            defaults={
                                'actual_time': aware_dt,
                                'status': MedicineDose.STATUS_TAKEN,
                                'logged_by': demo_user
                            }
                        )
        self.stdout.write("[OK] Populated historical dose administration logs")

        # 8. Refill Records (Apollo Pharmacy / MedPlus)
        MedicineRefill.objects.get_or_create(
            medicine=telma,
            refill_date=today - timedelta(days=28),
            defaults={'refill_quantity': 30, 'cost': 240.00, 'pharmacy_source': 'Apollo Pharmacy, Indiranagar', 'notes': 'Monthly BP prescription refill'}
        )
        MedicineRefill.objects.get_or_create(
            medicine=thyronorm,
            refill_date=today - timedelta(days=60),
            defaults={'refill_quantity': 100, 'cost': 185.00, 'pharmacy_source': 'MedPlus Chemist', 'notes': 'Bottle of 100 tablets'}
        )

        # 9. Individualized Clinical Vitals
        # Rajesh (BP monitoring)
        rajesh_vitals = [
            (today - timedelta(days=24), 134, 86, 74, 79.2),
            (today - timedelta(days=18), 130, 84, 72, 78.9),
            (today - timedelta(days=12), 126, 82, 70, 78.7),
            (today - timedelta(days=6), 124, 80, 68, 78.5),
            (today - timedelta(days=1), 120, 78, 69, 78.5),
        ]
        for v_date, sys, dia, hr, wt in rajesh_vitals:
            VitalRecord.objects.get_or_create(
                family_member=rajesh,
                date=v_date,
                time=time(8, 15),
                defaults={
                    'blood_pressure_systolic': sys,
                    'blood_pressure_diastolic': dia,
                    'heart_rate': hr,
                    'weight_kg': wt,
                    'height_cm': 178.0,
                    'notes': 'Resting morning reading at home'
                }
            )

        # Priya (Heart rate & Weight monitoring)
        priya_vitals = [
            (today - timedelta(days=20), 116, 76, 72, 62.2),
            (today - timedelta(days=10), 114, 74, 70, 61.8),
            (today - timedelta(days=2), 112, 72, 68, 61.5),
        ]
        for v_date, sys, dia, hr, wt in priya_vitals:
            VitalRecord.objects.get_or_create(
                family_member=priya,
                date=v_date,
                time=time(9, 0),
                defaults={
                    'blood_pressure_systolic': sys,
                    'blood_pressure_diastolic': dia,
                    'heart_rate': hr,
                    'weight_kg': wt,
                    'height_cm': 162.0,
                    'notes': 'Post-yoga vital check'
                }
            )

        # Aarav (Pediatric vitals & SpO2)
        VitalRecord.objects.get_or_create(
            family_member=aarav,
            date=today - timedelta(days=3),
            time=time(17, 30),
            defaults={
                'heart_rate': 84,
                'oxygen_saturation': 99.0,
                'temperature_c': 36.6,
                'weight_kg': 35.0,
                'height_cm': 142.0,
                'notes': 'Routine pediatric vitals after cricket practice'
            }
        )

        # Saraswati (Fasting blood sugar log)
        saraswati_glucose = [
            (today - timedelta(days=15), 142.0, 134, 84),
            (today - timedelta(days=10), 136.0, 132, 82),
            (today - timedelta(days=5), 126.0, 130, 80),
            (today - timedelta(days=1), 118.0, 128, 80),
        ]
        for v_date, gluc, sys, dia in saraswati_glucose:
            VitalRecord.objects.get_or_create(
                family_member=saraswati,
                date=v_date,
                time=time(7, 30),
                defaults={
                    'blood_sugar_fasting': gluc,
                    'blood_pressure_systolic': sys,
                    'blood_pressure_diastolic': dia,
                    'weight_kg': 64.0,
                    'height_cm': 156.0,
                    'notes': 'Accu-Chek fingerstick fasting glucose'
                }
            )
        self.stdout.write("[OK] Seeded personalized clinical vitals across all 4 family members")

        # 10. Appointments
        Appointment.objects.get_or_create(
            user=demo_user,
            family_member=rajesh,
            doctor=dr_arvind,
            date=today + timedelta(days=6),
            time=time(10, 30),
            defaults={
                'reason': 'Hypertension & Lipid Follow-up Consultation',
                'location': 'Apollo Hospitals, Greams Road - Suite 204',
                'status': Appointment.STATUS_UPCOMING,
                'notes': 'Carry home blood pressure log chart'
            }
        )
        Appointment.objects.get_or_create(
            user=demo_user,
            family_member=saraswati,
            doctor=dr_meenakshi,
            date=today + timedelta(days=12),
            time=time(11, 0),
            defaults={
                'reason': 'Quarterly HbA1c & Diabetic Review',
                'location': 'Fortis Hospital, Bannerghatta - OPD 3',
                'status': Appointment.STATUS_UPCOMING,
                'notes': 'Fast for 10 hours prior for lipid and HbA1c blood tests'
            }
        )
        Appointment.objects.get_or_create(
            user=demo_user,
            family_member=aarav,
            doctor=dr_vikram,
            date=today - timedelta(days=15),
            time=time(16, 0),
            defaults={
                'reason': 'Seasonal Allergy & Wheezing Assessment',
                'location': "Rainbow Children's Hospital, Banjara Hills",
                'status': Appointment.STATUS_COMPLETED,
                'notes': 'Started Montair-LC Kid chewable course'
            }
        )

        # 11. Vaccinations (Indian Immunization Schedule)
        Vaccination.objects.get_or_create(
            family_member=rajesh,
            vaccine_name='Covishield / COVID-19 Booster',
            dose_number='Precautionary Booster Dose',
            vaccination_date=today - timedelta(days=365),
            defaults={'status': Vaccination.STATUS_COMPLETED, 'provider': 'Manipal Hospital, Bangalore'}
        )
        Vaccination.objects.get_or_create(
            family_member=aarav,
            vaccine_name='Typhoid Conjugate Vaccine (TCV)',
            dose_number='Booster Dose',
            vaccination_date=today - timedelta(days=180),
            defaults={'status': Vaccination.STATUS_COMPLETED, 'provider': "Rainbow Children's Clinic"}
        )
        Vaccination.objects.get_or_create(
            family_member=saraswati,
            vaccine_name='Pneumococcal Polysaccharide (Pneumovax 23)',
            dose_number='Senior Dose',
            vaccination_date=today - timedelta(days=90),
            next_due_date=today + timedelta(days=275),
            defaults={'status': Vaccination.STATUS_COMPLETED, 'provider': 'Apollo Senior Care'}
        )

        # 12. Allergies
        Allergy.objects.get_or_create(
            family_member=rajesh,
            allergen='Penicillin / Amoxicillin',
            defaults={
                'allergy_type': 'DRUG',
                'severity': 'SEVERE',
                'reaction': 'Generalized cutaneous hives, severe itching, and facial puffiness'
            }
        )
        Allergy.objects.get_or_create(
            family_member=priya,
            allergen='Sulfa Antibiotics',
            defaults={
                'allergy_type': 'DRUG',
                'severity': 'MODERATE',
                'reaction': 'Erythematous skin rash on arms and torso'
            }
        )
        Allergy.objects.get_or_create(
            family_member=aarav,
            allergen='Dust Mites & Particulate Smog',
            defaults={
                'allergy_type': 'ENVIRONMENTAL',
                'severity': 'MODERATE',
                'reaction': 'Sneezing bursts, allergic rhinitis, nocturnal dry cough'
            }
        )

        # 13. Symptoms
        SymptomRecord.objects.get_or_create(
            family_member=rajesh,
            symptom_name='Work-related Tension Headache',
            date=today - timedelta(days=2),
            time=time(17, 30),
            defaults={
                'severity': SymptomRecord.SEVERITY_MILD,
                'duration_hours': 2.0,
                'triggers': 'Continuous video calls, screen fatigue',
                'description': 'Dull aching across temples. Resolved with hydration and rest.'
            }
        )
        SymptomRecord.objects.get_or_create(
            family_member=saraswati,
            symptom_name='Bilateral Knee Joint Stiffness',
            date=today - timedelta(days=4),
            time=time(6, 30),
            defaults={
                'severity': SymptomRecord.SEVERITY_MODERATE,
                'duration_hours': 1.5,
                'triggers': 'Cold morning weather, prolonged sitting',
                'description': 'Stiffness when getting out of bed. Eased after warm water shower and gentle stretching.'
            }
        )

        # 14. DISTINCT LIFESTYLE & WELLNESS FOR EACH FAMILY MEMBER
        # -------------------------------------------------------------
        # 14.1 Rajesh Sharma: Jogging, Poha/Dal-Chawal, 7h Sleep, 10k Steps Goal
        # -------------------------------------------------------------
        MealRecord.objects.get_or_create(
            family_member=rajesh,
            date=today,
            meal_type=MealRecord.MEAL_BREAKFAST,
            defaults={'food_items': 'Poha with roasted peanuts, curry leaves & lemon + Green Tea', 'calories': 340, 'water_intake_ml': 400}
        )
        MealRecord.objects.get_or_create(
            family_member=rajesh,
            date=today,
            meal_type=MealRecord.MEAL_LUNCH,
            defaults={'food_items': '2 Multigrain Rotis, Palak Dal, Bhindi Masala, Cucumber Salad & Fresh Curd', 'calories': 560, 'water_intake_ml': 500}
        )
        ActivityRecord.objects.get_or_create(
            family_member=rajesh,
            date=today,
            activity_type=ActivityRecord.TYPE_RUNNING,
            defaults={
                'duration_minutes': 45,
                'distance_km': 5.2,
                'calories_burned': 390,
                'steps_count': 6400,
                'notes': 'Morning brisk jog around the neighborhood park'
            }
        )
        SleepRecord.objects.get_or_create(
            family_member=rajesh,
            date=today,
            defaults={
                'bedtime': time(23, 30),
                'wake_time': time(6, 45),
                'duration_hours': 7.25,
                'sleep_quality': SleepRecord.QUALITY_GOOD,
                'interruptions_count': 0,
                'notes': 'Woke up refreshed before the alarm'
            }
        )
        HealthGoal.objects.get_or_create(
            family_member=rajesh,
            title='Daily 10,000 Steps Target',
            defaults={
                'goal_type': HealthGoal.TYPE_STEPS,
                'target_value': 10000,
                'current_value': 6400,
                'unit': 'steps',
                'status': HealthGoal.STATUS_ACTIVE,
                'notes': 'Hit 10k steps daily through morning jogs and evening walks'
            }
        )
        HealthGoal.objects.get_or_create(
            family_member=rajesh,
            title='Target Body Weight: 74 kg',
            defaults={
                'goal_type': HealthGoal.TYPE_WEIGHT,
                'target_value': 74.0,
                'current_value': 78.5,
                'unit': 'kg',
                'status': HealthGoal.STATUS_ACTIVE,
                'notes': 'Reduce visceral fat and improve cardiovascular endurance'
            }
        )

        # -------------------------------------------------------------
        # 14.2 Priya Sharma: Power Yoga, Moong Chilla/Quinoa, 7.8h Sleep, Hydration Goal
        # -------------------------------------------------------------
        MealRecord.objects.get_or_create(
            family_member=priya,
            date=today,
            meal_type=MealRecord.MEAL_BREAKFAST,
            defaults={'food_items': '2 Sprouted Moong Dal Chillas with mint coriander chutney + Warm Lemon Water', 'calories': 290, 'water_intake_ml': 500}
        )
        MealRecord.objects.get_or_create(
            family_member=priya,
            date=today,
            meal_type=MealRecord.MEAL_LUNCH,
            defaults={'food_items': 'Vegetable Quinoa Khichdi, Boondi Raita & Steamed French Beans', 'calories': 480, 'water_intake_ml': 500}
        )
        ActivityRecord.objects.get_or_create(
            family_member=priya,
            date=today,
            activity_type=ActivityRecord.TYPE_YOGA,
            defaults={
                'duration_minutes': 40,
                'calories_burned': 260,
                'steps_count': 1400,
                'notes': 'Surya Namaskar (12 cycles), Pranayama and core stretching'
            }
        )
        SleepRecord.objects.get_or_create(
            family_member=priya,
            date=today,
            defaults={
                'bedtime': time(22, 30),
                'wake_time': time(6, 15),
                'duration_hours': 7.75,
                'sleep_quality': SleepRecord.QUALITY_EXCELLENT,
                'interruptions_count': 0,
                'notes': 'Deep and peaceful sleep'
            }
        )
        HealthGoal.objects.get_or_create(
            family_member=priya,
            title='Daily Hydration: 2.5 Liters',
            defaults={
                'goal_type': HealthGoal.TYPE_WATER,
                'target_value': 2500,
                'current_value': 1800,
                'unit': 'ml',
                'status': HealthGoal.STATUS_ACTIVE,
                'notes': 'Maintain high hydration for thyroid and skin vitality'
            }
        )

        # -------------------------------------------------------------
        # 14.3 Aarav Sharma: Cricket Coaching & Swimming, Paratha/Rajma, 9h Sleep
        # -------------------------------------------------------------
        MealRecord.objects.get_or_create(
            family_member=aarav,
            date=today,
            meal_type=MealRecord.MEAL_BREAKFAST,
            defaults={'food_items': '1 Paneer Paratha with homemade butter, a boiled egg & Badam Milk', 'calories': 440, 'water_intake_ml': 350}
        )
        MealRecord.objects.get_or_create(
            family_member=aarav,
            date=today,
            meal_type=MealRecord.MEAL_LUNCH,
            defaults={'food_items': 'Rajma Chawal with sliced carrot, cucumber & a sweet gulab jamun', 'calories': 580, 'water_intake_ml': 500}
        )
        ActivityRecord.objects.get_or_create(
            family_member=aarav,
            date=today,
            activity_type=ActivityRecord.TYPE_OTHER,
            defaults={
                'duration_minutes': 60,
                'calories_burned': 350,
                'steps_count': 4800,
                'notes': 'School Cricket Academy batting practice and sprint fielding drills'
            }
        )
        SleepRecord.objects.get_or_create(
            family_member=aarav,
            date=today,
            defaults={
                'bedtime': time(21, 30),
                'wake_time': time(6, 30),
                'duration_hours': 9.0,
                'sleep_quality': SleepRecord.QUALITY_EXCELLENT,
                'interruptions_count': 0,
                'notes': 'Uninterrupted restful growth sleep'
            }
        )
        HealthGoal.objects.get_or_create(
            family_member=aarav,
            title='60 Mins Daily Outdoor Sports',
            defaults={
                'goal_type': HealthGoal.TYPE_CUSTOM,
                'target_value': 60,
                'current_value': 60,
                'unit': 'minutes',
                'status': HealthGoal.STATUS_COMPLETED,
                'notes': 'Active physical development and fresh air exercise'
            }
        )

        # -------------------------------------------------------------
        # 14.4 Saraswati Sharma: Physiotherapy Stroll, Ragi/Khichdi, 6.5h Sleep, Glucose Goal
        # -------------------------------------------------------------
        MealRecord.objects.get_or_create(
            family_member=saraswati,
            date=today,
            meal_type=MealRecord.MEAL_BREAKFAST,
            defaults={'food_items': '2 Steamed Ragi Idlis with vegetable sambar & roasted tomato chutney', 'calories': 280, 'water_intake_ml': 300}
        )
        MealRecord.objects.get_or_create(
            family_member=saraswati,
            date=today,
            meal_type=MealRecord.MEAL_LUNCH,
            defaults={'food_items': '1 Methi Thepla, Moong Dal Khichdi, Lauki Sabzi & a glass of Spiced Buttermilk', 'calories': 420, 'water_intake_ml': 400}
        )
        ActivityRecord.objects.get_or_create(
            family_member=saraswati,
            date=today,
            activity_type=ActivityRecord.TYPE_WALKING,
            defaults={
                'duration_minutes': 25,
                'distance_km': 1.4,
                'calories_burned': 95,
                'steps_count': 2100,
                'notes': 'Gentle evening garden walk and knee physiotherapy quadriceps flexes'
            }
        )
        SleepRecord.objects.get_or_create(
            family_member=saraswati,
            date=today,
            defaults={
                'bedtime': time(22, 0),
                'wake_time': time(5, 0),
                'duration_hours': 6.5,
                'sleep_quality': SleepRecord.QUALITY_FAIR,
                'interruptions_count': 1,
                'notes': 'Woke up at 2:30 AM for water, fell back asleep'
            }
        )
        HealthGoal.objects.get_or_create(
            family_member=saraswati,
            title='Fasting Glucose Target < 120 mg/dL',
            defaults={
                'goal_type': HealthGoal.TYPE_CUSTOM,
                'target_value': 120,
                'current_value': 118,
                'unit': 'mg/dL',
                'status': HealthGoal.STATUS_COMPLETED,
                'notes': 'Maintain tight glycemic control via Glycomet-SR and diet'
            }
        )
        self.stdout.write("[OK] Seeded distinct activities, nutrition meals, sleep, and goals for all 4 family members")

        # 15. In-App Notifications
        create_notification(
            user=demo_user,
            family_member=rajesh,
            category='REFILL',
            priority='HIGH',
            title='Low Stock Alert: Rosuvas 10',
            message='Only 5 tablets remaining for Rajesh Sharma. Reorder from Apollo Pharmacy or MedPlus.',
            action_url=f"/medications/stock/{rosuvas.id}/refill/"
        )

        create_notification(
            user=demo_user,
            family_member=rajesh,
            category='APPOINTMENT',
            priority='NORMAL',
            title='Upcoming Visit with Dr. Arvind Swaminathan',
            message=f"Consultation scheduled on {(today + timedelta(days=6)).strftime('%b %d')} at 10:30 AM at Apollo Hospitals.",
            action_url="/medical/appointments/"
        )

        # 16. Audit Log
        AuditLog.objects.create(
            user=demo_user,
            action='SYSTEM_SEED',
            module='SYSTEM',
            description="Indian clinical healthcare universe seeded successfully."
        )

        self.stdout.write(self.style.SUCCESS(
            "\n===========================================================\n"
            "   INDIAN HEALTH ORGANIZER UNIVERSE SEEDED SUCCESSFULLY!  \n"
            "===========================================================\n"
            "Credentials:\n"
            "  Primary Account: username: 'demo'    | password: 'DemoPass123!'\n"
            "  Administrator:   username: 'admin'   | password: 'AdminPass123!'\n"
            "Patients:\n"
            "  1. Rajesh Sharma (Father, 42)    - Jogging, BP monitoring, Telma 40\n"
            "  2. Priya Sharma (Mother, 39)     - Power Yoga, Thyroid, Thyronorm 50\n"
            "  3. Aarav Sharma (Son, 11)        - Cricket/Sports, Allergy, Montair-LC\n"
            "  4. Saraswati Sharma (Mother, 68) - Physiotherapy, Diabetes, Glycomet\n"
            "===========================================================\n"
        ))

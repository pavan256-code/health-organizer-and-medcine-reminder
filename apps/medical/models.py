"""
Clinical, physician, vitals, symptoms, vaccinations, allergies, and secure document models.
"""

from django.db import models
from django.conf import settings
from django.utils import timezone
from apps.core.models import TimeStampedModel
from apps.family.models import FamilyMember


class Doctor(TimeStampedModel):
    """
    Physician or specialist directory associated with a user's family care network.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='doctors')
    full_name = models.CharField(max_length=150)
    specialization = models.CharField(max_length=100, help_text="e.g. Cardiologist, Pediatrician, General Practitioner")
    hospital_clinic = models.CharField(max_length=150, blank=True, default='')
    phone = models.CharField(max_length=30, blank=True, default='')
    email = models.EmailField(blank=True, default='')
    address = models.TextField(blank=True, default='')
    notes = models.TextField(blank=True, default='')

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'
        ordering = ['full_name']

    def __str__(self):
        return f"{self.full_name} ({self.specialization})"


class Appointment(TimeStampedModel):
    """
    Medical and clinical visits.
    """
    STATUS_UPCOMING = 'UPCOMING'
    STATUS_COMPLETED = 'COMPLETED'
    STATUS_CANCELLED = 'CANCELLED'
    STATUS_MISSED = 'MISSED'

    STATUS_CHOICES = [
        (STATUS_UPCOMING, 'Upcoming'),
        (STATUS_COMPLETED, 'Completed'),
        (STATUS_CANCELLED, 'Cancelled'),
        (STATUS_MISSED, 'Missed'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='appointments')
    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateField(db_index=True)
    time = models.TimeField()
    location = models.CharField(max_length=200, blank=True, default='')
    reason = models.CharField(max_length=250, help_text="e.g. Annual physical, Follow-up consultation")
    notes = models.TextField(blank=True, default='')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_UPCOMING, db_index=True)
    reminder_sent = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'
        ordering = ['date', 'time']
        indexes = [
            models.Index(fields=['family_member', 'date']),
            models.Index(fields=['status', 'date']),
        ]

    def __str__(self):
        return f"{self.family_member.full_name} with {self.doctor.full_name} on {self.date} at {self.time}"


class Prescription(TimeStampedModel):
    """
    Doctor's written prescription linked to patient and containing clinical diagnosis.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='prescriptions')
    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE, related_name='prescriptions')
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True, related_name='prescriptions')
    title = models.CharField(max_length=200)
    prescription_date = models.DateField(default=timezone.now)
    diagnosis = models.TextField(blank=True, default='', help_text="Clinical assessment or diagnosis")
    instructions = models.TextField(blank=True, default='')
    notes = models.TextField(blank=True, default='')
    document_file = models.FileField(upload_to='documents/prescriptions/', null=True, blank=True)

    class Meta:
        verbose_name = 'Prescription'
        verbose_name_plural = 'Prescriptions'
        ordering = ['-prescription_date']

    def __str__(self):
        return f"{self.title} - {self.family_member.full_name} ({self.prescription_date})"


class PrescriptionMedicine(TimeStampedModel):
    """
    Itemized medicines listed on a prescription.
    """
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name='items')
    medicine_name = models.CharField(max_length=150)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100, help_text="e.g. Twice daily for 5 days")
    duration_days = models.PositiveIntegerField(null=True, blank=True)
    instructions = models.CharField(max_length=255, blank=True, default='')

    class Meta:
        verbose_name = 'Prescription Medicine Item'
        verbose_name_plural = 'Prescription Medicine Items'

    def __str__(self):
        return f"{self.medicine_name} ({self.dosage})"


class HealthProfile(TimeStampedModel):
    """
    Comprehensive permanent health profile of a patient.
    """
    family_member = models.OneToOneField(FamilyMember, on_delete=models.CASCADE, related_name='health_profile')
    blood_group = models.CharField(max_length=10, default='UNKNOWN')
    height_cm = models.FloatField(null=True, blank=True, help_text="Height in centimeters")
    weight_kg = models.FloatField(null=True, blank=True, help_text="Weight in kilograms")
    medical_conditions = models.TextField(blank=True, default='', help_text="Chronic illnesses or medical conditions (e.g. Asthma, Hypertension)")
    previous_surgeries = models.TextField(blank=True, default='', help_text="Past surgical procedures and dates")
    family_medical_history = models.TextField(blank=True, default='', help_text="Hereditary or family history")
    important_notes = models.TextField(blank=True, default='')

    class Meta:
        verbose_name = 'Health Profile'
        verbose_name_plural = 'Health Profiles'

    def __str__(self):
        return f"Health Profile: {self.family_member.full_name}"

    @property
    def bmi(self):
        if self.height_cm and self.weight_kg and self.height_cm > 0:
            h_m = self.height_cm / 100.0
            return round(self.weight_kg / (h_m * h_m), 1)
        return None


class VitalRecord(TimeStampedModel):
    """
    Quantitative physiological measurements: BP, glucose, heart rate, BMI, SpO2, temp.
    """
    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE, related_name='vitals')
    date = models.DateField(default=timezone.now, db_index=True)
    time = models.TimeField(default=timezone.now)

    # Blood Pressure
    blood_pressure_systolic = models.PositiveIntegerField(null=True, blank=True, help_text="Systolic (mmHg)")
    blood_pressure_diastolic = models.PositiveIntegerField(null=True, blank=True, help_text="Diastolic (mmHg)")

    # Blood Glucose
    blood_sugar_fasting = models.FloatField(null=True, blank=True, help_text="Fasting Blood Glucose (mg/dL)")
    blood_sugar_postprandial = models.FloatField(null=True, blank=True, help_text="Postprandial Glucose (mg/dL)")

    # Cardio & Respiratory
    heart_rate = models.PositiveIntegerField(null=True, blank=True, help_text="Resting Heart Rate (BPM)")
    oxygen_saturation = models.FloatField(null=True, blank=True, help_text="Blood Oxygen Saturation SpO2 (%)")
    temperature_c = models.FloatField(null=True, blank=True, help_text="Body Temperature (°C)")

    # Anthropometry
    weight_kg = models.FloatField(null=True, blank=True, help_text="Weight (kg)")
    height_cm = models.FloatField(null=True, blank=True, help_text="Height (cm)")
    bmi = models.FloatField(null=True, blank=True, help_text="Computed Body Mass Index")

    notes = models.CharField(max_length=255, blank=True, default='')

    class Meta:
        verbose_name = 'Vital Record'
        verbose_name_plural = 'Vital Records'
        ordering = ['-date', '-time']
        indexes = [
            models.Index(fields=['family_member', '-date', '-time']),
        ]

    def save(self, *args, **kwargs):
        # Calculate BMI automatically if height & weight provided
        if self.height_cm and self.weight_kg and self.height_cm > 0:
            h_m = self.height_cm / 100.0
            self.bmi = round(self.weight_kg / (h_m * h_m), 1)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Vitals: {self.family_member.full_name} on {self.date}"

    @property
    def bp_category(self):
        if not (self.blood_pressure_systolic and self.blood_pressure_diastolic):
            return "Unrecorded"
        s = self.blood_pressure_systolic
        d = self.blood_pressure_diastolic
        if s < 120 and d < 80:
            return "Normal"
        elif 120 <= s <= 129 and d < 80:
            return "Elevated"
        elif (130 <= s <= 139) or (80 <= d <= 89):
            return "Hypertension Stage 1"
        elif s >= 180 or d >= 120:
            return "Hypertensive Crisis"
        elif s >= 140 or d >= 90:
            return "Hypertension Stage 2"
        return "Normal"


class SymptomRecord(TimeStampedModel):
    """
    Patient symptom journal with severity rating, duration, and triggers.
    """
    SEVERITY_MILD = 'MILD'
    SEVERITY_MODERATE = 'MODERATE'
    SEVERITY_SEVERE = 'SEVERE'

    SEVERITY_CHOICES = [
        (SEVERITY_MILD, 'Mild (Minor discomfort, daily activity unaffected)'),
        (SEVERITY_MODERATE, 'Moderate (Noticeable discomfort, interferes with tasks)'),
        (SEVERITY_SEVERE, 'Severe (Incapacitating, seek clinical evaluation)'),
    ]

    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE, related_name='symptoms')
    symptom_name = models.CharField(max_length=150)
    severity = models.CharField(max_length=15, choices=SEVERITY_CHOICES, default=SEVERITY_MILD)
    date = models.DateField(default=timezone.now, db_index=True)
    time = models.TimeField(default=timezone.now)
    duration_hours = models.FloatField(null=True, blank=True, help_text="Duration in hours")
    triggers = models.CharField(max_length=255, blank=True, default='', help_text="e.g. Cold weather, Stress, Exercise")
    description = models.TextField(blank=True, default='')
    notes = models.TextField(blank=True, default='')

    class Meta:
        verbose_name = 'Symptom Record'
        verbose_name_plural = 'Symptom Records'
        ordering = ['-date', '-time']

    def __str__(self):
        return f"{self.symptom_name} ({self.severity}) - {self.family_member.full_name}"


class Vaccination(TimeStampedModel):
    """
    Immunization records with dose tracking and scheduled due dates.
    """
    STATUS_COMPLETED = 'COMPLETED'
    STATUS_UPCOMING = 'UPCOMING'
    STATUS_OVERDUE = 'OVERDUE'

    STATUS_CHOICES = [
        (STATUS_COMPLETED, 'Completed'),
        (STATUS_UPCOMING, 'Upcoming Scheduled'),
        (STATUS_OVERDUE, 'Overdue'),
    ]

    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE, related_name='vaccinations')
    vaccine_name = models.CharField(max_length=150)
    dose_number = models.CharField(max_length=50, default='1st Dose')
    vaccination_date = models.DateField(default=timezone.now)
    next_due_date = models.DateField(null=True, blank=True)
    provider = models.CharField(max_length=150, blank=True, default='', help_text="Hospital / Health center")
    notes = models.TextField(blank=True, default='')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_COMPLETED)

    class Meta:
        verbose_name = 'Vaccination'
        verbose_name_plural = 'Vaccinations'
        ordering = ['-vaccination_date']

    def __str__(self):
        return f"{self.vaccine_name} ({self.dose_number}) - {self.family_member.full_name}"


class Allergy(TimeStampedModel):
    """
    Known drug, food, environmental, or chemical hypersensitivities.
    """
    TYPE_CHOICES = [
        ('DRUG', 'Drug / Pharmaceutical'),
        ('FOOD', 'Food / Dietary'),
        ('ENVIRONMENTAL', 'Environmental (Dust, Pollen)'),
        ('INSECT', 'Insect Venom'),
        ('OTHER', 'Other Substance'),
    ]

    SEVERITY_CHOICES = [
        ('MILD', 'Mild (Rash, itching)'),
        ('MODERATE', 'Moderate (Hives, swelling)'),
        ('SEVERE', 'Severe (Wheezing, difficulty breathing)'),
        ('CRITICAL', 'Critical / Anaphylactic Risk'),
    ]

    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE, related_name='allergies')
    allergen = models.CharField(max_length=150, help_text="e.g. Penicillin, Peanuts, Sulfa drugs")
    allergy_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='DRUG')
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES, default='MODERATE')
    reaction = models.CharField(max_length=250, help_text="e.g. Hives, facial swelling, anaphylaxis")
    date_identified = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True, default='')

    class Meta:
        verbose_name = 'Allergy'
        verbose_name_plural = 'Allergies'
        ordering = ['-severity', 'allergen']

    def __str__(self):
        return f"{self.allergen} ({self.severity}) - {self.family_member.full_name}"


class MedicalDocument(TimeStampedModel):
    """
    Secure local document vault for lab tests, diagnostic scans, and clinical certificates.
    """
    CAT_PRESCRIPTION = 'PRESCRIPTION'
    CAT_LAB_REPORT = 'LAB_REPORT'
    CAT_SCAN_REPORT = 'SCAN_REPORT'
    CAT_CERTIFICATE = 'CERTIFICATE'
    CAT_VACCINE = 'VACCINE'
    CAT_DOCTOR_REPORT = 'DOCTOR_REPORT'
    CAT_OTHER = 'OTHER'

    CATEGORY_CHOICES = [
        (CAT_PRESCRIPTION, 'Prescription'),
        (CAT_LAB_REPORT, 'Lab Test / Blood Report'),
        (CAT_SCAN_REPORT, 'Scan Report (X-Ray, MRI, CT, Ultrasound)'),
        (CAT_CERTIFICATE, 'Medical Certificate / Fit Certificate'),
        (CAT_VACCINE, 'Vaccination Card'),
        (CAT_DOCTOR_REPORT, 'Doctor Discharge / Consultation Summary'),
        (CAT_OTHER, 'Other Clinical Document'),
    ]

    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE, related_name='documents')
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default=CAT_LAB_REPORT)
    file = models.FileField(upload_to='documents/vault/')
    file_size = models.PositiveIntegerField(default=0, help_text="Size in bytes")
    file_type = models.CharField(max_length=50, blank=True, default='')
    document_date = models.DateField(default=timezone.now)
    notes = models.TextField(blank=True, default='')

    class Meta:
        verbose_name = 'Medical Document'
        verbose_name_plural = 'Medical Documents'
        ordering = ['-document_date', '-created_at']

    def __str__(self):
        return f"{self.title} ({self.get_category_display()}) - {self.family_member.full_name}"

    @property
    def file_size_mb(self):
        return round(self.file_size / (1024 * 1024), 2)

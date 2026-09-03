"""
Admin configurations for Medical app.
"""

from django.contrib import admin
from apps.medical.models import (
    Doctor, Appointment, Prescription, PrescriptionMedicine,
    HealthProfile, VitalRecord, SymptomRecord, Vaccination, Allergy, MedicalDocument
)


class PrescriptionMedicineInline(admin.TabularInline):
    model = PrescriptionMedicine
    extra = 1


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'specialization', 'hospital_clinic', 'phone', 'user')
    search_fields = ('full_name', 'specialization', 'hospital_clinic')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'family_member', 'date', 'time', 'status')
    list_filter = ('status', 'date')
    search_fields = ('doctor__full_name', 'family_member__first_name', 'reason')


@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    inlines = [PrescriptionMedicineInline]
    list_display = ('title', 'family_member', 'doctor', 'prescription_date')
    list_filter = ('prescription_date',)
    search_fields = ('title', 'diagnosis', 'family_member__first_name')


@admin.register(HealthProfile)
class HealthProfileAdmin(admin.ModelAdmin):
    list_display = ('family_member', 'blood_group', 'height_cm', 'weight_kg', 'bmi')


@admin.register(VitalRecord)
class VitalRecordAdmin(admin.ModelAdmin):
    list_display = ('family_member', 'date', 'time', 'blood_pressure_systolic', 'blood_pressure_diastolic', 'blood_sugar_fasting', 'heart_rate')
    list_filter = ('date',)
    search_fields = ('family_member__first_name',)


@admin.register(SymptomRecord)
class SymptomRecordAdmin(admin.ModelAdmin):
    list_display = ('symptom_name', 'family_member', 'severity', 'date', 'duration_hours')
    list_filter = ('severity', 'date')
    search_fields = ('symptom_name', 'triggers')


@admin.register(Vaccination)
class VaccinationAdmin(admin.ModelAdmin):
    list_display = ('vaccine_name', 'family_member', 'dose_number', 'vaccination_date', 'status')
    list_filter = ('status', 'vaccination_date')
    search_fields = ('vaccine_name',)


@admin.register(Allergy)
class AllergyAdmin(admin.ModelAdmin):
    list_display = ('allergen', 'family_member', 'allergy_type', 'severity')
    list_filter = ('allergy_type', 'severity')
    search_fields = ('allergen', 'reaction')


@admin.register(MedicalDocument)
class MedicalDocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'family_member', 'category', 'document_date', 'file_size', 'created_at')
    list_filter = ('category', 'document_date')
    search_fields = ('title', 'family_member__first_name')

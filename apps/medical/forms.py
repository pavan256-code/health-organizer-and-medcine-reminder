"""
Forms for medical management: Doctors, Appointments, Prescriptions, Vitals, Symptoms, Vaccinations, Allergies, and Documents.
"""

from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from apps.medical.models import (
    Doctor, Appointment, Prescription, HealthProfile,
    VitalRecord, SymptomRecord, Vaccination, Allergy, MedicalDocument
)
from apps.family.models import FamilyMember
from apps.core.utils import validate_medical_document


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['full_name', 'specialization', 'hospital_clinic', 'phone', 'email', 'address', 'notes']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Dr. Jane Smith'}),
            'specialization': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Cardiology'}),
            'hospital_clinic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Clinic or Hospital Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'doctor@example.com'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['family_member', 'doctor', 'date', 'time', 'location', 'reason', 'status', 'notes']
        widgets = {
            'family_member': forms.Select(attrs={'class': 'form-select'}),
            'doctor': forms.Select(attrs={'class': 'form-select'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hospital address or room'}),
            'reason': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Follow-up consultation'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.fields['family_member'].queryset = FamilyMember.objects.filter(user=user, is_active=True)
        self.fields['doctor'].queryset = Doctor.objects.filter(user=user)


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['family_member', 'doctor', 'title', 'prescription_date', 'diagnosis', 'instructions', 'notes', 'document_file']
        widgets = {
            'family_member': forms.Select(attrs={'class': 'form-select'}),
            'doctor': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Hypertension Review'}),
            'prescription_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'diagnosis': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Assessment / Diagnosis'}),
            'instructions': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'General instructions'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'document_file': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.fields['family_member'].queryset = FamilyMember.objects.filter(user=user, is_active=True)
        self.fields['doctor'].queryset = Doctor.objects.filter(user=user)


class HealthProfileForm(forms.ModelForm):
    class Meta:
        model = HealthProfile
        fields = ['blood_group', 'height_cm', 'weight_kg', 'medical_conditions', 'previous_surgeries', 'family_medical_history', 'important_notes']
        widgets = {
            'blood_group': forms.TextInput(attrs={'class': 'form-control'}),
            'height_cm': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'weight_kg': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'medical_conditions': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'previous_surgeries': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'family_medical_history': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'important_notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }


class VitalRecordForm(forms.ModelForm):
    class Meta:
        model = VitalRecord
        fields = [
            'family_member', 'date', 'time',
            'blood_pressure_systolic', 'blood_pressure_diastolic',
            'blood_sugar_fasting', 'blood_sugar_postprandial',
            'heart_rate', 'oxygen_saturation', 'temperature_c',
            'weight_kg', 'height_cm', 'notes'
        ]
        widgets = {
            'family_member': forms.Select(attrs={'class': 'form-select'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'blood_pressure_systolic': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 120'}),
            'blood_pressure_diastolic': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 80'}),
            'blood_sugar_fasting': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'mg/dL'}),
            'blood_sugar_postprandial': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'mg/dL'}),
            'heart_rate': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'BPM'}),
            'oxygen_saturation': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': '%'}),
            'temperature_c': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': '°C'}),
            'weight_kg': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'kg'}),
            'height_cm': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'placeholder': 'cm'}),
            'notes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Measurement notes'}),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['family_member'].queryset = FamilyMember.objects.filter(user=user, is_active=True)


class SymptomRecordForm(forms.ModelForm):
    class Meta:
        model = SymptomRecord
        fields = ['family_member', 'symptom_name', 'severity', 'date', 'time', 'duration_hours', 'triggers', 'description', 'notes']
        widgets = {
            'family_member': forms.Select(attrs={'class': 'form-select'}),
            'symptom_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Throbbing Headache'}),
            'severity': forms.Select(attrs={'class': 'form-select'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'duration_hours': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.5'}),
            'triggers': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Dehydration, Lack of sleep'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['family_member'].queryset = FamilyMember.objects.filter(user=user, is_active=True)


class VaccinationForm(forms.ModelForm):
    class Meta:
        model = Vaccination
        fields = ['family_member', 'vaccine_name', 'dose_number', 'vaccination_date', 'next_due_date', 'provider', 'status', 'notes']
        widgets = {
            'family_member': forms.Select(attrs={'class': 'form-select'}),
            'vaccine_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Influenza, COVID-19'}),
            'dose_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Annual Booster'}),
            'vaccination_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'next_due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'provider': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Clinic name'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['family_member'].queryset = FamilyMember.objects.filter(user=user, is_active=True)


class AllergyForm(forms.ModelForm):
    class Meta:
        model = Allergy
        fields = ['family_member', 'allergen', 'allergy_type', 'severity', 'reaction', 'date_identified', 'notes']
        widgets = {
            'family_member': forms.Select(attrs={'class': 'form-select'}),
            'allergen': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Amoxicillin, Peanuts'}),
            'allergy_type': forms.Select(attrs={'class': 'form-select'}),
            'severity': forms.Select(attrs={'class': 'form-select'}),
            'reaction': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Skin rash, shortness of breath'}),
            'date_identified': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['family_member'].queryset = FamilyMember.objects.filter(user=user, is_active=True)


class MedicalDocumentForm(forms.ModelForm):
    class Meta:
        model = MedicalDocument
        fields = ['family_member', 'title', 'category', 'document_date', 'file', 'notes']
        widgets = {
            'family_member': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Annual Blood Panel Report'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'document_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['family_member'].queryset = FamilyMember.objects.filter(user=user, is_active=True)

    def clean_file(self):
        f = self.cleaned_data.get('file')
        if f:
            validate_medical_document(f)
        return f

    def save(self, commit=True):
        doc = super().save(commit=False)
        if doc.file:
            doc.file_size = doc.file.size
            doc.file_type = doc.file.name.split('.')[-1].upper()
        if commit:
            doc.save()
        return doc

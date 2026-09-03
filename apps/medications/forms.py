"""
Forms for medicine cataloging, scheduling, dose logging, refills, and expiry tracking.
"""

from django import forms
from django.core.exceptions import ValidationError
from apps.medications.models import (
    Medicine, MedicineSchedule, MedicineDose, MedicineRefill, MedicineExpiry, MedicineStock
)
from apps.family.models import FamilyMember


class MedicineForm(forms.ModelForm):
    """
    Form for adding or editing a prescription or OTC medicine.
    """
    initial_stock = forms.IntegerField(
        required=False,
        initial=30,
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        label="Initial Quantity on Hand"
    )
    minimum_stock = forms.IntegerField(
        required=False,
        initial=5,
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        label="Minimum Stock Threshold"
    )

    class Meta:
        model = Medicine
        fields = [
            'family_member', 'name', 'generic_name', 'brand_name',
            'medicine_type', 'dosage', 'strength', 'unit',
            'instructions', 'start_date', 'end_date', 'prescribed_by',
            'status', 'notes'
        ]
        widgets = {
            'family_member': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Amoxicillin'}),
            'generic_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Active ingredient'}),
            'brand_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Brand name'}),
            'medicine_type': forms.Select(attrs={'class': 'form-select'}),
            'dosage': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 1 Tablet (500mg)'}),
            'strength': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 500'}),
            'unit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. mg, ml'}),
            'instructions': forms.Select(attrs={'class': 'form-select'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'prescribed_by': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dr. Name / Clinic'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Special medical notes'}),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.fields['family_member'].queryset = FamilyMember.objects.filter(user=user, is_active=True)

        if self.instance and self.instance.pk and hasattr(self.instance, 'stock'):
            self.fields['initial_stock'].initial = self.instance.stock.current_stock
            self.fields['minimum_stock'].initial = self.instance.stock.minimum_stock_level

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('start_date')
        end = cleaned_data.get('end_date')
        if start and end and end < start:
            self.add_error('end_date', "End date cannot be prior to start date.")
        return cleaned_data

    def save(self, commit=True):
        medicine = super().save(commit=False)
        medicine.user = self.user
        if commit:
            medicine.save()
            # Provision or update MedicineStock
            init_stock = self.cleaned_data.get('initial_stock') or 30
            min_stock = self.cleaned_data.get('minimum_stock') or 5
            MedicineStock.objects.update_or_create(
                medicine=medicine,
                defaults={
                    'current_stock': init_stock,
                    'initial_quantity': init_stock,
                    'minimum_stock_level': min_stock,
                    'unit': medicine.unit or 'units'
                }
            )
        return medicine


class MedicineScheduleForm(forms.ModelForm):
    """
    Form for scheduling dosing routines (times and days).
    """
    times_input = forms.CharField(
        label="Dosing Times (24h format, comma-separated)",
        initial="08:00, 20:00",
        help_text="e.g. 08:00, 14:00, 20:00",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '08:00, 20:00'})
    )

    WEEKDAY_CHOICES = [
        (0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'),
        (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')
    ]

    selected_days = forms.MultipleChoiceField(
        choices=WEEKDAY_CHOICES,
        widget=forms.CheckboxSelectMultiple(),
        required=False,
        label="Days of the Week (for weekly or custom schedules)"
    )

    class Meta:
        model = MedicineSchedule
        fields = ['frequency', 'start_date', 'end_date', 'is_active']
        widgets = {
            'frequency': forms.Select(attrs={'class': 'form-select'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            if self.instance.specific_times:
                self.fields['times_input'].initial = ", ".join(self.instance.specific_times)
            if self.instance.days_of_week:
                self.fields['selected_days'].initial = [str(d) for d in self.instance.days_of_week]

    def clean_times_input(self):
        raw = self.cleaned_data.get('times_input', '')
        times_list = [t.strip() for t in raw.split(',') if t.strip()]
        if not times_list:
            raise ValidationError("At least one scheduled dose time is required.")

        import re
        for t in times_list:
            if not re.match(r'^(?:[01]?\d|2[0-3]):[0-5]\d$', t):
                raise ValidationError(f"Invalid time format '{t}'. Please use HH:MM (e.g. 08:30).")
        return times_list

    def save(self, medicine=None, commit=True):
        schedule = super().save(commit=False)
        if medicine:
            schedule.medicine = medicine
        schedule.specific_times = self.cleaned_data.get('times_input', [])
        sel_days = self.cleaned_data.get('selected_days', [])
        schedule.days_of_week = [int(d) for d in sel_days]

        if commit:
            schedule.save()
        return schedule


class DoseSkipForm(forms.Form):
    """
    Form for recording the clinical reason when a patient skips a dose.
    """
    REASON_CHOICES = [
        ('SIDE_EFFECTS', 'Experienced uncomfortable side effects'),
        ('DOCTOR_ADVICE', 'Advised to hold dose by physician'),
        ('FASTING', 'Fasting for clinical lab test'),
        ('FEELING_WELL', 'Felt better / symptoms resolved'),
        ('OUT_OF_STOCK', 'Medication out of stock / awaiting refill'),
        ('OTHER', 'Other reason (specified in notes)'),
    ]

    reason_category = forms.ChoiceField(
        choices=REASON_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    notes = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Optional additional notes'})
    )


class MedicineRefillForm(forms.ModelForm):
    """
    Form for logging an inventory replenishment.
    """
    class Meta:
        model = MedicineRefill
        fields = ['refill_date', 'refill_quantity', 'cost', 'pharmacy_source', 'notes']
        widgets = {
            'refill_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'refill_quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'cost': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Total purchase cost'}),
            'pharmacy_source': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Local Chemist / Pharmacy'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }


class MedicineExpiryForm(forms.ModelForm):
    """
    Form for registering a pharmaceutical batch lot and expiration date.
    """
    class Meta:
        model = MedicineExpiry
        fields = ['batch_number', 'expiry_date', 'alert_days_before', 'notes']
        widgets = {
            'batch_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Batch or Lot #'}),
            'expiry_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'alert_days_before': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 365}),
            'notes': forms.TextInput(attrs={'class': 'form-control'}),
        }

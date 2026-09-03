"""
Forms for adding, editing, and managing family members.
"""

from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from apps.family.models import FamilyMember


class FamilyMemberForm(forms.ModelForm):
    """
    Form for registering and updating dependent and family member profiles.
    """
    class Meta:
        model = FamilyMember
        fields = [
            'first_name', 'last_name', 'relationship', 'date_of_birth',
            'gender', 'blood_group', 'avatar', 'emergency_contact', 'notes'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'relationship': forms.Select(attrs={'class': 'form-select'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'blood_group': forms.Select(attrs={'class': 'form-select'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
            'emergency_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number or contact'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Known conditions, allergies, or notes'}),
        }

    def clean_date_of_birth(self):
        dob = self.cleaned_data.get('date_of_birth')
        if dob and dob > timezone.now().date():
            raise ValidationError("Date of birth cannot be in the future.")
        return dob

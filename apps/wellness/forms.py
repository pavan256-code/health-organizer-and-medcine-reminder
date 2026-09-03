"""
Forms for Wellness: Meals, Hydration, Fitness, Sleep, and Health Goals.
"""

from django import forms
from apps.wellness.models import MealRecord, ActivityRecord, SleepRecord, HealthGoal
from apps.family.models import FamilyMember


class MealRecordForm(forms.ModelForm):
    class Meta:
        model = MealRecord
        fields = ['family_member', 'date', 'meal_type', 'food_items', 'calories', 'water_intake_ml', 'notes']
        widgets = {
            'family_member': forms.Select(attrs={'class': 'form-select'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'meal_type': forms.Select(attrs={'class': 'form-select'}),
            'food_items': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'e.g. Greek yogurt with almonds, apple slices'}),
            'calories': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'kcal'}),
            'water_intake_ml': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ml'}),
            'notes': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['family_member'].queryset = FamilyMember.objects.filter(user=user, is_active=True)


class ActivityRecordForm(forms.ModelForm):
    class Meta:
        model = ActivityRecord
        fields = ['family_member', 'date', 'activity_type', 'duration_minutes', 'distance_km', 'calories_burned', 'steps_count', 'notes']
        widgets = {
            'family_member': forms.Select(attrs={'class': 'form-select'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'activity_type': forms.Select(attrs={'class': 'form-select'}),
            'duration_minutes': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'distance_km': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'calories_burned': forms.NumberInput(attrs={'class': 'form-control'}),
            'steps_count': forms.NumberInput(attrs={'class': 'form-control'}),
            'notes': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['family_member'].queryset = FamilyMember.objects.filter(user=user, is_active=True)


class SleepRecordForm(forms.ModelForm):
    class Meta:
        model = SleepRecord
        fields = ['family_member', 'date', 'bedtime', 'wake_time', 'duration_hours', 'sleep_quality', 'interruptions_count', 'notes']
        widgets = {
            'family_member': forms.Select(attrs={'class': 'form-select'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'bedtime': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'wake_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'duration_hours': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'sleep_quality': forms.Select(attrs={'class': 'form-select'}),
            'interruptions_count': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'notes': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['family_member'].queryset = FamilyMember.objects.filter(user=user, is_active=True)


class HealthGoalForm(forms.ModelForm):
    class Meta:
        model = HealthGoal
        fields = ['family_member', 'title', 'goal_type', 'target_value', 'current_value', 'unit', 'start_date', 'target_date', 'status', 'notes']
        widgets = {
            'family_member': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Walk 10,000 Steps Daily'}),
            'goal_type': forms.Select(attrs={'class': 'form-select'}),
            'target_value': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'current_value': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'unit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. steps, kg, ml'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'target_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['family_member'].queryset = FamilyMember.objects.filter(user=user, is_active=True)

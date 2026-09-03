"""
Lifestyle & Wellness models: Diet & Meals, Hydration, Activity & Fitness, Sleep, and Health Goals.
"""

from django.db import models
from django.conf import settings
from django.utils import timezone
from apps.core.models import TimeStampedModel
from apps.family.models import FamilyMember


class MealRecord(TimeStampedModel):
    """
    Daily meal tracking: Breakfast, Lunch, Dinner, and Snacks with calorie counts.
    """
    MEAL_BREAKFAST = 'BREAKFAST'
    MEAL_LUNCH = 'LUNCH'
    MEAL_DINNER = 'DINNER'
    MEAL_SNACK = 'SNACK'

    MEAL_CHOICES = [
        (MEAL_BREAKFAST, 'Breakfast'),
        (MEAL_LUNCH, 'Lunch'),
        (MEAL_DINNER, 'Dinner'),
        (MEAL_SNACK, 'Healthy Snack'),
    ]

    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE, related_name='meals')
    date = models.DateField(default=timezone.now, db_index=True)
    meal_type = models.CharField(max_length=20, choices=MEAL_CHOICES, default=MEAL_BREAKFAST)
    food_items = models.TextField(help_text="Items consumed, e.g. Oatmeal with blueberries, boiled egg")
    calories = models.PositiveIntegerField(null=True, blank=True, help_text="Estimated calories (kcal)")
    water_intake_ml = models.PositiveIntegerField(default=0, help_text="Water consumed with meal (ml)")
    notes = models.TextField(blank=True, default='')

    class Meta:
        verbose_name = 'Meal Record'
        verbose_name_plural = 'Meal Records'
        ordering = ['-date', 'meal_type']

    def __str__(self):
        return f"{self.get_meal_type_display()} on {self.date} - {self.family_member.full_name}"


class ActivityRecord(TimeStampedModel):
    """
    Exercise and physical fitness logs: walking, running, swimming, strength, cycling.
    """
    TYPE_WALKING = 'WALKING'
    TYPE_RUNNING = 'RUNNING'
    TYPE_CYCLING = 'CYCLING'
    TYPE_SWIMMING = 'SWIMMING'
    TYPE_STRENGTH = 'STRENGTH'
    TYPE_YOGA = 'YOGA'
    TYPE_OTHER = 'OTHER'

    ACTIVITY_CHOICES = [
        (TYPE_WALKING, 'Walking / Casual Stroll'),
        (TYPE_RUNNING, 'Running / Jogging'),
        (TYPE_CYCLING, 'Cycling / Biking'),
        (TYPE_SWIMMING, 'Swimming'),
        (TYPE_STRENGTH, 'Resistance / Strength Training'),
        (TYPE_YOGA, 'Yoga / Stretching'),
        (TYPE_OTHER, 'Other Physical Exercise'),
    ]

    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE, related_name='activities')
    date = models.DateField(default=timezone.now, db_index=True)
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_CHOICES, default=TYPE_WALKING)
    duration_minutes = models.PositiveIntegerField(default=30, help_text="Duration in minutes")
    distance_km = models.FloatField(null=True, blank=True, help_text="Distance in kilometers")
    calories_burned = models.PositiveIntegerField(null=True, blank=True, help_text="Estimated calories burned")
    steps_count = models.PositiveIntegerField(null=True, blank=True, help_text="Pedometer steps")
    notes = models.TextField(blank=True, default='')

    class Meta:
        verbose_name = 'Activity Record'
        verbose_name_plural = 'Activity Records'
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f"{self.get_activity_type_display()} ({self.duration_minutes}m) - {self.family_member.full_name}"


class SleepRecord(TimeStampedModel):
    """
    Nightly sleep tracking: bedtime, wake time, duration, and sleep quality.
    """
    QUALITY_POOR = 'POOR'
    QUALITY_FAIR = 'FAIR'
    QUALITY_GOOD = 'GOOD'
    QUALITY_EXCELLENT = 'EXCELLENT'

    QUALITY_CHOICES = [
        (QUALITY_POOR, 'Poor (Restless / Fragmented)'),
        (QUALITY_FAIR, 'Fair (Moderate rest)'),
        (QUALITY_GOOD, 'Good (Restful sleep)'),
        (QUALITY_EXCELLENT, 'Excellent (Deep, refreshing sleep)'),
    ]

    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE, related_name='sleep_records')
    date = models.DateField(default=timezone.now, db_index=True)
    bedtime = models.TimeField(help_text="Time went to bed, e.g. 23:00")
    wake_time = models.TimeField(help_text="Time woke up, e.g. 07:00")
    duration_hours = models.FloatField(default=8.0, help_text="Total sleep hours")
    sleep_quality = models.CharField(max_length=20, choices=QUALITY_CHOICES, default=QUALITY_GOOD)
    interruptions_count = models.PositiveIntegerField(default=0, help_text="Times woken up during night")
    notes = models.TextField(blank=True, default='')

    class Meta:
        verbose_name = 'Sleep Record'
        verbose_name_plural = 'Sleep Records'
        ordering = ['-date']

    def __str__(self):
        return f"Sleep on {self.date}: {self.duration_hours}h ({self.sleep_quality}) - {self.family_member.full_name}"


class HealthGoal(TimeStampedModel):
    """
    Personal target goals: weight, daily steps, water intake, sleep, adherence.
    """
    TYPE_WEIGHT = 'WEIGHT'
    TYPE_STEPS = 'STEPS'
    TYPE_WATER = 'WATER'
    TYPE_SLEEP = 'SLEEP'
    TYPE_ADHERENCE = 'ADHERENCE'
    TYPE_CUSTOM = 'CUSTOM'

    GOAL_CHOICES = [
        (TYPE_WEIGHT, 'Target Body Weight (kg)'),
        (TYPE_STEPS, 'Daily Step Count'),
        (TYPE_WATER, 'Daily Hydration Target (ml)'),
        (TYPE_SLEEP, 'Daily Sleep Target (hours)'),
        (TYPE_ADHERENCE, 'Medicine Adherence Target (%)'),
        (TYPE_CUSTOM, 'Custom Wellness Goal'),
    ]

    STATUS_ACTIVE = 'ACTIVE'
    STATUS_COMPLETED = 'COMPLETED'
    STATUS_PAUSED = 'PAUSED'
    STATUS_FAILED = 'FAILED'

    STATUS_CHOICES = [
        (STATUS_ACTIVE, 'Active In Progress'),
        (STATUS_COMPLETED, 'Goal Achieved'),
        (STATUS_PAUSED, 'Paused'),
        (STATUS_FAILED, 'Discontinued / Failed'),
    ]

    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE, related_name='goals')
    title = models.CharField(max_length=150)
    goal_type = models.CharField(max_length=20, choices=GOAL_CHOICES, default=TYPE_STEPS)
    target_value = models.FloatField(help_text="Target numerical threshold")
    current_value = models.FloatField(default=0.0, help_text="Current progress value")
    unit = models.CharField(max_length=30, default='steps', help_text="e.g. kg, steps, ml, hours, %")
    start_date = models.DateField(default=timezone.now)
    target_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_ACTIVE, db_index=True)
    notes = models.TextField(blank=True, default='')

    class Meta:
        verbose_name = 'Health Goal'
        verbose_name_plural = 'Health Goals'
        ordering = ['status', '-created_at']

    def __str__(self):
        return f"{self.title}: {self.current_value}/{self.target_value} {self.unit} ({self.status})"

    @property
    def progress_percentage(self):
        if not self.target_value or self.target_value == 0:
            return 0
        pct = (self.current_value / self.target_value) * 100
        return min(100, max(0, int(pct)))

"""
Admin configurations for Wellness app.
"""

from django.contrib import admin
from apps.wellness.models import MealRecord, ActivityRecord, SleepRecord, HealthGoal


@admin.register(MealRecord)
class MealRecordAdmin(admin.ModelAdmin):
    list_display = ('family_member', 'date', 'meal_type', 'calories', 'water_intake_ml')
    list_filter = ('meal_type', 'date')
    search_fields = ('food_items', 'family_member__first_name')


@admin.register(ActivityRecord)
class ActivityRecordAdmin(admin.ModelAdmin):
    list_display = ('family_member', 'date', 'activity_type', 'duration_minutes', 'calories_burned', 'steps_count')
    list_filter = ('activity_type', 'date')
    search_fields = ('family_member__first_name',)


@admin.register(SleepRecord)
class SleepRecordAdmin(admin.ModelAdmin):
    list_display = ('family_member', 'date', 'duration_hours', 'sleep_quality', 'interruptions_count')
    list_filter = ('sleep_quality', 'date')


@admin.register(HealthGoal)
class HealthGoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'family_member', 'goal_type', 'target_value', 'current_value', 'status')
    list_filter = ('goal_type', 'status')
    search_fields = ('title', 'family_member__first_name')

"""
Wellness module URL patterns.
"""

from django.urls import path
from apps.wellness.views import (
    DietOverviewView, MealCreateView, WaterLogView,
    FitnessListView, FitnessCreateView,
    SleepListView, SleepCreateView,
    GoalListView, GoalCreateView, GoalUpdateProgressView, GoalDeleteView,
)

app_name = 'wellness'

urlpatterns = [
    # Diet & Meals
    path('diet/', DietOverviewView.as_view(), name='diet_overview'),
    path('diet/add/', MealCreateView.as_view(), name='meal_add'),
    path('diet/water/', WaterLogView.as_view(), name='water_log'),

    # Fitness & Activity
    path('fitness/', FitnessListView.as_view(), name='fitness_list'),
    path('fitness/add/', FitnessCreateView.as_view(), name='fitness_add'),

    # Sleep
    path('sleep/', SleepListView.as_view(), name='sleep_list'),
    path('sleep/add/', SleepCreateView.as_view(), name='sleep_add'),

    # Health Goals
    path('goals/', GoalListView.as_view(), name='goal_list'),
    path('goals/add/', GoalCreateView.as_view(), name='goal_add'),
    path('goals/<int:pk>/progress/', GoalUpdateProgressView.as_view(), name='goal_update_progress'),
    path('goals/<int:pk>/delete/', GoalDeleteView.as_view(), name='goal_delete'),
]

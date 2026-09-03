"""
Emergency module URL patterns.
"""

from django.urls import path
from apps.emergency.views import EmergencyCardView, InteractionCheckerView

app_name = 'emergency'

urlpatterns = [
    path('card/', EmergencyCardView.as_view(), name='emergency_card'),
    path('interactions/', InteractionCheckerView.as_view(), name='interaction_checker'),
]

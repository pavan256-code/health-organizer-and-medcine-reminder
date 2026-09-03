"""
Analytics URL patterns.
"""

from django.urls import path
from apps.analytics.views import HealthInsightsView

app_name = 'analytics'

urlpatterns = [
    path('', HealthInsightsView.as_view(), name='insights_dashboard'),
]

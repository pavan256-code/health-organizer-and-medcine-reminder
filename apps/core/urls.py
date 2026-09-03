"""
Core URL configurations for landing pages and public utility endpoints.
"""

from django.urls import path
from apps.core.views import (
    LandingPageView,
    AboutPageView,
    FeaturesPageView,
    ContactPageView,
    health_check_view,
)

app_name = 'core'

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('features/', FeaturesPageView.as_view(), name='features'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('health/', health_check_view, name='health_check'),
]

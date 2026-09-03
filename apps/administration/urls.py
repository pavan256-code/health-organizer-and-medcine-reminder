"""
Administration module URL patterns.
"""

from django.urls import path
from apps.administration.views import AdminDashboardView

app_name = 'administration'

urlpatterns = [
    path('', AdminDashboardView.as_view(), name='admin_dashboard'),
]

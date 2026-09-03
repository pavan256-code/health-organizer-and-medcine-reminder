"""
Calendar URL routes.
"""

from django.urls import path
from apps.calendar_app.views import UnifiedCalendarView

app_name = 'calendar_app'

urlpatterns = [
    path('', UnifiedCalendarView.as_view(), name='unified_calendar'),
]

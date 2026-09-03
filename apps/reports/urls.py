"""
Reports URL patterns.
"""

from django.urls import path
from apps.reports.views import (
    ReportIndexView,
    MedicationSchedulePDFView,
    DoctorVisitSummaryPDFView,
    MedicationLogsCSVView,
    VitalsCSVView
)

app_name = 'reports'

urlpatterns = [
    path('', ReportIndexView.as_view(), name='report_index'),
    path('pdf/schedule/<int:member_id>/', MedicationSchedulePDFView.as_view(), name='pdf_schedule'),
    path('pdf/doctor-brief/<int:member_id>/', DoctorVisitSummaryPDFView.as_view(), name='pdf_doctor_brief'),
    path('export/medications/csv/', MedicationLogsCSVView.as_view(), name='csv_medications'),
    path('export/vitals/csv/', VitalsCSVView.as_view(), name='csv_vitals'),
]

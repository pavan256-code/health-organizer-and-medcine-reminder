"""
URL patterns for Medications module.
"""

from django.urls import path
from apps.medications.views import (
    MedicineListView,
    MedicineDetailView,
    MedicineCreateView,
    MedicineUpdateView,
    MedicineDeleteView,
    ScheduleListView,
    ScheduleCreateView,
    ScheduleUpdateView,
    ScheduleDeleteView,
    DoseTakeView,
    DoseSkipView,
    DoseSnoozeView,
    StockListView,
    StockRefillView,
    ExpiryListView,
    ExpiryCreateView,
    MedicationHistoryView,
    AdherenceDashboardView,
)

app_name = 'medications'

urlpatterns = [
    # Medicines CRUD
    path('', MedicineListView.as_view(), name='medicine_list'),
    path('add/', MedicineCreateView.as_view(), name='medicine_add'),
    path('<int:pk>/', MedicineDetailView.as_view(), name='medicine_detail'),
    path('<int:pk>/edit/', MedicineUpdateView.as_view(), name='medicine_edit'),
    path('<int:pk>/delete/', MedicineDeleteView.as_view(), name='medicine_delete'),

    # Schedules
    path('schedules/', ScheduleListView.as_view(), name='schedule_list'),
    path('schedules/add/<int:medicine_id>/', ScheduleCreateView.as_view(), name='schedule_add'),
    path('schedules/<int:pk>/edit/', ScheduleUpdateView.as_view(), name='schedule_edit'),
    path('schedules/<int:pk>/delete/', ScheduleDeleteView.as_view(), name='schedule_delete'),

    # Dose Actions
    path('doses/<int:pk>/take/', DoseTakeView.as_view(), name='dose_take'),
    path('doses/<int:pk>/skip/', DoseSkipView.as_view(), name='dose_skip'),
    path('doses/<int:pk>/snooze/', DoseSnoozeView.as_view(), name='dose_snooze'),

    # Stock & Refills
    path('stock/', StockListView.as_view(), name='stock_list'),
    path('stock/<int:medicine_id>/refill/', StockRefillView.as_view(), name='stock_refill'),

    # Expiry
    path('expiry/', ExpiryListView.as_view(), name='expiry_list'),
    path('expiry/<int:medicine_id>/add/', ExpiryCreateView.as_view(), name='expiry_add'),

    # History Logs & Adherence
    path('logs/', MedicationHistoryView.as_view(), name='medication_logs'),
    path('adherence/', AdherenceDashboardView.as_view(), name='adherence_dashboard'),
]

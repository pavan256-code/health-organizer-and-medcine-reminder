"""
Medical module URL patterns.
"""

from django.urls import path
from apps.medical.views import (
    DoctorListView, DoctorCreateView, DoctorUpdateView, DoctorDeleteView,
    AppointmentListView, AppointmentCreateView, AppointmentUpdateView,
    AppointmentCancelView, AppointmentCompleteView,
    PrescriptionListView, PrescriptionDetailView, PrescriptionCreateView,
    PrescriptionUpdateView, PrescriptionDeleteView,
    HealthProfileView,
    VitalRecordListView, VitalRecordCreateView, VitalTrendView,
    SymptomListView, SymptomCreateView,
    VaccinationListView, VaccinationCreateView,
    AllergyListView, AllergyCreateView,
    DocumentListView, DocumentUploadView, DocumentDownloadView, DocumentDeleteView,
)

app_name = 'medical'

urlpatterns = [
    # Doctors
    path('doctors/', DoctorListView.as_view(), name='doctor_list'),
    path('doctors/add/', DoctorCreateView.as_view(), name='doctor_add'),
    path('doctors/<int:pk>/edit/', DoctorUpdateView.as_view(), name='doctor_edit'),
    path('doctors/<int:pk>/delete/', DoctorDeleteView.as_view(), name='doctor_delete'),

    # Appointments
    path('appointments/', AppointmentListView.as_view(), name='appointment_list'),
    path('appointments/add/', AppointmentCreateView.as_view(), name='appointment_add'),
    path('appointments/<int:pk>/edit/', AppointmentUpdateView.as_view(), name='appointment_edit'),
    path('appointments/<int:pk>/cancel/', AppointmentCancelView.as_view(), name='appointment_cancel'),
    path('appointments/<int:pk>/complete/', AppointmentCompleteView.as_view(), name='appointment_complete'),

    # Prescriptions
    path('prescriptions/', PrescriptionListView.as_view(), name='prescription_list'),
    path('prescriptions/add/', PrescriptionCreateView.as_view(), name='prescription_add'),
    path('prescriptions/<int:pk>/', PrescriptionDetailView.as_view(), name='prescription_detail'),
    path('prescriptions/<int:pk>/edit/', PrescriptionUpdateView.as_view(), name='prescription_edit'),
    path('prescriptions/<int:pk>/delete/', PrescriptionDeleteView.as_view(), name='prescription_delete'),

    # Health Profile & Vitals
    path('profile/', HealthProfileView.as_view(), name='health_profile'),
    path('vitals/', VitalRecordListView.as_view(), name='vital_list'),
    path('vitals/add/', VitalRecordCreateView.as_view(), name='vital_add'),
    path('vitals/trends/', VitalTrendView.as_view(), name='vital_trends'),

    # Symptoms
    path('symptoms/', SymptomListView.as_view(), name='symptom_list'),
    path('symptoms/add/', SymptomCreateView.as_view(), name='symptom_add'),

    # Vaccinations
    path('vaccinations/', VaccinationListView.as_view(), name='vaccination_list'),
    path('vaccinations/add/', VaccinationCreateView.as_view(), name='vaccination_add'),

    # Allergies
    path('allergies/', AllergyListView.as_view(), name='allergy_list'),
    path('allergies/add/', AllergyCreateView.as_view(), name='allergy_add'),

    # Document Vault
    path('documents/', DocumentListView.as_view(), name='document_list'),
    path('documents/upload/', DocumentUploadView.as_view(), name='document_upload'),
    path('documents/<int:pk>/download/', DocumentDownloadView.as_view(), name='document_download'),
    path('documents/<int:pk>/delete/', DocumentDeleteView.as_view(), name='document_delete'),
]

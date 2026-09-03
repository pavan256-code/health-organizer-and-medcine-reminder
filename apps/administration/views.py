"""
System Administration console and telemetry dashboard.
"""

import os
from django.conf import settings
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model

from apps.family.models import FamilyMember
from apps.medications.models import Medicine, MedicineDose, MedicationLog
from apps.medical.models import Appointment, VitalRecord, MedicalDocument
from apps.audit.models import AuditLog
from apps.accounts.models import UserSession

User = get_user_model()


class AdminDashboardView(LoginRequiredMixin, TemplateView):
    """
    Administrative overview showing system telemetry, active sessions, and database metrics.
    """
    template_name = 'administration/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 1. High level counts
        context['user_count'] = User.objects.count()
        context['family_member_count'] = FamilyMember.objects.count()
        context['medicine_count'] = Medicine.objects.count()
        context['dose_logs_count'] = MedicationLog.objects.count()
        context['appointment_count'] = Appointment.objects.count()
        context['vitals_count'] = VitalRecord.objects.count()
        context['documents_count'] = MedicalDocument.objects.count()
        context['audit_logs_count'] = AuditLog.objects.count()

        # 2. Database size
        db_path = settings.DATABASES['default']['NAME']
        db_size_mb = 0
        if os.path.exists(db_path):
            db_size_mb = round(os.path.getsize(db_path) / (1024 * 1024), 2)
        context['db_size_mb'] = db_size_mb

        # 3. Active sessions
        context['active_sessions'] = UserSession.objects.filter(is_active=True).select_related('user').order_by('-last_activity')[:10]

        # 4. Recent audit logs
        context['recent_audits'] = AuditLog.objects.select_related('user').order_by('-created_at')[:10]

        return context

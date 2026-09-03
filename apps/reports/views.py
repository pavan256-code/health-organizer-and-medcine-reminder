"""
Views for Report generation: PDF documents and CSV exports.
"""

from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

from apps.family.models import FamilyMember
from apps.reports.services.pdf_service import PDFReportService
from apps.reports.services.csv_service import CSVReportService


class ReportIndexView(LoginRequiredMixin, TemplateView):
    template_name = 'reports/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members'] = FamilyMember.objects.filter(user=self.request.user, is_active=True)
        return context


class MedicationSchedulePDFView(LoginRequiredMixin, View):
    def get(self, request, member_id):
        member = get_object_or_404(FamilyMember, id=member_id, user=request.user)
        pdf_content = PDFReportService.generate_medication_schedule_pdf(request.user, member)
        response = HttpResponse(pdf_content, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="Medication_Schedule_{member.first_name}.pdf"'
        return response


class DoctorVisitSummaryPDFView(LoginRequiredMixin, View):
    def get(self, request, member_id):
        member = get_object_or_404(FamilyMember, id=member_id, user=request.user)
        pdf_content = PDFReportService.generate_doctor_visit_summary_pdf(request.user, member)
        response = HttpResponse(pdf_content, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="Doctor_Visit_Summary_{member.first_name}.pdf"'
        return response


class MedicationLogsCSVView(LoginRequiredMixin, View):
    def get(self, request):
        member = getattr(request, 'active_family_member', None)
        csv_data = CSVReportService.export_medication_logs_csv(request.user, family_member=member)
        response = HttpResponse(csv_data, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="medication_logs.csv"'
        return response


class VitalsCSVView(LoginRequiredMixin, View):
    def get(self, request):
        member = getattr(request, 'active_family_member', None)
        csv_data = CSVReportService.export_vitals_csv(request.user, family_member=member)
        response = HttpResponse(csv_data, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="vitals_records.csv"'
        return response

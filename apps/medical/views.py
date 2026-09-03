"""
Views for Medical Management: Doctors, Appointments, Prescriptions, Vitals, Symptoms, Vaccines, Allergies, Documents.
"""

import os
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, View, TemplateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import FileResponse, Http404
from django.utils import timezone
from django.db.models import Q

from apps.medical.models import (
    Doctor, Appointment, Prescription, HealthProfile,
    VitalRecord, SymptomRecord, Vaccination, Allergy, MedicalDocument
)
from apps.medical.forms import (
    DoctorForm, AppointmentForm, PrescriptionForm, HealthProfileForm,
    VitalRecordForm, SymptomRecordForm, VaccinationForm, AllergyForm, MedicalDocumentForm
)
from apps.family.models import FamilyMember
from apps.audit.services import log_audit_event


# -------------------------------------------------------------
# 1. Doctor Management
# -------------------------------------------------------------
class DoctorListView(LoginRequiredMixin, ListView):
    model = Doctor
    template_name = 'medical/doctor_list.html'
    context_object_name = 'doctors'

    def get_queryset(self):
        qs = Doctor.objects.filter(user=self.request.user)
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(
                Q(full_name__icontains=q) |
                Q(specialization__icontains=q) |
                Q(hospital_clinic__icontains=q)
            )
        return qs.order_by('full_name')


class DoctorCreateView(LoginRequiredMixin, CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'medical/doctor_form.html'
    success_url = reverse_lazy('medical:doctor_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        doc = form.save()
        messages.success(self.request, f"Physician '{doc.full_name}' added to care network.")
        return super().form_valid(form)


class DoctorUpdateView(LoginRequiredMixin, UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'medical/doctor_form.html'
    success_url = reverse_lazy('medical:doctor_list')

    def get_queryset(self):
        return Doctor.objects.filter(user=self.request.user)


class DoctorDeleteView(LoginRequiredMixin, DeleteView):
    model = Doctor
    template_name = 'medical/doctor_confirm_delete.html'
    success_url = reverse_lazy('medical:doctor_list')

    def get_queryset(self):
        return Doctor.objects.filter(user=self.request.user)


# -------------------------------------------------------------
# 2. Appointment Management
# -------------------------------------------------------------
class AppointmentListView(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = 'medical/appointment_list.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        qs = Appointment.objects.filter(user=self.request.user)
        active_member = getattr(self.request, 'active_family_member', None)
        if active_member:
            qs = qs.filter(family_member=active_member)
        status = self.request.GET.get('status')
        if status:
            qs = qs.filter(status=status)
        return qs.select_related('doctor', 'family_member').order_by('date', 'time')


class AppointmentCreateView(LoginRequiredMixin, CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'medical/appointment_form.html'
    success_url = reverse_lazy('medical:appointment_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        appt = form.save()
        messages.success(self.request, f"Appointment booked with {appt.doctor.full_name} on {appt.date}.")
        return super().form_valid(form)


class AppointmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'medical/appointment_form.html'
    success_url = reverse_lazy('medical:appointment_list')

    def get_queryset(self):
        return Appointment.objects.filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class AppointmentCancelView(LoginRequiredMixin, View):
    def post(self, request, pk):
        appt = get_object_or_404(Appointment, id=pk, user=request.user)
        appt.status = Appointment.STATUS_CANCELLED
        appt.save(update_fields=['status'])
        messages.info(request, f"Appointment on {appt.date} marked as cancelled.")
        return redirect('medical:appointment_list')


class AppointmentCompleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        appt = get_object_or_404(Appointment, id=pk, user=request.user)
        appt.status = Appointment.STATUS_COMPLETED
        appt.save(update_fields=['status'])
        messages.success(request, f"Appointment on {appt.date} marked as completed.")
        return redirect('medical:appointment_list')


# -------------------------------------------------------------
# 3. Prescription Management
# -------------------------------------------------------------
class PrescriptionListView(LoginRequiredMixin, ListView):
    model = Prescription
    template_name = 'medical/prescription_list.html'
    context_object_name = 'prescriptions'

    def get_queryset(self):
        qs = Prescription.objects.filter(user=self.request.user)
        active_member = getattr(self.request, 'active_family_member', None)
        if active_member:
            qs = qs.filter(family_member=active_member)
        return qs.select_related('doctor', 'family_member').order_by('-prescription_date')


class PrescriptionDetailView(LoginRequiredMixin, DetailView):
    model = Prescription
    template_name = 'medical/prescription_detail.html'
    context_object_name = 'prescription'

    def get_queryset(self):
        return Prescription.objects.filter(user=self.request.user)


class PrescriptionCreateView(LoginRequiredMixin, CreateView):
    model = Prescription
    form_class = PrescriptionForm
    template_name = 'medical/prescription_form.html'
    success_url = reverse_lazy('medical:prescription_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        messages.success(self.request, "Prescription saved successfully.")
        return super().form_valid(form)


class PrescriptionUpdateView(LoginRequiredMixin, UpdateView):
    model = Prescription
    form_class = PrescriptionForm
    template_name = 'medical/prescription_form.html'
    success_url = reverse_lazy('medical:prescription_list')

    def get_queryset(self):
        return Prescription.objects.filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class PrescriptionDeleteView(LoginRequiredMixin, DeleteView):
    model = Prescription
    template_name = 'medical/prescription_confirm_delete.html'
    success_url = reverse_lazy('medical:prescription_list')

    def get_queryset(self):
        return Prescription.objects.filter(user=self.request.user)


# -------------------------------------------------------------
# 4. Health Profile & Vitals
# -------------------------------------------------------------
class HealthProfileView(LoginRequiredMixin, View):
    template_name = 'medical/health_profile.html'

    def get(self, request):
        member = getattr(request, 'active_family_member', None)
        if not member:
            member = FamilyMember.objects.filter(user=request.user, relationship='SELF').first()
            if not member:
                member = FamilyMember.objects.filter(user=request.user).first()

        profile, _ = HealthProfile.objects.get_or_create(family_member=member)
        form = HealthProfileForm(instance=profile)
        return render(request, self.template_name, {'form': form, 'profile': profile, 'member': member})

    def post(self, request):
        member = getattr(request, 'active_family_member', None)
        profile, _ = HealthProfile.objects.get_or_create(family_member=member)
        form = HealthProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, f"Health profile for {member.full_name} updated.")
            return redirect('medical:health_profile')
        return render(request, self.template_name, {'form': form, 'profile': profile, 'member': member})


class VitalRecordListView(LoginRequiredMixin, ListView):
    model = VitalRecord
    template_name = 'medical/vital_list.html'
    context_object_name = 'vitals'
    paginate_by = 25

    def get_queryset(self):
        qs = VitalRecord.objects.filter(family_member__user=self.request.user)
        active_member = getattr(self.request, 'active_family_member', None)
        if active_member:
            qs = qs.filter(family_member=active_member)
        return qs.select_related('family_member').order_by('-date', '-time')


class VitalRecordCreateView(LoginRequiredMixin, CreateView):
    model = VitalRecord
    form_class = VitalRecordForm
    template_name = 'medical/vital_form.html'
    success_url = reverse_lazy('medical:vital_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Vital signs recorded successfully.")
        return super().form_valid(form)


class VitalTrendView(LoginRequiredMixin, TemplateView):
    template_name = 'medical/vital_trends.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        member = getattr(self.request, 'active_family_member', None)

        qs = VitalRecord.objects.filter(family_member__user=user)
        if member:
            qs = qs.filter(family_member=member)

        recent = qs.order_by('-date', '-time')[:15]
        # Reverse to chronological for graphing
        chronological = list(reversed(recent))

        context['dates'] = [v.date.strftime('%b %d') for v in chronological]
        context['systolic'] = [v.blood_pressure_systolic or 0 for v in chronological]
        context['diastolic'] = [v.blood_pressure_diastolic or 0 for v in chronological]
        context['glucose'] = [v.blood_sugar_fasting or 0 for v in chronological]
        context['weights'] = [v.weight_kg or 0 for v in chronological]
        context['vitals_count'] = len(chronological)
        return context


# -------------------------------------------------------------
# 5. Symptom Journal
# -------------------------------------------------------------
class SymptomListView(LoginRequiredMixin, ListView):
    model = SymptomRecord
    template_name = 'medical/symptom_list.html'
    context_object_name = 'symptoms'

    def get_queryset(self):
        qs = SymptomRecord.objects.filter(family_member__user=self.request.user)
        active_member = getattr(self.request, 'active_family_member', None)
        if active_member:
            qs = qs.filter(family_member=active_member)
        return qs.select_related('family_member').order_by('-date', '-time')


class SymptomCreateView(LoginRequiredMixin, CreateView):
    model = SymptomRecord
    form_class = SymptomRecordForm
    template_name = 'medical/symptom_form.html'
    success_url = reverse_lazy('medical:symptom_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Symptom journal entry logged.")
        return super().form_valid(form)


# -------------------------------------------------------------
# 6. Vaccination Management
# -------------------------------------------------------------
class VaccinationListView(LoginRequiredMixin, ListView):
    model = Vaccination
    template_name = 'medical/vaccination_list.html'
    context_object_name = 'vaccinations'

    def get_queryset(self):
        qs = Vaccination.objects.filter(family_member__user=self.request.user)
        active_member = getattr(self.request, 'active_family_member', None)
        if active_member:
            qs = qs.filter(family_member=active_member)
        return qs.select_related('family_member').order_by('-vaccination_date')


class VaccinationCreateView(LoginRequiredMixin, CreateView):
    model = Vaccination
    form_class = VaccinationForm
    template_name = 'medical/vaccination_form.html'
    success_url = reverse_lazy('medical:vaccination_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Vaccination record added.")
        return super().form_valid(form)


# -------------------------------------------------------------
# 7. Allergy Management
# -------------------------------------------------------------
class AllergyListView(LoginRequiredMixin, ListView):
    model = Allergy
    template_name = 'medical/allergy_list.html'
    context_object_name = 'allergies'

    def get_queryset(self):
        qs = Allergy.objects.filter(family_member__user=self.request.user)
        active_member = getattr(self.request, 'active_family_member', None)
        if active_member:
            qs = qs.filter(family_member=active_member)
        return qs.select_related('family_member').order_by('-severity', 'allergen')


class AllergyCreateView(LoginRequiredMixin, CreateView):
    model = Allergy
    form_class = AllergyForm
    template_name = 'medical/allergy_form.html'
    success_url = reverse_lazy('medical:allergy_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Allergy profile logged.")
        return super().form_valid(form)


# -------------------------------------------------------------
# 8. Medical Document Vault
# -------------------------------------------------------------
class DocumentListView(LoginRequiredMixin, ListView):
    model = MedicalDocument
    template_name = 'medical/document_list.html'
    context_object_name = 'documents'

    def get_queryset(self):
        qs = MedicalDocument.objects.filter(family_member__user=self.request.user)
        active_member = getattr(self.request, 'active_family_member', None)
        if active_member:
            qs = qs.filter(family_member=active_member)
        cat = self.request.GET.get('category')
        if cat:
            qs = qs.filter(category=cat)
        return qs.select_related('family_member').order_by('-document_date')


class DocumentUploadView(LoginRequiredMixin, CreateView):
    model = MedicalDocument
    form_class = MedicalDocumentForm
    template_name = 'medical/document_form.html'
    success_url = reverse_lazy('medical:document_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        doc = form.save()
        log_audit_event(
            user=self.request.user,
            action='CREATE',
            module='MEDICAL',
            description=f"Uploaded medical document: {doc.title} ({doc.get_category_display()})",
            object_repr=doc.title,
            request=self.request
        )
        messages.success(self.request, f"Document '{doc.title}' stored securely in local vault.")
        return super().form_valid(form)


class DocumentDownloadView(LoginRequiredMixin, View):
    """
    Controlled streaming endpoint for protected medical documents.
    Verifies user ownership before sending file binary stream.
    """
    def get(self, request, pk):
        doc = get_object_or_404(MedicalDocument, id=pk, family_member__user=request.user)
        if not doc.file or not os.path.exists(doc.file.path):
            raise Http404("Document file not found on local disk.")

        log_audit_event(
            user=request.user,
            action='VIEW',
            module='MEDICAL',
            description=f"Downloaded protected document: {doc.title}",
            object_repr=doc.title,
            request=request
        )

        response = FileResponse(open(doc.file.path, 'rb'), as_attachment=True, filename=os.path.basename(doc.file.name))
        return response


class DocumentDeleteView(LoginRequiredMixin, DeleteView):
    model = MedicalDocument
    template_name = 'medical/document_confirm_delete.html'
    success_url = reverse_lazy('medical:document_list')

    def get_queryset(self):
        return MedicalDocument.objects.filter(family_member__user=self.request.user)

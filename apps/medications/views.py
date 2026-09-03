"""
Views for Medication Management: Medicines, Schedules, Doses, Refills, Expiries, and Adherence.
"""

from datetime import datetime, time
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, View, FormView, TemplateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q

from apps.medications.models import (
    Medicine, MedicineSchedule, MedicineDose, MedicationLog,
    MedicineStock, MedicineRefill, MedicineExpiry
)
from apps.medications.forms import (
    MedicineForm, MedicineScheduleForm, DoseSkipForm,
    MedicineRefillForm, MedicineExpiryForm
)
from apps.medications.services.scheduler_service import MedicationSchedulerService
from apps.medications.services.adherence_service import MedicationAdherenceService
from apps.medications.services.stock_service import MedicationStockService
from apps.medications.services.expiry_service import MedicationExpiryService
from apps.audit.services import log_audit_event


class MedicineListView(LoginRequiredMixin, ListView):
    """
    Lists all medicines with multi-field search and category filtering.
    """
    model = Medicine
    template_name = 'medications/medicine_list.html'
    context_object_name = 'medicines'
    paginate_by = 15

    def get_queryset(self):
        qs = Medicine.objects.filter(user=self.request.user)

        # Scoped to active family member if present
        active_member = getattr(self.request, 'active_family_member', None)
        if active_member:
            qs = qs.filter(family_member=active_member)

        # Search
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(
                Q(name__icontains=q) |
                Q(generic_name__icontains=q) |
                Q(brand_name__icontains=q) |
                Q(prescribed_by__icontains=q)
            )

        # Filters
        med_type = self.request.GET.get('type')
        status = self.request.GET.get('status')
        if med_type:
            qs = qs.filter(medicine_type=med_type)
        if status:
            qs = qs.filter(status=status)

        return qs.select_related('family_member', 'stock').order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type_choices'] = Medicine.TYPE_CHOICES
        context['status_choices'] = Medicine.STATUS_CHOICES
        context['search_query'] = self.request.GET.get('q', '')
        context['selected_type'] = self.request.GET.get('type', '')
        context['selected_status'] = self.request.GET.get('status', '')
        return context


class MedicineDetailView(LoginRequiredMixin, DetailView):
    """
    Comprehensive clinical dossier for a medicine.
    """
    model = Medicine
    template_name = 'medications/medicine_detail.html'
    context_object_name = 'medicine'

    def get_queryset(self):
        return Medicine.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        med = self.object
        context['schedules'] = med.schedules.filter(is_active=True)
        context['recent_logs'] = med.logs.select_related('family_member').order_by('-actual_time')[:10]
        context['refills'] = med.refills.order_by('-refill_date')[:5]
        context['expiry_batches'] = med.expiry_batches.order_by('expiry_date')
        return context


class MedicineCreateView(LoginRequiredMixin, CreateView):
    """
    Adds a new prescription or OTC medication.
    """
    model = Medicine
    form_class = MedicineForm
    template_name = 'medications/medicine_form.html'
    success_url = reverse_lazy('medications:medicine_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        medicine = form.save()

        # Generate rolling doses immediately
        MedicationSchedulerService.generate_doses_for_window(days_ahead=7, user=self.request.user)

        log_audit_event(
            user=self.request.user,
            action='CREATE',
            module='MEDICATION',
            description=f"Added medicine '{medicine.name}' for {medicine.family_member.full_name}",
            object_repr=medicine.name,
            object_id=medicine.id,
            request=self.request
        )

        messages.success(self.request, f"Medicine '{medicine.name}' was registered successfully.")
        return redirect('medications:medicine_detail', pk=medicine.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Add New Medication"
        context['submit_btn_text'] = "Save & Continue"
        return context


class MedicineUpdateView(LoginRequiredMixin, UpdateView):
    """
    Updates medicine formulation, dosage, instructions, or status.
    """
    model = Medicine
    form_class = MedicineForm
    template_name = 'medications/medicine_form.html'

    def get_queryset(self):
        return Medicine.objects.filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        medicine = form.save()

        log_audit_event(
            user=self.request.user,
            action='UPDATE',
            module='MEDICATION',
            description=f"Updated medication '{medicine.name}'",
            object_repr=medicine.name,
            object_id=medicine.id,
            request=self.request
        )

        messages.success(self.request, f"Updated details for '{medicine.name}'.")
        return redirect('medications:medicine_detail', pk=medicine.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f"Edit {self.object.name}"
        context['submit_btn_text'] = "Update Medicine"
        return context


class MedicineDeleteView(LoginRequiredMixin, DeleteView):
    """
    Discontinues a medication without erasing historical dose tracking records.
    """
    model = Medicine
    template_name = 'medications/medicine_confirm_delete.html'
    success_url = reverse_lazy('medications:medicine_list')

    def get_queryset(self):
        return Medicine.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        med = self.get_object()
        med.status = Medicine.STATUS_DISCONTINUED
        med.save(update_fields=['status'])

        log_audit_event(
            user=request.user,
            action='DELETE',
            module='MEDICATION',
            description=f"Discontinued medication '{med.name}'",
            object_repr=med.name,
            object_id=med.id,
            request=request
        )

        messages.success(request, f"Medication '{med.name}' has been marked as discontinued.")
        return redirect(self.success_url)


class ScheduleListView(LoginRequiredMixin, ListView):
    """
    Lists all active and configured dosing routines.
    """
    model = MedicineSchedule
    template_name = 'medications/schedule_list.html'
    context_object_name = 'schedules'

    def get_queryset(self):
        qs = MedicineSchedule.objects.filter(medicine__user=self.request.user)
        active_member = getattr(self.request, 'active_family_member', None)
        if active_member:
            qs = qs.filter(medicine__family_member=active_member)
        return qs.select_related('medicine', 'medicine__family_member').order_by('-is_active', 'medicine__name')


class ScheduleCreateView(LoginRequiredMixin, CreateView):
    """
    Configures a new schedule pattern for a specific medicine.
    """
    model = MedicineSchedule
    form_class = MedicineScheduleForm
    template_name = 'medications/schedule_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.medicine = get_object_or_404(Medicine, pk=self.kwargs.get('medicine_id'), user=request.user)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        schedule = form.save(medicine=self.medicine)

        # Re-generate doses
        MedicationSchedulerService.generate_doses_for_window(days_ahead=7, user=self.request.user)

        log_audit_event(
            user=self.request.user,
            action='CREATE',
            module='MEDICATION',
            description=f"Created dosing schedule for '{self.medicine.name}'",
            object_repr=self.medicine.name,
            object_id=schedule.id,
            request=self.request
        )

        messages.success(self.request, f"Dosing schedule saved for {self.medicine.name}.")
        return redirect('medications:medicine_detail', pk=self.medicine.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['medicine'] = self.medicine
        context['page_title'] = f"Add Dosing Schedule for {self.medicine.name}"
        return context


class ScheduleUpdateView(LoginRequiredMixin, UpdateView):
    """
    Updates an existing schedule.
    """
    model = MedicineSchedule
    form_class = MedicineScheduleForm
    template_name = 'medications/schedule_form.html'

    def get_queryset(self):
        return MedicineSchedule.objects.filter(medicine__user=self.request.user)

    def form_valid(self, form):
        schedule = form.save()
        MedicationSchedulerService.generate_doses_for_window(days_ahead=7, user=self.request.user)
        messages.success(self.request, "Dosing schedule updated.")
        return redirect('medications:medicine_detail', pk=schedule.medicine.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['medicine'] = self.object.medicine
        context['page_title'] = f"Edit Schedule for {self.object.medicine.name}"
        return context


class ScheduleDeleteView(LoginRequiredMixin, DeleteView):
    """
    Deactivates a dosing schedule.
    """
    model = MedicineSchedule
    template_name = 'medications/schedule_confirm_delete.html'

    def get_queryset(self):
        return MedicineSchedule.objects.filter(medicine__user=self.request.user)

    def get_success_url(self):
        return reverse('medications:medicine_detail', kwargs={'pk': self.object.medicine.id})

    def delete(self, request, *args, **kwargs):
        sched = self.get_object()
        sched.is_active = False
        sched.save(update_fields=['is_active'])
        messages.success(request, "Schedule has been deactivated.")
        return redirect(self.get_success_url())


# Dose Actions
class DoseTakeView(LoginRequiredMixin, View):
    """
    Marks a scheduled dose as taken:
    1. Updates dose status and actual_time
    2. Decrements medicine stock
    3. Records MedicationLog entry
    4. Records AuditLog
    """
    def post(self, request, pk):
        dose = get_object_or_404(MedicineDose, id=pk, schedule__medicine__user=request.user)
        now = timezone.now()
        dose.mark_as_taken(now)

        # Decrement stock
        med = dose.schedule.medicine
        if hasattr(med, 'stock'):
            med.stock.decrement(1)

        # Audit log & Medication log
        MedicationLog.objects.create(
            medicine=med,
            family_member=med.family_member,
            dose=dose,
            scheduled_time=timezone.make_aware(datetime.combine(dose.date, dose.scheduled_time)),
            actual_time=now,
            status=MedicineDose.STATUS_TAKEN,
            logged_by=request.user
        )

        log_audit_event(
            user=request.user,
            action='UPDATE',
            module='MEDICATION',
            description=f"Recorded dose TAKEN: {med.name} for {med.family_member.full_name}",
            object_repr=med.name,
            request=request
        )

        messages.success(request, f"✓ Recorded dose for {med.name} as taken.")
        next_url = request.POST.get('next') or request.META.get('HTTP_REFERER') or reverse('accounts:dashboard')
        return redirect(next_url)


class DoseSkipView(LoginRequiredMixin, View):
    """
    Marks a scheduled dose as skipped with a clinical reason.
    """
    def post(self, request, pk):
        dose = get_object_or_404(MedicineDose, id=pk, schedule__medicine__user=request.user)
        reason = request.POST.get('reason', 'Skipped by user')
        dose.mark_as_skipped(reason)

        med = dose.schedule.medicine
        MedicationLog.objects.create(
            medicine=med,
            family_member=med.family_member,
            dose=dose,
            scheduled_time=timezone.make_aware(datetime.combine(dose.date, dose.scheduled_time)),
            actual_time=timezone.now(),
            status=MedicineDose.STATUS_SKIPPED,
            reason_for_skip=reason,
            logged_by=request.user
        )

        log_audit_event(
            user=request.user,
            action='UPDATE',
            module='MEDICATION',
            description=f"Recorded dose SKIPPED: {med.name} (Reason: {reason})",
            object_repr=med.name,
            request=request
        )

        messages.info(request, f"Dose for {med.name} marked as skipped.")
        next_url = request.POST.get('next') or request.META.get('HTTP_REFERER') or reverse('accounts:dashboard')
        return redirect(next_url)


class DoseSnoozeView(LoginRequiredMixin, View):
    """
    Snoozes a dose alert by X minutes.
    """
    def post(self, request, pk):
        dose = get_object_or_404(MedicineDose, id=pk, schedule__medicine__user=request.user)
        minutes = int(request.POST.get('minutes', 15))
        dose.snooze(minutes)
        messages.info(request, f"Reminder for {dose.schedule.medicine.name} snoozed for {minutes} minutes.")
        next_url = request.POST.get('next') or request.META.get('HTTP_REFERER') or reverse('accounts:dashboard')
        return redirect(next_url)


# Stock & Refills
class StockListView(LoginRequiredMixin, ListView):
    """
    Displays current inventory on hand and identifies items below safety threshold.
    """
    model = MedicineStock
    template_name = 'medications/stock_list.html'
    context_object_name = 'stocks'

    def get_queryset(self):
        qs = MedicineStock.objects.filter(medicine__user=self.request.user, medicine__status='ACTIVE')
        active_member = getattr(self.request, 'active_family_member', None)
        if active_member:
            qs = qs.filter(medicine__family_member=active_member)
        return qs.select_related('medicine', 'medicine__family_member').order_by('current_stock')


class StockRefillView(LoginRequiredMixin, CreateView):
    """
    Records a medicine purchase/refill and augments inventory count.
    """
    model = MedicineRefill
    form_class = MedicineRefillForm
    template_name = 'medications/stock_refill_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.medicine = get_object_or_404(Medicine, pk=self.kwargs.get('medicine_id'), user=request.user)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.medicine = self.medicine
        refill = form.save()

        log_audit_event(
            user=self.request.user,
            action='CREATE',
            module='MEDICATION',
            description=f"Refilled {refill.refill_quantity} units of {self.medicine.name}",
            object_repr=self.medicine.name,
            request=self.request
        )

        messages.success(
            self.request,
            f"Successfully added {refill.refill_quantity} units to {self.medicine.name} inventory."
        )
        return redirect('medications:stock_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['medicine'] = self.medicine
        return context


# Expiry Tracker
class ExpiryListView(LoginRequiredMixin, ListView):
    """
    Surveillance console for pharmaceutical batch expiration dates.
    """
    model = MedicineExpiry
    template_name = 'medications/expiry_list.html'
    context_object_name = 'batches'

    def get_queryset(self):
        # Refresh statuses
        MedicationExpiryService.check_expiries_and_alert(self.request.user)
        qs = MedicineExpiry.objects.filter(medicine__user=self.request.user)
        
        active_member = getattr(self.request, 'active_family_member', None)
        scope = self.request.GET.get('scope')
        if scope != 'all' and active_member:
            member_qs = qs.filter(medicine__family_member=active_member)
            if member_qs.exists() or scope == 'patient':
                qs = member_qs

        status_filter = self.request.GET.get('status')
        if status_filter in ['EXPIRED', 'EXPIRING_SOON', 'SAFE']:
            qs = qs.filter(status=status_filter)

        return qs.select_related('medicine', 'medicine__family_member').order_by('expiry_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_user_batches = MedicineExpiry.objects.filter(medicine__user=self.request.user)
        active_member = getattr(self.request, 'active_family_member', None)
        
        context['total_batches_count'] = all_user_batches.count()
        context['expired_count'] = all_user_batches.filter(status='EXPIRED').count()
        context['expiring_soon_count'] = all_user_batches.filter(status='EXPIRING_SOON').count()
        context['safe_count'] = all_user_batches.filter(status='SAFE').count()
        
        context['current_scope'] = self.request.GET.get('scope', 'patient' if active_member else 'all')
        context['current_status'] = self.request.GET.get('status', '')
        return context


class ExpiryCreateView(LoginRequiredMixin, CreateView):
    """
    Registers a new batch lot number and expiration date for a medicine.
    """
    model = MedicineExpiry
    form_class = MedicineExpiryForm
    template_name = 'medications/expiry_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.medicine = get_object_or_404(Medicine, pk=self.kwargs.get('medicine_id'), user=request.user)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.medicine = self.medicine
        batch = form.save()
        batch.update_status()

        messages.success(self.request, f"Registered batch {batch.batch_number} for {self.medicine.name}.")
        return redirect('medications:expiry_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['medicine'] = self.medicine
        return context


class MedicationHistoryView(LoginRequiredMixin, ListView):
    """
    Complete audit history of all recorded dose events.
    """
    model = MedicationLog
    template_name = 'medications/medication_logs.html'
    context_object_name = 'logs'
    paginate_by = 30

    def get_queryset(self):
        qs = MedicationLog.objects.filter(medicine__user=self.request.user)
        active_member = getattr(self.request, 'active_family_member', None)
        if active_member:
            qs = qs.filter(family_member=active_member)

        status = self.request.GET.get('status')
        if status:
            qs = qs.filter(status=status)

        return qs.select_related('medicine', 'family_member').order_by('-actual_time')


class AdherenceDashboardView(LoginRequiredMixin, TemplateView):
    """
    In-depth compliance analytics, medicine-wise adherence, and compliance graphs.
    """
    template_name = 'medications/adherence.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        active_member = getattr(self.request, 'active_family_member', None)

        days = int(self.request.GET.get('days', 30))
        metrics = MedicationAdherenceService.get_adherence_metrics(user, family_member=active_member, days=days)
        medicine_breakdown = MedicationAdherenceService.get_medicine_wise_adherence(user, family_member=active_member, days=days)

        context['metrics'] = metrics
        context['medicine_breakdown'] = medicine_breakdown
        context['selected_days'] = days
        return context

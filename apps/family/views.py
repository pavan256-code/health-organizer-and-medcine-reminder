"""
Views for managing family members and switching patient contexts.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from apps.family.models import FamilyMember
from apps.family.forms import FamilyMemberForm
from apps.audit.services import log_audit_event


class FamilyMemberListView(LoginRequiredMixin, ListView):
    """
    Displays all registered family members and dependants for the authenticated user.
    """
    model = FamilyMember
    template_name = 'family/list.html'
    context_object_name = 'members'

    def get_queryset(self):
        return FamilyMember.objects.filter(user=self.request.user, is_active=True)


class FamilyMemberCreateView(LoginRequiredMixin, CreateView):
    """
    Registers a new family member (e.g. child, spouse, parent) under user management.
    """
    model = FamilyMember
    form_class = FamilyMemberForm
    template_name = 'family/form.html'
    success_url = reverse_lazy('family:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        member = form.save()

        log_audit_event(
            user=self.request.user,
            action='CREATE',
            module='FAMILY',
            description=f"Added family member: {member.full_name} ({member.get_relationship_display()})",
            object_repr=member.full_name,
            object_id=member.id,
            request=self.request
        )

        messages.success(self.request, f"Family profile for '{member.full_name}' created successfully.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Add Family Member"
        context['submit_btn_text'] = "Save Family Member"
        return context


class FamilyMemberUpdateView(LoginRequiredMixin, UpdateView):
    """
    Updates an existing family member's details.
    """
    model = FamilyMember
    form_class = FamilyMemberForm
    template_name = 'family/form.html'
    success_url = reverse_lazy('family:list')

    def get_queryset(self):
        return FamilyMember.objects.filter(user=self.request.user)

    def form_valid(self, form):
        member = form.save()

        log_audit_event(
            user=self.request.user,
            action='UPDATE',
            module='FAMILY',
            description=f"Updated family member profile: {member.full_name}",
            object_repr=member.full_name,
            object_id=member.id,
            request=self.request
        )

        messages.success(self.request, f"Profile for '{member.full_name}' updated successfully.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f"Edit {self.object.full_name}"
        context['submit_btn_text'] = "Update Details"
        return context


class FamilyMemberDeleteView(LoginRequiredMixin, DeleteView):
    """
    Deactivates a family member safely without hard-deleting historical medical records.
    """
    model = FamilyMember
    template_name = 'family/confirm_delete.html'
    success_url = reverse_lazy('family:list')

    def get_queryset(self):
        return FamilyMember.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        member = self.get_object()
        if member.relationship == 'SELF':
            messages.error(request, "The primary account holder profile ('Self') cannot be deleted.")
            return redirect('family:list')

        member.is_active = False
        member.save(update_fields=['is_active'])

        # If currently active in session, reset to SELF
        if request.session.get('active_family_member_id') == member.id:
            self_member = FamilyMember.objects.filter(user=request.user, relationship='SELF').first()
            request.session['active_family_member_id'] = self_member.id if self_member else None

        log_audit_event(
            user=request.user,
            action='DELETE',
            module='FAMILY',
            description=f"Deactivated family member: {member.full_name}",
            object_repr=member.full_name,
            object_id=member.id,
            request=request
        )

        messages.success(request, f"Family profile '{member.full_name}' was deactivated.")
        return redirect(self.success_url)


class FamilyMemberDetailView(LoginRequiredMixin, DetailView):
    """
    Overview dossier of a specific family member showing health profile,
    active medications, latest vitals, and upcoming visits.
    """
    model = FamilyMember
    template_name = 'family/detail.html'
    context_object_name = 'member'

    def get_queryset(self):
        return FamilyMember.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        member = self.object

        try:
            from apps.medications.models import Medicine
            from apps.medical.models import Appointment, VitalRecord, HealthProfile, Allergy, Vaccination

            context['health_profile'] = HealthProfile.objects.filter(family_member=member).first()
            context['active_medicines'] = Medicine.objects.filter(family_member=member, status='ACTIVE')
            context['recent_vitals'] = VitalRecord.objects.filter(family_member=member).order_by('-date', '-time')[:5]
            context['upcoming_appointments'] = Appointment.objects.filter(
                family_member=member, status='UPCOMING'
            ).order_by('date', 'time')[:5]
            context['allergies'] = Allergy.objects.filter(family_member=member)
            context['vaccinations'] = Vaccination.objects.filter(family_member=member).order_by('-vaccination_date')
        except Exception:
            pass

        return context


class SwitchActiveFamilyMemberView(LoginRequiredMixin, View):
    """
    Switches the active patient context in the session and redirects back.
    Supports both POST and GET, and member_id from URL or request params.
    """
    def switch_member(self, request, member_id=None):
        target_id = member_id or request.POST.get('member_id') or request.GET.get('member_id')
        if target_id:
            member = get_object_or_404(FamilyMember, id=target_id, user=request.user, is_active=True)
            request.session['active_family_member_id'] = member.id
            request.active_family_member = member
            messages.info(request, f"Active patient profile switched to: {member.full_name}")

        next_url = (
            request.POST.get('next') or
            request.GET.get('next') or
            request.META.get('HTTP_REFERER') or
            reverse_lazy('accounts:dashboard')
        )
        return redirect(next_url)

    def post(self, request, member_id=None):
        return self.switch_member(request, member_id)

    def get(self, request, member_id=None):
        return self.switch_member(request, member_id)

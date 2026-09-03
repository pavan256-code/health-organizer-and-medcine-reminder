"""
Views for Emergency Health Card and Local Drug Interaction Checker.
"""

from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.family.models import FamilyMember
from apps.emergency.services.interaction_checker import DrugInteractionEngine


class EmergencyCardView(LoginRequiredMixin, TemplateView):
    """
    Print-ready wallet-sized or full-sheet emergency medical ID card.
    """
    template_name = 'emergency/emergency_card.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        member = getattr(self.request, 'active_family_member', None)
        if not member:
            member = FamilyMember.objects.filter(user=user, relationship='SELF').first()
            if not member:
                member = FamilyMember.objects.filter(user=user).first()

        context['member'] = member
        if member:
            context['health_profile'] = getattr(member, 'health_profile', None)
            context['allergies'] = member.allergies.all()
            context['active_meds'] = member.medicines.filter(status='ACTIVE')
            context['recent_vitals'] = member.vitals.first()
        return context


class InteractionCheckerView(LoginRequiredMixin, TemplateView):
    """
    Local drug interaction checker with automated cross-screening of active medications.
    """
    template_name = 'emergency/interaction_checker.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        member = getattr(self.request, 'active_family_member', None)

        # 1. Screen active medicines for current patient automatically
        auto_conflicts = []
        if member:
            active_med_names = list(member.medicines.filter(status='ACTIVE').values_list('name', flat=True))
            auto_conflicts = DrugInteractionEngine.check_interaction(active_med_names)

        # 2. Check query string if user entered manual drug pairs
        query_drugs = self.request.GET.get('drugs', '')
        manual_conflicts = []
        if query_drugs:
            drug_list = [d.strip() for d in query_drugs.split(',') if d.strip()]
            manual_conflicts = DrugInteractionEngine.check_interaction(drug_list)

        context['auto_conflicts'] = auto_conflicts
        context['manual_conflicts'] = manual_conflicts
        context['query_drugs'] = query_drugs
        context['member'] = member
        return context

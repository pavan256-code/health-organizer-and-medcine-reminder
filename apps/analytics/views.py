"""
Analytics & Health Intelligence Views.
"""

from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.analytics.services.insight_engine import HealthInsightEngine


class HealthInsightsView(LoginRequiredMixin, TemplateView):
    template_name = 'analytics/insights.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        member = getattr(self.request, 'active_family_member', None)

        insights = HealthInsightEngine.generate_insights(user, family_member=member)
        health_score = HealthInsightEngine.calculate_health_score(user, family_member=member)

        context['insights'] = insights
        context['health_score'] = health_score
        return context

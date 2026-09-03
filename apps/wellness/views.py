"""
Views for Lifestyle & Wellness: Diet, Nutrition, Water Intake, Fitness, Sleep, and Goals.
"""

from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils import timezone
from django.db.models import Sum

from apps.wellness.models import MealRecord, ActivityRecord, SleepRecord, HealthGoal
from apps.wellness.forms import MealRecordForm, ActivityRecordForm, SleepRecordForm, HealthGoalForm
from apps.family.models import FamilyMember


# -------------------------------------------------------------
# 1. Diet & Nutrition
# -------------------------------------------------------------
class DietOverviewView(LoginRequiredMixin, TemplateView):
    template_name = 'wellness/diet_overview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        member = getattr(self.request, 'active_family_member', None)
        today = timezone.now().date()

        qs = MealRecord.objects.filter(family_member__user=user, date=today)
        if member:
            qs = qs.filter(family_member=member)

        context['todays_meals'] = qs
        context['total_calories'] = qs.aggregate(Sum('calories'))['calories__sum'] or 0
        context['total_water'] = qs.aggregate(Sum('water_intake_ml'))['water_intake_ml__sum'] or 0
        context['recent_meals'] = MealRecord.objects.filter(family_member__user=user).order_by('-date')[:15]
        return context


class MealCreateView(LoginRequiredMixin, CreateView):
    model = MealRecord
    form_class = MealRecordForm
    template_name = 'wellness/meal_form.html'
    success_url = reverse_lazy('wellness:diet_overview')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Meal logged successfully.")
        return super().form_valid(form)


class WaterLogView(LoginRequiredMixin, View):
    """
    Quick one-click logging for 250ml glass of water.
    """
    def post(self, request):
        member = getattr(request, 'active_family_member', None)
        if not member:
            member = FamilyMember.objects.filter(user=request.user, relationship='SELF').first()

        amount_ml = int(request.POST.get('amount_ml', 250))
        today = timezone.now().date()

        # Add or update meal record for water
        meal = MealRecord.objects.filter(family_member=member, date=today, meal_type='SNACK', food_items='Hydration').first()
        if meal:
            meal.water_intake_ml += amount_ml
            meal.save(update_fields=['water_intake_ml'])
        else:
            MealRecord.objects.create(
                family_member=member,
                date=today,
                meal_type='SNACK',
                food_items='Hydration',
                water_intake_ml=amount_ml
            )

        messages.success(request, f"✓ Added +{amount_ml}ml to today's hydration total.")
        return redirect('wellness:diet_overview')


# -------------------------------------------------------------
# 2. Fitness & Activity
# -------------------------------------------------------------
class FitnessListView(LoginRequiredMixin, ListView):
    model = ActivityRecord
    template_name = 'wellness/fitness_list.html'
    context_object_name = 'activities'
    paginate_by = 25

    def get_queryset(self):
        qs = ActivityRecord.objects.filter(family_member__user=self.request.user)
        member = getattr(self.request, 'active_family_member', None)
        if member:
            qs = qs.filter(family_member=member)
        return qs.select_related('family_member').order_by('-date', '-created_at')


class FitnessCreateView(LoginRequiredMixin, CreateView):
    model = ActivityRecord
    form_class = ActivityRecordForm
    template_name = 'wellness/fitness_form.html'
    success_url = reverse_lazy('wellness:fitness_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Physical activity recorded.")
        return super().form_valid(form)


# -------------------------------------------------------------
# 3. Sleep Tracker
# -------------------------------------------------------------
class SleepListView(LoginRequiredMixin, ListView):
    model = SleepRecord
    template_name = 'wellness/sleep_list.html'
    context_object_name = 'sleep_records'
    paginate_by = 25

    def get_queryset(self):
        qs = SleepRecord.objects.filter(family_member__user=self.request.user)
        member = getattr(self.request, 'active_family_member', None)
        if member:
            qs = qs.filter(family_member=member)
        return qs.select_related('family_member').order_by('-date')


class SleepCreateView(LoginRequiredMixin, CreateView):
    model = SleepRecord
    form_class = SleepRecordForm
    template_name = 'wellness/sleep_form.html'
    success_url = reverse_lazy('wellness:sleep_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Sleep night log recorded.")
        return super().form_valid(form)


# -------------------------------------------------------------
# 4. Health Goals
# -------------------------------------------------------------
class GoalListView(LoginRequiredMixin, ListView):
    model = HealthGoal
    template_name = 'wellness/goal_list.html'
    context_object_name = 'goals'

    def get_queryset(self):
        qs = HealthGoal.objects.filter(family_member__user=self.request.user)
        member = getattr(self.request, 'active_family_member', None)
        if member:
            qs = qs.filter(family_member=member)
        return qs.select_related('family_member').order_by('status', '-created_at')


class GoalCreateView(LoginRequiredMixin, CreateView):
    model = HealthGoal
    form_class = HealthGoalForm
    template_name = 'wellness/goal_form.html'
    success_url = reverse_lazy('wellness:goal_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "New wellness goal registered.")
        return super().form_valid(form)


class GoalUpdateProgressView(LoginRequiredMixin, View):
    def post(self, request, pk):
        goal = get_object_or_404(HealthGoal, id=pk, family_member__user=request.user)
        val = float(request.POST.get('current_value', goal.current_value))
        goal.current_value = val
        if goal.current_value >= goal.target_value:
            goal.status = HealthGoal.STATUS_COMPLETED
        goal.save(update_fields=['current_value', 'status', 'updated_at'])
        messages.success(request, f"Updated progress for '{goal.title}'.")
        return redirect('wellness:goal_list')


class GoalDeleteView(LoginRequiredMixin, DeleteView):
    model = HealthGoal
    template_name = 'wellness/goal_confirm_delete.html'
    success_url = reverse_lazy('wellness:goal_list')

    def get_queryset(self):
        return HealthGoal.objects.filter(family_member__user=self.request.user)

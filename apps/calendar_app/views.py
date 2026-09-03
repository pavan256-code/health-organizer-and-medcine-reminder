"""
Unified Health Calendar aggregating appointments, medication doses, vaccines, and refills.
"""

from datetime import datetime, date, timedelta
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

from apps.medications.models import MedicineDose, MedicineRefill
from apps.medical.models import Appointment, Vaccination


class UnifiedCalendarView(LoginRequiredMixin, TemplateView):
    """
    Renders an integrated multi-domain calendar view combining:
    - Scheduled medication doses
    - Clinical appointments
    - Vaccination due dates
    - Inventory refill events
    """
    template_name = 'calendar/unified_calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        member = getattr(self.request, 'active_family_member', None)

        # Parse selected month and year or default to current
        today = timezone.now().date()
        year = int(self.request.GET.get('year', today.year))
        month = int(self.request.GET.get('month', today.month))

        import calendar
        cal = calendar.Calendar(firstweekday=0) # Monday first
        month_days = cal.monthdatescalendar(year, month)

        start_date = month_days[0][0]
        end_date = month_days[-1][-1]

        # 1. Fetch Doses
        dose_qs = MedicineDose.objects.filter(
            schedule__medicine__user=user,
            date__gte=start_date,
            date__lte=end_date
        )
        if member:
            dose_qs = dose_qs.filter(schedule__medicine__family_member=member)

        # 2. Fetch Appointments
        appt_qs = Appointment.objects.filter(
            user=user,
            date__gte=start_date,
            date__lte=end_date
        )
        if member:
            appt_qs = appt_qs.filter(family_member=member)

        # 3. Fetch Vaccinations
        vac_qs = Vaccination.objects.filter(
            family_member__user=user,
            next_due_date__gte=start_date,
            next_due_date__lte=end_date
        )
        if member:
            vac_qs = vac_qs.filter(family_member=member)

        # Build date indexed dictionary
        events_by_date = {}

        for d in dose_qs.select_related('schedule__medicine', 'schedule__medicine__family_member'):
            d_str = d.date.strftime('%Y-%m-%d')
            if d_str not in events_by_date:
                events_by_date[d_str] = []
            events_by_date[d_str].append({
                'type': 'DOSE',
                'title': f"💊 {d.schedule.medicine.name} ({d.scheduled_time.strftime('%H:%M')})",
                'patient': d.schedule.medicine.family_member.first_name,
                'status': d.status,
                'color': 'primary' if d.status == 'PENDING' else ('success' if d.status == 'TAKEN' else 'danger')
            })

        for a in appt_qs.select_related('doctor', 'family_member'):
            d_str = a.date.strftime('%Y-%m-%d')
            if d_str not in events_by_date:
                events_by_date[d_str] = []
            events_by_date[d_str].append({
                'type': 'APPOINTMENT',
                'title': f"🩺 {a.doctor.full_name} ({a.time.strftime('%H:%M')})",
                'patient': a.family_member.first_name,
                'status': a.status,
                'color': 'warning'
            })

        for v in vac_qs.select_related('family_member'):
            d_str = v.next_due_date.strftime('%Y-%m-%d')
            if d_str not in events_by_date:
                events_by_date[d_str] = []
            events_by_date[d_str].append({
                'type': 'VACCINE',
                'title': f"💉 Due: {v.vaccine_name}",
                'patient': v.family_member.first_name,
                'status': 'DUE',
                'color': 'info'
            })

        # Build calendar matrix for template
        calendar_grid = []
        for week in month_days:
            week_days = []
            for day in week:
                d_str = day.strftime('%Y-%m-%d')
                week_days.append({
                    'date': day,
                    'is_current_month': (day.month == month),
                    'is_today': (day == today),
                    'events': events_by_date.get(d_str, [])
                })
            calendar_grid.append(week_days)

        # Previous and next month pagination
        prev_month = month - 1 if month > 1 else 12
        prev_year = year if month > 1 else year - 1
        next_month = month + 1 if month < 12 else 1
        next_year = year if month < 12 else year + 1

        context['calendar_grid'] = calendar_grid
        context['current_month_name'] = calendar.month_name[month]
        context['current_year'] = year
        context['current_month'] = month
        context['prev_month'] = prev_month
        context['prev_year'] = prev_year
        context['next_month'] = next_month
        context['next_year'] = next_year
        return context

"""
Dose generation, recurrence scheduling, and timeline processing engine.
"""

from datetime import datetime, time, timedelta
from django.utils import timezone
from apps.medications.models import MedicineSchedule, MedicineDose


class MedicationSchedulerService:
    """
    Generates deterministic MedicineDose instances for active schedules
    within a target date window without creating duplicates.
    """
    @staticmethod
    def generate_doses_for_date(target_date=None, user=None):
        """
        Scans all active schedules and provisions doses for target_date.
        """
        if not target_date:
            target_date = timezone.now().date()

        schedules = MedicineSchedule.objects.filter(
            is_active=True,
            medicine__status='ACTIVE',
            start_date__lte=target_date
        )

        if user:
            schedules = schedules.filter(medicine__user=user)

        created_count = 0
        weekday = target_date.weekday()  # 0=Monday, 6=Sunday

        for sched in schedules.select_related('medicine', 'medicine__family_member'):
            # Check end date
            if sched.end_date and sched.end_date < target_date:
                continue

            # Check recurrence pattern
            should_run = False
            freq = sched.frequency

            if freq in ['DAILY', 'TWICE_DAILY', 'THREE_TIMES_DAILY', 'FOUR_TIMES_DAILY']:
                should_run = True
            elif freq == 'WEEKLY':
                # Check if matches start_date weekday or configured days
                if sched.days_of_week:
                    should_run = weekday in sched.days_of_week
                else:
                    should_run = (weekday == sched.start_date.weekday())
            elif freq == 'CUSTOM':
                if sched.days_of_week:
                    should_run = weekday in sched.days_of_week
                else:
                    should_run = True
            elif freq == 'ONCE':
                should_run = (sched.start_date == target_date)

            if not should_run:
                continue

            # Determine times
            times = sched.specific_times
            if not times:
                if freq == 'ONCE' or freq == 'DAILY':
                    times = ['08:00']
                elif freq == 'TWICE_DAILY':
                    times = ['08:00', '20:00']
                elif freq == 'THREE_TIMES_DAILY':
                    times = ['08:00', '14:00', '20:00']
                elif freq == 'FOUR_TIMES_DAILY':
                    times = ['08:00', '12:00', '18:00', '22:00']
                else:
                    times = ['08:00']

            for t_str in times:
                try:
                    hour, minute = [int(p) for p in t_str.split(':')[:2]]
                    parsed_time = time(hour=hour, minute=minute)
                except Exception:
                    parsed_time = time(hour=8, minute=0)

                # Provision dose idempotently
                dose, created = MedicineDose.objects.get_or_create(
                    schedule=sched,
                    date=target_date,
                    scheduled_time=parsed_time,
                    defaults={'status': MedicineDose.STATUS_PENDING}
                )
                if created:
                    created_count += 1

        return created_count

    @staticmethod
    def generate_doses_for_window(days_ahead=7, user=None):
        """
        Provisions doses across an upcoming rolling window (e.g. 7 days).
        """
        today = timezone.now().date()
        total_created = 0
        for i in range(days_ahead + 1):
            target = today + timedelta(days=i)
            total_created += MedicationSchedulerService.generate_doses_for_date(target, user=user)
        return total_created

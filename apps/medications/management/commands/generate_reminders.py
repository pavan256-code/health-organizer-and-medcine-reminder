"""
Management command to generate rolling medicine doses and reminders.
Run via: python manage.py generate_reminders
"""

from django.core.management.base import BaseCommand
from apps.medications.services.scheduler_service import MedicationSchedulerService


class Command(BaseCommand):
    help = "Generates rolling dose schedules for the next 7 days for all active patients."

    def add_arguments(self, parser):
        parser.add_argument(
            '--days',
            type=int,
            default=7,
            help='Number of days in advance to provision scheduled doses (default 7).'
        )

    def handle(self, *args, **options):
        days = options['days']
        self.stdout.write(f"Generating medication dose schedules for the next {days} days...")
        count = MedicationSchedulerService.generate_doses_for_window(days_ahead=days)
        self.stdout.write(self.style.SUCCESS(f"Successfully created or verified {count} dose records."))

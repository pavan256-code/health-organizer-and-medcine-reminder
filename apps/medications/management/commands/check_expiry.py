"""
Management command to refresh batch lot expiration statuses and send warnings.
Run via: python manage.py check_expiry
"""

from django.core.management.base import BaseCommand
from apps.medications.services.expiry_service import MedicationExpiryService


class Command(BaseCommand):
    help = "Refreshes pharmaceutical lot expiry statuses and generates alerts for expiring/expired batches."

    def handle(self, *args, **options):
        self.stdout.write("Checking pharmaceutical batch expiry statuses...")
        count = MedicationExpiryService.check_expiries_and_alert()
        self.stdout.write(self.style.SUCCESS(f"Updated lot statuses and dispatched {count} expiry notifications."))

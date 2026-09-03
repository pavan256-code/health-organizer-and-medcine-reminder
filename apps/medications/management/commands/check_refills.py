"""
Management command to check medicine inventory stock and fire refill alerts.
Run via: python manage.py check_refills
"""

from django.core.management.base import BaseCommand
from apps.medications.services.stock_service import MedicationStockService


class Command(BaseCommand):
    help = "Checks all medicine stocks and dispatches low stock refill warnings."

    def handle(self, *args, **options):
        self.stdout.write("Checking medicine inventory levels...")
        count = MedicationStockService.check_low_stocks_and_alert()
        self.stdout.write(self.style.SUCCESS(f"Generated {count} low-stock notification alerts."))

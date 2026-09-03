"""
Medicine inventory, stock level verification, and refill alerting.
"""

from apps.medications.models import MedicineStock
from apps.notifications.services import create_notification


class MedicationStockService:
    @staticmethod
    def check_low_stocks_and_alert(user=None):
        """
        Scans inventory stocks and dispatches low-stock alerts.
        """
        qs = MedicineStock.objects.all().select_related('medicine', 'medicine__user', 'medicine__family_member')
        if user:
            qs = qs.filter(medicine__user=user)

        alerts_created = 0
        for stock in qs:
            if stock.is_low_stock():
                # Trigger in-app notification
                create_notification(
                    user=stock.medicine.user,
                    family_member=stock.medicine.family_member,
                    category='REFILL',
                    priority='HIGH',
                    title=f"Low Stock Alert: {stock.medicine.name}",
                    message=f"Only {stock.current_stock} {stock.unit} remaining for {stock.medicine.family_member.full_name}. Please reorder or refill.",
                    action_url=f"/medications/stock/{stock.medicine.id}/refill/"
                )
                alerts_created += 1

        return alerts_created

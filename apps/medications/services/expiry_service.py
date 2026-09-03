"""
Pharmaceutical batch lot expiry monitoring and status synchronizer.
"""

from apps.medications.models import MedicineExpiry
from apps.notifications.services import create_notification


class MedicationExpiryService:
    @staticmethod
    def check_expiries_and_alert(user=None):
        """
        Refreshes expiry statuses across all medicine batches and fires expiry alerts.
        """
        qs = MedicineExpiry.objects.all().select_related('medicine', 'medicine__user', 'medicine__family_member')
        if user:
            qs = qs.filter(medicine__user=user)

        alerts_created = 0
        for batch in qs:
            old_status = batch.status
            new_status = batch.update_status()

            if new_status in ['EXPIRING_SOON', 'EXPIRED'] and old_status != new_status:
                priority = 'URGENT' if new_status == 'EXPIRED' else 'HIGH'
                title = f"{'EXPIRED' if new_status == 'EXPIRED' else 'Expiring Soon'}: {batch.medicine.name}"
                msg = f"Batch {batch.batch_number} of {batch.medicine.name} expires on {batch.expiry_date}. Status: {batch.get_status_display()}."

                create_notification(
                    user=batch.medicine.user,
                    family_member=batch.medicine.family_member,
                    category='EXPIRY',
                    priority=priority,
                    title=title,
                    message=msg,
                    action_url="/medications/expiry/"
                )
                alerts_created += 1

        return alerts_created

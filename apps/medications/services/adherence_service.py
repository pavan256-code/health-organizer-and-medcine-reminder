"""
Adherence mathematics, compliance metrics, and statistical aggregators.
"""

from datetime import timedelta
from django.utils import timezone
from apps.medications.models import MedicineDose, Medicine


class MedicationAdherenceService:
    """
    Computes clinical adherence percentages, taken/missed ratios,
    and medicine/patient compliance rankings.
    """
    @staticmethod
    def get_adherence_metrics(user, family_member=None, days=30):
        """
        Calculates compliance statistics over the last N days.
        """
        today = timezone.now().date()
        start_date = today - timedelta(days=days)

        qs = MedicineDose.objects.filter(
            schedule__medicine__user=user,
            date__gte=start_date,
            date__lte=today
        )
        if family_member:
            qs = qs.filter(schedule__medicine__family_member=family_member)

        total_doses = qs.count()
        taken_doses = qs.filter(status=MedicineDose.STATUS_TAKEN).count()
        skipped_doses = qs.filter(status=MedicineDose.STATUS_SKIPPED).count()
        missed_doses = qs.filter(status=MedicineDose.STATUS_MISSED).count()
        delayed_doses = qs.filter(status=MedicineDose.STATUS_DELAYED).count()
        pending_doses = qs.filter(status=MedicineDose.STATUS_PENDING).count()

        evaluated_doses = taken_doses + skipped_doses + missed_doses + delayed_doses

        adherence_rate = 100.0
        if evaluated_doses > 0:
            # Taken or delayed count as compliant
            compliant = taken_doses + delayed_doses
            adherence_rate = round((compliant / evaluated_doses) * 100, 1)

        taken_rate = round((taken_doses / total_doses * 100), 1) if total_doses > 0 else 0
        missed_rate = round((missed_doses / total_doses * 100), 1) if total_doses > 0 else 0
        skipped_rate = round((skipped_doses / total_doses * 100), 1) if total_doses > 0 else 0

        return {
            'total_doses': total_doses,
            'taken_doses': taken_doses,
            'skipped_doses': skipped_doses,
            'missed_doses': missed_doses,
            'delayed_doses': delayed_doses,
            'pending_doses': pending_doses,
            'adherence_rate': adherence_rate,
            'taken_rate': taken_rate,
            'missed_rate': missed_rate,
            'skipped_rate': skipped_rate,
            'evaluated_doses': evaluated_doses,
            'days': days,
        }

    @staticmethod
    def get_medicine_wise_adherence(user, family_member=None, days=30):
        """
        Computes adherence breakdown per medicine.
        """
        today = timezone.now().date()
        start_date = today - timedelta(days=days)

        meds = Medicine.objects.filter(user=user, status='ACTIVE')
        if family_member:
            meds = meds.filter(family_member=family_member)

        results = []
        for med in meds:
            doses = MedicineDose.objects.filter(
                schedule__medicine=med,
                date__gte=start_date,
                date__lte=today
            )
            total = doses.count()
            taken = doses.filter(status__in=[MedicineDose.STATUS_TAKEN, MedicineDose.STATUS_DELAYED]).count()
            missed = doses.filter(status=MedicineDose.STATUS_MISSED).count()
            skipped = doses.filter(status=MedicineDose.STATUS_SKIPPED).count()

            rate = round((taken / total * 100), 1) if total > 0 else 100.0
            results.append({
                'medicine': med,
                'total': total,
                'taken': taken,
                'missed': missed,
                'skipped': skipped,
                'adherence_rate': rate,
            })

        return sorted(results, key=lambda x: x['adherence_rate'])

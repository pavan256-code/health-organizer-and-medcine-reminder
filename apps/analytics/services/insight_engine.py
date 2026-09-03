"""
Local deterministic rule-based health intelligence & clinical heuristic engine.
Zero external AI or cloud APIs. Evaluates metrics purely on local database state.
"""

from datetime import timedelta
from django.utils import timezone
from apps.medications.models import Medicine, MedicineStock, MedicineExpiry, MedicineDose
from apps.medications.services.adherence_service import MedicationAdherenceService
from apps.medical.models import VitalRecord
from apps.wellness.models import HealthGoal


class HealthInsightEngine:
    """
    Analyzes local patient records to generate clinical warnings, compliance notices,
    and computes the overall Family Health Score (0-100).
    """
    @classmethod
    def generate_insights(cls, user, family_member=None):
        insights = []

        # 1. Adherence Check
        adherence_data = MedicationAdherenceService.get_adherence_metrics(user, family_member=family_member, days=14)
        if adherence_data['evaluated_doses'] >= 5 and adherence_data['adherence_rate'] < 75.0:
            insights.append({
                'category': 'ADHERENCE',
                'severity': 'HIGH',
                'title': 'Sub-optimal Medication Adherence Detected',
                'description': f"Medication adherence over the last 14 days is {adherence_data['adherence_rate']}%. Adherence below 75% significantly reduces clinical efficacy. Consider adjusting reminder alert times.",
                'icon': '⚠️'
            })

        # 2. Blood Pressure Trend Check
        vital_qs = VitalRecord.objects.filter(family_member__user=user)
        if family_member:
            vital_qs = vital_qs.filter(family_member=family_member)

        recent_bp = list(vital_qs.filter(blood_pressure_systolic__isnull=False).order_by('-date', '-time')[:3])
        if len(recent_bp) >= 3:
            high_bp_count = sum(1 for v in recent_bp if v.blood_pressure_systolic >= 130 or (v.blood_pressure_diastolic and v.blood_pressure_diastolic >= 80))
            if high_bp_count == 3:
                insights.append({
                    'category': 'VITALS',
                    'severity': 'URGENT',
                    'title': 'Sustained Elevated Blood Pressure',
                    'description': f"The last 3 blood pressure readings (most recent: {recent_bp[0].blood_pressure_systolic}/{recent_bp[0].blood_pressure_diastolic} mmHg) meet Stage 1 or 2 Hypertension thresholds. We recommend sharing this trend with your physician.",
                    'icon': '❤️'
                })

        # 3. Blood Sugar Diabetic Screen
        recent_glucose = list(vital_qs.filter(blood_sugar_fasting__isnull=False).order_by('-date', '-time')[:2])
        if recent_glucose and any(g.blood_sugar_fasting >= 126 for g in recent_glucose):
            insights.append({
                'category': 'METABOLIC',
                'severity': 'HIGH',
                'title': 'Elevated Fasting Glucose Warning',
                'description': f"Fasting blood glucose was recorded at {recent_glucose[0].blood_sugar_fasting} mg/dL (threshold >= 126 mg/dL indicates hyperglycemia). Ensure proper fasting conditions and consult your doctor.",
                'icon': '🩸'
            })

        # 4. Low Inventory Stock Check
        stocks = MedicineStock.objects.filter(medicine__user=user, medicine__status='ACTIVE')
        if family_member:
            stocks = stocks.filter(medicine__family_member=family_member)

        for s in stocks:
            if s.is_low_stock():
                insights.append({
                    'category': 'REFILL',
                    'severity': 'MEDIUM',
                    'title': f"Low Stock: {s.medicine.name}",
                    'description': f"Only {s.current_stock} {s.unit} remaining for {s.medicine.family_member.full_name}. Refill is required soon.",
                    'icon': '📦'
                })

        # 5. Expiring Lots Check
        expiries = MedicineExpiry.objects.filter(medicine__user=user)
        if family_member:
            expiries = expiries.filter(medicine__family_member=family_member)

        for e in expiries:
            e.update_status()
            if e.status == 'EXPIRED':
                insights.append({
                    'category': 'EXPIRY',
                    'severity': 'URGENT',
                    'title': f"Expired Medication: {e.medicine.name}",
                    'description': f"Batch {e.batch_number} expired on {e.expiry_date}. Do not administer expired pharmaceuticals.",
                    'icon': '⛔'
                })
            elif e.status == 'EXPIRING_SOON':
                insights.append({
                    'category': 'EXPIRY',
                    'severity': 'MEDIUM',
                    'title': f"Expiring Soon: {e.medicine.name}",
                    'description': f"Batch {e.batch_number} will expire on {e.expiry_date} ({e.days_remaining} days left).",
                    'icon': '⚠️'
                })

        return insights

    @classmethod
    def calculate_health_score(cls, user, family_member=None):
        """
        Calculates a dynamic holistic Health Score from 0 to 100 based on:
        - Medication Adherence (40 points max)
        - Vitals stability (30 points max)
        - Active Health Goals achievement (30 points max)
        """
        # Adherence component (0-40)
        adherence_data = MedicationAdherenceService.get_adherence_metrics(user, family_member=family_member, days=14)
        adh_rate = adherence_data['adherence_rate']
        adherence_score = (adh_rate / 100.0) * 40.0

        # Vitals component (0-30)
        v_qs = VitalRecord.objects.filter(family_member__user=user)
        if family_member:
            v_qs = v_qs.filter(family_member=family_member)

        recent_bp = v_qs.filter(blood_pressure_systolic__isnull=False).first()
        vitals_score = 30.0
        if recent_bp:
            if recent_bp.blood_pressure_systolic > 140 or (recent_bp.blood_pressure_diastolic and recent_bp.blood_pressure_diastolic > 90):
                vitals_score -= 15.0
            elif recent_bp.blood_pressure_systolic > 120:
                vitals_score -= 7.0

        # Goals component (0-30)
        g_qs = HealthGoal.objects.filter(family_member__user=user, status__in=['ACTIVE', 'COMPLETED'])
        if family_member:
            g_qs = g_qs.filter(family_member=family_member)

        goals_score = 25.0
        if g_qs.exists():
            avg_prog = sum(g.progress_percentage for g in g_qs) / g_qs.count()
            goals_score = (avg_prog / 100.0) * 30.0

        total = round(adherence_score + vitals_score + goals_score)
        return min(100, max(0, total))

"""
CSV Export service for medication logs and vital signs records.
"""

import csv
import io


class CSVReportService:
    @staticmethod
    def export_medication_logs_csv(user, family_member=None):
        from apps.medications.models import MedicationLog
        output = io.StringIO()
        writer = csv.writer(output)

        writer.writerow([
            'Log ID', 'Patient Name', 'Medicine Name', 'Dosage',
            'Scheduled Time', 'Actual Time', 'Status', 'Reason for Skip', 'Notes'
        ])

        qs = MedicationLog.objects.filter(medicine__user=user)
        if family_member:
            qs = qs.filter(family_member=family_member)

        for log in qs.select_related('family_member', 'medicine').order_by('-actual_time'):
            writer.writerow([
                log.id,
                log.family_member.full_name,
                log.medicine.name,
                log.medicine.dosage,
                log.scheduled_time.strftime('%Y-%m-%d %H:%M'),
                log.actual_time.strftime('%Y-%m-%d %H:%M'),
                log.status,
                log.reason_for_skip,
                log.notes
            ])

        return output.getvalue()

    @staticmethod
    def export_vitals_csv(user, family_member=None):
        from apps.medical.models import VitalRecord
        output = io.StringIO()
        writer = csv.writer(output)

        writer.writerow([
            'Record ID', 'Patient Name', 'Date', 'Time',
            'Systolic BP (mmHg)', 'Diastolic BP (mmHg)', 'BP Category',
            'Heart Rate (BPM)', 'Fasting Glucose (mg/dL)', 'SpO2 (%)',
            'Weight (kg)', 'Height (cm)', 'BMI', 'Notes'
        ])

        qs = VitalRecord.objects.filter(family_member__user=user)
        if family_member:
            qs = qs.filter(family_member=family_member)

        for v in qs.select_related('family_member').order_by('-date', '-time'):
            writer.writerow([
                v.id,
                v.family_member.full_name,
                v.date.strftime('%Y-%m-%d'),
                v.time.strftime('%H:%M'),
                v.blood_pressure_systolic or '',
                v.blood_pressure_diastolic or '',
                v.bp_category,
                v.heart_rate or '',
                v.blood_sugar_fasting or '',
                v.oxygen_saturation or '',
                v.weight_kg or '',
                v.height_cm or '',
                v.bmi or '',
                v.notes
            ])

        return output.getvalue()

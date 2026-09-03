"""
Professional PDF reporting engine utilizing local ReportLab.
Generates Doctor Visit Summaries, Medication Schedules, and Full Health Dossiers.
"""

import io
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors


class PDFReportService:
    @staticmethod
    def generate_medication_schedule_pdf(user, family_member):
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
        elements = []
        styles = getSampleStyleSheet()

        title_style = ParagraphStyle(
            'ReportTitle',
            parent=styles['Heading1'],
            fontSize=18,
            textColor=colors.HexColor('#0284c7'),
            spaceAfter=8
        )
        subtitle_style = ParagraphStyle(
            'ReportSub',
            parent=styles['Normal'],
            fontSize=10,
            textColor=colors.HexColor('#475569'),
            spaceAfter=14
        )

        # Header
        elements.append(Paragraph("MEDICINE REMINDER & HEALTH ORGANIZER", title_style))
        elements.append(Paragraph(f"Official Medication Regimen Schedule • Patient: {family_member.full_name} • Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}", subtitle_style))
        elements.append(Spacer(1, 10))

        # Query medicines and active schedules
        meds = family_member.medicines.filter(status='ACTIVE')

        table_data = [
            ["Medicine", "Formulation", "Dosage", "Timing / Meal", "Scheduled Times"]
        ]

        for m in meds:
            schedules = m.schedules.filter(is_active=True)
            times_list = []
            for s in schedules:
                if s.specific_times:
                    times_list.extend(s.specific_times)
            times_str = ", ".join(times_list) if times_list else "As needed"

            table_data.append([
                m.name,
                m.get_medicine_type_display(),
                m.dosage,
                m.get_instructions_display(),
                times_str
            ])

        t = Table(table_data, colWidths=[130, 90, 90, 130, 100])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0284c7')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 9),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e1')),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 8),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        elements.append(t)

        doc.build(elements)
        buffer.seek(0)
        return buffer.getvalue()

    @staticmethod
    def generate_doctor_visit_summary_pdf(user, family_member):
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
        elements = []
        styles = getSampleStyleSheet()

        title_style = ParagraphStyle('Title', parent=styles['Heading1'], fontSize=16, textColor=colors.HexColor('#0f172a'))
        section_style = ParagraphStyle('Section', parent=styles['Heading2'], fontSize=12, textColor=colors.HexColor('#0284c7'), spaceBefore=12, spaceAfter=6)
        body_style = ParagraphStyle('Body', parent=styles['Normal'], fontSize=9, textColor=colors.HexColor('#334155'))

        elements.append(Paragraph(f"Clinical Visit Brief: {family_member.full_name}", title_style))
        elements.append(Paragraph(f"DOB: {family_member.date_of_birth or 'N/A'} • Blood Group: {family_member.blood_group} • Generated: {datetime.now().strftime('%Y-%m-%d')}", body_style))
        elements.append(Spacer(1, 10))

        # 1. Allergies
        elements.append(Paragraph("Known Allergies & Sensitivities", section_style))
        allergies = family_member.allergies.all()
        if allergies.exists():
            alg_data = [["Allergen", "Type", "Severity", "Clinical Reaction"]]
            for a in allergies:
                alg_data.append([a.allergen, a.get_allergy_type_display(), a.severity, a.reaction])
            t_alg = Table(alg_data, colWidths=[130, 110, 80, 220])
            t_alg.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#e2e8f0')),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 8),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e1')),
            ]))
            elements.append(t_alg)
        else:
            elements.append(Paragraph("No known drug or environmental allergies recorded.", body_style))

        # 2. Recent Vitals
        elements.append(Paragraph("Recent Physiological Vitals (Last 5 Readings)", section_style))
        vitals = family_member.vitals.order_by('-date', '-time')[:5]
        if vitals.exists():
            v_data = [["Date", "Blood Pressure", "Heart Rate", "Glucose", "Weight"]]
            for v in vitals:
                bp = f"{v.blood_pressure_systolic}/{v.blood_pressure_diastolic}" if v.blood_pressure_systolic else "-"
                v_data.append([
                    v.date.strftime('%Y-%m-%d'),
                    bp,
                    f"{v.heart_rate} BPM" if v.heart_rate else "-",
                    f"{v.blood_sugar_fasting} mg/dL" if v.blood_sugar_fasting else "-",
                    f"{v.weight_kg} kg" if v.weight_kg else "-"
                ])
            t_v = Table(v_data, colWidths=[100, 110, 110, 110, 110])
            t_v.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#e2e8f0')),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 8),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e1')),
            ]))
            elements.append(t_v)

        # 3. Active Medications
        elements.append(Paragraph("Current Active Medications", section_style))
        meds = family_member.medicines.filter(status='ACTIVE')
        if meds.exists():
            m_data = [["Medicine", "Dosage", "Instructions", "Prescribed By"]]
            for m in meds:
                m_data.append([m.name, m.dosage, m.get_instructions_display(), m.prescribed_by or "OTC"])
            t_m = Table(m_data, colWidths=[150, 100, 170, 120])
            t_m.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#e2e8f0')),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 8),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cbd5e1')),
            ]))
            elements.append(t_m)

        doc.build(elements)
        buffer.seek(0)
        return buffer.getvalue()

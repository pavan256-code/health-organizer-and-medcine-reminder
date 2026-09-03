# Medicine Reminder & Health Organizer - User Manual

Welcome to the **Medicine Reminder & Health Organizer**. This comprehensive guide walks you through every feature and workflow in the application.

---

## 1. Getting Started & Authentication

### Logging In
1. Open your browser and navigate to `http://127.0.0.1:8000/`.
2. Click **Sign In** on the top navigation bar.
3. Enter your credentials:
   - Default Demo User: `demo` / `DemoPass123!`
   - Or register a new account using the **Create Account** button.

### Switching Active Patients
At the top of the sidebar or dashboard header, locate the **Patient Switcher**:
- Click the patient avatar/name.
- Select the family member (e.g. John, Sarah, Tommy, or Eleanor).
- The entire application (medicines, vitals, appointments, and diet) will immediately filter to that person's dossier.

---

## 2. Managing Medications & Daily Doses

### Adding a Medication
1. Navigate to **Medicines** in the sidebar.
2. Click **➕ Add Medication**.
3. Fill in the commercial name (e.g., *Atorvastatin*), generic molecule (*Atorvastatin Calcium*), formulation (*Tablet*), strength (*20mg*), and dietary timing (*At Bedtime*).
4. Enter initial quantity on hand (e.g. 30 tablets) and minimum alert threshold (e.g. 7 tablets).
5. Click **Save & Continue**.

### Configuring a Dosing Routine
1. On the medicine's detail page, click **+ Dosing Schedule**.
2. Select frequency (e.g., *Daily*, *Twice a Day*, or *Custom Days*).
3. Enter the scheduled reminder times in 24-hour format (e.g., `08:00, 20:00`).
4. Click **Save Dosing Routine**. Daily dose slots are automatically provisioned.

### Recording Doses (Taken, Skipped, Snoozed)
From the **Dashboard** or **Dosing Routine** view:
- **Mark Taken**: Click the green **✓ Taken** button. The dose timestamp is recorded, inventory stock is decremented by 1, and your adherence rate rises.
- **Skip Dose**: Click **Skip**. Select a clinical reason (e.g., *Side effects*, *Doctor advised*, or *Fasting*) to maintain an accurate medical record.
- **Snooze**: Click **Snooze** to defer the reminder alert by 15 or 30 minutes.

### Managing Inventory & Refills
1. Go to **Inventory / Stock** in the sidebar.
2. Low stock items are highlighted with an amber/red alert tag.
3. Click **+ Log Refill** on any medicine.
4. Enter quantity purchased, purchase date, cost, and pharmacy. The inventory count is instantly updated.

---

## 3. Medical Records, Appointments & Vitals

### Recording Daily Vitals
1. Click **Vitals & Metrics** in the sidebar.
2. Click **➕ Record Measurement**.
3. Enter blood pressure (Systolic / Diastolic), resting heart rate, fasting glucose, or weight.
4. Click **Save Vital Signs**. BMI is calculated automatically.
5. Click **📈 Interactive Trends** to view canvas-based graphs of your historical readings.

### Booking Clinical Appointments
1. Navigate to **Appointments**.
2. Click **➕ Schedule Visit**.
3. Select the patient, consulting physician, visit date, and clinic location.
4. When the visit is finished, click **✓** to mark it as completed.

### Medical Document Vault
1. Navigate to **Document Vault**.
2. Click **➕ Upload Document**.
3. Choose category (e.g., *Blood Report*, *Scan*, or *Prescription*), select your PDF or image, and submit.
4. To view or retrieve files, click **⬇️ Download** for secure local streaming.

---

## 4. Lifestyle & Wellness Tracking

- **Diet & Hydration**: Track meals and tap **+250ml Glass** to record water intake.
- **Fitness & Workouts**: Log running, walking, cycling, or strength exercises with duration and distance.
- **Sleep Continuity**: Record bedtimes, waking times, and sleep quality ratings.
- **Health Goals**: Establish target step counts, weight goals, or water targets and update progress.

---

## 5. Reports, Emergency Card & Drug Interactions

- **Printable Emergency Card**: Click **Emergency Card** in the sidebar. Print a wallet-sized ID sheet with blood group, allergies, medications, and emergency contacts.
- **Drug Interaction Checker**: Screen your current active medicines for dangerous drug-drug interactions or cross-check any two pharmaceutical substances locally.
- **PDF & CSV Reports**: Go to **Reports & Exports** to download official PDF Medication Regimens or export CSV logs.

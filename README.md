# Medicine Reminder & Health Organizer (MRHO)

> **A Complete, Professional, Production-Style Web Application Built in Python 3.12 & Django 5.x**

---

## 🌟 Executive Overview

**Medicine Reminder & Health Organizer** is a fully self-contained, privacy-first healthcare management platform engineered strictly for local execution. It delivers end-to-end clinical workflows for individuals and multi-generational families without relying on external cloud APIs, third-party analytics, cloud storage, or external SaaS dependencies.

The system manages the complete lifecycle of chronic and acute medication regimens, prescription digitization, physiological vitals tracking, symptom journals, immunization records, dietary nutrition, fitness activities, sleep continuity, and automated local clinical heuristics.

---

## 🚀 Key Highlights & Architecture

- **100% Self-Contained Local Execution**: Zero external API dependencies, no cloud tracking, no third-party CDN requirements.
- **Multi-Patient Family Care**: Unified account model supporting multiple family members (Self, Spouse, Children, Elderly Parents) with seamless active patient switching.
- **Precision Dosing & Adherence Engine**: Deterministic dose generation, time-window evaluation, stock depletion upon dose confirmation, snooze mechanics, and adherence percentages.
- **Interactive Local Data Visualizations**: Canvas-based SVG/HTML5 charts for blood pressure, fasting glucose, and weight trends without external charting libraries.
- **Printable Clinical Reports & PDFs**: Built-in ReportLab integration producing physician-ready Medication Regimens and Doctor Briefs.
- **Enterprise Security & Audit Logging**: Session inactivity timeouts, lockout brute-force defense, state-changing audit middleware, and file mime-type validation.

---

## 🛠️ Technology Stack

| Layer | Technology / Framework |
|---|---|
| **Language** | Python 3.12+ |
| **Backend Framework** | Django 5.x (MTV Architecture) |
| **Database** | SQLite3 (Configured with WAL Mode, Foreign Keys ON, busy_timeout=5000) |
| **Frontend Styling** | Custom Vanilla CSS Design System (Light & Dark Themes, Responsive Grid) |
| **Frontend Scripting** | Vanilla JavaScript (ES6+), Local Canvas Charting, Web Audio Chimes |
| **Document Generation** | ReportLab 5.x (Offline Vector PDF Compilation) |
| **Data Export** | Python Standard CSV Stream Engine |

---

## ⚡ Quick Start & Installation

### 1. Clone or Open the Workspace
Ensure you are in the project root directory containing `manage.py`:
```bash
cd "c:\Users\pawan kalyan\OneDrive\Desktop\hospital management"
```

### 2. Environment Verification
Verify Python 3.12+ and Django are installed:
```bash
python --version
python -m django --version
```

### 3. Database Migration
Apply all database schemas and tables:
```bash
python manage.py migrate
```

### 4. Seed Complete Demo Universe
Seed realistic multi-generational clinical data (patients, doctors, prescriptions, active medications, vitals, appointments, and logs):
```bash
python manage.py seed_demo_data
```

### 5. Run the Local Development Server
```bash
python manage.py runserver
```
Navigate your browser to: **`http://127.0.0.1:8000/`**

---

## 🔐 Default Credentials

| Role | Username | Password | Purpose |
|---|---|---|---|
| **Primary Patient** | `demo` | `DemoPass123!` | Complete family patient dataset, chronic medications, vitals history, and reminders |
| **System Administrator** | `admin` | `AdminPass123!` | Superuser privileges, administrative console, and full Django admin access |

---

## 🧪 Running the Comprehensive Test Suite

To run all automated unit and integration tests across all modules:
```bash
python manage.py test apps.accounts apps.family apps.core apps.audit apps.notifications apps.medications apps.medical apps.wellness
```

---

## 📁 Project Structure

```
hospital management/
├── manage.py
├── config/                  # Project configuration & settings
│   ├── settings.py          # SQLite WAL, security, sessions, apps
│   ├── urls.py              # Root URL router
│   ├── wsgi.py / asgi.py
├── apps/
│   ├── core/                # Base models, landing pages, error handlers, seeder
│   ├── accounts/            # Custom User model, profile, lockout, session tracking
│   ├── family/              # Multi-member patient switcher, dossier views
│   ├── medications/         # Catalog, schedules, doses, stock, refills, expiry
│   ├── medical/             # Doctors, appointments, prescriptions, vitals, symptoms, vaccines, vault
│   ├── wellness/            # Diet, hydration, workouts, sleep journal, goals
│   ├── calendar_app/        # Unified health calendar
│   ├── analytics/           # Rule-based health insight heuristics & dynamic scoring
│   ├── reports/             # ReportLab PDF generation and CSV exports
│   ├── emergency/           # Emergency medical ID card & local drug interaction checker
│   ├── audit/               # Security and state-changing request audit logs
│   ├── notifications/       # In-app notification center & sound chimes
│   ├── backups/             # Local database backup & snapshot manager
│   └── administration/      # Administrative telemetry dashboard
├── static/
│   ├── css/                 # base.css, layout.css, components.css, dashboard.css
│   └── js/                  # main.js, notifications.js, charts.js
├── templates/               # Modular Django templates across all domains
└── docs/                    # Architectural, Database, and User Guide manuals
```

---

## 📜 License & Compliance

**Proprietary Software**. All rights reserved. 
This application is strictly proprietary and closed-source. No license is granted for public distribution, replication, or open-source sublicensing. Developed for private, offline, self-hosted operational healthcare and patient safety surveillance.

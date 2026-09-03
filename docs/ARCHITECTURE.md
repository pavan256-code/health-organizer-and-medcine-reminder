# System Architecture & Technical Specifications

## 1. Architectural Philosophy

The **Medicine Reminder & Health Organizer** web application is built on the classical, battle-tested Django Model-Template-View (MTV) pattern, augmented with a distinct service layer for complex domain workflows (dose generation, adherence calculation, PDF compilation, and drug interaction heuristic evaluation).

### Key Design Tenets:
1. **Air-Gapped Privacy**: Zero communication with external cloud endpoints. All data processing (analytics, charting, PDF compiling, notifications) executes locally.
2. **Domain Separation**: Functionality is modularized into 13 distinct Django apps under `apps/` with clean boundaries.
3. **Auditability & Traceability**: Every state-changing HTTP request (POST/DELETE) is captured in an immutable audit ledger (`apps.audit`).
4. **Idempotency**: Dosing schedules and lot alerts can be re-evaluated repeatedly without spawning duplicate records.

---

## 2. Component Diagram

```
+-------------------------------------------------------------------------+
|                              Browser UI                                 |
|      (HTML5 Semantic Templates, Vanilla CSS Design System, Vanilla JS)  |
+------------------------------------+------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|                           Django HTTP Stack                             |
|  - SessionTimeoutMiddleware (enforcing auto-logout per user profile)    |
|  - AuditLoggingMiddleware (capturing state-changing mutations)          |
|  - active_family_member context processor (patient context switching)   |
+------------------------------------+------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|                             View Layer                                  |
|  (Class-Based Views: ListView, DetailView, CreateView, UpdateView)      |
+------------------------------------+------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|                            Service Layer                                |
|  - MedicationSchedulerService (deterministic dose generation)           |
|  - MedicationAdherenceService (compliance analytics & metrics)          |
|  - HealthInsightEngine (rule-based clinical heuristics)                 |
|  - DrugInteractionEngine (local pair screening)                         |
|  - PDFReportService (ReportLab document compilation)                    |
|  - CSVReportService (tabular data streaming)                            |
+------------------------------------+------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|                        Data Layer (Django ORM)                          |
|  - SQLite3 with Write-Ahead Logging (WAL) & Foreign Keys                |
|  - Abstract models: TimeStampedModel, UUIDModel, SoftDeleteModel        |
+-------------------------------------------------------------------------+
```

---

## 3. Core Domain Flows

### 3.1 Medication Dosing & Adherence Lifecycle
1. **Cataloging**: A medicine is registered under a family member profile with formulation, strength, unit, and dietary instruction (e.g. `After Food`).
2. **Scheduling**: A `MedicineSchedule` is linked with frequency (`DAILY`, `TWICE_DAILY`, `WEEKLY`, `CUSTOM`) and explicit time strings (`['08:00', '20:00']`).
3. **Generation**: `MedicationSchedulerService.generate_doses_for_window()` provisions concrete `MedicineDose` records idempotently.
4. **Administration**:
   - **Taken**: Dose marked as `TAKEN`, `actual_time` stamped, stock decremented by 1, `MedicationLog` entry created, `AuditLog` stamped.
   - **Skipped**: Dose marked as `SKIPPED`, clinical reason recorded, `MedicationLog` entry created.
   - **Snoozed**: Reminder deferred by X minutes.
5. **Adherence Computation**: Evaluates $\text{Adherence Rate} = \frac{\text{Taken} + \text{Delayed}}{\text{Evaluated Doses}} \times 100\%$.

### 3.2 Patient Switching Mechanism
- The user's active patient context is persisted in `request.session['active_family_member_id']`.
- The `active_family_member` context processor injects the currently selected `FamilyMember` object into all templates and request pipelines.
- Switching patient instantly scopes medicines, vitals, appointments, and diet overview to the chosen individual.

### 3.3 Offline Document & File Security
- Uploaded medical documents (lab panels, scan reports) are validated for file extension and MIME types.
- Files are served strictly through an authenticated streaming view (`DocumentDownloadView`) ensuring users cannot access documents outside their authorized family tree.

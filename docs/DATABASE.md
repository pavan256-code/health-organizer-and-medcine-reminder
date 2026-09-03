# Database Schema & Data Dictionary

## 1. Relational Database Overview

The platform uses SQLite configured with enterprise-grade parameters:
- `PRAGMA journal_mode=WAL;` (High concurrent read/write concurrency)
- `PRAGMA synchronous=NORMAL;` (Optimal durability and write throughput)
- `PRAGMA foreign_keys=ON;` (Referential integrity enforcement)
- `PRAGMA busy_timeout=5000;` (5-second lock timeout prevention)

---

## 2. Entity Relationship Overview

```
                      +-------------------+
                      |   accounts.User   |
                      +---------+---------+
                                | 1
                                |
                                | *
                      +---------v---------+
                      |   FamilyMember    |
                      +----+----+----+----+
                           |    |    |
           +---------------+    |    +----------------+
           | 1                  | 1                   | 1
           |                    |                     |
           | *                  | *                   | *
+----------v---------+  +-------v---------+  +--------v--------+
|      Medicine      |  |   VitalRecord   |  |   Appointment   |
+----------+---------+  +-----------------+  +--------+--------+
           | 1                                        | *
           |                                          |
           | *                                        | 1
+----------v---------+                       +--------v--------+
|  MedicineSchedule  |                       |     Doctor      |
+----------+---------+                       +-----------------+
           | 1
           |
           | *
+----------v---------+
|    MedicineDose    |
+--------------------+
```

---

## 3. Core Models Specification

### 3.1 `accounts.User` & `accounts.UserProfile`
- Custom `User` model inheriting from `AbstractUser`.
- Unique `email` as secondary identifier, `failed_login_attempts` counter, and `lockout_until` timestamp.
- `UserProfile` captures demographic info, theme preferences, and session inactivity timeout thresholds.

### 3.2 `family.FamilyMember`
- Fields: `user`, `first_name`, `last_name`, `relationship`, `date_of_birth`, `gender`, `blood_group`, `emergency_contact`, `is_active`.
- Represents the individual patient receiving care.

### 3.3 `medications.Medicine`
- Fields: `user`, `family_member`, `name`, `generic_name`, `brand_name`, `medicine_type`, `dosage`, `strength`, `unit`, `instructions`, `start_date`, `end_date`, `prescribed_by`, `status`, `notes`.
- Indexed on `(user, status)` and `(family_member, status)`.

### 3.4 `medications.MedicineSchedule`
- Recurrence configuration: `frequency` (`DAILY`, `TWICE_DAILY`, `WEEKLY`, `CUSTOM`), `specific_times` (JSON array of `HH:MM` strings), `days_of_week` (JSON array of integer weekdays).

### 3.5 `medications.MedicineDose`
- Concrete scheduled dose: `schedule`, `date`, `scheduled_time`, `actual_time`, `status` (`PENDING`, `TAKEN`, `SKIPPED`, `MISSED`, `DELAYED`, `SNOOZED`), `snooze_until`.
- Unique constraint on `(schedule, date, scheduled_time)`.

### 3.6 `medications.MedicineStock` & `MedicineRefill`
- `MedicineStock`: `current_stock`, `initial_quantity`, `consumed_quantity`, `minimum_stock_level`, `unit`.
- `MedicineRefill`: logs purchases with `refill_quantity`, `refill_date`, `cost`, `pharmacy_source`. Automatically increments `current_stock` upon addition.

### 3.7 `medications.MedicineExpiry`
- Batch lot surveillance: `batch_number`, `expiry_date`, `alert_days_before`, `status` (`SAFE`, `EXPIRING_SOON`, `EXPIRED`).

### 3.8 `medical.VitalRecord`
- Physiological quantitative metrics: `blood_pressure_systolic`, `blood_pressure_diastolic`, `blood_sugar_fasting`, `blood_sugar_postprandial`, `heart_rate`, `oxygen_saturation`, `temperature_c`, `weight_kg`, `height_cm`, `bmi`. Automatically computes BMI on save.

### 3.9 `medical.MedicalDocument`
- Local document storage: `title`, `category` (`PRESCRIPTION`, `LAB_REPORT`, `SCAN_REPORT`, etc.), `file`, `file_size`, `file_type`, `document_date`.

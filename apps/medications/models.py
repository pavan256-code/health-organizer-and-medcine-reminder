"""
Models for Medication Management: Medicines, Schedules, Doses, Logs, Stock, Refills, and Expiry.
"""

from django.db import models
from django.conf import settings
from django.utils import timezone
from apps.core.models import TimeStampedModel
from apps.family.models import FamilyMember


class Medicine(TimeStampedModel):
    """
    Core pharmaceutical or OTC medicine record associated with a user and family member.
    """
    TYPE_TABLET = 'TABLET'
    TYPE_CAPSULE = 'CAPSULE'
    TYPE_SYRUP = 'SYRUP'
    TYPE_INJECTION = 'INJECTION'
    TYPE_CREAM = 'CREAM'
    TYPE_DROPS = 'DROPS'
    TYPE_POWDER = 'POWDER'
    TYPE_INHALER = 'INHALER'
    TYPE_OTHER = 'OTHER'

    TYPE_CHOICES = [
        (TYPE_TABLET, 'Tablet'),
        (TYPE_CAPSULE, 'Capsule'),
        (TYPE_SYRUP, 'Syrup / Liquid Suspension'),
        (TYPE_INJECTION, 'Injection'),
        (TYPE_CREAM, 'Topical Cream / Ointment'),
        (TYPE_DROPS, 'Drops (Eye / Ear / Nasal)'),
        (TYPE_POWDER, 'Powder / Sachet'),
        (TYPE_INHALER, 'Inhaler / Respules'),
        (TYPE_OTHER, 'Other Formulation'),
    ]

    INSTRUCTION_BEFORE_FOOD = 'BEFORE_FOOD'
    INSTRUCTION_AFTER_FOOD = 'AFTER_FOOD'
    INSTRUCTION_WITH_FOOD = 'WITH_FOOD'
    INSTRUCTION_EMPTY_STOMACH = 'EMPTY_STOMACH'
    INSTRUCTION_BEDTIME = 'BEDTIME'
    INSTRUCTION_AS_NEEDED = 'AS_NEEDED'

    INSTRUCTION_CHOICES = [
        (INSTRUCTION_BEFORE_FOOD, 'Before Food (30 mins prior)'),
        (INSTRUCTION_AFTER_FOOD, 'After Food (with water)'),
        (INSTRUCTION_WITH_FOOD, 'With Food / Meal'),
        (INSTRUCTION_EMPTY_STOMACH, 'On an Empty Stomach'),
        (INSTRUCTION_BEDTIME, 'At Bedtime'),
        (INSTRUCTION_AS_NEEDED, 'As Needed (SOS / PRN)'),
    ]

    STATUS_ACTIVE = 'ACTIVE'
    STATUS_INACTIVE = 'INACTIVE'
    STATUS_COMPLETED = 'COMPLETED'
    STATUS_DISCONTINUED = 'DISCONTINUED'

    STATUS_CHOICES = [
        (STATUS_ACTIVE, 'Active Prescribed'),
        (STATUS_INACTIVE, 'Inactive / Paused'),
        (STATUS_COMPLETED, 'Course Completed'),
        (STATUS_DISCONTINUED, 'Discontinued by Doctor'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='medicines'
    )
    family_member = models.ForeignKey(
        FamilyMember,
        on_delete=models.CASCADE,
        related_name='medicines'
    )
    name = models.CharField(max_length=150, help_text="Brand or Commercial Name (e.g., Lipitor)")
    generic_name = models.CharField(max_length=150, blank=True, default='', help_text="Active Pharmaceutical Ingredient (e.g., Atorvastatin)")
    brand_name = models.CharField(max_length=150, blank=True, default='')
    medicine_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default=TYPE_TABLET)
    dosage = models.CharField(max_length=100, help_text="e.g., 1 tablet, 5ml, 2 puffs")
    strength = models.CharField(max_length=50, blank=True, default='', help_text="e.g., 500, 20, 10")
    unit = models.CharField(max_length=20, default='mg', help_text="e.g., mg, mcg, ml, IU")
    instructions = models.CharField(max_length=30, choices=INSTRUCTION_CHOICES, default=INSTRUCTION_AFTER_FOOD)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(null=True, blank=True, help_text="Leave blank for ongoing/chronic regimens")
    prescribed_by = models.CharField(max_length=150, blank=True, default='', help_text="Doctor or Clinic name")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_ACTIVE, db_index=True)
    notes = models.TextField(blank=True, default='')

    class Meta:
        verbose_name = 'Medicine'
        verbose_name_plural = 'Medicines'
        ordering = ['status', 'name']
        indexes = [
            models.Index(fields=['user', 'status']),
            models.Index(fields=['family_member', 'status']),
        ]

    def __str__(self):
        return f"{self.name} ({self.dosage}) - {self.family_member.full_name}"

    @property
    def is_chronic(self):
        return self.end_date is None


class MedicineSchedule(TimeStampedModel):
    """
    Defines recurrence patterns, frequencies, and specific times of day for a medicine.
    """
    FREQ_ONCE = 'ONCE'
    FREQ_DAILY = 'DAILY'
    FREQ_TWICE_DAILY = 'TWICE_DAILY'
    FREQ_THREE_TIMES_DAILY = 'THREE_TIMES_DAILY'
    FREQ_FOUR_TIMES_DAILY = 'FOUR_TIMES_DAILY'
    FREQ_WEEKLY = 'WEEKLY'
    FREQ_AS_NEEDED = 'AS_NEEDED'
    FREQ_CUSTOM = 'CUSTOM'

    FREQUENCY_CHOICES = [
        (FREQ_ONCE, 'Once (Single dose)'),
        (FREQ_DAILY, 'Daily (Once a day)'),
        (FREQ_TWICE_DAILY, 'Twice a Day (Morning & Evening)'),
        (FREQ_THREE_TIMES_DAILY, 'Three Times a Day (Morning, Noon, Night)'),
        (FREQ_FOUR_TIMES_DAILY, 'Four Times a Day (Every 6 hours)'),
        (FREQ_WEEKLY, 'Weekly (Specific Day)'),
        (FREQ_AS_NEEDED, 'As Needed (PRN)'),
        (FREQ_CUSTOM, 'Custom Schedule / Selected Days'),
    ]

    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='schedules')
    frequency = models.CharField(max_length=30, choices=FREQUENCY_CHOICES, default=FREQ_DAILY)
    specific_times = models.JSONField(
        default=list,
        help_text="List of time strings in HH:MM format, e.g., ['08:00', '20:00']"
    )
    days_of_week = models.JSONField(
        default=list,
        blank=True,
        help_text="List of weekday integers (0=Mon, 6=Sun), e.g. [0, 2, 4]"
    )
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True, db_index=True)

    class Meta:
        verbose_name = 'Medicine Schedule'
        verbose_name_plural = 'Medicine Schedules'
        ordering = ['medicine', '-created_at']

    def __str__(self):
        times_str = ", ".join(self.specific_times) if self.specific_times else "No times"
        return f"{self.medicine.name} [{self.get_frequency_display()} @ {times_str}]"


class MedicineDose(TimeStampedModel):
    """
    Concrete scheduled dose instance for a specific calendar date and time.
    """
    STATUS_PENDING = 'PENDING'
    STATUS_TAKEN = 'TAKEN'
    STATUS_SKIPPED = 'SKIPPED'
    STATUS_MISSED = 'MISSED'
    STATUS_DELAYED = 'DELAYED'
    STATUS_SNOOZED = 'SNOOZED'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_TAKEN, 'Taken'),
        (STATUS_SKIPPED, 'Skipped'),
        (STATUS_MISSED, 'Missed / Overdue'),
        (STATUS_DELAYED, 'Taken Late / Delayed'),
        (STATUS_SNOOZED, 'Snoozed'),
    ]

    schedule = models.ForeignKey(MedicineSchedule, on_delete=models.CASCADE, related_name='doses')
    date = models.DateField(db_index=True)
    scheduled_time = models.TimeField()
    actual_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=STATUS_PENDING, db_index=True)
    snooze_until = models.DateTimeField(null=True, blank=True)
    notes = models.CharField(max_length=255, blank=True, default='')

    class Meta:
        verbose_name = 'Medicine Dose'
        verbose_name_plural = 'Medicine Doses'
        ordering = ['date', 'scheduled_time']
        unique_together = ('schedule', 'date', 'scheduled_time')
        indexes = [
            models.Index(fields=['date', 'status']),
            models.Index(fields=['schedule', 'date']),
        ]

    def __str__(self):
        return f"{self.schedule.medicine.name} on {self.date} at {self.scheduled_time} ({self.status})"

    def mark_as_taken(self, actual_dt=None):
        """Mark dose as taken and record timestamp."""
        now = actual_dt or timezone.now()
        self.status = self.STATUS_TAKEN
        self.actual_time = now
        self.save(update_fields=['status', 'actual_time', 'updated_at'])

    def mark_as_skipped(self, reason=''):
        """Mark dose as skipped with a clinical reason."""
        self.status = self.STATUS_SKIPPED
        self.notes = reason
        self.save(update_fields=['status', 'notes', 'updated_at'])

    def snooze(self, minutes=15):
        """Snooze reminder by specified minutes."""
        self.status = self.STATUS_SNOOZED
        self.snooze_until = timezone.now() + timezone.timedelta(minutes=minutes)
        self.save(update_fields=['status', 'snooze_until', 'updated_at'])


class MedicationLog(TimeStampedModel):
    """
    Permanent clinical audit log of all dose actions taken, skipped, or missed.
    """
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='logs')
    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE, related_name='medication_logs')
    dose = models.ForeignKey(MedicineDose, on_delete=models.SET_NULL, null=True, blank=True, related_name='audit_logs')
    scheduled_time = models.DateTimeField(default=timezone.now)
    actual_time = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=MedicineDose.STATUS_CHOICES)
    reason_for_skip = models.CharField(max_length=255, blank=True, default='')
    notes = models.TextField(blank=True, default='')
    logged_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Medication Log'
        verbose_name_plural = 'Medication Logs'
        ordering = ['-actual_time']
        indexes = [
            models.Index(fields=['family_member', 'actual_time']),
            models.Index(fields=['medicine', 'status']),
        ]

    def __str__(self):
        return f"{self.medicine.name} - {self.status} at {self.actual_time.strftime('%Y-%m-%d %H:%M')}"


class MedicineStock(TimeStampedModel):
    """
    Inventory tracker monitoring quantities on hand, consumption, and minimum thresholds.
    """
    medicine = models.OneToOneField(Medicine, on_delete=models.CASCADE, related_name='stock')
    current_stock = models.IntegerField(default=30)
    initial_quantity = models.IntegerField(default=30)
    consumed_quantity = models.IntegerField(default=0)
    minimum_stock_level = models.IntegerField(default=5, help_text="Alert triggered when stock falls to or below this")
    refill_reminder_days = models.IntegerField(default=7, help_text="Days of supply left before alert")
    unit = models.CharField(max_length=20, default='tablets')

    class Meta:
        verbose_name = 'Medicine Stock'
        verbose_name_plural = 'Medicine Stocks'

    def __str__(self):
        return f"{self.medicine.name}: {self.current_stock} {self.unit} remaining"

    def is_low_stock(self):
        return self.current_stock <= self.minimum_stock_level

    def decrement(self, amount=1):
        """Decrements stock and increments consumed count upon dose taking."""
        self.current_stock = max(0, self.current_stock - amount)
        self.consumed_quantity += amount
        self.save(update_fields=['current_stock', 'consumed_quantity', 'updated_at'])


class MedicineRefill(TimeStampedModel):
    """
    Records of inventory refills, purchases, pharmacy sources, and costs.
    """
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='refills')
    refill_date = models.DateField(default=timezone.now)
    refill_quantity = models.PositiveIntegerField(default=30)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pharmacy_source = models.CharField(max_length=150, blank=True, default='')
    notes = models.TextField(blank=True, default='')

    class Meta:
        verbose_name = 'Medicine Refill'
        verbose_name_plural = 'Medicine Refills'
        ordering = ['-refill_date']

    def __str__(self):
        return f"+{self.refill_quantity} for {self.medicine.name} on {self.refill_date}"

    def save(self, *args, **kwargs):
        is_new = self._state.adding
        super().save(*args, **kwargs)
        if is_new and hasattr(self.medicine, 'stock'):
            stock = self.medicine.stock
            stock.current_stock += self.refill_quantity
            stock.save(update_fields=['current_stock', 'updated_at'])


class MedicineExpiry(TimeStampedModel):
    """
    Monitors batch lot numbers and pharmaceutical expiration dates.
    """
    STATUS_SAFE = 'SAFE'
    STATUS_EXPIRING_SOON = 'EXPIRING_SOON'
    STATUS_EXPIRED = 'EXPIRED'

    STATUS_CHOICES = [
        (STATUS_SAFE, 'Safe / Unexpired'),
        (STATUS_EXPIRING_SOON, 'Expiring Soon (<= 30 Days)'),
        (STATUS_EXPIRED, 'Expired - Do Not Use'),
    ]

    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name='expiry_batches')
    batch_number = models.CharField(max_length=50, blank=True, default='LOT-01')
    expiry_date = models.DateField()
    alert_days_before = models.PositiveIntegerField(default=30)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_SAFE, db_index=True)
    notes = models.CharField(max_length=255, blank=True, default='')

    class Meta:
        verbose_name = 'Medicine Expiry Batch'
        verbose_name_plural = 'Medicine Expiry Batches'
        ordering = ['expiry_date']

    def __str__(self):
        return f"{self.medicine.name} (Batch {self.batch_number}) Exp: {self.expiry_date}"

    @property
    def days_remaining(self):
        today = timezone.now().date()
        return (self.expiry_date - today).days

    def update_status(self):
        today = timezone.now().date()
        days_left = (self.expiry_date - today).days
        if days_left < 0:
            new_status = self.STATUS_EXPIRED
        elif days_left <= self.alert_days_before:
            new_status = self.STATUS_EXPIRING_SOON
        else:
            new_status = self.STATUS_SAFE

        if self.status != new_status:
            self.status = new_status
            self.save(update_fields=['status', 'updated_at'])
        return self.status

"""
Notification models for alerts, reminders, and health insights.
"""

from django.db import models
from django.conf import settings
from django.utils import timezone
from apps.core.models import TimeStampedModel
from apps.family.models import FamilyMember


class Notification(TimeStampedModel):
    """
    In-app notification entity supporting priority levels and direct link routing.
    """
    CATEGORY_MEDICINE = 'MEDICINE'
    CATEGORY_REFILL = 'REFILL'
    CATEGORY_EXPIRY = 'EXPIRY'
    CATEGORY_APPOINTMENT = 'APPOINTMENT'
    CATEGORY_GOAL = 'GOAL'
    CATEGORY_INSIGHT = 'INSIGHT'
    CATEGORY_GENERAL = 'GENERAL'

    CATEGORY_CHOICES = [
        (CATEGORY_MEDICINE, 'Medicine Reminder'),
        (CATEGORY_REFILL, 'Refill Alert'),
        (CATEGORY_EXPIRY, 'Expiry Alert'),
        (CATEGORY_APPOINTMENT, 'Appointment Alert'),
        (CATEGORY_GOAL, 'Health Goal Alert'),
        (CATEGORY_INSIGHT, 'Health Insight'),
        (CATEGORY_GENERAL, 'General Notification'),
    ]

    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('URGENT', 'Urgent'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notifications'
    )
    family_member = models.ForeignKey(
        FamilyMember,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='notifications'
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=CATEGORY_GENERAL, db_index=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='MEDIUM', db_index=True)
    title = models.CharField(max_length=200)
    message = models.TextField()
    action_url = models.CharField(max_length=255, blank=True, default='')
    is_read = models.BooleanField(default=False, db_index=True)
    read_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', 'is_read', '-created_at']),
        ]

    def __str__(self):
        return f"[{self.category}] {self.title} ({'Read' if self.is_read else 'Unread'})"

    def mark_as_read(self):
        if not self.is_read:
            self.is_read = True
            self.read_at = timezone.now()
            self.save(update_fields=['is_read', 'read_at'])

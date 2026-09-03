"""
Core abstract models, mixins, and system entities.
"""

import uuid
from django.db import models
from django.utils import timezone
from django.conf import settings


class TimeStampedModel(models.Model):
    """
    Abstract base model that provides self-updating
    created_at and updated_at timestamp fields.
    """
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']


class UUIDModel(models.Model):
    """
    Abstract model with a universally unique identifier (UUID) primary key.
    Useful for publicly referenced or sensitive medical objects.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']


class SoftDeleteModel(TimeStampedModel):
    """
    Abstract base model that supports soft deletion of records
    to prevent accidental permanent deletion of patient health histories.
    """
    is_deleted = models.BooleanField(default=False, db_index=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def soft_delete(self):
        """Mark the instance as deleted with current timestamp."""
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save(update_fields=['is_deleted', 'deleted_at'])

    def restore(self):
        """Restore a soft-deleted instance."""
        self.is_deleted = False
        self.deleted_at = None
        self.save(update_fields=['is_deleted', 'deleted_at'])


class SystemNotice(TimeStampedModel):
    """
    System-wide announcements or health advisories broadcasted locally.
    """
    NOTICE_TYPES = [
        ('info', 'Information'),
        ('warning', 'Advisory Warning'),
        ('maintenance', 'System Notice'),
        ('health_tip', 'Health & Wellness Tip'),
    ]

    title = models.CharField(max_length=200)
    message = models.TextField()
    notice_type = models.CharField(max_length=20, choices=NOTICE_TYPES, default='info')
    is_active = models.BooleanField(default=True, db_index=True)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(null=True, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='created_notices'
    )

    class Meta:
        verbose_name = 'System Notice'
        verbose_name_plural = 'System Notices'
        ordering = ['-created_at']

    def __str__(self):
        return f"[{self.get_notice_type_display()}] {self.title}"


class ContactInquiry(TimeStampedModel):
    """
    Stores contact form submissions locally without requiring external email SMTP/APIs.
    """
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    is_resolved = models.BooleanField(default=False, db_index=True)
    admin_notes = models.TextField(blank=True, default='')

    class Meta:
        verbose_name = 'Contact Inquiry'
        verbose_name_plural = 'Contact Inquiries'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject} ({self.created_at.strftime('%Y-%m-%d')})"

"""
Audit log models for tracking all system activity, healthcare modifications, and security events.
"""

from django.db import models
from django.conf import settings
from django.utils import timezone


class AuditLog(models.Model):
    """
    Immutable audit log entry recording all security-relevant and clinical mutations.
    """
    ACTION_CHOICES = [
        ('LOGIN', 'User Login'),
        ('LOGOUT', 'User Logout'),
        ('FAILED_LOGIN', 'Failed Login Attempt'),
        ('CREATE', 'Record Created'),
        ('UPDATE', 'Record Updated'),
        ('DELETE', 'Record Deleted'),
        ('VIEW', 'Sensitive Record Accessed'),
        ('EXPORT', 'Data Exported'),
        ('BACKUP', 'System Backup Created'),
        ('RESTORE', 'System Backup Restored'),
        ('PASSWORD_CHANGE', 'Password Changed'),
        ('SETTINGS_CHANGE', 'System Settings Modified'),
    ]

    MODULE_CHOICES = [
        ('AUTH', 'Authentication & Access'),
        ('FAMILY', 'Family Members'),
        ('MEDICATION', 'Medications & Prescriptions'),
        ('MEDICAL', 'Medical Records & Clinical Data'),
        ('WELLNESS', 'Lifestyle & Wellness'),
        ('ANALYTICS', 'Intelligence & Reports'),
        ('SYSTEM', 'System Administration'),
        ('EMERGENCY', 'Emergency & Caregivers'),
    ]

    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='audit_logs'
    )
    action = models.CharField(max_length=30, choices=ACTION_CHOICES, db_index=True)
    module = models.CharField(max_length=30, choices=MODULE_CHOICES, db_index=True)
    object_repr = models.CharField(max_length=255, blank=True, default='')
    object_id = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True, default='')
    is_security_event = models.BooleanField(default=False, db_index=True)
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        verbose_name = 'Audit Log'
        verbose_name_plural = 'Audit Logs'
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['module', 'action']),
            models.Index(fields=['user', 'timestamp']),
        ]

    def __str__(self):
        user_str = self.user.username if self.user else "Anonymous/System"
        return f"[{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}] {user_str} - {self.action} on {self.module}"

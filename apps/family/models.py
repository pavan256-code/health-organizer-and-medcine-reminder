"""
Family member patient models.
"""

from django.db import models
from django.conf import settings
from django.utils import timezone
from apps.core.models import TimeStampedModel


class FamilyMember(TimeStampedModel):
    """
    Patient identity representing either the primary account holder ('SELF')
    or dependants/relatives under their medical care.
    """
    RELATIONSHIP_CHOICES = [
        ('SELF', 'Self (Primary User)'),
        ('FATHER', 'Father'),
        ('MOTHER', 'Mother'),
        ('SPOUSE', 'Spouse'),
        ('SON', 'Son'),
        ('DAUGHTER', 'Daughter'),
        ('BROTHER', 'Brother'),
        ('SISTER', 'Sister'),
        ('GRANDFATHER', 'Grandfather'),
        ('GRANDMOTHER', 'Grandmother'),
        ('OTHER', 'Other Relative/Dependent'),
    ]

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    BLOOD_GROUP_CHOICES = [
        ('A+', 'A Positive (A+)'),
        ('A-', 'A Negative (A-)'),
        ('B+', 'B Positive (B+)'),
        ('B-', 'B Negative (B-)'),
        ('AB+', 'AB Positive (AB+)'),
        ('AB-', 'AB Negative (AB-)'),
        ('O+', 'O Positive (O+)'),
        ('O-', 'O Negative (O-)'),
        ('UNKNOWN', 'Unknown'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='family_members'
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, default='')
    relationship = models.CharField(max_length=20, choices=RELATIONSHIP_CHOICES, default='OTHER')
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='M')
    blood_group = models.CharField(max_length=10, choices=BLOOD_GROUP_CHOICES, default='UNKNOWN')
    avatar = models.ImageField(upload_to='avatars/family/', null=True, blank=True)
    emergency_contact = models.CharField(max_length=50, blank=True, default='')
    notes = models.TextField(blank=True, default='')
    is_active = models.BooleanField(default=True, db_index=True)

    class Meta:
        verbose_name = 'Family Member'
        verbose_name_plural = 'Family Members'
        ordering = ['relationship', 'first_name']
        indexes = [
            models.Index(fields=['user', 'is_active']),
        ]

    def __str__(self):
        rel = self.get_relationship_display()
        return f"{self.full_name} ({rel})"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    @property
    def age(self):
        if not self.date_of_birth:
            return None
        today = timezone.now().date()
        return today.year - self.date_of_birth.year - (
            (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
        )

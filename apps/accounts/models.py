"""
User authentication, profile, roles, login history, and session management models.
"""

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
from apps.core.models import TimeStampedModel


class CustomUserManager(BaseUserManager):
    """
    Custom user manager supporting email-or-username registration
    and secure superuser provisioning.
    """
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set.')
        if email:
            email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    """
    Custom User model with unique email and mobile number support.
    """
    email = models.EmailField('email address', unique=True, db_index=True)
    phone_number = models.CharField(max_length=20, blank=True, default='', db_index=True)
    is_email_verified = models.BooleanField(default=True)
    is_phone_verified = models.BooleanField(default=True)
    failed_login_attempts = models.PositiveIntegerField(default=0)
    account_locked_until = models.DateTimeField(null=True, blank=True)

    objects = CustomUserManager()

    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-date_joined']

    def __str__(self):
        return self.get_full_name() or self.username

    def is_locked(self):
        """Check if account is temporarily locked due to brute-force attempts."""
        if self.account_locked_until and self.account_locked_until > timezone.now():
            return True
        return False


class Role(TimeStampedModel):
    """
    Role definitions for role-based access control (RBAC).
    """
    ROLE_SUPERADMIN = 'superadmin'
    ROLE_ADMIN = 'admin'
    ROLE_USER = 'user'
    ROLE_FAMILY_MEMBER = 'family_member'
    ROLE_CAREGIVER = 'caregiver'

    ROLE_CHOICES = [
        (ROLE_SUPERADMIN, 'Super Administrator'),
        (ROLE_ADMIN, 'Administrator'),
        (ROLE_USER, 'Standard User'),
        (ROLE_FAMILY_MEMBER, 'Family Member'),
        (ROLE_CAREGIVER, 'Caregiver'),
    ]

    slug = models.CharField(max_length=50, unique=True, choices=ROLE_CHOICES)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')

    # Module permissions
    can_manage_users = models.BooleanField(default=False)
    can_manage_family = models.BooleanField(default=True)
    can_manage_medications = models.BooleanField(default=True)
    can_manage_medical = models.BooleanField(default=True)
    can_manage_wellness = models.BooleanField(default=True)
    can_view_analytics = models.BooleanField(default=True)
    can_export_reports = models.BooleanField(default=True)
    can_manage_system = models.BooleanField(default=False)
    can_perform_backup = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'
        ordering = ['slug']

    def __str__(self):
        return self.name


class UserRole(TimeStampedModel):
    """
    Associates users with administrative and clinical roles.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_roles')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='assigned_users')
    assigned_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='roles_assigned'
    )

    class Meta:
        verbose_name = 'User Role Assignment'
        verbose_name_plural = 'User Role Assignments'
        unique_together = ('user', 'role')

    def __str__(self):
        return f"{self.user.username} -> {self.role.name}"


class UserProfile(TimeStampedModel):
    """
    Detailed personal and clinical demographics profile for the primary user.
    """
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('P', 'Prefer not to say'),
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

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='P')
    blood_group = models.CharField(max_length=10, choices=BLOOD_GROUP_CHOICES, default='UNKNOWN')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    address = models.TextField(blank=True, default='')
    city = models.CharField(max_length=100, blank=True, default='')
    state = models.CharField(max_length=100, blank=True, default='')
    postal_code = models.CharField(max_length=20, blank=True, default='')
    country = models.CharField(max_length=100, blank=True, default='Local')

    # Emergency Contact
    emergency_contact_name = models.CharField(max_length=150, blank=True, default='')
    emergency_contact_phone = models.CharField(max_length=25, blank=True, default='')
    emergency_contact_relation = models.CharField(max_length=50, blank=True, default='')

    # Security & Preferences
    session_timeout_minutes = models.PositiveIntegerField(default=60)
    enable_login_alerts = models.BooleanField(default=True)
    enable_sound_notifications = models.BooleanField(default=True)
    preferred_theme = models.CharField(
        max_length=10,
        choices=[('light', 'Light Mode'), ('dark', 'Dark Mode'), ('system', 'System Default')],
        default='light'
    )
    time_format = models.CharField(
        max_length=5,
        choices=[('12', '12-Hour (AM/PM)'), ('24', '24-Hour')],
        default='12'
    )
    date_format = models.CharField(
        max_length=15,
        choices=[('YYYY-MM-DD', 'YYYY-MM-DD'), ('DD/MM/YYYY', 'DD/MM/YYYY'), ('MM/DD/YYYY', 'MM/DD/YYYY')],
        default='YYYY-MM-DD'
    )

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return f"Profile of {self.user.username}"

    @property
    def age(self):
        if not self.date_of_birth:
            return None
        today = timezone.now().date()
        return today.year - self.date_of_birth.year - (
            (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
        )


class LoginHistory(models.Model):
    """
    Security audit trail for user authentication events.
    """
    STATUS_SUCCESS = 'SUCCESS'
    STATUS_FAILED = 'FAILED'
    STATUS_CHOICES = [
        (STATUS_SUCCESS, 'Successful Login'),
        (STATUS_FAILED, 'Failed Attempt'),
    ]

    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='login_history'
    )
    username_attempted = models.CharField(max_length=150, blank=True, default='')
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True, default='')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_SUCCESS)
    failure_reason = models.CharField(max_length=255, blank=True, default='')
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        verbose_name = 'Login History'
        verbose_name_plural = 'Login Histories'
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.username_attempted} - {self.status} at {self.timestamp}"


class UserSession(models.Model):
    """
    Active browser session tracking for concurrent session management
    and remote session termination.
    """
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='active_sessions')
    session_key = models.CharField(max_length=40, unique=True, db_index=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True, default='')
    device_type = models.CharField(max_length=50, blank=True, default='Desktop Browser')
    last_activity = models.DateTimeField(default=timezone.now, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'User Session'
        verbose_name_plural = 'User Sessions'
        ordering = ['-last_activity']

    def __str__(self):
        return f"{self.user.username} ({self.ip_address}) - {self.device_type}"

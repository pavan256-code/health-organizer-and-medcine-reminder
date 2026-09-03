"""
Django settings for Medicine Reminder & Health Organizer.
Production-style, fully local and self-contained configuration.
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'django-insecure-med-health-organizer-local-master-key-$8f93k1!49x%q#z0'
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    # Built-in Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Custom Core & Domain Apps
    'apps.core.apps.CoreConfig',
    'apps.accounts.apps.AccountsConfig',
    'apps.family.apps.FamilyConfig',
    'apps.medications.apps.MedicationsConfig',
    'apps.medical.apps.MedicalConfig',
    'apps.wellness.apps.WellnessConfig',
    'apps.reminders.apps.RemindersConfig',
    'apps.notifications.apps.NotificationsConfig',
    'apps.analytics.apps.AnalyticsConfig',
    'apps.calendar_app.apps.CalendarAppConfig',
    'apps.reports.apps.ReportsConfig',
    'apps.audit.apps.AuditConfig',
    'apps.backups.apps.BackupsConfig',
    'apps.administration.apps.AdministrationConfig',
    'apps.emergency.apps.EmergencyConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Custom Security, Session & Audit Middlewares
    'apps.audit.middleware.AuditLoggingMiddleware',
    'apps.accounts.middleware.SessionTimeoutMiddleware',
    'apps.family.middleware.ActiveFamilyMemberMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Custom Context Processors
                'apps.core.context_processors.app_metadata',
                'apps.family.context_processors.active_family_member',
                'apps.notifications.context_processors.unread_notifications_count',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'
ASGI_APPLICATION = 'config.asgi.application'

# Database configuration: SQLite with WAL (Write-Ahead Logging) mode
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'OPTIONS': {
            'timeout': 30,
            'init_command': 'PRAGMA journal_mode=WAL; PRAGMA foreign_keys=ON;',
        },
    }
}

# Custom User Model
AUTH_USER_MODEL = 'accounts.User'

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files (User uploads, medical files, avatars)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
PROTECTED_MEDIA_ROOT = BASE_DIR / 'media' / 'documents'

# Maximum upload size: 15 MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 15728640
FILE_UPLOAD_MAX_MEMORY_SIZE = 15728640

# Session & Cookie Security
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_NAME = 'med_sessionid'
SESSION_COOKIE_AGE = 86400  # 24 hours
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
CSRF_COOKIE_HTTPONLY = False
CSRF_COOKIE_SAMESITE = 'Lax'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentication URLs
LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'accounts:dashboard'
LOGOUT_REDIRECT_URL = 'core:landing'

# App specific settings
APP_NAME = "Medicine Reminder & Health Organizer"
APP_VERSION = "2.4.0"
APP_ORGANIZATION = "Personal Health Guardian"

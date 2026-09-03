"""
Core context processors providing application metadata, theme state, and system info.
"""

from django.conf import settings
from django.utils import timezone
from apps.core.models import SystemNotice


def app_metadata(request):
    """
    Expose global application branding, version, and active system notices
    to all rendered Django templates.
    """
    now = timezone.now().date()
    active_notices = SystemNotice.objects.filter(
        is_active=True,
        start_date__lte=now
    ).filter(
        models_end_date_filter(now)
    ).order_by('-created_at')[:3]

    return {
        'APP_NAME': getattr(settings, 'APP_NAME', 'Medicine Reminder & Health Organizer'),
        'APP_VERSION': getattr(settings, 'APP_VERSION', '2.4.0'),
        'APP_ORGANIZATION': getattr(settings, 'APP_ORGANIZATION', 'Personal Health Guardian'),
        'SYSTEM_NOTICES': active_notices,
        'CURRENT_YEAR': timezone.now().year,
    }


def models_end_date_filter(now):
    from django.db.models import Q
    return Q(end_date__isnull=True) | Q(end_date__gte=now)

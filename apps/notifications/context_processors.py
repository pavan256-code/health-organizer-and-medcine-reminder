"""
Context processor providing unread notifications count and recent notifications.
"""

from apps.notifications.models import Notification


def unread_notifications_count(request):
    """
    Supplies the unread count and latest unread alerts for the header bell icon.
    """
    if not request.user.is_authenticated:
        return {
            'unread_notifications_count': 0,
            'recent_notifications': [],
        }

    unread_qs = Notification.objects.filter(user=request.user, is_read=False)
    count = unread_qs.count()
    recent = Notification.objects.filter(user=request.user).order_by('-created_at')[:5]

    return {
        'unread_notifications_count': count,
        'recent_notifications': recent,
    }

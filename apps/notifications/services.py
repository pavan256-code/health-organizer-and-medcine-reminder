"""
Notification dispatching and helper services.
"""

from apps.notifications.models import Notification


def create_notification(user, title, message, category='GENERAL', priority='MEDIUM', family_member=None, action_url=''):
    """
    Creates an in-app notification for a user.
    """
    return Notification.objects.create(
        user=user,
        family_member=family_member,
        category=category,
        priority=priority,
        title=title,
        message=message,
        action_url=action_url
    )


def mark_all_notifications_read(user):
    """
    Marks all unread notifications for a user as read.
    """
    from django.utils import timezone
    return Notification.objects.filter(user=user, is_read=False).update(
        is_read=True,
        read_at=timezone.now()
    )

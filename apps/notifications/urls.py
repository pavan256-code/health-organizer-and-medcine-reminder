"""
Notification URL configurations.
"""

from django.urls import path
from apps.notifications.views import (
    NotificationListView,
    MarkNotificationReadView,
    MarkAllNotificationsReadView,
    DeleteNotificationView,
    UnreadCountAPIView,
)

app_name = 'notifications'

urlpatterns = [
    path('', NotificationListView.as_view(), name='list'),
    path('<int:pk>/read/', MarkNotificationReadView.as_view(), name='mark_read'),
    path('mark-all-read/', MarkAllNotificationsReadView.as_view(), name='mark_all_read'),
    path('<int:pk>/delete/', DeleteNotificationView.as_view(), name='delete'),
    path('api/unread-count/', UnreadCountAPIView.as_view(), name='api_unread_count'),
]

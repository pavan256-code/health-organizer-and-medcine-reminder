"""
Admin configuration for Notifications.
"""

from django.contrib import admin
from apps.notifications.models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'family_member', 'category', 'priority', 'is_read', 'created_at')
    list_filter = ('category', 'priority', 'is_read', 'created_at')
    search_fields = ('title', 'message', 'user__username', 'user__email')
    ordering = ('-created_at',)

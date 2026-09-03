"""
Django admin registrations for core models.
"""

from django.contrib import admin
from apps.core.models import SystemNotice, ContactInquiry


@admin.register(SystemNotice)
class SystemNoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'notice_type', 'is_active', 'start_date', 'end_date', 'created_at')
    list_filter = ('notice_type', 'is_active', 'start_date')
    search_fields = ('title', 'message')
    ordering = ('-created_at',)


@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'is_resolved', 'created_at')
    list_filter = ('is_resolved', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)

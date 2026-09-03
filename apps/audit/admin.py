"""
Admin registration for AuditLog.
"""

from django.contrib import admin
from apps.audit.models import AuditLog


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'user', 'action', 'module', 'object_repr', 'ip_address', 'is_security_event')
    list_filter = ('action', 'module', 'is_security_event', 'timestamp')
    search_fields = ('description', 'object_repr', 'ip_address', 'user__username', 'user__email')
    readonly_fields = [f.name for f in AuditLog._meta.fields]
    ordering = ('-timestamp',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

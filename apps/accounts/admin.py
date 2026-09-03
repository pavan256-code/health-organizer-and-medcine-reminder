"""
Custom Django admin configuration for User, UserProfile, Role, UserRole, LoginHistory, and UserSession.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from apps.accounts.models import User, UserProfile, Role, UserRole, LoginHistory, UserSession


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile Details'
    fk_name = 'user'


class UserRoleInline(admin.TabularInline):
    model = UserRole
    extra = 1
    fk_name = 'user'


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline, UserRoleInline)
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'phone_number',
        'is_staff', 'is_active', 'failed_login_attempts', 'date_joined'
    )
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'is_email_verified')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'phone_number')
    ordering = ('-date_joined',)
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Verification & Security', {
            'fields': (
                'phone_number', 'is_email_verified', 'is_phone_verified',
                'failed_login_attempts', 'account_locked_until'
            )
        }),
    )


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'can_manage_users', 'can_manage_system', 'can_manage_medications')
    list_filter = ('slug', 'can_manage_users', 'can_manage_system')
    search_fields = ('name', 'description')


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'assigned_by', 'created_at')
    list_filter = ('role', 'created_at')
    search_fields = ('user__username', 'user__email', 'role__name')


@admin.register(LoginHistory)
class LoginHistoryAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'username_attempted', 'status', 'ip_address', 'failure_reason')
    list_filter = ('status', 'timestamp')
    search_fields = ('username_attempted', 'ip_address', 'failure_reason')
    readonly_fields = [f.name for f in LoginHistory._meta.fields]
    ordering = ('-timestamp',)

    def has_add_permission(self, request):
        return False


@admin.register(UserSession)
class UserSessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'session_key', 'ip_address', 'device_type', 'last_activity', 'is_active')
    list_filter = ('is_active', 'last_activity', 'device_type')
    search_fields = ('user__username', 'session_key', 'ip_address')
    readonly_fields = ('created_at', 'last_activity')

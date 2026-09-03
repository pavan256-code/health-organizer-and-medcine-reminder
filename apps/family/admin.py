"""
Admin registrations for FamilyMember model.
"""

from django.contrib import admin
from apps.family.models import FamilyMember


@admin.register(FamilyMember)
class FamilyMemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'relationship', 'user', 'gender', 'blood_group', 'is_active', 'created_at')
    list_filter = ('relationship', 'gender', 'blood_group', 'is_active')
    search_fields = ('first_name', 'last_name', 'user__username', 'user__email')
    ordering = ('user', 'relationship', 'first_name')

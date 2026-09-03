"""
Authentication signals for auto-creating user profiles and default roles.
"""

from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.accounts.models import User, UserProfile, Role, UserRole


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Creates a UserProfile instance whenever a new User is created,
    and assigns the default 'user' role if none assigned.
    """
    if created:
        UserProfile.objects.create(user=instance)

        # Assign default 'user' or 'superadmin' role
        role_slug = Role.ROLE_SUPERADMIN if instance.is_superuser else Role.ROLE_USER
        role, _ = Role.objects.get_or_create(
            slug=role_slug,
            defaults={
                'name': 'Super Administrator' if instance.is_superuser else 'Standard User',
                'can_manage_users': instance.is_superuser,
                'can_manage_system': instance.is_superuser,
                'can_perform_backup': instance.is_superuser,
                'can_manage_family': True,
                'can_manage_medications': True,
                'can_manage_medical': True,
                'can_manage_wellness': True,
                'can_view_analytics': True,
                'can_export_reports': True,
            }
        )
        UserRole.objects.get_or_create(user=instance, role=role)
    else:
        if hasattr(instance, 'profile'):
            instance.profile.save()

"""
Audit views for viewing audit logs, security events, and user activity.
"""

from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from apps.audit.models import AuditLog


class AuditLogListView(LoginRequiredMixin, ListView):
    """
    Displays audit history. Standard users can see actions performed
    on their accounts and family members. Staff/Superusers can inspect
    system-wide events.
    """
    model = AuditLog
    template_name = 'audit/log_list.html'
    context_object_name = 'logs'
    paginate_by = 30

    def get_queryset(self):
        qs = AuditLog.objects.all()
        user = self.request.user
        if not (user.is_staff or user.is_superuser):
            qs = qs.filter(user=user)

        # Filters
        module = self.request.GET.get('module')
        action = self.request.GET.get('action')
        search = self.request.GET.get('q')

        if module:
            qs = qs.filter(module=module)
        if action:
            qs = qs.filter(action=action)
        if search:
            qs = qs.filter(
                Q(description__icontains=search) |
                Q(object_repr__icontains=search) |
                Q(ip_address__icontains=search)
            )

        return qs.select_related('user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['module_choices'] = AuditLog.MODULE_CHOICES
        context['action_choices'] = AuditLog.ACTION_CHOICES
        context['selected_module'] = self.request.GET.get('module', '')
        context['selected_action'] = self.request.GET.get('action', '')
        context['search_query'] = self.request.GET.get('q', '')
        return context

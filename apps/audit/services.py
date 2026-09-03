"""
Audit logging service helpers.
"""

from apps.audit.models import AuditLog
from apps.core.utils import get_client_ip


def log_audit_event(user, action, module, description, object_repr='', object_id='', request=None, is_security=False):
    """
    Explicitly records an audit entry from service methods or views.
    """
    ip_address = None
    user_agent = ''

    if request:
        ip_address = get_client_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT', '')[:500]

    return AuditLog.objects.create(
        user=user if getattr(user, 'is_authenticated', False) else None,
        action=action,
        module=module,
        object_repr=str(object_repr)[:255],
        object_id=str(object_id)[:100],
        description=description,
        ip_address=ip_address,
        user_agent=user_agent,
        is_security_event=is_security
    )

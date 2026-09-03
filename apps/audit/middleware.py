"""
Audit logging middleware to capture HTTP requests and security modifications.
"""

from apps.core.utils import get_client_ip
from apps.audit.models import AuditLog


class AuditLoggingMiddleware:
    """
    Inspects outgoing responses and logs mutation actions (POST, PUT, DELETE)
    and administrative activities to the AuditLog database model.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # We log state-changing HTTP methods or sensitive paths
        if request.method in ['POST', 'PUT', 'DELETE', 'PATCH']:
            # Skip static, media, or favicon requests
            path = request.path
            if not (path.startswith('/static/') or path.startswith('/media/') or path == '/favicon.ico'):
                self._record_audit_event(request, response)

        return response

    def _record_audit_event(self, request, response):
        try:
            user = request.user if request.user.is_authenticated else None
            ip = get_client_ip(request)
            user_agent = request.META.get('HTTP_USER_AGENT', '')[:500]
            path = request.path

            # Determine module
            module = 'SYSTEM'
            if '/auth/' in path or '/accounts/' in path:
                module = 'AUTH'
            elif '/family/' in path:
                module = 'FAMILY'
            elif '/medications/' in path:
                module = 'MEDICATION'
            elif '/medical/' in path:
                module = 'MEDICAL'
            elif '/wellness/' in path:
                module = 'WELLNESS'
            elif '/analytics/' in path or '/reports/' in path:
                module = 'ANALYTICS'
            elif '/emergency/' in path:
                module = 'EMERGENCY'

            action = 'UPDATE'
            if 'delete' in path or request.method == 'DELETE':
                action = 'DELETE'
            elif 'add' in path or 'create' in path or 'register' in path:
                action = 'CREATE'
            elif 'login' in path:
                action = 'LOGIN' if response.status_code in [200, 302] else 'FAILED_LOGIN'
            elif 'logout' in path:
                action = 'LOGOUT'
            elif 'backup' in path:
                action = 'BACKUP'
            elif 'restore' in path:
                action = 'RESTORE'

            description = f"HTTP {request.method} to {path} (Status: {response.status_code})"

            AuditLog.objects.create(
                user=user,
                action=action,
                module=module,
                object_repr=path[:255],
                description=description,
                ip_address=ip,
                user_agent=user_agent,
                is_security_event=(response.status_code >= 400 or action in ['LOGIN', 'FAILED_LOGIN', 'LOGOUT'])
            )
        except Exception:
            # Audit logging failure must never crash the primary request
            pass

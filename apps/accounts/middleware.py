"""
Session timeout and active session tracking middleware.
"""

import time
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.utils import timezone
from apps.core.utils import get_client_ip


class SessionTimeoutMiddleware:
    """
    Enforces user inactivity timeouts based on the user's profile setting
    and tracks active session timestamps.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            now = time.time()
            last_touch = request.session.get('last_touch')

            timeout_minutes = 60
            if hasattr(request.user, 'profile') and request.user.profile.session_timeout_minutes:
                timeout_minutes = request.user.profile.session_timeout_minutes

            max_idle_seconds = timeout_minutes * 60

            if last_touch and (now - last_touch > max_idle_seconds):
                # Expired session
                logout(request)
                messages.warning(
                    request,
                    f"Your session expired due to {timeout_minutes} minutes of inactivity. Please log in again."
                )
                return redirect('accounts:login')

            request.session['last_touch'] = now

            # Track in UserSession model if session_key is available
            if request.session.session_key:
                self._update_user_session(request)

        response = self.get_response(request)
        return response

    def _update_user_session(self, request):
        try:
            from apps.accounts.models import UserSession
            session_key = request.session.session_key
            ip = get_client_ip(request)
            user_agent = request.META.get('HTTP_USER_AGENT', '')

            device_type = 'Desktop Browser'
            ua_lower = user_agent.lower()
            if 'mobile' in ua_lower or 'android' in ua_lower or 'iphone' in ua_lower:
                device_type = 'Mobile Device'
            elif 'tablet' in ua_lower or 'ipad' in ua_lower:
                device_type = 'Tablet'

            UserSession.objects.update_or_create(
                session_key=session_key,
                defaults={
                    'user': request.user,
                    'ip_address': ip,
                    'user_agent': user_agent[:500],
                    'device_type': device_type,
                    'last_activity': timezone.now(),
                    'is_active': True,
                }
            )
        except Exception:
            pass

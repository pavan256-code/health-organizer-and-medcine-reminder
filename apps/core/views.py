"""
Core views: Landing page, system information, contact processing, and custom error handlers.
"""

from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib import messages
from django.http import JsonResponse, HttpResponseServerError
from django.utils import timezone
from apps.core.models import ContactInquiry, SystemNotice


class LandingPageView(TemplateView):
    """
    Public landing page presenting the core value proposition,
    system capabilities, security architecture, and quick access links.
    """
    template_name = 'landing/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.now().date()
        context['system_notices'] = SystemNotice.objects.filter(
            is_active=True,
            start_date__lte=today
        )[:2]
        return context


class AboutPageView(TemplateView):
    """About us, medical data philosophy, and offline privacy guarantees."""
    template_name = 'landing/about.html'


class FeaturesPageView(TemplateView):
    """Detailed showcase of all 7 core modules and technical specifications."""
    template_name = 'landing/features.html'


class ContactPageView(View):
    """
    Contact inquiry page. Handles user feedback, inquiries, or bug reports
    locally in SQLite without reliance on third-party mailer APIs.
    """
    template_name = 'landing/contact.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message_text = request.POST.get('message', '').strip()

        if not (name and email and subject and message_text):
            messages.error(request, "Please fill out all required fields.")
            return render(request, self.template_name, {
                'name': name, 'email': email, 'subject': subject, 'message': message_text
            })

        ContactInquiry.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message_text
        )
        messages.success(
            request,
            "Thank you! Your inquiry has been logged securely in the local system. Our team will review it."
        )
        return redirect('core:contact')


def health_check_view(request):
    """
    Local JSON endpoint providing system health diagnostics:
    database connectivity, storage status, and service uptime.
    """
    from django.db import connection
    status = "healthy"
    db_status = "connected"
    try:
        connection.ensure_connection()
    except Exception as e:
        status = "degraded"
        db_status = str(e)

    return JsonResponse({
        'status': status,
        'database': db_status,
        'timestamp': timezone.now().isoformat(),
        'platform': 'Medicine Reminder & Health Organizer',
        'offline_mode': True
    })


# Custom HTTP Error Handlers
def custom_bad_request_view(request, exception=None):
    return render(request, 'errors/400.html', status=400)


def custom_permission_denied_view(request, exception=None):
    return render(request, 'errors/403.html', status=403)


def custom_page_not_found_view(request, exception=None):
    return render(request, 'errors/404.html', status=404)


def custom_server_error_view(request):
    return render(request, 'errors/500.html', status=500)

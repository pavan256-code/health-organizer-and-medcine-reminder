"""
URL configuration for Medicine Reminder & Health Organizer.
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

# Root URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('auth/login/', RedirectView.as_view(url='/accounts/login/', permanent=True)),
    path('family/', include('apps.family.urls')),
    path('notifications/', include('apps.notifications.urls')),
    path('audit/', include('apps.audit.urls')),
    path('medications/', include('apps.medications.urls')),
    path('medical/', include('apps.medical.urls')),
    path('wellness/', include('apps.wellness.urls')),
    path('reminders/', include('apps.reminders.urls')),
    path('analytics/', include('apps.analytics.urls')),
    path('calendar/', include('apps.calendar_app.urls')),
    path('reports/', include('apps.reports.urls')),
    path('backups/', include('apps.backups.urls')),
    path('administration/', include('apps.administration.urls')),
    path('emergency/', include('apps.emergency.urls')),
]

# Static & Media file serving for local operation
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom Error Handlers
handler400 = 'apps.core.views.custom_bad_request_view'
handler403 = 'apps.core.views.custom_permission_denied_view'
handler404 = 'apps.core.views.custom_page_not_found_view'
handler500 = 'apps.core.views.custom_server_error_view'

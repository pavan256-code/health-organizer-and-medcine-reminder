#!/usr/bin/env python
"""
WSGI / ASGI application bootstrap entry point.
Exposes the application callable for modern web servers, Docker, and WSGI containers.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
app = application

if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(['app.py', 'runserver', '0.0.0.0:8000'])

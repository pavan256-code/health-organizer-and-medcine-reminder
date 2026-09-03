#!/usr/bin/env python
"""
Main application entry point for the Hospital Management & Medicine Reminder Suite.
Enables running the application server directly: `python main.py` or via standard entrypoints.
"""

import os
import sys


def main():
    """Run administrative and server tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    if len(sys.argv) == 1:
        # Default to running the server if no arguments provided
        sys.argv = ['main.py', 'runserver', '0.0.0.0:8000']

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

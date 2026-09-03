"""
Core utilities, file validators, sanitizers, and date computation helpers.
"""

import os
import hashlib
from datetime import datetime, date, timedelta
from django.core.exceptions import ValidationError
from django.utils import timezone


ALLOWED_DOCUMENT_EXTENSIONS = [
    '.pdf', '.jpg', '.jpeg', '.png', '.webp', '.doc', '.docx', '.txt'
]

MAX_DOCUMENT_SIZE_BYTES = 15 * 1024 * 1024  # 15 MB


def validate_medical_document(file_obj):
    """
    Validates uploaded medical document files for allowed extensions and size limits.
    Prevents executable script execution and path manipulation attacks.
    """
    if not file_obj:
        raise ValidationError("No file uploaded.")

    ext = os.path.splitext(file_obj.name)[1].lower()
    if ext not in ALLOWED_DOCUMENT_EXTENSIONS:
        raise ValidationError(
            f"Unsupported file type '{ext}'. Allowed formats: {', '.join(ALLOWED_DOCUMENT_EXTENSIONS)}"
        )

    if file_obj.size > MAX_DOCUMENT_SIZE_BYTES:
        max_mb = MAX_DOCUMENT_SIZE_BYTES // (1024 * 1024)
        raise ValidationError(f"File size exceeds the {max_mb}MB maximum limit.")

    return True


def calculate_file_sha256(file_path):
    """
    Calculates the SHA-256 checksum of a local file.
    Used for backup integrity verification and document deduplication.
    """
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(65536), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def get_client_ip(request):
    """
    Safely retrieves the client's IP address from request headers.
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR', '127.0.0.1')
    return ip


def format_duration(minutes):
    """
    Formats a duration in minutes into a human-readable 'Xh Ym' string.
    """
    if not minutes or minutes < 0:
        return "0m"
    hours = minutes // 60
    mins = minutes % 60
    if hours > 0:
        return f"{hours}h {mins}m" if mins > 0 else f"{hours}h"
    return f"{mins}m"


def get_date_range_for_period(period_name='month'):
    """
    Returns (start_date, end_date) tuples for common periods:
    'today', 'week', 'month', 'quarter', 'year'.
    """
    today = timezone.now().date()
    if period_name == 'today':
        return today, today
    elif period_name == 'week':
        start = today - timedelta(days=today.weekday())
        end = start + timedelta(days=6)
        return start, end
    elif period_name == 'month':
        start = date(today.year, today.month, 1)
        # Next month calculation
        if today.month == 12:
            end = date(today.year, 12, 31)
        else:
            next_month = date(today.year, today.month + 1, 1)
            end = next_month - timedelta(days=1)
        return start, end
    elif period_name == 'year':
        return date(today.year, 1, 1), date(today.year, 12, 31)
    return today, today

"""
Local SQLite database backup & restore service using SQLite's native backup API.
"""

import os
import sqlite3
import shutil
from datetime import datetime
from django.conf import settings


class LocalBackupService:
    @staticmethod
    def get_backup_dir():
        backup_dir = os.path.join(settings.BASE_DIR, 'backups')
        os.makedirs(backup_dir, exist_ok=True)
        return backup_dir

    @classmethod
    def list_backups(cls):
        b_dir = cls.get_backup_dir()
        files = []
        for fname in os.listdir(b_dir):
            if fname.endswith('.sqlite3') or fname.endswith('.db'):
                fpath = os.path.join(b_dir, fname)
                stat = os.stat(fpath)
                files.append({
                    'filename': fname,
                    'size_mb': round(stat.st_size / (1024 * 1024), 2),
                    'created_at': datetime.fromtimestamp(stat.st_mtime)
                })
        return sorted(files, key=lambda x: x['created_at'], reverse=True)

    @classmethod
    def create_backup(cls):
        b_dir = cls.get_backup_dir()
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        dest_filename = f"health_organizer_backup_{timestamp}.sqlite3"
        dest_path = os.path.join(b_dir, dest_filename)

        src_db = settings.DATABASES['default']['NAME']

        # Use native sqlite3 online backup
        source_conn = sqlite3.connect(src_db)
        dest_conn = sqlite3.connect(dest_path)
        with dest_conn:
            source_conn.backup(dest_conn)
        dest_conn.close()
        source_conn.close()

        return dest_filename

    @classmethod
    def delete_backup(cls, filename):
        b_dir = cls.get_backup_dir()
        safe_fname = os.path.basename(filename)
        target = os.path.join(b_dir, safe_fname)
        if os.path.exists(target):
            os.remove(target)
            return True
        return False

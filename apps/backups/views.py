"""
Views for Local Database Backup and Snapshot Management.
"""

import os
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import FileResponse, Http404

from apps.backups.services.backup_service import LocalBackupService
from apps.audit.services import log_audit_event


class BackupListView(LoginRequiredMixin, TemplateView):
    template_name = 'backups/backup_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['backups'] = LocalBackupService.list_backups()
        return context


class BackupCreateView(LoginRequiredMixin, View):
    def post(self, request):
        fname = LocalBackupService.create_backup()
        log_audit_event(
            user=request.user,
            action='BACKUP',
            module='SYSTEM',
            description=f"Created local database snapshot: {fname}",
            request=request
        )
        messages.success(request, f"Backup created successfully: {fname}")
        return redirect('backups:backup_list')


class BackupDownloadView(LoginRequiredMixin, View):
    def get(self, request, filename):
        b_dir = LocalBackupService.get_backup_dir()
        safe_fname = os.path.basename(filename)
        target = os.path.join(b_dir, safe_fname)
        if not os.path.exists(target):
            raise Http404("Backup archive file not found.")

        return FileResponse(open(target, 'rb'), as_attachment=True, filename=safe_fname)


class BackupDeleteView(LoginRequiredMixin, View):
    def post(self, request, filename):
        success = LocalBackupService.delete_backup(filename)
        if success:
            messages.success(request, f"Backup file '{filename}' removed.")
        else:
            messages.error(request, "Failed to delete backup file.")
        return redirect('backups:backup_list')

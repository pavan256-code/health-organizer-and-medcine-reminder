"""
Backup module URL patterns.
"""

from django.urls import path
from apps.backups.views import (
    BackupListView, BackupCreateView, BackupDownloadView, BackupDeleteView
)

app_name = 'backups'

urlpatterns = [
    path('', BackupListView.as_view(), name='backup_list'),
    path('create/', BackupCreateView.as_view(), name='backup_create'),
    path('download/<str:filename>/', BackupDownloadView.as_view(), name='backup_download'),
    path('delete/<str:filename>/', BackupDeleteView.as_view(), name='backup_delete'),
]

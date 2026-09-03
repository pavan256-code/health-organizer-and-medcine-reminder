"""
Accounts URL configurations.
"""

from django.urls import path
from apps.accounts.views import (
    RegisterView,
    LoginView,
    LogoutView,
    ProfileView,
    ChangePasswordView,
    LoginHistoryListView,
    SessionManagementView,
    TerminateSessionView,
    LogoutAllSessionsView,
    DashboardView,
)

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('password-change/', ChangePasswordView.as_view(), name='change_password'),
    path('login-history/', LoginHistoryListView.as_view(), name='login_history'),
    path('sessions/', SessionManagementView.as_view(), name='sessions'),
    path('sessions/<int:session_id>/terminate/', TerminateSessionView.as_view(), name='terminate_session'),
    path('sessions/logout-all/', LogoutAllSessionsView.as_view(), name='logout_all_sessions'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]

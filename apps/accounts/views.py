"""
Views for authentication, registration, user profiles, session control, and the main dashboard.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, UpdateView, ListView, View, TemplateView
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.utils import timezone

from apps.accounts.models import User, UserProfile, LoginHistory, UserSession
from apps.accounts.forms import (
    UserRegistrationForm,
    UserLoginForm,
    UserProfileForm,
    UserPasswordChangeForm
)
from apps.core.utils import get_client_ip
from apps.audit.services import log_audit_event


class RegisterView(CreateView):
    """
    Handles self-registration of primary users.
    Creates account, initiates default profile, creates Self family member, and logs event.
    """
    model = User
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        user = form.save()
        # Automatically create default 'Self' family member for the user
        from apps.family.models import FamilyMember
        FamilyMember.objects.create(
            user=user,
            first_name=user.first_name or user.username,
            last_name=user.last_name or '',
            relationship='SELF',
            is_active=True
        )

        log_audit_event(
            user=user,
            action='CREATE',
            module='AUTH',
            description=f"New user account registered: {user.username} ({user.email})",
            object_repr=user.username,
            request=self.request
        )

        messages.success(
            self.request,
            "Account successfully created! You may now sign in to your secure organizer."
        )
        return super().form_valid(form)


class LoginView(FormView):
    """
    Local authentication view with brute-force tracking, remember-me support,
    and LoginHistory logging.
    """
    form_class = UserLoginForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('accounts:dashboard')

    def form_valid(self, form):
        user = form.cleaned_data['user']
        remember_me = form.cleaned_data.get('remember_me', False)

        # Reset failed attempts on success
        user.failed_login_attempts = 0
        user.account_locked_until = None
        user.save(update_fields=['failed_login_attempts', 'account_locked_until'])

        login(self.request, user)

        # Configure session expiry
        if remember_me:
            # 30 days
            self.request.session.set_expiry(2592000)
        else:
            # Browser session
            self.request.session.set_expiry(0)

        # Record login history
        ip = get_client_ip(self.request)
        ua = self.request.META.get('HTTP_USER_AGENT', '')
        LoginHistory.objects.create(
            user=user,
            username_attempted=user.username,
            ip_address=ip,
            user_agent=ua,
            status=LoginHistory.STATUS_SUCCESS
        )

        log_audit_event(
            user=user,
            action='LOGIN',
            module='AUTH',
            description=f"User {user.username} successfully logged in from {ip}",
            object_repr=user.username,
            request=self.request
        )

        messages.info(self.request, f"Welcome back, {user.first_name or user.username}!")
        return super().form_valid(form)

    def form_invalid(self, form):
        username = form.data.get('username_or_email', '')
        ip = get_client_ip(self.request)
        ua = self.request.META.get('HTTP_USER_AGENT', '')

        # Track failed attempts
        user = None
        if '@' in username:
            user = User.objects.filter(email__iexact=username).first()
        else:
            user = User.objects.filter(username=username).first()

        if user:
            user.failed_login_attempts += 1
            if user.failed_login_attempts >= 5:
                user.account_locked_until = timezone.now() + timezone.timedelta(minutes=15)
            user.save(update_fields=['failed_login_attempts', 'account_locked_until'])

        LoginHistory.objects.create(
            user=user,
            username_attempted=username,
            ip_address=ip,
            user_agent=ua,
            status=LoginHistory.STATUS_FAILED,
            failure_reason="Invalid credentials or locked account"
        )

        return super().form_invalid(form)


class LogoutView(View):
    """
    Securely terminates the active session, deletes session state,
    and writes audit log.
    """
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            session_key = request.session.session_key
            if session_key:
                UserSession.objects.filter(session_key=session_key).update(is_active=False)

            log_audit_event(
                user=request.user,
                action='LOGOUT',
                module='AUTH',
                description=f"User {request.user.username} logged out",
                object_repr=request.user.username,
                request=request
            )
            logout(request)
            messages.success(request, "You have been successfully logged out.")
        return redirect('core:landing')


class ProfileView(LoginRequiredMixin, UpdateView):
    """
    Manages user personal demographics, medical identifiers, and emergency details.
    """
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self, queryset=None):
        profile, _ = UserProfile.objects.get_or_create(user=self.request.user)
        return profile

    def form_valid(self, form):
        messages.success(self.request, "Your personal health profile has been updated.")
        log_audit_event(
            user=self.request.user,
            action='UPDATE',
            module='AUTH',
            description="User profile demographics updated",
            object_repr=self.request.user.username,
            request=self.request
        )
        return super().form_valid(form)


class ChangePasswordView(LoginRequiredMixin, FormView):
    """
    Secure password change view validating existing password against PBKDF2 hash.
    """
    form_class = UserPasswordChangeForm
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('accounts:profile')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        # Keep user logged in after password change
        update_session_auth_hash(self.request, self.request.user)

        log_audit_event(
            user=self.request.user,
            action='PASSWORD_CHANGE',
            module='AUTH',
            description="User changed their account password",
            object_repr=self.request.user.username,
            request=self.request,
            is_security=True
        )
        messages.success(self.request, "Your password was successfully updated.")
        return super().form_valid(form)


class LoginHistoryListView(LoginRequiredMixin, ListView):
    """
    Lists recent authentication attempts and device security details for the user.
    """
    model = LoginHistory
    template_name = 'accounts/login_history.html'
    context_object_name = 'login_records'
    paginate_by = 25

    def get_queryset(self):
        return LoginHistory.objects.filter(user=self.request.user).order_by('-timestamp')


class SessionManagementView(LoginRequiredMixin, ListView):
    """
    View all active sessions associated with the user across devices.
    """
    model = UserSession
    template_name = 'accounts/sessions.html'
    context_object_name = 'user_sessions'

    def get_queryset(self):
        return UserSession.objects.filter(
            user=self.request.user,
            is_active=True
        ).order_by('-last_activity')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_session_key'] = self.request.session.session_key
        return context


class TerminateSessionView(LoginRequiredMixin, View):
    """
    Terminates a specific remote session key.
    """
    def post(self, request, session_id):
        user_session = get_object_or_404(UserSession, id=session_id, user=request.user)
        # Delete from Django session backend
        Session.objects.filter(session_key=user_session.session_key).delete()
        user_session.is_active = False
        user_session.save(update_fields=['is_active'])

        log_audit_event(
            user=request.user,
            action='DELETE',
            module='AUTH',
            description=f"Remote session terminated: {user_session.ip_address} ({user_session.device_type})",
            object_repr=user_session.session_key,
            request=request,
            is_security=True
        )
        messages.success(request, "The specified session has been terminated.")
        return redirect('accounts:sessions')


class LogoutAllSessionsView(LoginRequiredMixin, View):
    """
    Revokes all active sessions except the current one.
    """
    def post(self, request):
        current_key = request.session.session_key
        sessions_to_revoke = UserSession.objects.filter(
            user=request.user,
            is_active=True
        ).exclude(session_key=current_key)

        for s in sessions_to_revoke:
            Session.objects.filter(session_key=s.session_key).delete()
            s.is_active = False
            s.save(update_fields=['is_active'])

        messages.success(request, "All other active sessions have been revoked.")
        return redirect('accounts:sessions')


class DashboardView(LoginRequiredMixin, TemplateView):
    """
    Central Health Organizer dashboard presenting:
    - Today's medicine doses (taken, missed, pending)
    - Upcoming clinical appointments
    - Active health vitals summary
    - Medication adherence percentage
    - Active health alerts, low stock & expiry warnings
    - Quick actions menu
    """
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        today = timezone.now().date()

        # Retrieve active family member from session context
        active_member = getattr(self.request, 'active_family_member', None)

        # Dynamic querysets scoped to active member or user
        try:
            from apps.medications.models import MedicineDose, MedicineStock, MedicineExpiry, Medicine
            from apps.medical.models import Appointment, VitalRecord, SymptomRecord
            from apps.wellness.models import HealthGoal

            dose_qs = MedicineDose.objects.filter(
                schedule__medicine__user=user,
                date=today
            )
            if active_member:
                dose_qs = dose_qs.filter(schedule__medicine__family_member=active_member)

            context['todays_doses'] = dose_qs.select_related('schedule__medicine').order_by('scheduled_time')
            context['doses_taken_count'] = dose_qs.filter(status='TAKEN').count()
            context['doses_pending_count'] = dose_qs.filter(status='PENDING').count()
            context['doses_missed_count'] = dose_qs.filter(status='MISSED').count()
            context['doses_total_count'] = dose_qs.count()

            # Adherence % for today
            if context['doses_total_count'] > 0:
                context['today_adherence'] = int(
                    (context['doses_taken_count'] / context['doses_total_count']) * 100
                )
            else:
                context['today_adherence'] = 100

            # Upcoming appointments (next 14 days)
            appt_qs = Appointment.objects.filter(
                user=user,
                date__gte=today,
                status='UPCOMING'
            )
            if active_member:
                appt_qs = appt_qs.filter(family_member=active_member)
            context['upcoming_appointments'] = appt_qs.select_related('doctor', 'family_member').order_by('date', 'time')[:5]

            # Recent Vitals
            vital_qs = VitalRecord.objects.filter(family_member__user=user)
            if active_member:
                vital_qs = vital_qs.filter(family_member=active_member)
            context['latest_vital'] = vital_qs.order_by('-date', '-time').first()

            # Low stock medicines
            stock_qs = MedicineStock.objects.filter(medicine__user=user)
            if active_member:
                stock_qs = stock_qs.filter(medicine__family_member=active_member)
            context['low_stock_medicines'] = [
                s for s in stock_qs.select_related('medicine') if s.is_low_stock()
            ][:5]

            # Expiring medicines
            expiry_qs = MedicineExpiry.objects.filter(
                medicine__user=user,
                status__in=['EXPIRING_SOON', 'EXPIRED']
            )
            if active_member:
                expiry_qs = expiry_qs.filter(medicine__family_member=active_member)
            context['expiring_medicines'] = expiry_qs.select_related('medicine')[:5]

            # Active Health Goals
            goal_qs = HealthGoal.objects.filter(family_member__user=user, status='ACTIVE')
            if active_member:
                goal_qs = goal_qs.filter(family_member=active_member)
            context['active_goals'] = goal_qs[:4]

            # Active Medicines count
            med_qs = Medicine.objects.filter(user=user, status='ACTIVE')
            if active_member:
                med_qs = med_qs.filter(family_member=active_member)
            context['active_medicines_count'] = med_qs.count()

        except Exception:
            # Safe fallbacks if modules are being migrated
            context['todays_doses'] = []
            context['doses_taken_count'] = 0
            context['doses_pending_count'] = 0
            context['doses_missed_count'] = 0
            context['doses_total_count'] = 0
            context['today_adherence'] = 100
            context['upcoming_appointments'] = []
            context['latest_vital'] = None
            context['low_stock_medicines'] = []
            context['expiring_medicines'] = []
            context['active_goals'] = []
            context['active_medicines_count'] = 0

        context['today_date'] = today
        return context

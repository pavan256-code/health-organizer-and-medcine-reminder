"""
Automated tests for audit logging and middleware.
"""

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from apps.audit.models import AuditLog

User = get_user_model()


class AuditTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='agent_smith',
            email='smith@matrix.local',
            password='Password12345!'
        )

    def test_audit_logs_mutation(self):
        self.client.login(username='agent_smith', password='Password12345!')
        # Post to family member add
        self.client.post(reverse('family:add'), {
            'first_name': 'Agent',
            'last_name': 'Brown',
            'relationship': 'OTHER',
            'gender': 'M',
            'blood_group': 'UNKNOWN'
        })
        # Verify AuditLog entry was recorded
        self.assertTrue(AuditLog.objects.filter(user=self.user, module='FAMILY').exists())

    def test_audit_log_list_view_restricted(self):
        # Unauthenticated request redirects to login
        response = self.client.get(reverse('audit:log_list'))
        self.assertEqual(response.status_code, 302)

        # Authenticated user can see their logs
        self.client.login(username='agent_smith', password='Password12345!')
        response = self.client.get(reverse('audit:log_list'))
        self.assertEqual(response.status_code, 200)

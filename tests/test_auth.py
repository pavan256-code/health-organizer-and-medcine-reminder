"""
Authentication and User Account Unit Tests.
"""
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class AuthenticationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@hospital.local',
            password='TestPassword123!'
        )

    def test_user_creation(self):
        """Verify user instance properties."""
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@hospital.local')
        self.assertTrue(self.user.check_password('TestPassword123!'))

    def test_login_success(self):
        """Verify successful user authentication flow."""
        response = self.client.post(reverse('accounts:login'), {
            'username_or_email': 'testuser',
            'password': 'TestPassword123!'
        })
        self.assertEqual(response.status_code, 302)

    def test_login_invalid_credentials(self):
        """Verify authentication failure handling."""
        response = self.client.post(reverse('accounts:login'), {
            'username_or_email': 'testuser',
            'password': 'WrongPassword999'
        })
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        """Verify session termination."""
        self.client.force_login(self.user)
        response = self.client.get(reverse('accounts:logout'))
        self.assertEqual(response.status_code, 302)

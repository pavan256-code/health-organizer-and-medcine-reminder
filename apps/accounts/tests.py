"""
Automated unit and integration tests for accounts, auth, roles, and profiles.
"""

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from apps.accounts.models import Role, UserRole, UserProfile, LoginHistory

User = get_user_model()


class AuthenticationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='dr_watson',
            email='watson@bakerstreet.org',
            password='StrongPassword123!',
            first_name='John',
            last_name='Watson',
            phone_number='+1234567890'
        )

    def test_user_registration_success(self):
        response = self.client.post(reverse('accounts:register'), {
            'username': 'mary_morstan',
            'email': 'mary@bakerstreet.org',
            'first_name': 'Mary',
            'last_name': 'Morstan',
            'phone_number': '+1987654321',
            'password': 'SecurePassword88!',
            'confirm_password': 'SecurePassword88!',
            'terms_accepted': True
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='mary_morstan').exists())
        # Check auto-created profile and 'SELF' family member
        mary = User.objects.get(username='mary_morstan')
        self.assertTrue(hasattr(mary, 'profile'))
        self.assertTrue(mary.family_members.filter(relationship='SELF').exists())

    def test_duplicate_email_registration_rejected(self):
        response = self.client.post(reverse('accounts:register'), {
            'username': 'imposter',
            'email': 'watson@bakerstreet.org',
            'password': 'StrongPassword123!',
            'confirm_password': 'StrongPassword123!',
            'terms_accepted': True
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username='imposter').exists())

    def test_password_mismatch_rejected(self):
        response = self.client.post(reverse('accounts:register'), {
            'username': 'bad_pass_user',
            'email': 'badpass@example.com',
            'password': 'StrongPassword123!',
            'confirm_password': 'DifferentPassword456!',
            'terms_accepted': True
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username='bad_pass_user').exists())

    def test_login_with_username_success(self):
        response = self.client.post(reverse('accounts:login'), {
            'username_or_email': 'dr_watson',
            'password': 'StrongPassword123!',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('accounts:dashboard'))
        self.assertTrue(LoginHistory.objects.filter(user=self.user, status='SUCCESS').exists())

    def test_login_with_email_success(self):
        response = self.client.post(reverse('accounts:login'), {
            'username_or_email': 'watson@bakerstreet.org',
            'password': 'StrongPassword123!',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('accounts:dashboard'))

    def test_invalid_login_records_failure(self):
        response = self.client.post(reverse('accounts:login'), {
            'username_or_email': 'dr_watson',
            'password': 'WrongPassword!',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(LoginHistory.objects.filter(status='FAILED').exists())

    def test_profile_update(self):
        self.client.login(username='dr_watson', password='StrongPassword123!')
        response = self.client.post(reverse('accounts:profile'), {
            'first_name': 'John H.',
            'last_name': 'Watson',
            'phone_number': '+1122334455',
            'blood_group': 'O+',
            'gender': 'M',
            'city': 'London',
            'session_timeout_minutes': 45,
            'preferred_theme': 'dark',
            'time_format': '24',
            'date_format': 'YYYY-MM-DD',
        })
        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'John H.')
        self.assertEqual(self.user.profile.blood_group, 'O+')
        self.assertEqual(self.user.profile.preferred_theme, 'dark')

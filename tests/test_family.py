"""
Family Profile & Active Patient Switching Unit Tests.
"""
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from apps.family.models import FamilyMember

User = get_user_model()


class FamilyProfileTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='familytest',
            email='family@hospital.local',
            password='TestPassword123!'
        )
        self.self_member = FamilyMember.objects.create(
            user=self.user,
            first_name='Alex',
            last_name='Morgan',
            relationship='SELF',
            is_active=True
        )
        self.spouse_member = FamilyMember.objects.create(
            user=self.user,
            first_name='Taylor',
            last_name='Morgan',
            relationship='SPOUSE',
            is_active=True
        )

    def test_family_member_count(self):
        """Verify user family members association."""
        members = FamilyMember.objects.filter(user=self.user, is_active=True)
        self.assertEqual(members.count(), 2)

    def test_active_patient_switch(self):
        """Verify switching active patient context in session."""
        self.client.force_login(self.user)
        response = self.client.post(
            reverse('family:switch', kwargs={'member_id': self.spouse_member.id}),
            {'next': reverse('accounts:dashboard')},
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            self.client.session.get('active_family_member_id'),
            self.spouse_member.id
        )

    def test_switch_direct_endpoint(self):
        """Verify fallback direct switch endpoint."""
        self.client.force_login(self.user)
        response = self.client.post(
            reverse('family:switch_direct'),
            {'member_id': self.self_member.id, 'next': reverse('accounts:dashboard')},
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            self.client.session.get('active_family_member_id'),
            self.self_member.id
        )

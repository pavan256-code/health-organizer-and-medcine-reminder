"""
Automated tests for family member management, switching context, and data isolation.
"""

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from apps.family.models import FamilyMember

User = get_user_model()


class FamilyManagementTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='clara_oswald',
            email='clara@tardis.net',
            password='TimeTravelPassword123!'
        )
        self.self_member = FamilyMember.objects.create(
            user=self.user,
            first_name='Clara',
            last_name='Oswald',
            relationship='SELF'
        )

    def test_add_family_member(self):
        self.client.login(username='clara_oswald', password='TimeTravelPassword123!')
        response = self.client.post(reverse('family:add'), {
            'first_name': 'Danny',
            'last_name': 'Pink',
            'relationship': 'SPOUSE',
            'gender': 'M',
            'blood_group': 'A+',
            'emergency_contact': '+1555987654',
            'notes': 'No known drug allergies'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(FamilyMember.objects.filter(user=self.user, first_name='Danny').exists())

    def test_cannot_delete_self_profile(self):
        self.client.login(username='clara_oswald', password='TimeTravelPassword123!')
        response = self.client.post(reverse('family:delete', args=[self.self_member.id]))
        self.assertEqual(response.status_code, 302)
        self.self_member.refresh_from_db()
        self.assertTrue(self.self_member.is_active)

    def test_deactivate_other_family_member(self):
        child = FamilyMember.objects.create(
            user=self.user,
            first_name='Child',
            relationship='SON'
        )
        self.client.login(username='clara_oswald', password='TimeTravelPassword123!')
        response = self.client.post(reverse('family:delete', args=[child.id]))
        self.assertEqual(response.status_code, 302)
        child.refresh_from_db()
        self.assertFalse(child.is_active)

    def test_switch_active_family_member(self):
        father = FamilyMember.objects.create(
            user=self.user,
            first_name='Dave',
            last_name='Oswald',
            relationship='FATHER'
        )
        self.client.login(username='clara_oswald', password='TimeTravelPassword123!')
        response = self.client.post(reverse('family:switch', args=[father.id]))
        self.assertEqual(response.status_code, 302)
        session = self.client.session
        self.assertEqual(session.get('active_family_member_id'), father.id)

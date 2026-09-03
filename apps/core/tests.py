"""
Automated tests for core landing views, health check endpoint, and contact submissions.
"""

from django.test import TestCase, Client
from django.urls import reverse
from apps.core.models import ContactInquiry


class CoreViewsTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_landing_page_accessible(self):
        response = self.client.get(reverse('core:landing'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Never Miss a Dose")

    def test_about_page_accessible(self):
        response = self.client.get(reverse('core:about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Privacy Philosophy")

    def test_features_page_accessible(self):
        response = self.client.get(reverse('core:features'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Complete Architectural Modules")

    def test_contact_inquiry_submission(self):
        response = self.client.post(reverse('core:contact'), {
            'name': 'Sarah Connor',
            'email': 'sarah@resistance.org',
            'subject': 'Local data retention',
            'message': 'Confirming this runs completely offline without sending telemetry.'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(ContactInquiry.objects.filter(email='sarah@resistance.org').exists())

    def test_health_check_endpoint(self):
        response = self.client.get(reverse('core:health_check'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['status'], 'healthy')
        self.assertTrue(data['offline_mode'])

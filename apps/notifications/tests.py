"""
Automated tests for notifications, unread counters, and mark-as-read workflows.
"""

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from apps.notifications.models import Notification
from apps.notifications.services import create_notification

User = get_user_model()


class NotificationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='bruce_wayne',
            email='bruce@wayne.corp',
            password='BatcaveSecretKey99!'
        )

    def test_create_and_read_notification(self):
        n = create_notification(
            user=self.user,
            title="Dose Time: Aspirin 100mg",
            message="Time to take your scheduled dose after lunch.",
            category='MEDICINE',
            priority='HIGH'
        )
        self.assertFalse(n.is_read)

        self.client.login(username='bruce_wayne', password='BatcaveSecretKey99!')
        response = self.client.get(reverse('notifications:mark_read', args=[n.id]))
        self.assertEqual(response.status_code, 302)
        n.refresh_from_db()
        self.assertTrue(n.is_read)

    def test_unread_count_api(self):
        create_notification(self.user, "Alert 1", "Message 1")
        create_notification(self.user, "Alert 2", "Message 2")

        self.client.login(username='bruce_wayne', password='BatcaveSecretKey99!')
        response = self.client.get(reverse('notifications:api_unread_count'))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['unread_count'], 2)
        self.assertEqual(len(data['items']), 2)

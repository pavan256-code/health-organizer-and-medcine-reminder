"""
Automated unit tests for Wellness: Meals, Hydration, Exercise, Sleep, and Goals.
"""

from datetime import date, time
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from apps.family.models import FamilyMember
from apps.wellness.models import MealRecord, ActivityRecord, SleepRecord, HealthGoal

User = get_user_model()


class WellnessModuleTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='arnold_s',
            email='arnold@gym.com',
            password='PumpItUpPassword123!'
        )
        self.member = FamilyMember.objects.create(
            user=self.user,
            first_name='Arnold',
            last_name='Schwarzenegger',
            relationship='SELF'
        )

    def test_meal_and_water_logging(self):
        self.client.login(username='arnold_s', password='PumpItUpPassword123!')
        response = self.client.post(reverse('wellness:meal_add'), {
            'family_member': self.member.id,
            'date': date.today().strftime('%Y-%m-%d'),
            'meal_type': 'BREAKFAST',
            'food_items': '6 Scrambled egg whites and oatmeal',
            'calories': 450,
            'water_intake_ml': 500
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(MealRecord.objects.filter(family_member=self.member).exists())

        # Quick water increment
        res_water = self.client.post(reverse('wellness:water_log'), {'amount_ml': 250})
        self.assertEqual(res_water.status_code, 302)

    def test_fitness_activity_logging(self):
        self.client.login(username='arnold_s', password='PumpItUpPassword123!')
        response = self.client.post(reverse('wellness:fitness_add'), {
            'family_member': self.member.id,
            'date': date.today().strftime('%Y-%m-%d'),
            'activity_type': 'STRENGTH',
            'duration_minutes': 60,
            'calories_burned': 500
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(ActivityRecord.objects.filter(activity_type='STRENGTH').exists())

    def test_sleep_tracking(self):
        self.client.login(username='arnold_s', password='PumpItUpPassword123!')
        response = self.client.post(reverse('wellness:sleep_add'), {
            'family_member': self.member.id,
            'date': date.today().strftime('%Y-%m-%d'),
            'bedtime': '22:30',
            'wake_time': '06:30',
            'duration_hours': 8.0,
            'sleep_quality': 'EXCELLENT',
            'interruptions_count': 0
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(SleepRecord.objects.filter(sleep_quality='EXCELLENT').exists())

    def test_health_goal_lifecycle(self):
        self.client.login(username='arnold_s', password='PumpItUpPassword123!')
        response = self.client.post(reverse('wellness:goal_add'), {
            'family_member': self.member.id,
            'title': 'Daily Steps Goal',
            'goal_type': 'STEPS',
            'target_value': 10000,
            'current_value': 5000,
            'unit': 'steps',
            'start_date': date.today().strftime('%Y-%m-%d'),
            'status': 'ACTIVE'
        })
        self.assertEqual(response.status_code, 302)
        goal = HealthGoal.objects.get(title='Daily Steps Goal')
        self.assertEqual(goal.progress_percentage, 50)

        # Update progress to 10000 -> completes goal
        res_up = self.client.post(reverse('wellness:goal_update_progress', args=[goal.id]), {
            'current_value': 10500
        })
        self.assertEqual(res_up.status_code, 302)
        goal.refresh_from_db()
        self.assertEqual(goal.status, 'COMPLETED')
        self.assertEqual(goal.progress_percentage, 100)

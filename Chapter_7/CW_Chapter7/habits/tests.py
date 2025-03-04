from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.

class HabitsTestCase(APITestCase):
    def setUp(self):
        pass

    def test_create_habit(self):
        """ Тестирование создания привычки."""
        data = {
            'action': 'Test'
        }
        responce = self.client.post(
            'habits/',
            data=data
        )
        self.assertEqual(
            responce.status_code,
            status.HTTP_201_CREATED
        )
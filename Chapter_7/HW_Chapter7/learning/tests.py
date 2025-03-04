from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from learning.models import Lesson, Course

from users.models import User

from learning.models import Subscription


class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="admin2@mail.ru")
        self.course = Course.objects.create(course_name="Психология")
        self.lesson = Lesson.objects.create(
            lesson_name="познание себя", course=self.course, owner=self.user
        )
        self.client.force_authenticate(
            user=self.user
        )  # используется для аутентификации пользователей

    def test_lesson_retrieve(self):
        self.url = reverse("learning:lesson-get", args=(self.lesson.pk,))
        response = self.client.get(self.url)
        # print(response.json())
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("lesson_name"), self.lesson.lesson_name)
        self.assertEqual(data.get("lesson_description"), self.lesson.lesson_description)
        self.assertEqual(data.get("url_video"), self.lesson.url_video)

    def test_lesson_create(self):
        self.url = reverse("learning:lesson-create")
        data = {"lesson_name": "аура"}
        response = self.client.post(self.url, data)
        # print(response.json())

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        self.url = reverse("learning:lesson-update", args=(self.lesson.pk,))

        data = {"lesson_name": "познание себя new"}
        response = self.client.patch(self.url, data)
        # print(response.json())

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("lesson_name"), "познание себя new")

    def test_lesson_delete(self):
        self.url = reverse("learning:lesson-delete", args=(self.lesson.pk,))
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        self.url = reverse("learning:lesson-list")
        response = self.client.get(self.url)
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "url_video": None,
                    "lesson_name": "познание себя",
                    "lesson_description": None,
                    "lesson_image": None,
                    "course": self.course.pk,
                    "owner": self.user.pk,
                }
            ],
        }
        data = response.json()
        # print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='admin2@mail.ru')
        self.course = Course.objects.create(course_name='Test Course', course_description='Test Course')
        self.subscription = Subscription.objects.create(user=self.user, course=self.course)
        self.client.force_authenticate(user=self.user)

    def test_subscription_create(self):
        self.url = reverse("learning:subscription-create")
        data = {
            'user': self.user.pk,
            'course': self.course.pk,
        }
        response = self.client.post(self.url, data)
        print(response.json())
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )

    def test_subscription_list(self):
        self.url = reverse("learning:subscription-list")
        response = self.client.get(self.url)
        print(response.json())
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

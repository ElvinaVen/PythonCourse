from django.urls import path
from rest_framework.routers import DefaultRouter

from learning.apps import LearningConfig

from learning.views import (
    CourseViewSet,
    LessonCreateAPIView,
    LessonListAPIView,
    LessonRetrieveAPIView,
    LessonUpdateAPIView,
    LessonDestroyAPIView,
)

from learning.views import SubscriptionCreateAPIView

from learning.views import SubscriptionListAPIView

app_name = LearningConfig.name

router = DefaultRouter()
router.register(r"course", CourseViewSet, basename="course")

urlpatterns = [
    path("lesson/create/", LessonCreateAPIView.as_view(), name="lesson-create"),
    path("lesson/list/", LessonListAPIView.as_view(), name="lesson-list"),
    path("lesson/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson-get"),
    path(
        "lesson/update/<int:pk>/", LessonUpdateAPIView.as_view(), name="lesson-update"
    ),
    path(
        "lesson/delete/<int:pk>/", LessonDestroyAPIView.as_view(), name="lesson-delete"
    ),
    path("subscription/create/", SubscriptionCreateAPIView.as_view(), name="subscription-create"),
    path('subscription/list/', SubscriptionListAPIView.as_view(), name='subscription_list'),
] + router.urls

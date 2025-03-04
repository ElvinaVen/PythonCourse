from django.urls import path
from rest_framework.routers import SimpleRouter

from habits.apps import HabitsConfig

from habits.views import HabitViewSet, UserHabitViewSet



app_name = HabitsConfig.name

router = SimpleRouter()
router.register(r"", HabitViewSet)

urlpatterns = [
    path("user_habits_list/", UserHabitViewSet.as_view(), name="user_habits_list")
]+ router.urls

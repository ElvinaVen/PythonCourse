from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.serializer import HabitSerializer
from users.permissions import IsModer, IsOwner


class HabitViewSet(ModelViewSet):
    """
    Представление для модели Habit
    """

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [AllowAny, ]

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()

    def get_permissions(self):
        if self.action in ["retrieve", "update", "partial_update", "destroy"]:
            self.permission_classes = [IsOwner | IsModer]
        return super().get_permissions()


class UserHabitViewSet(APIView):
    """
    Представление для получения списка всех привычек пользователя
    """

    def get(self, request):
        habits = Habit.objects.filter(user=request.user)
        paginator = HabitPaginator()
        result = paginator.paginate_queryset(habits, request)
        serializer = HabitSerializer(result, many=True)
        return paginator.get_paginated_response(serializer.data)

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView, get_object_or_404,
)
from learning.models import Course, Lesson
from learning.serializers import (
    CourseSerializer,
    LessonSerializer,
    CourseDetailSerializer,
)

from users.permissions import IsModerator

from users.permissions import IsOwner

from learning.models import Subscription
from learning.serializers import SubscriptionSerializer
from rest_framework.response import Response

from learning.paginators import CoursePaginator, LessonPaginator


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    pagination_class = CoursePaginator

    def get_serializer_class(self):
        if self.action == "retrieve":
            return CourseDetailSerializer
        return CourseSerializer

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        if self.action == ["create"]:
            self.permission_classes = (~IsModerator,)
        elif self.action in ["retrieve", "update"]:
            self.permission_classes = (IsModerator | IsOwner,)
        elif self.action == "destroy":
            self.permission_classes = (~IsModerator | IsOwner,)
        return super().get_permissions()




class LessonCreateAPIView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (~IsModerator, IsAuthenticated)  # должен быть не модером и дб авторизованным

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListAPIView(ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsModerator]

    pagination_class = LessonPaginator


class LessonRetrieveAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsModerator | IsOwner)  # дб авторизованным и либо модером либо владельцем


class LessonUpdateAPIView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsModerator | IsOwner)


class LessonDestroyAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = (
    IsAuthenticated, IsOwner | ~IsModerator)  # дб авторизованным и либо не модером либо владельцем


class SubscriptionListAPIView(ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsModerator]


class SubscriptionCreateAPIView(CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def post(self, *args, **kwargs):
        user = self.request.user  # получаем пользователя из self.request
        course_id = self.request.data.get('course')  # получаем id курса из self.request.data
        course_item = get_object_or_404(Course, pk=course_id)  # получаем объект курса из базы с помощью get_object_or_404

        subs_item = Subscription.objects.filter(user=user, course=course_item)  # получаем объекты подписок по текущему пользователю и курса

        if subs_item.exists():  # Если подписка у пользователя на этот курс есть - удаляем ее
            subs_item.delete()
            message = 'подписка удалена'
        else:  # Если подписки у пользователя на этот курс нет - создаем ее
            Subscription.objects.create(user=user, course=course_item)
            message = 'подписка добавлена'
        return Response({"message": message}, status=status.HTTP_201_CREATED)  # Возвращаем ответ в API

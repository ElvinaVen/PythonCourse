from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from learning.models import Course, Lesson

from learning.validators import validate_youtube

from learning.models import Subscription


class CourseSerializer(ModelSerializer):
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_is_subscribed(self, obj):
        """
        при выборке данных по курсу пользователю необходимо присылать признак подписки текущего пользователя на курс
        """
        user = self.context['request'].user
        return Subscription.objects.all().filter(user=user, course=obj).exists()



class LessonSerializer(ModelSerializer):
    url_video = serializers.CharField(validators=[validate_youtube])

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    lessons_count = SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def get_lessons_count(self, obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = ("course_name", "lessons_count", "lessons")


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"

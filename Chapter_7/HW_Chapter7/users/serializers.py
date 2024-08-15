from rest_framework.serializers import ModelSerializer
from users.models import Payment


class PaymentSerializer(ModelSerializer):

    class Meta:
        model = Payment
        fields = "__all__"


# class LessonSerializer(ModelSerializer):
#
#     class Meta:
#         model = Lesson
#         fields = "__all__"
#
#
# class CourseDetailSerializer(ModelSerializer):
#     lessons_count = SerializerMethodField()
#     lessons = LessonSerializer(many=True, read_only=True)
#
#     def get_lessons_count(self, obj):
#         return obj.lessons.count()
#
#     class Meta:
#         model = Course
#         fields = ('course_name', 'lessons_count', 'lessons')




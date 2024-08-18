from rest_framework.generics import ListAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.models import Payment

from users.serializers import PaymentSerializer, UserSerializer

from users.models import User


class PaymentListAPIView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ("paid_lesson", "paid_course", "payment_type")
    ordering_fields = ("-payment_date",)


class UsersCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()

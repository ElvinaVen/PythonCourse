from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny

from vehicle.models import Car, Moto, Milage
from vehicle.serializers import (
    CarSerializer,
    MotoSerializer,
    MilageSerializer,
    MotoMilageSerializer,
    MotoCreateSerializer,
)

from vehicle.permissions import IsOwnerOrStaff

from vehicle.paginators import VehiclePaginator

from vehicle.tasks import check_milage


class CarViewSet(viewsets.ModelViewSet):
    """
    ViewSet for cars
    """
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]  # для проверки тестов


class MotoCreateAPIView(generics.CreateAPIView):
    serializer_class = MotoCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_moto = serializer.save()
        new_moto.owner = self.request.user
        new_moto.save()


class MotoListAPIView(generics.ListAPIView):
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer
    pagination_class = VehiclePaginator


class MotoRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer


class MotoUpdateAPIView(generics.UpdateAPIView):
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer
    permission_classes = [IsOwnerOrStaff]


class MotoDestroyAPIView(generics.DestroyAPIView):
    queryset = Moto.objects.all()


class MilageCreateAPIView(generics.CreateAPIView):
    serializer_class = MilageSerializer

    def perform_create(self, serializer):
        new_milage = serializer.save()
        if new_milage.car:
            check_milage.delay(new_milage.car_id, "Car")
        else:
            check_milage.delay(new_milage.moto_id, "Moto")


class MilageListAPIView(generics.ListAPIView):
    queryset = Milage.objects.all()
    serializer_class = MilageSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ("car", "moto")
    ordering_fields = ("year",)
    pagination_class = VehiclePaginator


class MotoMilageListAPIView(generics.ListAPIView):
    queryset = Milage.objects.filter(moto__isnull=False)
    serializer_class = MotoMilageSerializer
    pagination_class = VehiclePaginator

from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from vehicle.models import Car, Moto, Milage
from vehicle.serializers import (
    CarSerializer,
    MotoSerializer,
    MilageSerializer,
    MotoMilageSerializer,
    MotoCreateSerializer,
)


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class MotoCreateAPIView(generics.CreateAPIView):
    serializer_class = MotoCreateSerializer


class MotoListAPIView(generics.ListAPIView):
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer


class MotoRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer


class MotoUpdateAPIView(generics.UpdateAPIView):
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer


class MotoDestroyAPIView(generics.DestroyAPIView):
    queryset = Moto.objects.all()


class MilageCreateAPIView(generics.CreateAPIView):
    serializer_class = MilageSerializer


class MilageListAPIView(generics.ListAPIView):
    queryset = Milage.objects.all()
    serializer_class = MilageSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('car', 'moto')
    ordering_fields = ('year',)


class MotoMilageListAPIView(generics.ListAPIView):
    queryset = Milage.objects.filter(moto__isnull=False)
    serializer_class = MotoMilageSerializer



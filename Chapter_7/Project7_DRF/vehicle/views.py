from rest_framework import viewsets, generics

from vehicle.models import Car, Moto
from vehicle.serializers import CarSerializer, MotoSerializer


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class MotoCreateAPIView(generics.CreateAPIView):
    serializer_class = MotoSerializer


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

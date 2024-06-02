from django.urls import path

from main.views import index, contact

from main.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
]

from django.urls import path

from main.views import contact, StudentListView, StudentDetailView

from main.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', StudentListView.as_view(), name='index'),
    path('contact/', contact, name='contact'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='view_student'),
]

from django.urls import path
from django.views.decorators.cache import cache_page

from main.views import contact, StudentListView, StudentDetailView, StudentCreateView, StudentUpdateView, StudentDeleteView, toggle_active

from main.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', cache_page(60)(StudentListView.as_view()), name='index'),
    path('contact/', contact, name='contact'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='view_student'),
    path('create/', StudentCreateView.as_view(), name='create_student'),
    path('edit/<int:pk>/', StudentUpdateView.as_view(), name='update_student'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='delete_student'),
    path('activity/<int:pk>/', toggle_active, name='toggle_activity')
]

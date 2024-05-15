from django.urls import path

from main.views import index
from views import index

app_name = 'students_list'

urlpatterns = [
    path('', index)
]
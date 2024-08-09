from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("learning/", include("learning.urls", namespace="learning")),
]

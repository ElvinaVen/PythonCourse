
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path("users/", include("users.urls", namespace="users")),
    path("blogs/", include("blogs.urls", namespace="blogs")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

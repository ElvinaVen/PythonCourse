from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig

from users.views import RegisterView, email_verification

from users.views import ProfileView

from users.views import reset_password

app_name = UsersConfig.name
urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('reset_password/', reset_password, name='reset_password'),
    path('profile/', ProfileView.as_view(), name='profile'),
]

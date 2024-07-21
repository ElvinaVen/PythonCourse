from django.urls import path


# from main.views import NewsletterListView

from main.apps import MainConfig

from main.views import NewsletterListView, NewsletterDetailView

app_name = MainConfig.name

urlpatterns = [
    path('', NewsletterListView.as_view(), name='index'),
    path('newsletter/<int:pk>/', NewsletterDetailView.as_view(), name='view_newsletter'),

    # path('student/<int:pk>/', StudentDetailView.as_view(), name='view_student'),
    # path('create/', StudentCreateView.as_view(), name='create_student'),
    # path('edit/<int:pk>/', StudentUpdateView.as_view(), name='update_student'),
    # path('delete/<int:pk>/', StudentDeleteView.as_view(), name='delete_student'),
    # path('activity/<int:pk>/', toggle_active, name='toggle_activity')
]

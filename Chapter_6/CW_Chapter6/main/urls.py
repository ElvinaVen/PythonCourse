from django.urls import path


# from main.views import NewsletterListView

from main.apps import MainConfig

from main.views import NewsletterListView, NewsletterDetailView, NewsletterCreateView, NewsletterUpdateView, NewsletterDeleteView

app_name = MainConfig.name

urlpatterns = [
    path('', NewsletterListView.as_view(), name='index'),
    path('newsletter/<int:pk>/', NewsletterDetailView.as_view(), name='view_newsletter'),
    path('create/', NewsletterCreateView.as_view(), name='create_newsletter'),
    path('edit/<int:pk>/', NewsletterUpdateView.as_view(), name='update_newsletter'),
    path('delete/<int:pk>/', NewsletterDeleteView.as_view(), name='delete_newsletter'),
    # path('activity/<int:pk>/', toggle_active, name='toggle_activity')
]

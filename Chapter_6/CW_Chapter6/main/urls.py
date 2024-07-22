from django.urls import path
from main.apps import MainConfig
from main.views import NewsletterListView, NewsletterDetailView, NewsletterCreateView, NewsletterUpdateView, \
    NewsletterDeleteView, IndexView, ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView, \
    ClientDetailView

app_name = MainConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('newsletter/', NewsletterListView.as_view(), name='list_newsletter'),
    path('newsletter/<int:pk>/', NewsletterDetailView.as_view(), name='view_newsletter'),
    path('newsletter/create/', NewsletterCreateView.as_view(), name='create_newsletter'),
    path('newsletter/edit/<int:pk>/', NewsletterUpdateView.as_view(), name='update_newsletter'),
    path('newsletter/delete/<int:pk>/', NewsletterDeleteView.as_view(), name='delete_newsletter'),

    path('client/', ClientListView.as_view(), name='list_client'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='view_client'),
    path('client/create/', ClientCreateView.as_view(), name='create_client'),
    path('client/edit/<int:pk>/', ClientUpdateView.as_view(), name='update_client'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),
]

from django.urls import path
from main.apps import MainConfig
from main.views import NewsletterListView, NewsletterDetailView, NewsletterCreateView, NewsletterUpdateView, \
    NewsletterDeleteView, IndexView, ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView, \
    ClientDetailView,MessageListView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView

from main.views import LogListView

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

    path('message/', MessageListView.as_view(), name='list_message'),
    path('message/<int:pk>/', MessageDetailView.as_view(), name='view_message'),
    path('message/create/', MessageCreateView.as_view(), name='create_message'),
    path('message/edit/<int:pk>/', MessageUpdateView.as_view(), name='update_message'),
    path('message/delete/<int:pk>/', MessageDeleteView.as_view(), name='delete_message'),

    path('log_list/', LogListView.as_view(), name='log_list'),
]

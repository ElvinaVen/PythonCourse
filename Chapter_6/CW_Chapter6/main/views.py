from random import random

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from main.models import Newsletter, Client


class IndexView(TemplateView):
    template_name = 'main/index.html'
    extra_context = {
        'title': 'Главная',
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # context_data['mail_count'] = get_cache_for_mailings()
        # context_data['active_mail_count'] = len(Newsletter.objects.filter(is_active=True))
        context_data['client_count'] = len(Client.objects.all())
        # context_data['object_list'] = random.sample(list(Blog.objects.all()), 3)
        return context_data


class NewsletterListView(ListView):
    model = Newsletter
    extra_context = {
        'title': "Рассылки ",
    }
    template_name = 'main/newsletter_list.html'
    success_url = reverse_lazy('main:newsletter_list')


class NewsletterDetailView(DetailView):
    model = Newsletter
    extra_context = {
        'title': "Рассылки ",
    }
    success_url = reverse_lazy('main:list_newsletter')
    # template_name = 'main/newsletter_detail.html'


class NewsletterCreateView(CreateView):
    model = Newsletter
    extra_context = {
        'title': "Рассылки ",
    }
    fields = '__all__'
    success_url = reverse_lazy('main:list_newsletter')


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    extra_context = {
        'title': "Рассылки ",
    }
    fields = '__all__'
    success_url = reverse_lazy('main:list_newsletter')


class NewsletterDeleteView(DeleteView):
    model = Newsletter
    extra_context = {
        'title': "Рассылки ",
    }
    success_url = reverse_lazy('main:list_newsletter')


class ClientListView(ListView):
    model = Client
    extra_context = {
        'title': "Клиенты",
    }
    template_name = 'main/client_list.html'
    success_url = reverse_lazy('main:list_client')


class ClientCreateView(CreateView):
    model = Client
    extra_context = {
        'title': "Клиенты",
    }
    fields = '__all__'
    success_url = reverse_lazy('main:list_client')


class ClientDetailView(DetailView):
    model = Client
    extra_context = {
        'title': "Клиенты",
    }
    success_url = reverse_lazy('main:list_client')
    # template_name = 'main/newsletter_detail.html'


class ClientUpdateView(UpdateView):
    model = Client
    extra_context = {
        'title': "Клиенты",
    }
    fields = '__all__'
    success_url = reverse_lazy('main:list_client')


class ClientDeleteView(DeleteView):
    model = Client
    extra_context = {
        'title': "Клиенты",
    }
    success_url = reverse_lazy('main:list_client')

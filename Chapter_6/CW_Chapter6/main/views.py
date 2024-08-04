from random import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from main.models import Newsletter, Client, Message, Log

from main.forms import NewsletterForm, MessageForm, ClientForm

from main.forms import ManagerNewsletterForm
from main.services import get_newsletter_from_cache

from blogs.models import Blog

from blogs.services import get_articles_from_cache


class IndexView(TemplateView):
    template_name = 'main/index.html'
    extra_context = {
        'title': 'Главная',
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['mail_count'] = len(get_newsletter_from_cache())
        context_data['active_mail_count'] = len(Newsletter.objects.filter(status__in=('создана', 'запущена')))
        context_data['client_count'] = len(Client.objects.all())
        # context_data['object_list'] = random.sample(list(Blog.objects.all()), 3)
        context_data['random_blogs'] = get_articles_from_cache().order_by('?')[:3]
        return context_data


class NewsletterListView(LoginRequiredMixin, ListView):
    model = Newsletter
    extra_context = {
        'title': "Рассылки ",
    }
    template_name = 'main/newsletter_list.html'
    success_url = reverse_lazy('main:newsletter_list')

    def get_queryset(self, queryset=None):
        queryset = super().get_queryset()
        user = self.request.user
        if not user.is_superuser and not user.groups.filter(name='manager'):
            queryset = queryset.filter(owner=self.request.user)
        return queryset


class NewsletterDetailView(LoginRequiredMixin, DetailView):
    model = Newsletter
    extra_context = {
        'title': "Рассылки ",
    }
    success_url = reverse_lazy('main:list_newsletter')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if not user.is_superuser and not user.groups.filter(name='manager') and user != self.object.owner:
            raise PermissionDenied
        else:
            return self.object


class NewsletterCreateView(LoginRequiredMixin, CreateView):
    model = Newsletter
    form_class = NewsletterForm
    extra_context = {
        'title': "Рассылки ",
    }
    success_url = reverse_lazy('main:list_newsletter')

    def form_valid(self, form):
        newsletter = form.save()
        user = self.request.user
        newsletter.owner = user
        newsletter.save()
        return super().form_valid(form)


class NewsletterUpdateView(LoginRequiredMixin, UpdateView):
    model = Newsletter
    extra_context = {
        'title': "Рассылки ",
    }
    form_class = NewsletterForm
    success_url = reverse_lazy('main:list_newsletter')

    def get_form_class(self):
        """
        Функция, определяющая поля для редактирования в зависимости от прав пользователя
        """
        user = self.request.user
        if user == self.object.owner or user.is_superuser:
            return NewsletterForm
        elif user.has_perm('main.deactivate_mailing'):
            return ManagerNewsletterForm
        else:
            raise PermissionDenied


class NewsletterDeleteView(LoginRequiredMixin, DeleteView):
    model = Newsletter
    extra_context = {
        'title': "Рассылки ",
    }
    success_url = reverse_lazy('main:list_newsletter')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner or self.request.user.is_superuser:
            return self.object
        raise PermissionDenied


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    extra_context = {
        'title': "Клиенты",
    }
    template_name = 'main/client_list.html'
    success_url = reverse_lazy('main:list_client')

    def get_queryset(self, queryset=None):
        queryset = super().get_queryset()
        user = self.request.user
        if not user.is_superuser and not user.groups.filter(name='manager'):
            queryset = queryset.filter(owner=self.request.user)
        return queryset


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    extra_context = {
        'title': "Клиенты",
    }
    form_class = ClientForm
    success_url = reverse_lazy('main:list_client')

    def form_valid(self, form):
        client = form.save()
        user = self.request.user
        client.owner = user
        client.save()
        return super().form_valid(form)


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    extra_context = {
        'title': "Клиенты",
    }
    success_url = reverse_lazy('main:list_client')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner or self.request.user.is_superuser:
            return self.object
        raise PermissionDenied


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    extra_context = {
        'title': "Клиенты",
    }
    form_class = ClientForm
    success_url = reverse_lazy('main:list_client')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner or self.request.user.is_superuser:
            return self.object
        raise PermissionDenied


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    extra_context = {
        'title': "Клиенты",
    }
    success_url = reverse_lazy('main:list_client')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner or self.request.user.is_superuser:
            return self.object
        raise PermissionDenied


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    extra_context = {
        'title': "Сообщения",
    }
    template_name = 'main/message_list.html'
    success_url = reverse_lazy('main:list_message')

    def get_queryset(self, queryset=None):
        queryset = super().get_queryset()
        user = self.request.user
        if not user.is_superuser and not user.groups.filter(name='manager'):
            queryset = queryset.filter(owner=self.request.user)
        return queryset


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    extra_context = {
        'title': "Сообщения",
    }
    form_class = MessageForm
    success_url = reverse_lazy('main:list_message')

    def form_valid(self, form):
        message = form.save()
        user = self.request.user
        message.owner = user
        message.save()
        return super().form_valid(form)


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    extra_context = {
        'title': "Сообщения",
    }
    success_url = reverse_lazy('main:list_message')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner or self.request.user.is_superuser:
            return self.object
        raise PermissionDenied


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    extra_context = {
        'title': "Сообщения",
    }
    form_class = MessageForm
    success_url = reverse_lazy('main:list_message')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner or self.request.user.is_superuser:
            return self.object
        raise PermissionDenied


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    extra_context = {
        'title': "Сообщения",
    }
    success_url = reverse_lazy('main:list_message')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner or self.request.user.is_superuser:
            return self.object
        raise PermissionDenied


class LogListView(LoginRequiredMixin, ListView):
    """
    Контроллер отвечающий за отображение списка попыток рассылок
    """
    model = Log

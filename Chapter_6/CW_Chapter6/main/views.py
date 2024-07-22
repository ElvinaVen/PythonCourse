from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main.models import Newsletter, Client
# from main.forms import NewsletterForm


class NewsletterListView(ListView):
    model = Newsletter
    # template_name = 'main/index.html'


class NewsletterDetailView(DetailView):
    model = Newsletter
    # template_name = 'main/newsletter_detail.html'


class NewsletterCreateView(CreateView):
    model = Newsletter
    fields = '__all__'
    success_url = reverse_lazy('main:index')


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    fields = '__all__'
    success_url = reverse_lazy('main:index')


class NewsletterDeleteView(DeleteView):
    model = Newsletter
    success_url = reverse_lazy('main:index')



def client(request):
    client_list = Client.objects.all()
    context = {
        'object_list': client_list,
        'title': 'Клиенты'
    }
    return render(request, 'main/client.html', context)

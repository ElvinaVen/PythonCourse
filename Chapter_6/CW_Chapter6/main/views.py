from django.shortcuts import render
from django.views.generic import ListView, DetailView

from main.models import Newsletter, Client


class NewsletterListView(ListView):
    model = Newsletter
    # template_name = 'main/index.html'


class NewsletterDetailView(DetailView):
    model = Newsletter
    # template_name = 'main/newsletter_detail.html'


def client(request):
    client_list = Client.objects.all()
    context = {
        'object_list': client_list,
        'title': 'Клиенты'
    }
    return render(request, 'main/client.html', context)

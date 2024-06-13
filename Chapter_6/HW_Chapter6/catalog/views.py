from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import render
from catalog.models import Product


# def home(request):
#     return render(request, "home.html")

class ContactTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

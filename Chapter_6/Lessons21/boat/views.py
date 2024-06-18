

from django.shortcuts import render

from boat.models import Boat
from django.views.generic import ListView, DetailView


class BoatListView(ListView):
    model = Boat


class BoatDetailView(DetailView):
    model = Boat

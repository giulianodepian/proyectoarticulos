from django.shortcuts import render
from .models import Articulos
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.


class ArticulosListView(ListView):
    model = Articulos


class ArticulosDetailView(DetailView):
    model = Articulos

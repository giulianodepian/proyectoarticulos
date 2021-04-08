from django.shortcuts import render
from .models import Articulos
from django.views.generic.list import ListView

# Create your views here.


class ArticulosListView(ListView):
    model = Articulos

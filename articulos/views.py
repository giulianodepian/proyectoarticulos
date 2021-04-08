from django.shortcuts import render
from .models import Articulos
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse

# Create your views here.


class ArticulosListView(ListView):
    model = Articulos


class ArticulosDetailView(DetailView):
    model = Articulos


class ArticulosCreateView(CreateView):
    model = Articulos
    fields = ['titulo', 'descripcion']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articulo', kwargs={'pk': self.object.id})


class ArticulosUpdateView(UpdateView):
    model = Articulos
    fields = ['titulo', 'descripcion']

    def get_success_url(self):
        return reverse('articulo', kwargs={'pk': self.object.id})


class ArticulosDeleteView(DeleteView):
    model = Articulos

    def get_success_url(self):
        return reverse('index')

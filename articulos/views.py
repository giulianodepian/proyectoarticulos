from django.shortcuts import redirect
from .models import Articulos
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import CustomUserCreation
from django.shortcuts import render

# Create your views here.


class ArticulosListView(ListView):
    model = Articulos


class ArticulosDetailView(DetailView):
    model = Articulos


@method_decorator(login_required, name='dispatch')
class ArticulosCreateView(CreateView):
    model = Articulos
    fields = ['titulo', 'descripcion']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articulo', kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class ArticulosUpdateView(UpdateView):
    model = Articulos
    fields = ['titulo', 'descripcion']

    def get_success_url(self):
        return reverse('articulo', kwargs={'pk': self.object.id})


@method_decorator(login_required, name='dispatch')
class ArticulosDeleteView(DeleteView):
    model = Articulos

    def get_success_url(self):
        return reverse('index')


class Login(LoginView):
    template_name = 'templates/login.html'


class Logout(LogoutView):
    template_name = 'templates/logout.html'
    next_page = '/'


class CreateView(View):
    def post(self, request):
        form = CustomUserCreation(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
        return render(request, 'templates/crearUsuario.html', {'form': form})

    def get(self, request):
        form = CustomUserCreation()
        return render(request, 'templates/crearUsuario.html', {'form': form})

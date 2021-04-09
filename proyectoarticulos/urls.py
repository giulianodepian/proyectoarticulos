"""proyectoarticulos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from articulos.views import ArticulosListView, ArticulosDetailView, ArticulosCreateView, ArticulosUpdateView, ArticulosDeleteView, LoginView, LogoutView, CreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ArticulosListView.as_view(template_name='templates/index.html'), name='index'),
    path('articulo/<int:pk>/', ArticulosDetailView.as_view(template_name='templates/articulo.html'), name='articulo'),
    path('crearArticulo/', ArticulosCreateView.as_view(template_name='templates/crearArticulo.html'), name='crearArticulo'),
    path('modificarArticulo/<int:pk>/', ArticulosUpdateView.as_view(template_name='templates/modificarArticulo.html'), name='modificarArticulo'),
    path('eliminarArticulo/<int:pk>/', ArticulosDeleteView.as_view(template_name='templates/eliminarArticulo.html'), name='eliminarArticulo'),
    path('login/', LoginView.as_view(template_name='templates/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='templates/logout.html', next_page='/'), name='logout'),
    path('crearUsuario/', CreateView.as_view(), name='crearUsuario')
]

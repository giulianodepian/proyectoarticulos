from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Articulos(models.Model):
    titulo = models.CharField(max_length=50)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateTimeField(auto_now=True)
    descripcion = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "articulos"

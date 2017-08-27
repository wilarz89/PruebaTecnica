from django.db import models

# Create your models here.
class Modelo(models.Model):
    entrada = models.CharField(max_length=10000)
    salida = models.CharField(max_length=10000)
    fechaCreacion = models.DateTimeField(auto_now_add=True)


# cliente/models.py

from django.db import models
from django.contrib.auth.models import User

class PerfilCliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre_completo = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    empresa = models.CharField(max_length=255)
    numero_telefono = models.CharField(max_length=20)
    correo_electronico = models.EmailField()

    def __str__(self):
        return self.nombre_completo

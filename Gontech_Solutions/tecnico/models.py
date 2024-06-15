# tecnico/models.py

from django.db import models
from django.contrib.auth.models import User

class PerfilTecnico(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre_completo = models.CharField(max_length=255)
    fecha_de_nacimiento = models.DateField()
    direccion = models.CharField(max_length=255)
    celular = models.CharField(max_length=20)
    correo_electronico = models.EmailField()
    estado = models.CharField(max_length=20, choices=[
        ('habilitado', 'Habilitado'),
        ('no_habilitado', 'No Habilitado')
    ])

    def __str__(self):
        return self.nombre_completo

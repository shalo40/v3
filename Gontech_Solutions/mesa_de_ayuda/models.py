# mesa_de_ayuda/models.py

from django.db import models
from django.contrib.auth.models import User

class TicketServicio(models.Model):
    DESARROLLO = 'Desarrollo'
    SERVICIO_TECNICO = 'Servicio Técnico'
    CONSULTORIA_TI = 'Consultoría TI'
    TIPO_SERVICIO_CHOICES = [
        (DESARROLLO, 'Desarrollo'),
        (SERVICIO_TECNICO, 'Servicio Técnico'),
        (CONSULTORIA_TI, 'Consultoría TI'),
    ]

    nombre_completo = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    empresa = models.CharField(max_length=255)
    numero_telefono = models.CharField(max_length=20)
    correo_electronico = models.EmailField()
    descripcion_problema = models.TextField()
    tipo_servicio = models.CharField(max_length=50, choices=TIPO_SERVICIO_CHOICES)
    urgencia_servicio = models.CharField(max_length=50)
    plazo_deseado = models.DateField()
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    prioridad = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets_creados')

    def __str__(self):
        return self.descripcion_problema

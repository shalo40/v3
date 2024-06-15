# mesa_de_ayuda/models.py

from django.db import models
from cliente.models import PerfilCliente

class TicketServicio(models.Model):
    # Información del Solicitante (referencia al modelo PerfilCliente)
    cliente = models.ForeignKey(PerfilCliente, on_delete=models.CASCADE)
    
    # Detalles del Servicio Solicitado
    descripcion_problema = models.TextField()
    tipo_servicio = models.CharField(max_length=50, choices=[
        ('desarrollo', 'Desarrollo'),
        ('servicio_tecnico', 'Servicio Técnico'),
        ('consultoria_ti', 'Consultoría TI')
    ])
    urgencia_servicio = models.CharField(max_length=20, choices=[
        ('alta', 'Prioridad Alta'),
        ('media', 'Prioridad Media'),
        ('baja', 'Prioridad Baja')
    ])
    plazo_deseado = models.DateField()

    def __str__(self):
        return f'Ticket {self.id} para {self.cliente.nombre_completo}'

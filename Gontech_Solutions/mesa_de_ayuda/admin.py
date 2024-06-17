# mesa_de_ayuda/admin.py

from django.contrib import admin
from .models import TicketServicio

@admin.register(TicketServicio)
class TicketServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'tipo_servicio', 'prioridad', 'estado', 'fecha_creacion')
    search_fields = ('nombre_completo', 'empresa', 'tipo_servicio')
    list_filter = ('tipo_servicio', 'prioridad', 'estado')

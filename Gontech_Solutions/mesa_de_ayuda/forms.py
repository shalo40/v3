# mesa_de_ayuda/forms.py

from django import forms
from .models import TicketServicio

class TicketServicioForm(forms.ModelForm):
    class Meta:
        model = TicketServicio
        fields = [
            'nombre_completo', 'cargo', 'empresa', 'numero_telefono', 'correo_electronico',
            'descripcion_problema', 'tipo_servicio', 'urgencia_servicio', 'plazo_deseado',
            'cliente', 'prioridad', 'estado'
        ]

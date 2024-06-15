# mesa_de_ayuda/forms.py

from django import forms
from .models import TicketServicio

class TicketServicioForm(forms.ModelForm):
    class Meta:
        model = TicketServicio
        fields = ['cliente', 'descripcion_problema', 'tipo_servicio', 'urgencia_servicio', 'plazo_deseado']

# cliente/forms.py

from django import forms
from .models import PerfilCliente

class PerfilClienteForm(forms.ModelForm):
    class Meta:
        model = PerfilCliente
        fields = ['nombre_completo', 'cargo', 'empresa', 'numero_telefono', 'correo_electronico']

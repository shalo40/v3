# tecnico/forms.py

from django import forms
from .models import PerfilTecnico

class DateInput(forms.DateInput):
    input_type = 'date'

class PerfilTecnicoForm(forms.ModelForm):
    class Meta:
        model = PerfilTecnico
        fields = ['nombre_completo', 'fecha_de_nacimiento', 'direccion', 'celular', 'correo_electronico', 'estado']
        widgets = {
            'fecha_de_nacimiento': DateInput(attrs={'format': 'YYYY-MM-DD'}),
        }

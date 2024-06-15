# finanzas/forms.py

from django import forms
from .models import TransaccionFinanciera

class TransaccionFinancieraForm(forms.ModelForm):
    class Meta:
        model = TransaccionFinanciera
        fields = ['cliente', 'tipo_transaccion', 'monto', 'descripcion']

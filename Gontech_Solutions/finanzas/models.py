# finanzas/models.py

from django.db import models
from cliente.models import PerfilCliente

class TransaccionFinanciera(models.Model):
    cliente = models.ForeignKey(PerfilCliente, on_delete=models.CASCADE)
    fecha_transaccion = models.DateTimeField(auto_now_add=True)
    tipo_transaccion = models.CharField(max_length=50, choices=[
        ('compra', 'Compra'),
        ('pago', 'Pago'),
        ('abono', 'Abono')
    ])
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()

    def __str__(self):
        return f'Transacción {self.id} para {self.cliente.nombre_completo} - {self.tipo_transaccion}'

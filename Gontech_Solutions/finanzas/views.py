# finanzas/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import TransaccionFinanciera
from .forms import TransaccionFinancieraForm

def lista_transacciones(request):
    transacciones = TransaccionFinanciera.objects.all()
    return render(request, 'finanzas/lista_transacciones.html', {'transacciones': transacciones})

def detalle_transaccion(request, transaccion_id):
    transaccion = get_object_or_404(TransaccionFinanciera, id=transaccion_id)
    return render(request, 'finanzas/detalle_transaccion.html', {'transaccion': transaccion})

def crear_transaccion(request):
    if request.method == 'POST':
        form = TransaccionFinancieraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_transacciones')
    else:
        form = TransaccionFinancieraForm()
    return render(request, 'finanzas/crear_transaccion.html', {'form': form})

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .models import TransaccionFinanciera
from .forms import TransaccionFinancieraForm


@login_required
def lista_transacciones(request):
    transacciones = TransaccionFinanciera.objects.all()
    return render(request, 'finanzas/lista_transacciones.html', {'transacciones': transacciones})

@login_required
def detalle_transaccion(request, transaccion_id):
    transaccion = get_object_or_404(TransaccionFinanciera, id=transaccion_id)
    return render(request, 'finanzas/detalle_transaccion.html', {'transaccion': transaccion})

@login_required
def crear_transaccion(request):
    if request.method == 'POST':
        form = TransaccionFinancieraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_transacciones')
    else:
        form = TransaccionFinancieraForm()
    return render(request, 'finanzas/crear_transaccion.html', {'form': form})

@login_required
def generar_reporte_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_transacciones.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    p.setFont("Helvetica", 12)

    transacciones = TransaccionFinanciera.objects.all()
    y = 750

    p.drawString(100, 800, "Reporte de Transacciones Financieras")
    p.drawString(50, 770, "Cliente")
    p.drawString(200, 770, "Tipo de Transacción")
    p.drawString(350, 770, "Monto")
    p.drawString(450, 770, "Descripción")

    for transaccion in transacciones:
        p.drawString(50, y, transaccion.cliente.nombre_completo)
        p.drawString(200, y, transaccion.tipo_transaccion)
        p.drawString(350, y, str(transaccion.monto))
        p.drawString(450, y, transaccion.descripcion)
        y -= 20
        if y < 50:
            p.showPage()
            p.setFont("Helvetica", 12)
            y = 750

    p.showPage()
    p.save()
    return response

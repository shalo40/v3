# mesa_de_ayuda/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import TicketServicio
from .forms import TicketServicioForm

@login_required
def lista_tickets(request):
    tickets = TicketServicio.objects.all()
    return render(request, 'mesa_de_ayuda/lista_tickets.html', {'tickets': tickets})

@login_required
def detalle_ticket(request, id):
    ticket = get_object_or_404(TicketServicio, id=id)
    return render(request, 'mesa_de_ayuda/detalle_ticket.html', {'ticket': ticket})

@login_required
def crear_ticket(request):
    if request.method == 'POST':
        form = TicketServicioForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.usuario = request.user
            ticket.save()
            return redirect('lista_tickets')
    else:
        form = TicketServicioForm()
    return render(request, 'mesa_de_ayuda/crear_ticket.html', {'form': form})

@login_required
def comunicacion_clientes(request):
    return render(request, 'mesa_de_ayuda/comunicacion_clientes.html')

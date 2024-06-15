# mesa_de_ayuda/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import TicketServicio
from .forms import TicketServicioForm
from django.contrib.auth.decorators import login_required

@login_required
def lista_tickets(request):
    tickets = TicketServicio.objects.all()
    return render(request, 'mesa_de_ayuda/lista_tickets.html', {'tickets': tickets})

@login_required
def detalle_ticket(request, ticket_id):
    ticket = get_object_or_404(TicketServicio, id=ticket_id)
    return render(request, 'mesa_de_ayuda/detalle_ticket.html', {'ticket': ticket})

@login_required
def crear_ticket(request):
    if request.method == 'POST':
        form = TicketServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tickets')
    else:
        form = TicketServicioForm()
    return render(request, 'mesa_de_ayuda/crear_ticket.html', {'form': form})

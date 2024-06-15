from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import PerfilCliente
from .forms import PerfilClienteForm
from tecnico.views import generar_nombre_usuario
from django.contrib.auth.decorators import login_required


@login_required
def lista_clientes(request):
    clientes = PerfilCliente.objects.all()
    return render(request, 'cliente/lista_clientes.html', {'clientes': clientes})

@login_required
def detalle_cliente(request, cliente_id):
    cliente = get_object_or_404(PerfilCliente, id=cliente_id)
    return render(request, 'cliente/detalle_cliente.html', {'cliente': cliente})

@login_required
def crear_cliente(request):
    if request.method == 'POST':
        form = PerfilClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            nombre_usuario = generar_nombre_usuario(cliente.nombre_completo)
            usuario, creado = User.objects.get_or_create(username=nombre_usuario)
            if creado:
                usuario.set_password('defaultpassword')
                usuario.save()
            cliente.usuario = usuario
            cliente.save()
            return redirect('lista_clientes')
    else:
        form = PerfilClienteForm()
    return render(request, 'cliente/crear_cliente.html', {'form': form})

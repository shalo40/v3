# cliente/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import PerfilCliente
from .forms import PerfilClienteForm

def lista_clientes(request):
    clientes = PerfilCliente.objects.all()
    return render(request, 'cliente/lista_clientes.html', {'clientes': clientes})

def detalle_cliente(request, cliente_id):
    cliente = get_object_or_404(PerfilCliente, id=cliente_id)
    return render(request, 'cliente/detalle_cliente.html', {'cliente': cliente})

def generar_nombre_usuario(nombre_completo):
    nombres = nombre_completo.split()
    if len(nombres) < 2:
        return nombres[0][:3].lower()  # En caso de que solo haya un nombre, tomar los primeros 3 caracteres
    primer_nombre = nombres[0]
    primer_apellido = nombres[1]
    mitad_nombre = primer_nombre[:len(primer_nombre)//2].lower()
    mitad_apellido = primer_apellido[:len(primer_apellido)//2].lower()
    return mitad_nombre + mitad_apellido

def crear_cliente(request):
    if request.method == 'POST':
        form = PerfilClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            nombre_usuario = generar_nombre_usuario(cliente.nombre_completo)
            usuario, creado = User.objects.get_or_create(username=nombre_usuario)
            if creado:
                usuario.set_password('defaultpassword')  # Cambia esto para establecer una contraseña segura
                usuario.save()
            cliente.usuario = usuario
            cliente.save()
            return redirect('lista_clientes')
    else:
        form = PerfilClienteForm()
    return render(request, 'cliente/crear_cliente.html', {'form': form})

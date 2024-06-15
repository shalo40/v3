# tecnico/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import PerfilTecnico
from .forms import PerfilTecnicoForm

def lista_tecnicos(request):
    tecnicos = PerfilTecnico.objects.all()
    return render(request, 'tecnico/lista_tecnicos.html', {'tecnicos': tecnicos})

def detalle_tecnico(request, tecnico_id):
    tecnico = get_object_or_404(PerfilTecnico, id=tecnico_id)
    return render(request, 'tecnico/detalle_tecnico.html', {'tecnico': tecnico})

def generar_nombre_usuario(nombre_completo):
    nombres = nombre_completo.split()
    if len(nombres) < 2:
        return nombres[0][:3].lower()  # En caso de que solo haya un nombre, tomar los primeros 3 caracteres
    primer_nombre = nombres[0]
    primer_apellido = nombres[1]
    mitad_nombre = primer_nombre[:len(primer_nombre)//2].lower()
    mitad_apellido = primer_apellido[:len(primer_apellido)//2].lower()
    return mitad_nombre + mitad_apellido

def crear_tecnico(request):
    if request.method == 'POST':
        form = PerfilTecnicoForm(request.POST)
        if form.is_valid():
            tecnico = form.save(commit=False)
            nombre_usuario = generar_nombre_usuario(tecnico.nombre_completo)
            usuario, creado = User.objects.get_or_create(username=nombre_usuario)
            if creado:
                usuario.set_password('defaultpassword')  # Cambia esto para establecer una contraseña segura
                usuario.save()
            tecnico.usuario = usuario
            tecnico.save()
            return redirect('lista_tecnicos')
    else:
        form = PerfilTecnicoForm()
    return render(request, 'tecnico/crear_tecnico.html', {'form': form})

def editar_tecnico(request, tecnico_id):
    tecnico = get_object_or_404(PerfilTecnico, id=tecnico_id)
    if request.method == 'POST':
        form = PerfilTecnicoForm(request.POST, instance=tecnico)
        if form.is_valid():
            form.save()
            return redirect('detalle_tecnico', tecnico_id=tecnico.id)
    else:
        form = PerfilTecnicoForm(instance=tecnico)
    return render(request, 'tecnico/editar_tecnico.html', {'form': form})

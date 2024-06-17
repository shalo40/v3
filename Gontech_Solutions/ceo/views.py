
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def gestion_usuarios(request):
    # Lógica para la gestión de usuarios
    return render(request, 'ceo/gestion_usuarios.html')

@login_required
def gestion_proyectos(request):
    # Lógica para la gestión de proyectos
    return render(request, 'ceo/gestion_proyectos.html')

@login_required
def reportes_estadisticas(request):
    # Lógica para los reportes y estadísticas
    return render(request, 'ceo/reportes_estadisticas.html')

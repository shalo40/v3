# autenticacion/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard_administrador')  # Ajusta esto según tu vista de dashboard
        else:
            return HttpResponse("Usuario o contraseña incorrectos")
    return render(request, 'autenticacion/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    user = request.user
    if user.is_superuser or user.groups.filter(name='Administrador').exists():
        return redirect('dashboard_administrador')
    elif user.groups.filter(name='Gerente de Proyecto').exists():
        return redirect('dashboard_gerente')
    elif user.groups.filter(name='Desarrollador').exists():
        return redirect('dashboard_desarrollador')
    elif user.groups.filter(name='Cliente').exists():
        return redirect('dashboard_cliente')
    else:
        return redirect('login')  # Si no tiene un rol asignado, redirigir al login

@login_required
def dashboard_administrador(request):
    return render(request, 'autenticacion/dashboard_administrador.html')

@login_required
def dashboard_gerente(request):
    return render(request, 'autenticacion/dashboard_gerente.html')

@login_required
def dashboard_desarrollador(request):
    return render(request, 'autenticacion/dashboard_desarrollador.html')

@login_required
def dashboard_cliente(request):
    return render(request, 'autenticacion/dashboard_cliente.html')

@login_required
def gestion_usuarios(request):
    return render(request, 'autenticacion/gestion_usuarios.html')

@login_required
def gestion_proyectos(request):
    return render(request, 'autenticacion/gestion_proyectos.html')

@login_required
def reportes_estadisticas(request):
    return render(request, 'autenticacion/reportes_estadisticas.html')
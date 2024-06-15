# Gontech_Solutions/urls.py

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_login(request):
    return redirect('login')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_login, name='home'),  # Redirigir la URL raíz al inicio de sesión
    path('mesa_de_ayuda/', include('mesa_de_ayuda.urls')),
    path('tecnico/', include('tecnico.urls')),
    path('cliente/', include('cliente.urls')),
    path('finanzas/', include('finanzas.urls')),
    path('autenticacion/', include('autenticacion.urls')),
]

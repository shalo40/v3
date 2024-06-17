# Gontech_Solutions/urls.py

from django.contrib import admin
from django.urls import path, include
from autenticacion import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('autenticacion/', include('autenticacion.urls')),
    path('mesa_de_ayuda/', include('mesa_de_ayuda.urls')),
    path('tecnico/', include('tecnico.urls')),
    path('cliente/', include('cliente.urls')),
    path('finanzas/', include('finanzas.urls')),
    path('', auth_views.login_view, name='home'),  # Redirigir al login
]

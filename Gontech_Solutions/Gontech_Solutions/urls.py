# Gontech_Solutions/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mesa_de_ayuda/', include('mesa_de_ayuda.urls')),
    path('tecnico/', include('tecnico.urls')),
    path('cliente/', include('cliente.urls')),
]

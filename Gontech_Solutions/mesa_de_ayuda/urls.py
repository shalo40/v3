# mesa_de_ayuda/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('lista_tickets/', views.lista_tickets, name='lista_tickets'),
    path('detalle_ticket/<int:id>/', views.detalle_ticket, name='detalle_ticket'),
    path('crear_ticket/', views.crear_ticket, name='crear_ticket'),
    path('comunicacion_clientes/', views.comunicacion_clientes, name='comunicacion_clientes'),
]

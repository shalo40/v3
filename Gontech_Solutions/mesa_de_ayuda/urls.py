# mesa_de_ayuda/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tickets, name='lista_tickets'),
    path('<int:ticket_id>/', views.detalle_ticket, name='detalle_ticket'),
    path('crear/', views.crear_ticket, name='crear_ticket'),
]

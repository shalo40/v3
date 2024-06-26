# cliente/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),
    path('<int:cliente_id>/', views.detalle_cliente, name='detalle_cliente'),
    path('crear/', views.crear_cliente, name='crear_cliente'),
]

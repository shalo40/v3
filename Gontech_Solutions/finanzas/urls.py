# finanzas/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_transacciones, name='lista_transacciones'),
    path('<int:transaccion_id>/', views.detalle_transaccion, name='detalle_transaccion'),
    path('crear/', views.crear_transaccion, name='crear_transaccion'),
    path('reporte/', views.generar_reporte_pdf, name='generar_reporte_pdf'),
]

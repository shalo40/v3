# tecnico/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tecnicos, name='lista_tecnicos'),
    path('<int:tecnico_id>/', views.detalle_tecnico, name='detalle_tecnico'),
    path('crear/', views.crear_tecnico, name='crear_tecnico'),
    path('<int:tecnico_id>/editar/', views.editar_tecnico, name='editar_tecnico'),
]

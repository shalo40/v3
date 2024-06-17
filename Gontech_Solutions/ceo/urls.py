# ceo/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('gestion_usuarios/', views.gestion_usuarios, name='gestion_usuarios'),
    path('gestion_proyectos/', views.gestion_proyectos, name='gestion_proyectos'),
    path('reportes_estadisticas/', views.reportes_estadisticas, name='reportes_estadisticas'),
]

# autenticacion/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='autenticacion/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='autenticacion/logout.html'), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='autenticacion/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='autenticacion/password_change_done.html'), name='password_change_done'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard_administrador/', views.dashboard_administrador, name='dashboard_administrador'),
    path('dashboard_gerente/', views.dashboard_gerente, name='dashboard_gerente'),
    path('dashboard_desarrollador/', views.dashboard_desarrollador, name='dashboard_desarrollador'),
    path('dashboard_cliente/', views.dashboard_cliente, name='dashboard_cliente'),
    path('gestion_usuarios/', views.gestion_usuarios, name='gestion_usuarios'),
    path('gestion_proyectos/', views.gestion_proyectos, name='gestion_proyectos'),
     path('reportes_estadisticas/', views.reportes_estadisticas, name='reportes_estadisticas'),
]

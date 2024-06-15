# autenticacion/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='autenticacion/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='autenticacion/logout.html'), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='autenticacion/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='autenticacion/password_change_done.html'), name='password_change_done'),
]

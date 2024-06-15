# autenticacion/apps.py

from django.apps import AppConfig

class AutenticacionConfig(AppConfig):
    name = 'autenticacion'

    def ready(self):
        import autenticacion.signals

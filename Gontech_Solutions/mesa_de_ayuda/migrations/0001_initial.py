# Generated by Django 5.0.6 on 2024-06-16 14:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=255)),
                ('cargo', models.CharField(max_length=255)),
                ('empresa', models.CharField(max_length=255)),
                ('numero_telefono', models.CharField(max_length=20)),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('descripcion_problema', models.TextField()),
                ('tipo_servicio', models.CharField(choices=[('Desarrollo', 'Desarrollo'), ('Servicio Técnico', 'Servicio Técnico'), ('Consultoría TI', 'Consultoría TI')], max_length=50)),
                ('urgencia_servicio', models.CharField(max_length=50)),
                ('plazo_deseado', models.DateField()),
                ('prioridad', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets_creados', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

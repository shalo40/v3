# Generated by Django 5.0.6 on 2024-06-15 13:06

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
            name='PerfilTecnico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=255)),
                ('fecha_de_nacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=255)),
                ('celular', models.CharField(max_length=20)),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('estado', models.CharField(choices=[('habilitado', 'Habilitado'), ('no_habilitado', 'No Habilitado')], max_length=20)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

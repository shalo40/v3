# Generated by Django 5.0.6 on 2024-06-15 13:05

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
            name='PerfilCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=255)),
                ('cargo', models.CharField(max_length=255)),
                ('empresa', models.CharField(max_length=255)),
                ('numero_telefono', models.CharField(max_length=20)),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
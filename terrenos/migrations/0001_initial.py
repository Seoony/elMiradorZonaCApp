# Generated by Django 4.2 on 2024-02-12 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Terreno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=4, unique=True)),
                ('manzana', models.CharField(choices=[('A', 'Mz A, no existe'), ('B', 'Mz B'), ('G', 'Mz G'), ('H', 'Mz H'), ("H'", 'Mz H prima'), ('I', 'Mz I'), ('J', 'Mz J'), ('K', 'Mz K'), ('M', 'Mz M'), ('Ñ', 'Mz Ñ'), ('O', 'Mz O'), ('P', 'Mz P'), ('Q', 'Mz Q'), ('R', 'Mz R'), ('S', 'Mz S'), ('T', 'Mz T'), ('U', 'Mz U'), ('V', 'Mz V'), ('X', 'Mz X')], default='A', max_length=2)),
                ('lote', models.CharField(max_length=2)),
                ('area', models.DecimalField(decimal_places=2, default=160.0, max_digits=5)),
                ('otros_usos', models.BooleanField(default=False)),
                ('disponible', models.BooleanField(default=True)),
                ('observaciones', models.TextField(default='Ninguna')),
                ('ultima_modificacion', models.DateTimeField(auto_now=True)),
                ('estado', models.CharField(default='A', max_length=1)),
                ('creado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='terreno_creado_por', to=settings.AUTH_USER_MODEL)),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='terreno_modificado_por', to=settings.AUTH_USER_MODEL)),
                ('socio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='socio_asignado', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
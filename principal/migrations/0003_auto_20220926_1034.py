# Generated by Django 3.2.15 on 2022-09-26 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_alter_campaña_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaña',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='campaña',
            name='fecha_creacion',
        ),
        migrations.RemoveField(
            model_name='campaña',
            name='fecha_final',
        ),
        migrations.RemoveField(
            model_name='campaña',
            name='fecha_inicial',
        ),
        migrations.RemoveField(
            model_name='campaña',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='campaña',
            name='paquete',
        ),
        migrations.RemoveField(
            model_name='campaña',
            name='status',
        ),
        migrations.RemoveField(
            model_name='campaña',
            name='video',
        ),
    ]

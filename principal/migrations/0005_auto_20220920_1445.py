# Generated by Django 3.2.15 on 2022-09-20 19:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_alter_campaña_fecha_creacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='paquete',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
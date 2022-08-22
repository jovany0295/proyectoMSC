
from django import forms
from django.db import models

# Create your models here.
class roles(models.Model):
    nombre = models.CharField(
        max_length=80,
        null= False,
        blank= False,
        unique= True
    )
    descripcion = models.CharField(
        max_length=100,
        null= False,
        blank= False,
        unique= False
    )
class permisos(models.Model):
    nombre = models.CharField(
        max_length=80,
        null= False,
        blank= False,
        unique= True
    )
    descripcion = models.CharField(
        max_length=100,
        null= False,
        blank= False,
        unique= False
    )
class roles_has_permisos(models.Model):
    permiso = models.ForeignKey(permisos, on_delete=models.CASCADE)
    roles = models.ForeignKey(roles, on_delete=models.CASCADE)

        
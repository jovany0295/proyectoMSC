from django.db import models
from django.utils import timezone

# Create your models here.
class clientes(models.Model):
    nombre_cliente = models.CharField(max_length=80, null= False, blank= False,unique= False)
    razon_social = models.CharField(max_length=100, null= False, blank= False, unique= True)
    nombre_contacto = models.CharField(max_length=100, null= False, blank= False, unique= False)
    puesto = models.CharField(max_length=20, null= False, blank= False, unique= False)
    telefono_contacto = models.CharField(max_length=20,null= False, blank= False, unique= False)
    email_contacto = models.CharField(max_length=50, null= False, blank= False, unique= False)
    email_empresa = models.CharField(max_length=50, null= False, blank= False, unique= False)
    telefono_empresa = models.CharField(max_length=20, null= False,blank= False, unique= False)
    direccion_empresa = models.CharField(max_length=100, null= False, blank= False, unique= False )
    cfdi = models.CharField(max_length=20,null= False, blank= False, unique= False)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.nombre_cliente
class paquete(models.Model):
    nombre_paquete = models.CharField(max_length=80, null= False, blank= False, unique= True)
    duracion = models.CharField(max_length=80, null= False, blank= False, unique= True)
    frecuencia = models.CharField(max_length=80, null= False, blank= False, unique= True)
    precio = models.IntegerField(null= False, blank= False, unique= True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.nombre_paquete
class campaña(models.Model):
    LOAN_STATUS = (
        ('A', 'Activo'),
        ('I', 'Inactivo'),
        ('S', 'Suspendido'),
        )
    nombre_campaña = models.CharField(max_length=80, null= False, blank= False, unique= True)
    paquete = models.ForeignKey(paquete, on_delete=models.CASCADE)
    cliente = models.ForeignKey(clientes, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=LOAN_STATUS, blank=True, default='A')
    video = models.FileField()
    imagen = models.FileField()
    fecha_inicial = models.DateField(max_length=80, null= False, blank= False, unique= True)
    fecha_final = models.DateField(max_length=80, null= False, blank= False, unique= True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.nombre_campaña
    



        
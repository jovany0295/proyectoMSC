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
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nombre_cliente
class paquete(models.Model):
    nombre_paquete = models.CharField(max_length=80, null= False, blank= False, unique= True)
    duracion = models.CharField(max_length=80, null= False, blank= False )
    frecuencia = models.CharField(max_length=80, null= False, blank= False)
    precio = models.IntegerField(null= False, blank= False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nombre_paquete
class campaña(models.Model):   
    LOAN_STATUS = [
        ("ACTIVO", "ACTIVO"),
        ("INACTIVO", "INACTIVO"),
        ("SUSPENDIDO", "SUSPENDIDO"),
    ]
    LOAN_CAT = [
        ("AGROPECUARIO", "AGROPECUARIO"),
        ("AGRUPACIONES", "AGRUPACIONES"),
        ("ALIMENTOS", "ALIMENTOS"),
        ("AUTOMOTRIZ Y AFINES", "AUTOMOTRIZ Y AFINEZ"),
        ("BEBIDAS", "BEBIDAS"),
        ("COMPUTO, INTERNET, TELEFONIA Y TV PAGA", "COMPUTO, INTERNET, TELEFONIA Y TV PAGA"),
        ("EDUCACION Y DEPORTE", "EDUCACION Y DEPORTE"),
        ("GOBIERNO Y POLITICA", "GOBIERNO Y POLITICA"),
        ("INMOBILIRIA Y CONSTRUCCION", "INMOBILIARIA Y CONSTRUCCION"),
        ("LIMPIEZA DOMESTICA", "LIMPIEZA DOMESTICA"),
        ("MASCOTAS", "MASCOTAS"),
        ("MUEBLES, ELECTRODOMESTICOS Y ACCESORIOS", "MUEBLES, ELECTRODOMESTICOS Y ACCESORIOS"),
        ("ROPA, CALZADO Y ACCESORIOS", "ROPA, CALZADO Y ACCESORIOS"),
        ("SALUD Y BELLEZA", "SALUD Y BELLEZA"),
        ("SERVICIOS FINANCIEROS", "SERVICIOS FINANCIEROS"),
        ("SERVICIOS PROFESIONALES", "SERVICIOS PROFESIONALES"),
        ("SERVICIOS VARIOS", "SERVICIOS VARIOS"),
        ("TURISMO, RECREACION Y ENTRENAMIENTO", "TURISMO, RECREACION Y ENTRETENIMIENTO"),
        ("VARIOS, HOGAR Y OFICINA", "VARIOS, HOGAR Y OFICINA"),
    ]
  
    nombre_campaña = models.CharField(max_length=80, null= False, blank= False, unique= True)
    status = models.CharField(max_length=11,choices=LOAN_STATUS, blank= False)
    categoria = models.CharField(max_length=50,choices=LOAN_CAT, blank= False)
    paquete = models.ForeignKey(paquete, on_delete=models.CASCADE,null=True)
    cliente = models.ForeignKey(clientes, on_delete=models.CASCADE,null=True)
    video = models.FileField(upload_to='album/videos', null=False)
    imagen = models.FileField(upload_to='album/images',null=False)
    fecha_inicial = models.DateField(max_length=80, null= False, blank= False, default=timezone.now)
    fecha_final = models.DateField(max_length=80, null= False, blank= False,default=timezone.now)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nombre_campaña
    



        
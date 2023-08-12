from django.db import models

# Create your models here.
class Producto(models.Model):
    serialNumber=models.CharField(max_length=20) 
    marca=models.CharField(max_length=20)
    modelo=models.CharField(max_length=20)
    generacion=models.IntegerField()
    PArea=models.CharField(max_length=30)## gamer, oficinista
    precio=models.FloatField()
    color=models.CharField(max_length=10)
    imagen=models.ImageField(upload_to='productos/', default='default.jpg')
    
    class Meta:
        verbose_name= 'producto'
        verbose_name_plural='productos'

    def __str__(self):
        return self.serialNumber

class Venta(models.Model):
    vSerialNumber=models.CharField(max_length=20)
    ci=models.CharField(max_length=10)
    
    fecha=models.DateTimeField()

class Area(models.Model):
    tipo=models.CharField(max_length=30)##primary key
    nombre=models.CharField(max_length=20)
    demanda=models.CharField(max_length=30)

class AreaProductos(models.Model):
    tipo=models.CharField(max_length=30)##foranea key
    serialNumber=models.CharField(max_length=20) ##foranea key

class Usuario(models.Model):
    #ci=models.CharField(max_length=10)#primary key
    #vCliente=models.CharField(max_length=40)#foranea
    telf=models.CharField(max_length=20)
    tipo=models.CharField(max_length=30)##foranea key
    correo=models.CharField(max_length=30)
    nombre=models.CharField(max_length=40)
    contrasenia=models.CharField(max_length=20)

class UsuarioArea(models.Model):
    ci=models.CharField(max_length=10)#foranea
    tipo=models.CharField(max_length=30)##primary key



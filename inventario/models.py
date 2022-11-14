from xmlrpc.client import Boolean
from django.db import models
from product.models import Producto
from django.contrib.auth.models import User
# Create your models here.

class Metodo_abastecimiento(models.Model):
    nombre = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre


class Reglas_Inventario(models.Model):
    activo = models.BooleanField(default=True)
    retraso = models.IntegerField()
    nombre = models.CharField(max_length=50)
    metodo_abastecimiento = models.ForeignKey(Metodo_abastecimiento, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Almacen(models.Model):
    activo = models.BooleanField(default=True)
    descripcion = models.CharField(max_length=50)
    metodo = models.ForeignKey(Metodo_abastecimiento, verbose_name=("abastecimiento"), on_delete=models.CASCADE)
    reglas = models.ForeignKey(Reglas_Inventario, on_delete=models.CASCADE)

class Lote(models.Model):
    activo =models.BooleanField(default=True)
    producto = models.ForeignKey(Producto, on_delete= models.CASCADE)
    numero = models.CharField(max_length=10)
    secuencia = models.IntegerField()
    messec = models.CharField(max_length=2)

class Localidades(models.Model):
    activo = models.BooleanField(default=True)
    almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE)
    localidad = models.CharField(max_length=5)
    descripcion = models.CharField(max_length=50)


class Inventario(models.Model):
    activo = models.BooleanField(default=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    ''' este campo es para saber si el inventario lleva control de lote '''
    controllote= models.BooleanField(default=False)
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE)
    statuslote = models.BooleanField(default=True)
    almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE)
    localidad = models.ForeignKey(Localidades, verbose_name=("LOC"), on_delete=models.CASCADE)
    existencia = models.IntegerField()


class Transferencia(models.Model):
    activo = models.BooleanField(default=True)
    producto = models.ForeignKey(Producto, verbose_name=(""), on_delete=models.CASCADE)
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE)
    num_orden = models.CharField(max_length=50)
    almacen_origen =models.ForeignKey(Almacen, verbose_name=("Origen"),related_name="Origen", on_delete=models.CASCADE)
    localidad_origen = models.ForeignKey(Localidades, verbose_name=("LOC_Origen"), related_name="LOC_Origen", on_delete=models.CASCADE)
    almacen_destino = models.ForeignKey(Almacen, verbose_name=("Destino"),related_name="Destino", on_delete=models.CASCADE)
    localidad_destino = models.ForeignKey(Localidades, verbose_name=("LOC Destino"),related_name="LOC_Destino", on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
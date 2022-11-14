from itertools import chain
from locale import CHAR_MAX
from operator import index
from random import choices
from secrets import choice
from sqlite3 import Date
from tkinter import CASCADE
from xmlrpc.client import DateTime, boolean
from django.db import models

# Create your models here.




class Atributos(models.Model):
    nombre = models.CharField(max_length=30)
    secuencia = models.IntegerField()
    tipo = models
    def __str__(self):
        return (self.nombre)


class Categoria_productos(models.Model):
    nombre_completo = models.CharField(max_length=60)
    nombre = models.CharField(max_length=20)
    def __str__(self):
        return (self.nombre)



class Moneda(models.Model):
    activo = models.BooleanField(default=True)
    divisa = models.CharField(max_length=2)
    moneda = models.CharField(max_length=30)
    simbolo = models.CharField(max_length=5)
    def __str__(self):
        return (self.moneda)

class Tasa(models.Model):
    converted = models.FloatField()
    nombre = models.CharField(max_length=50)
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)
    fecha = models.DateField()
    tasa = models.FloatField()
    def __str__(self):
        return self.fecha


class Tarifa(models.Model):
    activo = models.BooleanField(default=True)
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    secuencia = models.IntegerField()
    def __str__(self):
        return self.nombre

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





class Lista_de_precios(models.Model):
    nombre = models.CharField(max_length=50)
    tarifa = models.ForeignKey(Tarifa, on_delete=models.CASCADE)
    cantidad1 = models.IntegerField()
    cantidad2 = models.IntegerField()
    cantidad3 = models.IntegerField()
    cantidad4 = models.IntegerField()
    def __str__(self):
        return self.nombre

class Unidad_Medida(models.Model):
    nombre = models.CharField(max_length=30)
    multiplicador=models.FloatField()
    def __str__(self):
        return self.nombre




class Cuenta(models.Model):
    codigo = models.CharField(max_length=50)
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    #costo = models.Choices()
    #ingreso = models.Choices()
    credito_apertura = models.FloatField()
    debito_apertura = models.FloatField()
    def __str__(self):
        return self.nombre


class ProveedorTipo(models.Model):
    ''' clase para defirnir los tipos de proveedores'''
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre



class Proveedores(models.Model):
    '''Clase para guardar los proveedores '''
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    rnc = models.CharField(max_length=20)
    tipo = models.ForeignKey(ProveedorTipo, on_delete=models.CASCADE)
    contacto = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    productos = models.ManyToManyField('self', through='Producto', symmetrical=False)
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    ''' clase para guardar los productos'''
    active = models.BooleanField(default=True)
    barcode = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria_productos, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=50)
    moneda_costo = models.ForeignKey(Moneda, on_delete=models.CASCADE, related_name='moneda_costo')
    metodo_costo = models.CharField(max_length=50)
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE, related_name='moneda_transacciones')
    descripcion = models.CharField(max_length=50) 
    entrada = models.IntegerField()
    precio = models.FloatField()
    tarifa = models.ForeignKey(Tarifa, on_delete=models.CASCADE)
    item_lista_de_precios = models.ForeignKey(Lista_de_precios, on_delete=models.CASCADE)
    cuenta_de_gasto = models.ForeignKey(Cuenta, on_delete=models.CASCADE, related_name='cuenta_gasto')
    cuenta_de_ingreso = models.ForeignKey(Cuenta, on_delete=models.CASCADE, related_name='cuenta_ingreso')
    cuenta_de_entrada_inventario = models.ForeignKey(Cuenta, on_delete=models.CASCADE, related_name='cuenta_entrada')
    cuenta_de_salida_inventario = models.ForeignKey(Cuenta, on_delete=models.CASCADE, related_name='cuenta_salida')
    imagen = models.CharField(max_length=50)
    proveedores = models.ManyToManyField(Proveedores, blank=True)
    #metodo_de_costo = models.Choices()
    def __str__(self):
        return self.nombre

class producto_proveedor():
    ''' clase que relaciones los diferentes productos y proveedores que lo ofrecen'''
    active = models.BooleanField(default=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    def __str__(self):
        return self.proveedor

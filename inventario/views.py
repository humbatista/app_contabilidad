from django.shortcuts import render
from product.models import Producto, Proveedores
from .models import *

# Create your views here.

def list_almacen(request):
    template_name = 'inventario/almacenes.html'
    listado_almacenes = Almacen.objects.iterator
    context ={
        'listado_almacenes':listado_almacenes,
    }
    return render(request, template_name, context)

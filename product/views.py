from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponseRedirect
from .models import *
from .forms import *
# Create your views here.

''' aqui creamos todos las vistas relacionada con el producto'''
def create_product(request):
    template_name = 'product/insert_product.html'
    form = ProductForm(request.POST)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect("/productos")
    return render(request,template_name,{'form':form,})


def list_product(request):
    template_name = 'product/list_product.html'
    listado_productos = Producto.objects.iterator
    context ={
        'listado_productos':listado_productos,
    }
    return render(request, template_name, context)

def detail_product(request, id):
    template_name='product/detail_product.html'
    context = {}
    obj = get_object_or_404(Producto, id = id)
    context["data"] = obj
    #context["data"] = Producto.objects.get(id = id)
    return render(request, template_name, context)

def update_product(request, id):
    template_name = 'product/update_product.html'
    context = {}
    obj = get_object_or_404(Producto, id = id)
    form = ProductForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)

    context["form"] = form

    return render(request, template_name, context)

def delete_product(request, id):
    template_name = 'product/delete_product'
    context ={}
    obj = get_object_or_404(Producto, id = id)
    
    if request.method =="POST":
        obj.delete()

        return HttpResponseRedirect("/")
    return render(request, template_name, context)


''' aqui vamos hacer el CRUD de proveedores'''


def create_proveedor(request):
    template_name = 'proveedor/insert_proveedor.html'
    form = ProveedorForm(request.POST)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponseRedirect("/productos/proveedor")
    return render(request,template_name,{'form':form,})


def list_proveedor(request):
    template_name = 'proveedor/list_proveedor.html'
    listado_proveedor = Proveedores.objects.iterator
    context ={
        'listado_proveedor':listado_proveedor,
    }
    return render(request, template_name, context)

def detail_proveedor(request, id):
    template_name='proveedor/detail_proveedor.html'
    context = {}
    obj = get_object_or_404(Proveedores, id = id)
    context["data"] = obj
    return render(request, template_name, context)

def update_proveedor(request, id):
    template_name = 'proveedor/update_proveedor.html'
    context = {}
    obj = get_object_or_404(Proveedores, id = id)
    form = ProveedorForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)

    context["form"] = form

    return render(request, template_name, context)

def delete_proveedor(request, id):
    template_name = 'proveedores/delete_product'
    context ={}
    obj = get_object_or_404(Proveedores, id = id)
    
    if request.method =="POST":
        obj.delete()

        return HttpResponseRedirect("/")
    return render(request, template_name, context)
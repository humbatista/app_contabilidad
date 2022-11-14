from django.contrib import admin
from .models import *
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    filter_horizontal = ('proveedores',)

class ProveedoresAdmin(admin.ModelAdmin):
    filter_horizontal=  ('productos',)


admin.site.register(Atributos)
admin.site.register(Categoria_productos)
admin.site.register(Moneda)
admin.site.register(Tasa)
admin.site.register(Tarifa)
admin.site.register(Metodo_abastecimiento)
admin.site.register(Reglas_Inventario)
admin.site.register(Unidad_Medida)
admin.site.register(Lista_de_precios)
admin.site.register(Cuenta)
admin.site.register(Proveedores, ProveedoresAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(ProveedorTipo)

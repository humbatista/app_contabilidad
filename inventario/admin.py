from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Almacen)
admin.site.register(Metodo_abastecimiento)
admin.site.register(Reglas_Inventario)
admin.site.register(Lote)
admin.site.register(Localidades)
admin.site.register(Inventario)
admin.site.register(Transferencia)
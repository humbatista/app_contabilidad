from django.urls import path
from . import views



urlpatterns = [
    path('create', views.create_product, name='create'),
    path('', views.list_product, name="listarproductos"),
    path('detail/<id>', views.detail_product),
    path('proveedor', views.list_proveedor, name="listarproveedor"),
    path('proveedor/create', views.create_proveedor, name="createproveedor"),
    path('proveedor/<id>', views.detail_proveedor),
]
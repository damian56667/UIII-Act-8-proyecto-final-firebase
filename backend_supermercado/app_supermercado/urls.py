from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),

    path('cajeros/', views.CajeroListView.as_view(), name='cajero_list'),
    path('cajeros/crear/', views.CajeroCreateView.as_view(), name='cajero_create'),
    path('cajeros/<int:pk>/', views.CajeroDetailView.as_view(), name='cajero_detail'),
    path('cajeros/<int:pk>/editar/', views.CajeroUpdateView.as_view(), name='cajero_update'),
    path('cajeros/<int:pk>/borrar/', views.CajeroDeleteView.as_view(), name='cajero_delete'),

    path('clientes/', views.ClienteSuperListView.as_view(), name='cliente_super_list'),
    path('clientes/crear/', views.ClienteSuperCreateView.as_view(), name='cliente_super_create'),
    path('clientes/<int:pk>/', views.ClienteSuperDetailView.as_view(), name='cliente_super_detail'),
    path('clientes/<int:pk>/editar/', views.ClienteSuperUpdateView.as_view(), name='cliente_super_update'),
    path('clientes/<int:pk>/borrar/', views.ClienteSuperDeleteView.as_view(), name='cliente_super_delete'),

    path('categorias/', views.CategoriaSuperListView.as_view(), name='categoria_super_list'),
    path('categorias/crear/', views.CategoriaSuperCreateView.as_view(), name='categoria_super_create'),
    path('categorias/<int:pk>/', views.CategoriaSuperDetailView.as_view(), name='categoria_super_detail'),
    path('categorias/<int:pk>/editar/', views.CategoriaSuperUpdateView.as_view(), name='categoria_super_update'),
    path('categorias/<int:pk>/borrar/', views.CategoriaSuperDeleteView.as_view(), name='categoria_super_delete'),

    path('proveedores/', views.ProveedorListView.as_view(), name='proveedor_list'),
    path('proveedores/crear/', views.ProveedorCreateView.as_view(), name='proveedor_create'),
    path('proveedores/<int:pk>/', views.ProveedorDetailView.as_view(), name='proveedor_detail'),
    path('proveedores/<int:pk>/editar/', views.ProveedorUpdateView.as_view(), name='proveedor_update'),
    path('proveedores/<int:pk>/borrar/', views.ProveedorDeleteView.as_view(), name='proveedor_delete'),

    path('productos/', views.ProductoSuperListView.as_view(), name='producto_super_list'),
    path('productos/crear/', views.ProductoSuperCreateView.as_view(), name='producto_super_create'),
    path('productos/<int:pk>/', views.ProductoSuperDetailView.as_view(), name='producto_super_detail'),
    path('productos/<int:pk>/editar/', views.ProductoSuperUpdateView.as_view(), name='producto_super_update'),
    path('productos/<int:pk>/borrar/', views.ProductoSuperDeleteView.as_view(), name='producto_super_delete'),

    path('ventas/', views.VentaSuperListView.as_view(), name='venta_super_list'),
    path('ventas/crear/', views.VentaSuperCreateView.as_view(), name='venta_super_create'),
    path('ventas/<int:pk>/', views.VentaSuperDetailView.as_view(), name='venta_super_detail'),
    path('ventas/<int:pk>/editar/', views.VentaSuperUpdateView.as_view(), name='venta_super_update'),
    path('ventas/<int:pk>/borrar/', views.VentaSuperDeleteView.as_view(), name='venta_super_delete'),

    path('detalles-venta/', views.DetalleVentaSuperListView.as_view(), name='detalle_venta_super_list'),
    path('detalles-venta/crear/', views.DetalleVentaSuperCreateView.as_view(), name='detalle_venta_super_create'),
    path('detalles-venta/<int:pk>/', views.DetalleVentaSuperDetailView.as_view(), name='detalle_venta_super_detail'),
    path('detalles-venta/<int:pk>/editar/', views.DetalleVentaSuperUpdateView.as_view(), name='detalle_venta_super_update'),
    path('detalles-venta/<int:pk>/borrar/', views.DetalleVentaSuperDeleteView.as_view(), name='detalle_venta_super_delete'),
]
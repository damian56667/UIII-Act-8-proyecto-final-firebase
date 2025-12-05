from django.contrib import admin
from .models import (
    Cajero,
    CategoriaSuper,
    Proveedor,
    ProductoSuper,
    ClienteSuper,
    VentaSuper,
    DetalleVentaSuper,
)

admin.site.register(Cajero)
admin.site.register(CategoriaSuper)
admin.site.register(Proveedor)
admin.site.register(ProductoSuper)
admin.site.register(ClienteSuper)
admin.site.register(VentaSuper)
admin.site.register(DetalleVentaSuper)

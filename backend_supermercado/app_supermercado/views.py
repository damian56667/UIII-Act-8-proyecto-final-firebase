from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import (
    Cajero, ClienteSuper, CategoriaSuper, Proveedor, 
    ProductoSuper, VentaSuper, DetalleVentaSuper
)

class HomeView(TemplateView):
    template_name = 'home.html'

# Cajero Views

class CajeroListView(ListView):
    model = Cajero
    template_name = 'cajero/cajero_list.html'
    context_object_name = 'cajeros'

class CajeroDetailView(DetailView):
    model = Cajero
    template_name = 'cajero/cajero_detail.html'
    context_object_name = 'cajero'

class CajeroCreateView(CreateView):
    model = Cajero
    fields = '__all__'
    template_name = 'cajero/cajero_form.html'
    success_url = reverse_lazy('cajero_list')

class CajeroUpdateView(UpdateView):
    model = Cajero
    fields = '__all__'
    template_name = 'cajero/cajero_form.html'
    success_url = reverse_lazy('cajero_list')

class CajeroDeleteView(DeleteView):
    model = Cajero
    template_name = 'cajero/cajero_confirm_delete.html'
    success_url = reverse_lazy('cajero_list')

# ClienteSuper Views
class ClienteSuperListView(ListView):
    model = ClienteSuper
    template_name = 'cliente_super/cliente_super_list.html'
    context_object_name = 'clientes'

class ClienteSuperDetailView(DetailView):
    model = ClienteSuper
    template_name = 'cliente_super/cliente_super_detail.html'
    context_object_name = 'cliente'

class ClienteSuperCreateView(CreateView):
    model = ClienteSuper
    fields = '__all__'
    template_name = 'cliente_super/cliente_super_form.html'
    success_url = reverse_lazy('cliente_super_list')

class ClienteSuperUpdateView(UpdateView):
    model = ClienteSuper
    fields = '__all__'
    template_name = 'cliente_super/cliente_super_form.html'
    success_url = reverse_lazy('cliente_super_list')

class ClienteSuperDeleteView(DeleteView):
    model = ClienteSuper
    template_name = 'cliente_super/cliente_super_confirm_delete.html'
    success_url = reverse_lazy('cliente_super_list')


# CategoriaSuper Views
class CategoriaSuperListView(ListView):
    model = CategoriaSuper
    template_name = 'categoria_super/categoria_super_list.html'
    context_object_name = 'categorias'

class CategoriaSuperDetailView(DetailView):
    model = CategoriaSuper
    template_name = 'categoria_super/categoria_super_detail.html'
    context_object_name = 'categoria'

class CategoriaSuperCreateView(CreateView):
    model = CategoriaSuper
    fields = '__all__'
    template_name = 'categoria_super/categoria_super_form.html'
    success_url = reverse_lazy('categoria_super_list')

class CategoriaSuperUpdateView(UpdateView):
    model = CategoriaSuper
    fields = '__all__'
    template_name = 'categoria_super/categoria_super_form.html'
    success_url = reverse_lazy('categoria_super_list')

class CategoriaSuperDeleteView(DeleteView):
    model = CategoriaSuper
    template_name = 'categoria_super/categoria_super_confirm_delete.html'
    success_url = reverse_lazy('categoria_super_list')


# Proveedor Views
class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'proveedor/proveedor_list.html'
    context_object_name = 'proveedores'

class ProveedorDetailView(DetailView):
    model = Proveedor
    template_name = 'proveedor/proveedor_detail.html'
    context_object_name = 'proveedor'

class ProveedorCreateView(CreateView):
    model = Proveedor
    fields = '__all__'
    template_name = 'proveedor/proveedor_form.html'
    success_url = reverse_lazy('proveedor_list')

class ProveedorUpdateView(UpdateView):
    model = Proveedor
    fields = '__all__'
    template_name = 'proveedor/proveedor_form.html'
    success_url = reverse_lazy('proveedor_list')

class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = 'proveedor/proveedor_confirm_delete.html'
    success_url = reverse_lazy('proveedor_list')


# ProductoSuper Views
class ProductoSuperListView(ListView):
    model = ProductoSuper
    template_name = 'producto_super/producto_super_list.html'
    context_object_name = 'productos'

class ProductoSuperDetailView(DetailView):
    model = ProductoSuper
    template_name = 'producto_super/producto_super_detail.html'
    context_object_name = 'producto'

class ProductoSuperCreateView(CreateView):
    model = ProductoSuper
    fields = '__all__'
    template_name = 'producto_super/producto_super_form.html'
    success_url = reverse_lazy('producto_super_list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view'] = {'title': 'Crear Producto'}
        return ctx


class ProductoSuperUpdateView(UpdateView):
    model = ProductoSuper
    fields = '__all__'
    template_name = 'producto_super/producto_super_form.html'
    success_url = reverse_lazy('producto_super_list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['view'] = {'title': 'Editar Producto'}
        return ctx

class ProductoSuperDeleteView(DeleteView):
    model = ProductoSuper
    template_name = 'producto_super/producto_super_confirm_delete.html'
    success_url = reverse_lazy('producto_super_list')


# VentaSuper Views
class VentaSuperListView(ListView):
    model = VentaSuper
    template_name = 'venta_super/venta_super_list.html'
    context_object_name = 'ventas'

class VentaSuperDetailView(DetailView):
    model = VentaSuper
    template_name = 'venta_super/venta_super_detail.html'
    context_object_name = 'venta'

class VentaSuperCreateView(CreateView):
    model = VentaSuper
    fields = '__all__'
    template_name = 'venta_super/venta_super_form.html'
    success_url = reverse_lazy('venta_super_list')

class VentaSuperUpdateView(UpdateView):
    model = VentaSuper
    fields = '__all__'
    template_name = 'venta_super/venta_super_form.html'
    success_url = reverse_lazy('venta_super_list')

class VentaSuperDeleteView(DeleteView):
    model = VentaSuper
    template_name = 'venta_super/venta_super_confirm_delete.html'
    success_url = reverse_lazy('venta_super_list')


# DetalleVentaSuper Views
class DetalleVentaSuperListView(ListView):
    model = DetalleVentaSuper
    template_name = 'detalle_venta_super/detalle_venta_super_list.html'
    context_object_name = 'detalles'

class DetalleVentaSuperDetailView(DetailView):
    model = DetalleVentaSuper
    template_name = 'detalle_venta_super/detalle_venta_super_detail.html'
    context_object_name = 'detalle'

class DetalleVentaSuperCreateView(CreateView):
    model = DetalleVentaSuper
    fields = '__all__'
    template_name = 'detalle_venta_super/detalle_venta_super_form.html'
    success_url = reverse_lazy('detalle_venta_super_list')

class DetalleVentaSuperUpdateView(UpdateView):
    model = DetalleVentaSuper
    fields = '__all__'
    template_name = 'detalle_venta_super/detalle_venta_super_form.html'
    success_url = reverse_lazy('detalle_venta_super_list')

class DetalleVentaSuperDeleteView(DeleteView):
    model = DetalleVentaSuper
    template_name = 'detalle_venta_super/detalle_venta_super_confirm_delete.html'
    success_url = reverse_lazy('detalle_venta_super_list')
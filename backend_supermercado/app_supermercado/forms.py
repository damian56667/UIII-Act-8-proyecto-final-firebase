from django import forms
from .models import (
    Producto_Super,
    Categoria_Super,
    Proveedor,
    Venta_Super,
    Detalle_Venta_Super,
    Cajero,
    Cliente_Super,
)

class ProductoSuperForm(forms.ModelForm):
    class Meta:
        model = ProductoSuper
        fields = "__all__"
        widgets = {
            # 1. Usamos DateInput
            # 2. Especificamos 'type': 'date' para el widget de HTML5
            # 3. Añadimos la clase Bootstrap 'form-control'
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            
            # (Opcional, pero recomendado: Añadir 'form-control' a todos los demás campos)
            'nombre_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'precio_unitario': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            # Las claves foráneas (ForeignKey) usan Select, si no las especificas, Django usa Select por defecto.
            'id_categoria': forms.Select(attrs={'class': 'form-control'}),
            'id_proveedor': forms.Select(attrs={'class': 'form-control'}),
            'codigo_barras': forms.TextInput(attrs={'class': 'form-control'}),
            'peso_gramos': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo_empaque': forms.TextInput(attrs={'class': 'form-control'}),
            
class Categoria_SuperForm(forms.ModelForm):
    class Meta:
        model = Categoria_Super
        fields = "__all__"

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = "__all__"

class Venta_SuperForm(forms.ModelForm):
    
    # 1. Definición explícita del campo para configurar input_formats
    fecha_venta = forms.DateTimeField(
        # Este es el formato de entrada (POST) que Django debe aceptar
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=forms.DateTimeInput(
            attrs={'type': 'datetime-local', 'class': 'form-control'},
            # Este es el formato de salida (lo que se muestra en el campo)
            format='%Y-%m-%dT%H:%M'
        )
    )

    class Meta:
        model = Venta_Super
        fields = "__all__"
        widgets = {
            # 2. Widgets para los demás campos de Bootstrap
            'id_cajero': forms.Select(attrs={'class': 'form-control'}),
            'id_cliente': forms.Select(attrs={'class': 'form-control'}),
            'total_venta': forms.NumberInput(attrs={'class': 'form-control'}),
            'metodo_pago': forms.TextInput(attrs={'class': 'form-control'}),
            'descuento_aplicado': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado_venta': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_ticket': forms.TextInput(attrs={'class': 'form-control'}),
            
            # Nota: fecha_venta no se incluye aquí porque ya se definió explícitamente arriba
        }

class Detalle_Venta_SuperForm(forms.ModelForm):
    class Meta:
        model = Detalle_Venta_Super
        fields = "__all__"

class CajeroForm(forms.ModelForm):
    class Meta:
        model = Cajero
        fields = "__all__"

from django import forms
from .models import ClienteSuper


lass Cliente_SuperForm(forms.ModelForm):
    class Meta:
        model = ClienteSuper
        fields = "__all__"
        widgets = {
            # Campos de texto/numéricos (se mantienen igual)
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'puntos_fidelidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'direccion_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            
            # 💡 SOLUCIÓN PARA EL SELECTOR DE CALENDARIO:
            'fecha_nacimiento': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'},
                # Este formato es lo que Django espera recibir de un input type="date"
                format='%Y-%m-%d' 
            ),
            'fecha_registro': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'},
                # Este formato es lo que Django espera recibir de un input type="date"
                format='%Y-%m-%d'
            ),
        }
from django import forms
from Tarifas.models import Tarifa
from Servicios.models import Servicio
from Recibos.models import TipoPago
from Propiedades.models import TipoPropiedad

class PagoSearchForm(forms.Form):
    propiedad_id = forms.IntegerField(
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'propiedad_id'})
    )
    recibo_id = forms.IntegerField(
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'recibo_id'})
    )
    tarifa = forms.ModelChoiceField(
        queryset=Tarifa.objects.all(), 
        required=False, 
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'tarifa'})
    )
    tipo_pago = forms.ModelChoiceField(
        queryset=TipoPago.objects.all(), 
        required=False, 
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'tipo_pago'})
    )
    servicio = forms.ModelChoiceField(
        queryset=Servicio.objects.all(), 
        required=False, 
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'servicio'})
    )
    fecha_inicio = forms.DateField(
        required=False, 
        widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'fecha_inicio'})
    )
    fecha_fin = forms.DateField(
        required=False, 
        widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'fecha_fin'})
    )




class ContribuyenteSearchForm(forms.Form):
    ESTATUS_OPCIONES = [
        ('', 'Seleccione un Estatus de pago'),  # Opción sin seleccionar
        ('Adeudo', 'Adeudo'),
        ('Pendiente', 'Pendiente'),
        ('Al día', 'Al día'),
    ]

    curp = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    folio_unico = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    nombre = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellido_paterno = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellido_materno = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefono = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    correo_electronico = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    tipo_propiedad = forms.ModelChoiceField(queryset=TipoPropiedad.objects.all(), required=False,
                                           widget=forms.Select(attrs={'class': 'form-control'}))
    numero_interior = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    numero_exterior = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    calle = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    entre_calles = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    colonia = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ciudad = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    estado = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    codigo_postal = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    referencias = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    estatus = forms.ChoiceField(choices=ESTATUS_OPCIONES, required=False,
                                           widget=forms.Select(attrs={'class': 'form-control'}))
    

from django import forms
from Tarifas.models import Tarifa
from Servicios.models import Servicio
from Recibos.models import TipoPago
from Propiedades.models import TipoPropiedad

class PagoSearchForm(forms.Form):
    propiedad_id = forms.IntegerField(
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'propiedad_id'}),
        help_text="Ingrese el ID de la propiedad asociada al pago."
    )
    recibo_id = forms.IntegerField(
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'recibo_id'}),
        help_text="Ingrese el ID del recibo relacionado con el pago."
    )
    tarifa = forms.ModelChoiceField(
        queryset=Tarifa.objects.all(), 
        required=False, 
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'tarifa'}),
        help_text="Seleccione la tarifa aplicable al pago."
    )
    tipo_pago = forms.ModelChoiceField(
        queryset=TipoPago.objects.all(), 
        required=False, 
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'tipo_pago'}),
        help_text="Seleccione el tipo de pago realizado."
    )
    servicio = forms.ModelChoiceField(
        queryset=Servicio.objects.all(), 
        required=False, 
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'servicio'}),
        help_text="Seleccione el servicio al que corresponde el pago."
    )
    fecha_inicio = forms.DateField(
        required=False, 
        widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'fecha_inicio'}),
        help_text="Seleccione la fecha de inicio del periodo de pago."
    )
    fecha_fin = forms.DateField(
        required=False, 
        widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'fecha_fin'}),
        help_text="Seleccione la fecha de finalización del periodo de pago."
    )


class ContribuyenteSearchForm(forms.Form):
    ESTATUS_OPCIONES = [
        ('', 'Seleccione un Estatus de pago'),  # Opción sin seleccionar
        ('Adeudo', 'Adeudo'),
        ('Pendiente', 'Pendiente'),
        ('Al día', 'Al día'),
    ]
    id_propiedad = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control'}), 
        help_text="Ingrese el ID de la propiedad."
    )
    tipo_propiedad = forms.ModelChoiceField(
        queryset=TipoPropiedad.objects.all(), 
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        help_text="Seleccione el tipo de propiedad."
    )
    curp = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control'}), 
        help_text="Ingrese la CURP del contribuyente."
    )
    folio_unico = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control'}), 
        help_text="Ingrese el folio único asignado al contribuyente."
    )
    nombre = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control'}), 
        help_text="Ingrese el nombre del contribuyente."
    )
    apellido_paterno = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control'}), 
        help_text="Ingrese el apellido paterno del contribuyente."
    )
    apellido_materno = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control'}), 
        help_text="Ingrese el apellido materno del contribuyente."
    )
    telefono = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control'}), 
        help_text="Ingrese el número de teléfono del contribuyente."
    )
    correo_electronico = forms.EmailField(
        required=False, 
        widget=forms.EmailInput(attrs={'class': 'form-control'}), 
        help_text="Ingrese el correo electrónico del contribuyente."
    )
    numero_interior = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control'}), 
        help_text="Ingrese el número interior de la propiedad (si aplica)."
    )
    numero_exterior = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control'}), 
        help_text="Ingrese el número exterior de la propiedad."
    )
    calle = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control'}), 
        help_text="Ingrese el nombre de la calle."
    )
    entre_calles = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control'}), 
        help_text="Ingrese las calles entre las que se encuentra la propiedad."
    )
    colonia = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control'}), 
        help_text="Ingrese la colonia en la que se encuentra la propiedad."
    )
    ciudad = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control'}), 
        help_text="Ingrese la ciudad donde se encuentra la propiedad."
    )
    estado = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control'}), 
        help_text="Ingrese el estado donde se encuentra la propiedad."
    )
    codigo_postal = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control'}), 
        help_text="Ingrese el código postal de la propiedad."
    )
    referencias = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control'}), 
        help_text="Ingrese referencias adicionales sobre la ubicación de la propiedad."
    )
    estatus = forms.ChoiceField(
        choices=ESTATUS_OPCIONES, 
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        help_text="Seleccione el estatus del pago del contribuyente."
    )


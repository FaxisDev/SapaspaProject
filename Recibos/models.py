from django.db import models
from Tarifas.models import Tarifa
from Propiedades.models import Propiedad

# Create your models here.
class Recibo(models.Model):

    propiedad = models.ForeignKey(Propiedad, on_delete=models.PROTECT,default=None)
    tarifa = models.ForeignKey(Tarifa, on_delete=models.PROTECT,default=None)
    
    descuento = models.DecimalField(max_digits =15 ,decimal_places=2, default=0.0)
    sub_total = models.DecimalField(max_digits =15 ,decimal_places=2, default=0.0)
    total = models.DecimalField(max_digits =15 ,decimal_places=2, default=0.0)
    adeudo = models.DecimalField(max_digits =15 ,decimal_places=2, default=0.0)
    mes_pago = models.DateField()

    # Otros campos del modelo...
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)


    
    class Meta:
        verbose_name = 'Recibo'
        verbose_name_plural = 'Recibos'
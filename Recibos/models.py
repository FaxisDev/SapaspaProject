from django.db import models
from Tarifas.models import Tarifa
from Propiedades.models import Propiedad
from Servicios.models import Servicio

class TipoPago(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)

        # Otros campos del modelo...
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.descripcion}"

    class Meta:
            verbose_name = 'Tipo de pago'
            verbose_name_plural = 'Tipos de pagos'


# Create your models here.
class Recibo(models.Model):
    id = models.AutoField(primary_key=True)
    propiedad = models.ForeignKey(Propiedad, on_delete=models.PROTECT,default=None)
    tarifa = models.ForeignKey(Tarifa, on_delete=models.PROTECT,default=None)
    tipo_pago = models.ForeignKey(TipoPago, on_delete=models.PROTECT,default=None)

    # Otros campos del modelo...
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.propiedad}"  
    
    class Meta:
        verbose_name = 'Recibo'
        verbose_name_plural = 'Recibos'

class Pago(models.Model):
    id = models.AutoField(primary_key=True)
    recibo = models.ForeignKey(Recibo, on_delete=models.CASCADE,default=None)
    servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT,default=None)
    
    descuento = models.DecimalField(max_digits =15 ,decimal_places=2, default=0.0)
    sub_total = models.DecimalField(max_digits =15 ,decimal_places=2, default=0.0)
    total = models.DecimalField(max_digits =15 ,decimal_places=2, default=0.0)
    mes_pago = models.DateField()

        # Otros campos del modelo...
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.mes_pago}, Total: {self.total}"  


    class Meta:
            verbose_name = 'Pago'
            verbose_name_plural = 'Pagos'


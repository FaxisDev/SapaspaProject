from django.db import models
from datetime import datetime
from Contribuyentes.models import Contribuyente

class TipoPropiedad(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.TextField(default=None)
    descripcion = models.TextField(default=None)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name = "Tipo de Propiedad"
        verbose_name_plural = "Tipo de Propiedades"


class Propiedad(models.Model):
    id = models.AutoField(primary_key=True)
    numero_interior = models.TextField(null=True, blank=True)
    numero_exterior = models.TextField(default=None)
    calle = models.TextField(default=None)
    entre_calles = models.TextField(default=None)
    colonia = models.TextField(default=None)
    ciudad = models.TextField(default=None)
    estado = models.TextField(default=None)
    codigo_postal = models.CharField(default=None, max_length=10)
    referencias = models.TextField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    tipo_propiedad = models.ForeignKey(
        TipoPropiedad, on_delete=models.PROTECT, default=None
    )
    contribuyente = models.ForeignKey(
        Contribuyente, on_delete=models.PROTECT, default=None
    )

    @property
    def info_pago(self):
        from Recibos.models import Pago  # Importación diferida

        # Obtiene el último pago asociado a la propiedad a través de los recibos
        ultimo_pago = (
            Pago.objects.filter(recibo__propiedad=self).order_by("-mes_pago").first()
        )

        if ultimo_pago:
            fecha_ultimo_pago = ultimo_pago.mes_pago
        else:
            fecha_ultimo_pago = self.fecha_creacion.date()

        # Obtiene la fecha actual
        fecha_actual = datetime.now().date()

        # Calcula la diferencia en meses
        diferencia_meses = (
            (fecha_actual.year - fecha_ultimo_pago.year) * 12
            + fecha_actual.month
            - fecha_ultimo_pago.month
        )

        # Determina el estatus según la diferencia en meses
        if diferencia_meses > 6:  # Más de 6 meses
            estatus = "Adeudo"
        elif diferencia_meses > 1:  # Entre 1 y 6 meses
            estatus = "Pendiente"
        else:  # 1 mes o menos
            estatus = "Al día"

        # Retorna el diccionario con la información solicitada
        return {"fecha_ultimo_pago": fecha_ultimo_pago, "estatus": estatus}

    def __str__(self):
        return f"({self.id}) {self.entre_calles} - {self.contribuyente}"

    class Meta:
        verbose_name = "Propiedad"
        verbose_name_plural = "Propiedades"

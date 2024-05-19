from django.db import models

from Contribuyentes.models import Contribuyente

class TipoPropiedad(models.Model):
    id = models.AutoField(primary_key=True)

    tipo = models.TextField(default=None)
    descripcion = models.TextField(default=None)
    # Otros campos del modelo...
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tipo
    
    class Meta:
        verbose_name = 'Tipo de Propiedad'
        verbose_name_plural = 'Tipo de Propiedades'

# Create your models here.
class Propiedad(models.Model):
    id = models.AutoField(primary_key=True)
    numero_interior = models.TextField(null=True,blank=True,)
    numero_exterior = models.TextField(default=None)
    calle = models.TextField(default=None)
    entre_calles = models.TextField(default=None)
    colonia = models.TextField(default=None)
    ciudad = models.TextField(default=None)
    estado = models.TextField(default=None)
    codigo_postal = models.CharField(default=None, max_length=10)
    referencias = models.TextField(null=True, blank=True,)
    # Otros campos del modelo...
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    tipo_propiedad = models.ForeignKey(TipoPropiedad, on_delete=models.PROTECT,default=None)
    contribuyente = models.ForeignKey(Contribuyente, on_delete=models.PROTECT,default=None)

    def __str__(self):
        return f"({self.id}) {self.entre_calles} - {self.contribuyente}"  

    class Meta:
        verbose_name = 'Propiedad'
        verbose_name_plural = 'Propiedades'



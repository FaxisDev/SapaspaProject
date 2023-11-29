from django.db import models

class Tarifa(models.Model):
    tipo = models.TextField(default=None)
    precio_base = models.DecimalField(max_digits =15 ,decimal_places=2, default=0.0)
    
    #vi
    fecha_inicio_vigencia = models.DateField()
    fecha_fin_vigencia = models.DateField(null=True, blank=True)

    #Agregamos campo de prorroga ¿Pregunta serìa?

    # Otros campos del modelo...
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tipo
    
    class Meta:
        verbose_name = 'Tarifa'
        verbose_name_plural = 'Tarifas'

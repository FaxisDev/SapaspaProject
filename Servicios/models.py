from django.db import models

# Create your models here.
class Servicio(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)

        # Otros campos del modelo...
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
            verbose_name = 'Servicio'
            verbose_name_plural = 'Servicios'


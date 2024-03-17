from django.db import models

# Create your models here.
class PreguntaFrecuente(models.Model):
    id = models.AutoField(primary_key=True)
    pregunta = models.TextField()
    descripcion = models.TextField()

        # Otros campos del modelo...
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
            verbose_name = 'Pregunta Frecuente'
            verbose_name_plural = 'Preguntas Frecuentes'


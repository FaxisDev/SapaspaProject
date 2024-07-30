from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class PreguntaFrecuente(models.Model):
    id = models.AutoField(primary_key=True)
    pregunta = models.TextField()
    descripcion = CKEditor5Field('descripcion', config_name='Essentials')

        # Otros campos del modelo...
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
            verbose_name = 'Pregunta Frecuente'
            verbose_name_plural = 'Preguntas Frecuentes'


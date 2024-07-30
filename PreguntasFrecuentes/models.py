from django.db import models  # Importa el módulo models de Django para definir modelos.
from django_ckeditor_5.fields import CKEditor5Field  # Importa CKEditor5Field para usar un editor de texto enriquecido.

# Crea tus modelos aquí.
class PreguntaFrecuente(models.Model):
    id = models.AutoField(primary_key=True)  # Campo de clave primaria que se autoincrementa automáticamente.
    pregunta = models.TextField()  # Campo de texto para almacenar la pregunta.
    descripcion = CKEditor5Field('descripcion', config_name='Essentials')  # Campo de texto enriquecido para la descripción, utilizando CKEditor.

    # Otros campos del modelo...
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Campo de fecha y hora que se establece automáticamente cuando se crea el objeto.
    fecha_actualizacion = models.DateTimeField(auto_now=True)  # Campo de fecha y hora que se actualiza automáticamente cada vez que se guarda el objeto.

    class Meta:
        verbose_name = 'Pregunta Frecuente'  # Nombre singular para representar el modelo en la interfaz de administración.
        verbose_name_plural = 'Preguntas Frecuentes'  # Nombre plural para representar el modelo en la interfaz de administración.

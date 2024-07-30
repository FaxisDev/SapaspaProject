from django.contrib import admin  # Importa el módulo admin de Django para registrar modelos en el panel de administración.

# Registra tus modelos aquí.
from .models import PreguntaFrecuente  # Importa el modelo PreguntaFrecuente desde el módulo de modelos local.

# Define una clase para personalizar la administración del modelo PreguntaFrecuente.
class PreguntaFrecuenteAdmin(admin.ModelAdmin):
    # Especifica los campos que se utilizarán para realizar búsquedas en el panel de administración.
    search_fields = ['pregunta', 'descripcion']
    # Define los campos que se mostrarán como columnas en la lista de objetos en el panel de administración.
    list_display = ['id', 'pregunta']

# Registra el modelo PreguntaFrecuente junto con su configuración personalizada en el panel de administración.
admin.site.register(PreguntaFrecuente, PreguntaFrecuenteAdmin)
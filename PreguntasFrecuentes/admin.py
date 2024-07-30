from django.contrib import admin

# Register your models here.
from .models import PreguntaFrecuente

class PreguntaFrecuenteAdmin(admin.ModelAdmin):
    search_fields = ['pregunta','descripcion'] #Busqueda de filtro
    list_display = ['id','pregunta'] #Visualizacion de columnas en panel de admin

admin.site.register(PreguntaFrecuente, PreguntaFrecuenteAdmin)
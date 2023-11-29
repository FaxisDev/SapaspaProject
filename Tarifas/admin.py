from django.contrib import admin

# Register your models here.

from .models import Tarifa

class TarifaAdmin(admin.ModelAdmin):
    search_fields = ['tipo'] #Busqueda de filtro
    list_display = ['tipo','precio_base','fecha_inicio_vigencia','fecha_fin_vigencia'] #Visualizacion de columnas en panel de admin

admin.site.register(Tarifa, TarifaAdmin)


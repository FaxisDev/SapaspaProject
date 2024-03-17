from django.contrib import admin

# Register your models here.
from .models import Contribuyente

class ContribuyenteAdmin(admin.ModelAdmin):
    search_fields = ['nombre'] #Busqueda de filtro
    list_display = ['id','folio_unico','nombre','apellido_paterno','apellido_materno','curp'] #Visualizacion de columnas en panel de admin

admin.site.register(Contribuyente, ContribuyenteAdmin)
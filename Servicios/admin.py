from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Servicio

class ServicioAdmin(admin.ModelAdmin):
    search_fields = ['id'] #Busqueda de filtro
    list_display = ['id','descripcion'] #Visualizacion de columnas en panel de admin

admin.site.register(Servicio, ServicioAdmin)

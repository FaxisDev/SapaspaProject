from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Propiedad, TipoPropiedad


class PropiedadAdmin(admin.ModelAdmin):
    search_fields = ["contribuyente"]  # Busqueda de filtro
    list_display = [
        "contribuyente",
        "tipo_propiedad",
        "numero_interior",
        "numero_exterior",
        "entre_calles",
        "codigo_postal",
    ]  # Visualizacion de columnas en panel de admin


class TipoPropiedadAdmin(admin.ModelAdmin):
    search_fields = ["tipo"]  # Busqueda de filtro


admin.site.register(Propiedad, PropiedadAdmin)
admin.site.register(TipoPropiedad, TipoPropiedadAdmin)

from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Recibo, Pago, TipoPago

class ReciboAdmin(admin.ModelAdmin):
    search_fields = ['id'] #Busqueda de filtro
    list_display = ['id','propiedad'] #Visualizacion de columnas en panel de admin

class PagoAdmin(admin.ModelAdmin):
    search_fields = ['id'] #Busqueda de filtro
    list_display = ['id','mes_pago'] #Visualizacion de columnas en panel de admin
    
class TipoPagoAdmin(admin.ModelAdmin):
    search_fields = ['id'] #Busqueda de filtro
    list_display = ['id','descripcion'] #Visualizacion de columnas en panel de admin

admin.site.register(Recibo, ReciboAdmin)
admin.site.register(Pago, PagoAdmin)
admin.site.register(TipoPago, TipoPagoAdmin)

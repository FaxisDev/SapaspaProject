from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Recibo, Pago, TipoPago

class ReciboAdmin(admin.ModelAdmin):
    search_fields = ['id'] #Busqueda de filtro
    list_display = ['id','propiedad','tipo_pago', 'fecha_creacion'] #Visualizacion de columnas en panel de admin
    list_filter = ['tipo_pago','fecha_creacion'] 

class PagoAdmin(admin.ModelAdmin):
    search_fields = ['id'] #Busqueda de filtro
    list_display = ['id','get_recibo_id','mes_pago','descuento','sub_total','total','fecha_creacion'] #Visualizacion de columnas en panel de admin

    # Función para obtener el id del recibo
    def get_recibo_id(self, obj):
        return obj.recibo.id  # Devuelve el id del recibo relacionado
    get_recibo_id.admin_order_field = 'recibo__id'  # Esto habilita el ordenamiento por el campo 'id' del recibo
    get_recibo_id.short_description = 'ID Recibo'  # Etiqueta personalizada para la columna
    
class TipoPagoAdmin(admin.ModelAdmin):
    search_fields = ['id'] #Busqueda de filtro
    list_display = ['id','descripcion'] #Visualizacion de columnas en panel de admin

admin.site.register(Recibo, ReciboAdmin)
admin.site.register(Pago, PagoAdmin)
admin.site.register(TipoPago, TipoPagoAdmin)

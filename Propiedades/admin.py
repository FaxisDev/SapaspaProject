from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import Propiedad, TipoPropiedad
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html

class EstatusPagoFilter(admin.SimpleListFilter):
    title = _("Estatus de Pago")  # Nombre del filtro en la UI
    parameter_name = "estatus_pago"

    def lookups(self, request, model_admin):
        return [
            ("al_dia", _("Al día")),
            ("pendiente", _("Pendiente")),
            ("adeudo", _("Adeudo")),
        ]

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset  # Retornar todo el queryset si no se ha seleccionado filtro

        from Recibos.models import Pago  # Importación diferida
        
        resultado = []
        for propiedad in queryset:
            # Obtener el último pago
            ultimo_pago = (
                Pago.objects.filter(recibo__propiedad=propiedad)
                .order_by("-mes_pago")
                .first()
            )

            # Determinar la fecha del último pago
            fecha_ultimo_pago = ultimo_pago.mes_pago if ultimo_pago else propiedad.fecha_creacion.date()
            fecha_actual = datetime.now().date()

            # Calcular diferencia en meses
            diferencia_meses = (
                (fecha_actual.year - fecha_ultimo_pago.year) * 12
                + fecha_actual.month - fecha_ultimo_pago.month
            )

            # Filtrar según la selección del usuario
            if self.value() == "adeudo" and diferencia_meses > 6:
                resultado.append(propiedad.id)
            elif self.value() == "pendiente" and 1 < diferencia_meses <= 6:
                resultado.append(propiedad.id)
            elif self.value() == "al_dia" and diferencia_meses <= 1:
                resultado.append(propiedad.id)

        return queryset.filter(id__in=resultado)


class PropiedadAdmin(admin.ModelAdmin):
    search_fields = [
        "contribuyente__nombre",
        "id",
        "contribuyente__folio_unico",
        "contribuyente__apellido_paterno",
        "contribuyente__apellido_materno",
    ]  # Busqueda de filtro
    list_filter = [EstatusPagoFilter,"tipo_propiedad"]  # Agregar el filtro aquí
    list_display = [
        "id",
        "contribuyente",
        "tipo_propiedad",
        "numero_exterior",
        "entre_calles",
        "colonia",
        "get_fecha_ultimo_pago",  # Nuevo método para mostrar la fecha del último pago
        "get_estatus",  # Nuevo método para mostrar el estatus del pago

    ]  # Visualizacion de columnas en panel de admin

    def get_fecha_ultimo_pago(self, obj):
        return obj.info_pago["fecha_ultimo_pago"]

    get_fecha_ultimo_pago.short_description = (
        "Último Pago"  # Nombre de la columna en el admin
    )

    def get_estatus(self, obj):
        """Devuelve el estatus con color en línea"""
        estatus = obj.info_pago["estatus"]
        colores = {
            "Adeudo": "#ffcccc",  # Rojo claro
            "Pendiente": "#fff4cc",  # Amarillo claro
            "Al día": "#ccffcc",  # Verde claro
        }
        color = colores.get(estatus, "#ffffff")  # Blanco por defecto
        return format_html(
            '<span style="background-color: {}; padding: 3px; border-radius: 3px;">{}</span>',
            color,
            estatus
        )

    get_estatus.short_description = (
        "Estatus de Pago"  # Nombre de la columna en el admin
    )


class TipoPropiedadAdmin(admin.ModelAdmin):
    search_fields = ["tipo"]  # Busqueda de filtro


admin.site.register(Propiedad, PropiedadAdmin)
admin.site.register(TipoPropiedad, TipoPropiedadAdmin)

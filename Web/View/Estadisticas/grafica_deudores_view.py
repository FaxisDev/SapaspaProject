from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from chartjs.views.lines import BaseLineChartView
from Propiedades.models import Propiedad


def contarEstatusPropiedades():
    """
    Obtiene el total de propiedades agrupadas por estatus de pago.
    
    - "Adeudo": Más de 6 meses sin pagar.
    - "Pendiente": Entre 1 y 5 meses de retraso.
    - "Al día": Pagos realizados en el último mes.
    
    Retorna un diccionario con el conteo de cada categoría.
    """
    total_propiedades = Propiedad.objects.all()
    total_adeudos = sum(1 for prop in total_propiedades if prop.info_pago["estatus"] == "Adeudo")
    total_pendientes = sum(1 for prop in total_propiedades if prop.info_pago["estatus"] == "Pendiente")
    total_al_dia = sum(1 for prop in total_propiedades if prop.info_pago["estatus"] == "Al día")
    
    total = total_adeudos + total_pendientes + total_al_dia
    if total == 0:  # Evitar división por cero
        porcentaje_adeudos = 0
        porcentaje_pendientes = 0
        porcentaje_al_dia = 0
    else:
        porcentaje_adeudos = (total_adeudos / total) * 100
        porcentaje_pendientes = (total_pendientes / total) * 100
        porcentaje_al_dia = (total_al_dia / total) * 100
    
    return {
        "total_adeudos": total_adeudos,
        "total_pendientes": total_pendientes,
        "total_al_dia": total_al_dia,
        "porcentaje_adeudos": round(porcentaje_adeudos, 2),
        "porcentaje_pendientes": round(porcentaje_pendientes, 2),
        "porcentaje_al_dia": round(porcentaje_al_dia, 2),
    }


@login_required
def graficaDeudoresView(request):
    """
    Vista que renderiza la página de estadísticas de deudores.
    
    Obtiene los datos de conteo de propiedades según su estatus de pago
    y los envía al template 'Estadisticas/grafica_deudores.html'.
    """
    data = contarEstatusPropiedades()
    return render(request, "Estadisticas/grafica_deudores.html", data)


class EstatusPropiedadesChartView(BaseLineChartView):
    """
    Genera los datos para la gráfica de estado de pagos en Chart.js.
    """

    def get_labels(self):
        """Define las etiquetas del eje X de la gráfica."""
        return ["Adeudos", "Pendientes", "Al Día"]

    def get_data(self):
        """
        Obtiene los datos de propiedades en cada estatus de pago
        y los organiza en un formato adecuado para Chart.js.
        """
        data = contarEstatusPropiedades()
        return [[data["total_adeudos"], data["total_pendientes"], data["total_al_dia"]]]

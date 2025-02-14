from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
from chartjs.views.lines import BaseLineChartView
from calendar import month_name
from collections import OrderedDict

from Tarifas.models import Tarifa
from Recibos.models import Pago, Recibo
from Contribuyentes.models import Contribuyente
from Propiedades.models import Propiedad

@login_required  # type: ignore
def principalView(request):
    # Obtener la fecha actual
    hoy = timezone.now().date()
    inicio_mes = hoy.replace(day=1)
    inicio_anio = hoy.replace(month=1, day=1)

    # Tarifas activas dentro del año actual
    tarifas_activas = Tarifa.objects.filter(fecha_inicio_vigencia__year=hoy.year).count()

    # Pagos totales
    pagos_hoy = Pago.objects.filter(fecha_creacion__date=hoy).count()
    pagos_mes = Pago.objects.filter(fecha_creacion__date__gte=inicio_mes).count()
    pagos_anio = Pago.objects.filter(fecha_creacion__date__gte=inicio_anio).count()

    # Suma total de pagos
    suma_pagos_hoy = Pago.objects.filter(fecha_creacion__date=hoy).aggregate(total=Sum('total'))['total'] or 0
    suma_pagos_mes = Pago.objects.filter(fecha_creacion__date__gte=inicio_mes).aggregate(total=Sum('total'))['total'] or 0
    suma_pagos_anio = Pago.objects.filter(fecha_creacion__date__gte=inicio_anio).aggregate(total=Sum('total'))['total'] or 0

    # Recibos totales
    recibos_hoy = Recibo.objects.filter(fecha_creacion__date=hoy).count()
    recibos_mes = Recibo.objects.filter(fecha_creacion__date__gte=inicio_mes).count()
    recibos_anio = Recibo.objects.filter(fecha_creacion__date__gte=inicio_anio).count()

    # Contribuyentes registrados
    contribuyentes_hoy = Contribuyente.objects.filter(fecha_creacion__date=hoy).count()
    contribuyentes_mes = Contribuyente.objects.filter(fecha_creacion__date__gte=inicio_mes).count()
    contribuyentes_total = Contribuyente.objects.all().count()

    # Total de propiedades
    total_propiedades = Propiedad.objects.all().count()

    # Datos para las gráficas
    pagos_por_mes = Pago.objects.filter(fecha_creacion__year=hoy.year).annotate(month=TruncMonth('fecha_creacion')).values('month').annotate(total=Sum('total')).order_by('month')
    recibos_por_mes = Recibo.objects.filter(fecha_creacion__year=hoy.year).annotate(month=TruncMonth('fecha_creacion')).values('month').annotate(total=Sum('id')).order_by('month')

    context = {
        'tarifas_activas': tarifas_activas,
        'pagos_hoy': pagos_hoy,
        'pagos_mes': pagos_mes,
        'pagos_anio': pagos_anio,
        'suma_pagos_hoy': suma_pagos_hoy,
        'suma_pagos_mes': suma_pagos_mes,
        'suma_pagos_anio': suma_pagos_anio,
        'recibos_hoy': recibos_hoy,
        'recibos_mes': recibos_mes,
        'recibos_anio': recibos_anio,
        'contribuyentes_hoy': contribuyentes_hoy,
        'contribuyentes_mes': contribuyentes_mes,
        'contribuyentes_total': contribuyentes_total,
        'total_propiedades': total_propiedades,
        'fecha': hoy,
        'pagos_por_mes': list(pagos_por_mes),
        'recibos_por_mes': list(recibos_por_mes),
    }

    return render(request, 'principal.html', context)


class PagosPorMesChartView(BaseLineChartView):
    def get_labels(self):
        # Genera las etiquetas de los meses en español de enero a diciembre
        meses_espanol = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]
        return meses_espanol

    def get_providers(self):
        return ["Pagos"]

    def get_data(self):
        hoy = timezone.now().date()
        
        # Obtener los pagos por mes
        pagos_por_mes = Pago.objects.filter(fecha_creacion__year=hoy.year) \
            .annotate(month=TruncMonth('fecha_creacion')) \
            .values('month') \
            .annotate(total=Sum('total')) \
            .order_by('month')

        # Crear un diccionario con todos los meses inicializados en 0
        data_dict = OrderedDict({i: 0 for i in range(1, 13)})

        # Llenar los valores reales de los pagos
        for item in pagos_por_mes:
            mes = item['month'].month  # Obtener el número del mes
            data_dict[mes] = item['total']

        # Retornar los valores en orden
        return [list(data_dict.values())]

class RecibosPorMesChartView(BaseLineChartView):
    def get_labels(self):
        # Meses en español en orden correcto
        return [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]

    def get_data(self):
        hoy = timezone.now().date()

        # Obtener los recibos por mes
        recibos_por_mes = Recibo.objects.filter(fecha_creacion__year=hoy.year) \
            .annotate(month=TruncMonth('fecha_creacion')) \
            .values('month') \
            .annotate(total=Count('id')) \
            .order_by('month')

        # Crear un diccionario con todos los meses inicializados en 0
        data_dict = OrderedDict({i: 0 for i in range(1, 13)})

        # Llenar los valores reales de los recibos
        for item in recibos_por_mes:
            mes = item['month'].month  # Obtener el número del mes
            data_dict[mes] = item['total']

        return [list(data_dict.values())]

    def get_providers(self):
        return ["Recibos"]
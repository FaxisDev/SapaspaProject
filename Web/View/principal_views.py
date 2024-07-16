from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from django.db.models import Sum, Count
from datetime import timedelta

from Tarifas.models import Tarifa
from Recibos.models import Pago, Recibo
from Tarifas.models import Tarifa
from Contribuyentes.models import Contribuyente
from Propiedades.models import  Propiedad
# Create your views here.
@login_required # type: ignore
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
        'fecha': hoy
    }

    return render(request, 'principal.html', context)
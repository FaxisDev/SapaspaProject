from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import csv

from django.http import HttpResponse

from Recibos.models import Pago
from .forms import PagoSearchForm

@login_required
def reportePagoslView(request):
    form = PagoSearchForm(request.GET or None)
    if 'export' in request.GET and form.is_valid():
        pagos = Pago.objects.all()

        if form.cleaned_data['propiedad_id']:
            pagos = pagos.filter(recibo__propiedad__id=form.cleaned_data['propiedad_id'])
        if form.cleaned_data['recibo_id']:
            pagos = pagos.filter(recibo__id=form.cleaned_data['recibo_id'])
        if form.cleaned_data['tarifa']:
            pagos = pagos.filter(recibo__tarifa=form.cleaned_data['tarifa'])
        if form.cleaned_data['tipo_pago']:
            pagos = pagos.filter(recibo__tipo_pago=form.cleaned_data['tipo_pago'])
        if form.cleaned_data['servicio']:
            pagos = pagos.filter(servicio=form.cleaned_data['servicio'])
        if form.cleaned_data['fecha_inicio']:
            pagos = pagos.filter(mes_pago__gte=form.cleaned_data['fecha_inicio'])
        if form.cleaned_data['fecha_fin']:
            pagos = pagos.filter(mes_pago__lte=form.cleaned_data['fecha_fin'])

        return export_pagos(request, pagos)

    context = {
        'form': form,
    }
    return render(request, 'Reportes/reporte_pagos.html', context)

def export_pagos(request, pagos):
    response = HttpResponse(content_type='text/csv; charset=utf-8-sig')
    response['Content-Disposition'] = 'attachment; filename="reporte_pagos.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Propiedad ID', 'Recibo ID', 'Tarifa', 'Tipo Pago', 'Servicio', 'Descuento', 'Sub Total', 'Total', 'Mes Pago'])

    for pago in pagos:
        writer.writerow([
            pago.id,
            pago.recibo.propiedad.id,
            pago.recibo.id,
            pago.recibo.tarifa,
            pago.recibo.tipo_pago,
            pago.servicio,
            pago.descuento,
            pago.sub_total,
            pago.total,
            pago.mes_pago
        ])

    return response
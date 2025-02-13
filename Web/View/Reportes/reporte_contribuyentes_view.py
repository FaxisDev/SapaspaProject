from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Q
import csv

from Propiedades.models import Propiedad
from .forms import ContribuyenteSearchForm

@login_required
def reporteContribuyentesView(request):
    form = ContribuyenteSearchForm(request.GET)
    propiedades = []

    if form.is_valid():
        curp = form.cleaned_data.get('curp')
        folio_unico = form.cleaned_data.get('folio_unico')
        nombre = form.cleaned_data.get('nombre')
        apellido_paterno = form.cleaned_data.get('apellido_paterno')
        apellido_materno = form.cleaned_data.get('apellido_materno')
        telefono = form.cleaned_data.get('telefono')
        correo_electronico = form.cleaned_data.get('correo_electronico')
     
        tipo_propiedad = form.cleaned_data.get('tipo_propiedad')
        numero_interior = form.cleaned_data.get('numero_interior')
        numero_exterior = form.cleaned_data.get('numero_exterior')
        calle = form.cleaned_data.get('calle')
        entre_calles = form.cleaned_data.get('entre_calles')
        colonia = form.cleaned_data.get('colonia')
        ciudad = form.cleaned_data.get('ciudad')
        estado = form.cleaned_data.get('estado')
        codigo_postal = form.cleaned_data.get('codigo_postal')
        referencias = form.cleaned_data.get('referencias')
        estatus = form.cleaned_data.get('estatus')

        # Construye la consulta filtrando por los campos del formulario
        propiedades = Propiedad.objects.filter(
            Q(contribuyente__curp__icontains=curp) if curp else Q(),
            Q(contribuyente__folio_unico__icontains=folio_unico) if folio_unico else Q(),
            Q(contribuyente__nombre__icontains=nombre) if nombre else Q(),
            Q(contribuyente__apellido_paterno__icontains=apellido_paterno) if apellido_paterno else Q(),
            Q(contribuyente__apellido_materno__icontains=apellido_materno) if apellido_materno else Q(),
            Q(contribuyente__telefono__icontains=telefono) if telefono else Q(),
            Q(contribuyente__correo_electronico__icontains=correo_electronico) if correo_electronico else Q(),

            Q(numero_interior__icontains=numero_interior) if numero_interior else Q(),
            Q(numero_exterior__icontains=numero_exterior) if numero_exterior else Q(),
            Q(calle__icontains=calle) if calle else Q(),
            Q(entre_calles__icontains=entre_calles) if entre_calles else Q(),
            Q(colonia__icontains=colonia) if colonia else Q(),
            Q(ciudad__icontains=ciudad) if ciudad else Q(),
            Q(estado__icontains=estado) if estado else Q(),
            Q(codigo_postal__icontains=codigo_postal) if codigo_postal else Q(),
            Q(referencias__icontains=referencias) if referencias else Q(),
            Q(tipo_propiedad=tipo_propiedad) if tipo_propiedad else Q(),
        
        )

        # Filtrar en Python según el estatus calculado
        if estatus:
            propiedades = [prop for prop in propiedades if prop.info_pago["estatus"] == estatus]

        # Lógica para exportar a CSV si se ha enviado el formulario para exportar
        if 'export' in request.GET:
            response = HttpResponse(content_type='text/csv; charset=utf-8-sig')
            response['Content-Disposition'] = 'attachment; filename="reporte_contribuyentes.csv"'

            writer = csv.writer(response)
            writer.writerow(['ID', 'ID Propiedad', 'Folio Unico', 'CURP', 'Nombre', 'Apellido Paterno', 'Apellido Materno',
                             'Teléfono', 'Correo Electronico', 'Estatus', 'Número Interior', 'Número Exterior',
                             'Calle', 'Entre Calles', 'Colonia', 'Ciudad', 'Estado', 'Código Postal', 'Referencias',
                             'Tipo de Propiedad', 'Último Estatus de Pago', 'Ultima Fecha de Pago'])

            for propiedad in propiedades:
                writer.writerow([
                    propiedad.contribuyente.id if propiedad.contribuyente else '',
                    propiedad.id,
                    propiedad.contribuyente.folio_unico if propiedad.contribuyente else '',
                    propiedad.contribuyente.curp if propiedad.contribuyente else '',
                    propiedad.contribuyente.nombre if propiedad.contribuyente else '',
                    propiedad.contribuyente.apellido_paterno if propiedad.contribuyente else '',
                    propiedad.contribuyente.apellido_materno if propiedad.contribuyente else '',
                    propiedad.contribuyente.telefono if propiedad.contribuyente else '',
                    propiedad.contribuyente.correo_electronico if propiedad.contribuyente else '',
                    propiedad.contribuyente.estatus if propiedad.contribuyente else '',
                    propiedad.numero_interior,
                    propiedad.numero_exterior,
                    propiedad.calle,
                    propiedad.entre_calles,
                    propiedad.colonia,
                    propiedad.ciudad,
                    propiedad.estado,
                    propiedad.codigo_postal,
                    propiedad.referencias,
                    propiedad.tipo_propiedad.tipo,
                    propiedad.info_pago['estatus'],
                    propiedad.info_pago['fecha_ultimo_pago']
                ])

            return response

    context = {
        'form': form,
        'propiedades': propiedades,
    }
    return render(request, 'Reportes/reporte_contribuyentes.html', context)

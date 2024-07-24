from django.shortcuts import render
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from Recibos.models import Pago, Recibo
from django.db.models import Sum


@api_view(["GET"])
def reciboPDFView(request, recibo_id, contribuyente_id):
    # Intentar obtener el recibo
    try:
        recibo = Recibo.objects.get(
            pk=recibo_id, propiedad__contribuyente__id=contribuyente_id
        )
    except Recibo.DoesNotExist:
        return Response(
            {"message": "No se encontró el recibo o el contribuyente."},
            status=status.HTTP_404_NOT_FOUND,
        )

    # Obtener los pagos asociados al recibo
    pagos = Pago.objects.filter(recibo=recibo)

    # Calcular el total pagado y el total de descuentos
    total_pagado = pagos.aggregate(Sum("total"))["total__sum"] or 0
    total_descuento = pagos.aggregate(Sum("descuento"))["descuento__sum"] or 0

    # Contexto para el template
    context = {
        "recibo": recibo,
        "pagos": pagos,
        "total_pagado": total_pagado,
        "total_descuento": total_descuento,
    }
    # Renderizar el template HTML a una cadena
    template = get_template("Pdfs/recibo.html")
    html = template.render(context)

    # Crear un objeto BytesIO para almacenar el PDF
    result = BytesIO()

    # Crear el PDF utilizando xhtml2pdf
    pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)

    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type="application/pdf")
        response['Content-Disposition'] = f'attachment; filename="recibo_{recibo_id}.pdf"'
        return response
    else:
        return Response(
            {"message": "Error al generar el PDF"}, status=status.HTTP_400_BAD_REQUEST
        )

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Contribuyentes.models import Contribuyente
from Propiedades.models import Propiedad
from Servicios.models import Servicio
from Recibos.models import TipoPago
from Recibos.views import ObtenerPagosListView, GenerarReciboView
import requests
from rest_framework.test import APIRequestFactory
from rest_framework import generics, status
import json

from rest_framework.response import Response  # type: ignore


@login_required  # type: ignore
def buscarContribuyentesView(request):
    message = None
    contribuyentes = None
    propiedades = None

    # Captura y limpieza de los parámetros de búsqueda
    id_val = request.GET.get("id", "").strip()
    folio = request.GET.get("folio", "").strip()
    curp = request.GET.get("curp", "").strip()
    telefono = request.GET.get("telefono", "").strip()

    # Verifica si se ingresó al menos un valor
    if not any([id_val, folio, curp, telefono]):
        message = "No ha llenado ningún campo de búsqueda."
    else:
        # Construye un diccionario con filtros exactos
        filtros = {}
        if id_val:
            try:
                filtros['id'] = int(id_val)
            except ValueError:
                filtros['id'] = -1  # Valor imposible para evitar coincidencias
        if folio:
            filtros['folio_unico'] = folio
        if curp:
            filtros['curp'] = curp
        if telefono:
            filtros['telefono'] = telefono

        contribuyentes = Contribuyente.objects.filter(**filtros)
        if contribuyentes.exists():
            propiedades = Propiedad.objects.filter(contribuyente__in=contribuyentes)
        else:
            message = "No se encontraron resultados para los criterios ingresados."

    context = {
        "id_val": id_val,
        "folio": folio,
        "curp": curp,
        "telefono": telefono,
        "contribuyentes": contribuyentes,
        "propiedades": propiedades,
        "message": message,
    }
    return render(request, "Recibos/buscar_contribuyentes.html", context)




@login_required
def generarRecibosView(request, propiedad_id):
    api_url = f"http://127.0.0.1:8000/api/obtener-pago?propiedad={propiedad_id}"

    # Obtener los tipos de pago
    tipos_pago = TipoPago.objects.all()
    
    try:
        response = requests.get(api_url)
        data = response.json()

        # Si la API devuelve una lista, la asignamos directamente
        pagos = data if isinstance(data, list) else []


        if not pagos:
            messages.info(request, "No hay pagos pendientes para esta propiedad.")
            return render(request, "Recibos/generar_recibos.html", {"pagos": []})

        # Calcular los totales
        suma_subtotal = sum(pago["sub_total"] for pago in pagos)
        suma_descuentos = sum(pago["descuento"] for pago in pagos)
        suma_total = sum(pago["total"] for pago in pagos)

        return render(request, "Recibos/generar_recibos.html", {
            "propiedad_id": propiedad_id,
            "pagos": pagos,
            "suma_subtotal": suma_subtotal,
            "suma_descuentos": suma_descuentos,
            "suma_total": suma_total,
            "tipos_pago": tipos_pago,
        })

    except requests.exceptions.RequestException as e:
        messages.error(request, f"Error al conectar con el servidor: {str(e)}")
        return render(request, "Recibos/generar_recibos.html", {"pagos": []})
    

@login_required
def procesarPagoView(request, propiedad_id):
    # Crear un objeto request simulando que es un request GET
    factory = APIRequestFactory()
    api_request = factory.get(f"/api/obtener-pago?propiedad={propiedad_id}")
    
    # Llamar la vista directamente como si fuera una vista normal
    view = ObtenerPagosListView.as_view()
    response = view(api_request)

    # Si la respuesta es exitosa, obtener los datos de los pagos
    if response.status_code == 200:
        pagos = response.data  # Aquí obtienes los datos de los pagos
    else:
        pagos = []

    # Procesar el tipo de pago si es un POST
    if request.method == "POST":
        id_tipo_pago = request.POST.get("id_tipo_pago")  # Capturar el valor del select
        
        # Preparar los datos a enviar a la vista de generar recibo
        data = {
            "pagos": pagos,  # Pasar los pagos obtenidos de la API
            "id_propiedad": propiedad_id,  # Cambié propiedad_id a id_propiedad
            "id_tipo_pago": id_tipo_pago,  # Incluir el tipo de pago en el contexto
        }

        # Crear el request para enviar a GenerarReciboView
        factory = APIRequestFactory()
        api_request = factory.post('/api/generar-recibo', json.dumps(data), content_type='application/json')

        # Llamar la vista de generar recibo
        generar_recibo_view = GenerarReciboView.as_view()
        response = generar_recibo_view(api_request)

        # Comprobar que la respuesta sea un Response de DRF
        if isinstance(response, Response):
            if response.status_code == 201:
                # Extraer los datos de la respuesta
                recibo_id = response.data.get('id_recibo')
                contribuyente_id = response.data.get('id_contribuyente')
                message = response.data.get('message')

                # Pasar los datos al contexto para renderizar
                context = {
                    "pagos": pagos,
                    "id_propiedad": propiedad_id,
                    "id_tipo_pago": id_tipo_pago,
                    "recibo_id": recibo_id,
                    "contribuyente_id": contribuyente_id,
                    "message": message
                }
                return render(request, "Recibos/procesar_pago.html", context)
            else:
                # Si la respuesta es de error, manejarla
                context = {
                    "pagos": pagos,
                    "id_propiedad": propiedad_id,
                    "id_tipo_pago": id_tipo_pago,
                    "error_message": "Error al generar el recibo."
                }
                return render(request, "Recibos/procesar_pago.html", context)
        else:
            # Si la respuesta no es de tipo Response, manejarlo como error
            return render(request, "Recibos/procesar_pago.html", {"error_message": "Error en la respuesta del servidor"})
    
    # Si alguien accede a la vista sin enviar POST, redirigir o mostrar un mensaje
    return render(request, "Recibos/procesar_pago.html", {"error_message": "No se ha enviado un pago válido"})

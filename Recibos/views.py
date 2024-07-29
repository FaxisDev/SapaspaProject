from Tarifas.serializers import TarifaSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response  # type: ignore
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
from .filters import ReciboFilter

from .serializers import PagoSerializer, ReciboSerializer, TipoPagoSerializer

from Propiedades.models import Propiedad
from Servicios.models import Servicio
from Tarifas.models import Tarifa
from .models import Pago, Recibo, TipoPago

class ReciboListView(generics.ListAPIView):
    queryset = Recibo.objects.all().order_by("-id")
    serializer_class = ReciboSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReciboFilter


class ReciboDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recibo.objects.all()
    serializer_class = ReciboSerializer


class PagoListCreateView(generics.ListCreateAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

    def create(self, request, *args, **kwargs):
        # Si los datos son una lista, deserializa cada elemento individualmente
        if isinstance(request.data, list):
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class PagoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer


class TipoPagoListView(generics.ListAPIView):
    queryset = TipoPago.objects.all()
    serializer_class = TipoPagoSerializer


class ObtenerPagosListView(APIView):
    def get(self, request):
        id_propiedad = request.query_params.get("propiedad")

        # Fecha actual
        fecha_actual = timezone.now().date()

        # Obtener Tarifa actual
        tarifa = Tarifa.objects.filter(
            fecha_inicio_vigencia__lt=fecha_actual, fecha_fin_vigencia__gt=fecha_actual
        ).first()

        if not tarifa:
            return Response(
                {
                    "title": "Precio No Disponible",
                    "message": "Actualmente no hay un precio disponible. Por favor, inténtalo de nuevo más tarde."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        precio_base = float(tarifa.precio_base)
        total = precio_base - 0

        lista_pagos = []

        if id_propiedad:
            try:
                # Obtenemos el último recibo generado a esa propiedad
                id_recibo = Recibo.objects.filter(propiedad=id_propiedad).latest(
                    "fecha_creacion"
                )

                if id_recibo:
                    # Obtenemos el último pago para obtener fechas de cobro nuevas
                    ultimo_pago = Pago.objects.filter(recibo=id_recibo).latest(
                        "mes_pago"
                    )

                    # Obtener la fecha del último pago
                    ultima_fecha_pago = ultimo_pago.mes_pago

                    # Incrementar mes a mes desde el último pago hasta la fecha actual
                    fecha_proximo_pago = ultima_fecha_pago

                    while fecha_proximo_pago <= fecha_actual:
                        # Incrementa un mes, manejando el cambio de año y mes
                        if fecha_proximo_pago.month == 12:
                            fecha_proximo_pago = fecha_proximo_pago.replace(
                                year=fecha_proximo_pago.year + 1, month=1
                            )
                        else:
                            fecha_proximo_pago = fecha_proximo_pago.replace(
                                month=fecha_proximo_pago.month + 1
                            )

                        if fecha_proximo_pago <= fecha_actual:
                            lista_pagos.append(
                                {
                                    "mes_pago": fecha_proximo_pago.strftime("%Y-%m-%d"),
                                    "servicio": 1,
                                    "sub_total": precio_base,
                                    "total": total,
                                    "descuento": 0,
                                }
                            )
                    
                    if not lista_pagos:
                        return Response(
                            {
                                "title": "¡Estas al dia!",
                                "message": "No hay pagos pendientes en este momento.",
                            },
                            status=status.HTTP_200_OK
                        )
                return Response(lista_pagos, status=status.HTTP_200_OK)

            except Recibo.DoesNotExist:
                # Si no se encuentra ningún recibo, usamos la fecha de creación de la propiedad
                ultimo_pago = Propiedad.objects.filter(pk=id_propiedad).first()
                if ultimo_pago is None:
                    return Response([], status=status.HTTP_404_NOT_FOUND)

                # Obtener la fecha del último pago
                ultima_fecha_pago = ultimo_pago.fecha_creacion.date()

                # Incrementar mes a mes desde el último pago hasta la fecha actual
                fecha_proximo_pago = ultima_fecha_pago

                while fecha_proximo_pago <= fecha_actual:
                    # Incrementa un mes, manejando el cambio de año y mes
                    if fecha_proximo_pago.month == 12:
                        fecha_proximo_pago = fecha_proximo_pago.replace(
                            year=fecha_proximo_pago.year + 1, month=1
                        )
                    else:
                        fecha_proximo_pago = fecha_proximo_pago.replace(
                            month=fecha_proximo_pago.month + 1
                        )

                    if fecha_proximo_pago <= fecha_actual:
                        lista_pagos.append(
                            {
                                "mes_pago": fecha_proximo_pago.strftime("%Y-%m-%d"),
                                "servicio": 1,
                                "sub_total": precio_base,
                                "total": total,
                                "descuento": 0,
                            }
                        )

                return Response(lista_pagos, status=status.HTTP_200_OK)

        return Response(
            {
                "title": "¡Estas al dia!",
                "message": "No hay pagos pendientes en este momento.",
            },
            status=status.HTTP_200_OK
        )


class GenerarReciboView(APIView):
    def post(self, request):
        id_propiedad = request.data.get("id_propiedad")
        pagos = request.data.get("pagos")

        if not id_propiedad or not pagos:
            return Response(
                {"message": "id_propiedad y pagos son campos requeridos."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Fecha actual
        fecha_actual = timezone.now().date()

        # Obtener Tarifa actual
        tarifa = Tarifa.objects.filter(
            fecha_inicio_vigencia__lt=fecha_actual, fecha_fin_vigencia__gt=fecha_actual
        ).first()

        if not tarifa:
            return Response(
                {
                    "message": "Actualmente no hay un precio disponible. Por favor, inténtalo de nuevo más tarde."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        # Obtener TipoPago correspondiente (ejemplo: ID 2)
        try:
            tipo_pago = TipoPago.objects.get(id=2)
        except TipoPago.DoesNotExist:
            return Response(
                {"message": "Tipo de pago no encontrado."},
                status=status.HTTP_404_NOT_FOUND,
            )
        
        # Obtener la instancia de Propiedad correspondiente
        try:
            propiedad = Propiedad.objects.get(id=id_propiedad)
        except Propiedad.DoesNotExist:
            return Response(
                {"message": "Propiedad no encontrada."},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Crear Recibo
        recibo = Recibo.objects.create(propiedad=propiedad, tipo_pago=tipo_pago, tarifa=tarifa)

        # Crear Pagos asociados
        for pago_data in pagos:
            servicio_id = pago_data.get("servicio")
            try:
                servicio = Servicio.objects.get(id=servicio_id)
            except Servicio.DoesNotExist:
                return Response(
                    {"message": f"Servicio con id {servicio_id} no existe."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            Pago.objects.create(
                recibo=recibo,
                servicio=servicio,
                mes_pago=pago_data.get("mes_pago"),
                sub_total=pago_data.get("sub_total"),
                total=pago_data.get("total"),
                descuento=pago_data.get("descuento", 0)
            )

        return Response(
            {"id_recibo": recibo.id, "message": "El recibo ha sido generado y ahora puedes descargarlo o visualizarlo en tu perfil, en la pestaña de recibos."},
            status=status.HTTP_201_CREATED,
        )
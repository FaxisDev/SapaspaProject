from Tarifas.serializers import TarifaSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from .models import Pago, Recibo, TipoPago
from Propiedades.models import Propiedad
from Tarifas.models import Tarifa
from .filters import ReciboFilter
from .serializers import PagoSerializer, ReciboSerializer, TipoPagoSerializer
from rest_framework.response import Response  # type: ignore
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone


class ReciboListCreateView(generics.ListCreateAPIView):
    queryset = Recibo.objects.all()
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
                    ultima_fecha_pago = ultimo_pago.mes_pago.date()

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
                "message": "No hay pagos pendientes en este momento."
            },
            status=status.HTTP_204_NO_CONTENT,
        )

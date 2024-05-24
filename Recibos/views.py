from rest_framework import generics, status
from rest_framework.views import APIView
from .models import Pago, Recibo, TipoPago
from .filters import ReciboFilter
from .serializers import PagoSerializer, ReciboSerializer, TipoPagoSerializer
from rest_framework.response import Response # type: ignore
from django_filters.rest_framework import DjangoFilterBackend


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
        id_propiedad = request.query_params.get('propiedad')

        if id_propiedad:
            #Obtenemos ultimo recibo generado a esa propiedad, en dado caso de no ser encontrado ninguno, se  tomara la fecha en la que se dio de alta el contribuyente
            id_recibo = Recibo.objects.filter(propiedad=id_propiedad).latest('fecha_creacion')

            if id_recibo:
                #Obtenemos el ultimo pago para obtener fechas de cobro nuevas
                ultimo_pago = Pago.objects.filter(recibo=id_recibo).latest('mes_pago')
         
                return Response({'fecha': ultimo_pago.mes_pago}, status=status.HTTP_200_OK)

        return Response({
            'status': 'success',
            'data': 1
        }, status=status.HTTP_200_OK)
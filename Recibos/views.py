from rest_framework import generics, status
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

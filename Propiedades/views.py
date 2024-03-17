from rest_framework import generics, status
from .models import Propiedad, TipoPropiedad
from .filters import PropiedadFilter
from .serializers import PropiedadSerializer, TipoPropiedadSerializer
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

class PropiedadListCreateView(generics.ListCreateAPIView):
    queryset = Propiedad.objects.all()
    serializer_class = PropiedadSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PropiedadFilter

class PropiedadDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Propiedad.objects.all()
    serializer_class = PropiedadSerializer


class TipoPropiedadListCreateView(generics.ListCreateAPIView):
    queryset = TipoPropiedad.objects.all()
    serializer_class = TipoPropiedadSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'

class TipoPropiedadDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoPropiedad.objects.all()
    serializer_class = TipoPropiedadSerializer

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            return Response({'message': 'Propiedad actualizada correctamente'}, status=status.HTTP_200_OK)
        return response
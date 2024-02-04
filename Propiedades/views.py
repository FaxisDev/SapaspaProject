from rest_framework import generics, status
from .models import Propiedad, TipoPropiedad
from .serializers import PropiedadSerializer, TipoPropiedadSerializer
from rest_framework.response import Response

class PropiedadListCreateView(generics.ListCreateAPIView):
    queryset = Propiedad.objects.all()
    serializer_class = PropiedadSerializer

class PropiedadDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Propiedad.objects.all()
    serializer_class = PropiedadSerializer


class TipoPropiedadListCreateView(generics.ListCreateAPIView):
    queryset = TipoPropiedad.objects.all()
    serializer_class = TipoPropiedadSerializer

class TipoPropiedadDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoPropiedad.objects.all()
    serializer_class = TipoPropiedadSerializer

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            return Response({'message': 'Propiedad actualizada correctamente'}, status=status.HTTP_200_OK)
        return response
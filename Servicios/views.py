from .serializers import ServicioSerializer
from .models import Servicio
from rest_framework import generics

class TarifaListView(generics.ListAPIView):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

from rest_framework import generics
from .serializers import TarifaSerializer
from .models import Tarifa
class TarifaListCreateView(generics.ListAPIView):
    queryset = Tarifa.objects.all()
    serializer_class = TarifaSerializer

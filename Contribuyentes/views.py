from rest_framework import generics
from .serializers import ContribuyenteSerializer
from .models import Contribuyente
from .filters import ContribuyenteFilter
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class ContribuyenteListCreateView(generics.ListCreateAPIView):
    queryset = Contribuyente.objects.all()
    serializer_class = ContribuyenteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ContribuyenteFilter

class ContribuyenteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contribuyente.objects.all()
    serializer_class = ContribuyenteSerializer
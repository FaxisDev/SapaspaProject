from rest_framework import generics  # Importa el módulo generics de Django REST Framework para vistas genéricas basadas en clases.
from .serializers import ContribuyenteSerializer  # Importa el serializer ContribuyenteSerializer desde el módulo de serializers local.
from .models import Contribuyente  # Importa el modelo Contribuyente desde el módulo de modelos local.
from .filters import ContribuyenteFilter  # Importa el conjunto de filtros ContribuyenteFilter desde el módulo de filtros local.
from django_filters.rest_framework import DjangoFilterBackend  # Importa DjangoFilterBackend para agregar funcionalidad de filtrado.
from rest_framework.response import Response  # type: ignore
from rest_framework import generics, status

# Define una vista para listar y crear instancias del modelo Contribuyente.
class ContribuyenteListCreateView(generics.ListCreateAPIView):
    queryset = Contribuyente.objects.all()  # Especifica el conjunto de datos que se recuperará, en este caso, todas las instancias de Contribuyente.
    serializer_class = ContribuyenteSerializer  # Especifica el serializer que se usará para convertir las instancias de Contribuyente a representaciones JSON.
    filter_backends = [DjangoFilterBackend]  # Define los backends de filtrado a utilizar, en este caso, DjangoFilterBackend para habilitar el filtrado.
    filterset_class = ContribuyenteFilter  # Especifica la clase de filtros a usar para filtrar el queryset según ciertos criterios.

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

# Define una vista para recuperar, actualizar y eliminar instancias del modelo Contribuyente.
class ContribuyenteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contribuyente.objects.all()  # Especifica el conjunto de datos que se recuperará, en este caso, todas las instancias de Contribuyente.
    serializer_class = ContribuyenteSerializer  # Especifica el serializer que se usará para convertir las instancias de Contribuyente a representaciones JSON.
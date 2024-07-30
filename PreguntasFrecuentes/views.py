from .serializers import PreguntaFrecuenteSerializer  # Importa el serializer PreguntaFrecuenteSerializer desde el módulo de serializers local.
from .models import PreguntaFrecuente  # Importa el modelo PreguntaFrecuente desde el módulo de modelos local.
from .filters import PreguntaFrecuenteFilter  # Importa el conjunto de filtros PreguntaFrecuenteFilter desde el módulo de filtros local.
from rest_framework import generics  # Importa el módulo generics de Django REST Framework para vistas genéricas basadas en clases.
from django_filters.rest_framework import DjangoFilterBackend  # Importa DjangoFilterBackend para agregar funcionalidad de filtrado.

# Define una vista para listar las instancias del modelo PreguntaFrecuente con paginación y filtrado.
class PreguntaFrecuenteListView(generics.ListAPIView):
    queryset = PreguntaFrecuente.objects.all().order_by("-id")  # Especifica el conjunto de datos que se recuperará, en este caso, todas las instancias de PreguntaFrecuente.
    serializer_class = PreguntaFrecuenteSerializer  # Especifica el serializer que se usará para convertir las instancias de PreguntaFrecuente a representaciones JSON.
    filter_backends = [DjangoFilterBackend]  # Define los backends de filtrado a utilizar, en este caso, DjangoFilterBackend para habilitar el filtrado.
    filterset_class = PreguntaFrecuenteFilter  # Especifica la clase de filtros a usar para filtrar el queryset según ciertos criterios.


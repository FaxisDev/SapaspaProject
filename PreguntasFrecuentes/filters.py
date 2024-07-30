from .models import PreguntaFrecuente  # Importa el modelo PreguntaFrecuente desde el módulo de modelos local.
import django_filters  # Importa el módulo django_filters, que proporciona herramientas para crear filtros.
from django.db.models import Q


# Define un conjunto de filtros para el modelo PreguntaFrecuente.
class PreguntaFrecuenteFilter(django_filters.FilterSet):
    # Define un filtro para el campo 'pregunta', que realiza una búsqueda insensible a mayúsculas y minúsculas.
    pregunta = django_filters.CharFilter(field_name="pregunta", lookup_expr="icontains")

    # Define un filtro para el campo 'descripcion', también insensible a mayúsculas y minúsculas.
    descripcion = django_filters.CharFilter(
        field_name="descripcion", lookup_expr="icontains"
    )

    # Metaclase que especifica el modelo al que se aplica el conjunto de filtros y los campos que se pueden filtrar.
    class Meta:
        model = PreguntaFrecuente  # El modelo que se va a filtrar.
        fields = []  # Indica que todos los campos del modelo son susceptibles de ser filtrados.

    def filter_queryset(self, queryset):
        # Obtiene los parámetros de búsqueda del request
        pregunta = self.request.GET.get("pregunta")
        descripcion = self.request.GET.get("descripcion")

        if pregunta and descripcion:
            # Si ambos parámetros están presentes, primero intenta filtrar por 'pregunta'
            queryset = queryset.filter(
                Q(pregunta__icontains=pregunta) | Q(descripcion__icontains=descripcion)
            )
        elif pregunta:
            # Si solo 'pregunta' está presente, filtra por 'pregunta'
            queryset = queryset.filter(pregunta__icontains=pregunta)
        elif descripcion:
            # Si solo 'descripcion' está presente, filtra por 'descripcion'
            queryset = queryset.filter(descripcion__icontains=descripcion)

        return queryset

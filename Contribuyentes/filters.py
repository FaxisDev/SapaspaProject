from .models import Contribuyente
import django_filters
from django.db.models import Q


class ContribuyenteFilter(django_filters.FilterSet):
    # Filtros para los campos folio_unico, telefono y curp
    folio_unico = django_filters.CharFilter(field_name="folio_unico", lookup_expr="exact")
    telefono = django_filters.NumberFilter(field_name="telefono", lookup_expr="exact")
    curp = django_filters.CharFilter(field_name="curp", lookup_expr="exact")

    class Meta:
        model = Contribuyente
        # Definimos los campos disponibles para el filtrado
        fields = ["folio_unico", "telefono", "curp"]

    def filter_queryset(self, queryset):
        """
        Sobrescribimos el método `filter_queryset` para aplicar lógica de filtrado personalizada.

        1. Si se proporcionan `folio_unico` y `telefono`, filtrar el queryset usando ambos.
        2. Si no se encuentran registros con `folio_unico` y `telefono`, filtrar usando `curp`.
        """

        # Obtenemos los valores del formulario limpio
        folio_unico = self.form.cleaned_data.get("folio_unico")
        telefono = self.form.cleaned_data.get("telefono")
        curp = self.form.cleaned_data.get("curp")

        if (folio_unico and telefono) or curp:
            # Si se proporcionan folio_unico y telefono, filtrar usando ambos con coincidencias parciales (icontains).
            # O, si se proporciona curp, filtrar por curp con coincidencias parciales.
            queryset = queryset.filter(
                Q(Q(folio_unico__exact=folio_unico) & Q(telefono__exact=telefono))
                | Q(curp__exact=curp)
            )
        else:
            return []

        return queryset

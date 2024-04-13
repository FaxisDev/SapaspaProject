from .models import Contribuyente

import django_filters

class ContribuyenteFilter(django_filters.FilterSet):
    folio_unico = django_filters.CharFilter(field_name='folio_unico', lookup_expr='exact')
    telefono = django_filters.NumberFilter(field_name='telefono', lookup_expr='exact')
    curp = django_filters.CharFilter(field_name='curp', lookup_expr='exact')

    class Meta:
        model = Contribuyente
        fields = '__all__'
from .models import Contribuyente

import django_filters

class ContribuyenteFilter(django_filters.FilterSet):
    nombre = django_filters.CharFilter(field_name='nombre', lookup_expr='icontains')

    class Meta:
        model = Contribuyente
        fields = '__all__'
from .models import Recibo

import django_filters

class ReciboFilter(django_filters.FilterSet):
    propiedad = django_filters.NumberFilter(field_name='propiedad', lookup_expr='exact')
    contribuyente = django_filters.CharFilter(field_name='propiedad__contribuyente__id', lookup_expr='exact')


    class Meta:
        model = Recibo
        fields = '__all__'
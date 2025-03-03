from .models import Propiedad

import django_filters

class PropiedadFilter(django_filters.FilterSet):
    ciudad = django_filters.CharFilter(field_name='ciudad', lookup_expr='icontains')
    referencias = django_filters.CharFilter(field_name='referencias', lookup_expr='icontains')
    contribuyente = django_filters.NumberFilter(field_name='contribuyente', lookup_expr='exact')

    class Meta:
        model = Propiedad
        fields = '__all__'
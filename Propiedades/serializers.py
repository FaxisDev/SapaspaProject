# propiedades/serializers.py
from rest_framework import serializers
from .models import Propiedad, TipoPropiedad

class PropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propiedad
        fields = '__all__'

class TipoPropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPropiedad
        fields = '__all__'

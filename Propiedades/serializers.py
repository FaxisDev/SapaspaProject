# propiedades/serializers.py
from rest_framework import serializers
from .models import Propiedad, TipoPropiedad

class TipoPropiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPropiedad
        fields = '__all__'
class PropiedadSerializer(serializers.ModelSerializer):
    info_pago = serializers.SerializerMethodField()

    def get_info_pago(self, objeto):
        return objeto.info_pago
    class Meta:
        model = Propiedad
        fields = '__all__'


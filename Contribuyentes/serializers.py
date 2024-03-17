from rest_framework import serializers
from .models import Contribuyente

class ContribuyenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribuyente
        fields = '__all__'


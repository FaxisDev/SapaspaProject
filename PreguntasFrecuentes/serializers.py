from rest_framework import serializers  # Importa el módulo serializers de Django REST Framework.
from .models import PreguntaFrecuente  # Importa el modelo PreguntaFrecuente desde el módulo de modelos local.

# Define un serializer para el modelo PreguntaFrecuente.
class PreguntaFrecuenteSerializer(serializers.ModelSerializer):
    # Metaclase que define el modelo y los campos que serán incluidos en la serialización.
    class Meta:
        model = PreguntaFrecuente  # Especifica el modelo PreguntaFrecuente como el modelo asociado al serializer.
        fields = '__all__'  # Indica que todos los campos del modelo deben ser incluidos en la serialización.

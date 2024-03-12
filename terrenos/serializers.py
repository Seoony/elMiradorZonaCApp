from rest_framework.serializers import ModelSerializer
from socios.serializers import SimplifiedSocioSerializer
from .models import Terreno

class TerrenoDetailedSerializer(ModelSerializer):
  socio = SimplifiedSocioSerializer(many=False)
  creado_por = SimplifiedSocioSerializer(many=False)
  modificado_por = SimplifiedSocioSerializer(many=False)
  class Meta:
    model = Terreno
    fields = '__all__'
    
class SimplifiedTerrenoSerializer(ModelSerializer):
  class Meta:
    model = Terreno
    fields = ['id', 'codigo', 'estado']
    
class TerrenoSimpleSerializer(ModelSerializer):
  class Meta:
    model = Terreno
    fields = ['id', 'manzana', 'lote', 'codigo', 'area', 'disponible', 'estado']
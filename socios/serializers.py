from rest_framework.serializers import ModelSerializer
from terrenos.models import Terreno
from .models import Socio

class SimplifiedTerrenoSerializer(ModelSerializer):
  class Meta:
    model = Terreno
    fields = ['id', 'codigo', 'estado']

class DetalleSocioSerializer(ModelSerializer):
  terreno = SimplifiedTerrenoSerializer(many=False)
  class Meta:
    model = Socio
    fields = ['id', 'dni', 'nombres', 'apellido_pat', 'apellido_mat',
              'fecha_nacimiento', 'terreno', 'direccion', 'celular',
              'estado', 'vivencia', 'exonerado', 'observaciones',
              'creado_por', 'modificado_por', 'is_staff', 'is_superuser']

class SocioSerializer(ModelSerializer):
  class Meta:
    model = Socio
    fields = ['id', 'dni', 'nombres', 'apellido_pat', 'apellido_mat',
              'celular', 'estado', 'vivencia', 'observaciones']
    
class SimplifiedSocioSerializer(ModelSerializer):
  class Meta:
    model = Socio
    fields = ['id', 'nombres', 'apellido_pat', 'apellido_mat',
              'estado']
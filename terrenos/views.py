from rest_framework.decorators import api_view
from rest_framework.response import Response
from terrenos.serializers import TerrenoSimpleSerializer, TerrenoDetailedSerializer
from terrenos.models import Terreno

@api_view(['GET'])
def list_terrenos(request):
  terrenos = Terreno.objects.all()
  serializer = TerrenoSimpleSerializer(terrenos, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def terreno_detail(request, pk):
  terreno = Terreno.objects.get(id=pk)
  serializer = TerrenoDetailedSerializer(terreno, many=False)
  return Response(serializer.data)

@api_view(['POST'])
def create_terreno(request):
  serializer = TerrenoSimpleSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)

@api_view(['PUT'])
def update_terreno(request, pk):
  terreno = Terreno.objects.get(id=pk)
  serializer = TerrenoSimpleSerializer(instance=terreno, data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)

@api_view(['PUT'])
def activar_terreno(request, pk):
  terreno = Terreno.objects.get(id=pk)
  terreno.estado = "A"
  terreno.save()
  return Response('Terreno activado')

@api_view(['PUT'])
def desactivar_terreno(request, pk):
  terreno = Terreno.objects.get(id=pk)
  terreno.estado = "I"
  terreno.save()
  return Response('Terreno desactivado')

@api_view(['PUT'])
def eliminar_terreno(request, pk):
  terreno = Terreno.objects.get(id=pk)
  terreno.estado = "*"
  terreno.save()
  return Response('Terreno eliminado lógicamente')
from rest_framework.decorators import api_view
from rest_framework.response import Response
from socios.serializers import SocioSerializer, DetalleSocioSerializer
from socios.models import Socio

@api_view(['GET'])
def socios_list(request):
  socios = Socio.objects.all()
  serializer = SocioSerializer(socios, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def socios_detail(request, pk):
  socio = Socio.objects.get(id=pk)
  serializer = DetalleSocioSerializer(socio, many=False)
  return Response(serializer.data)

@api_view(['POST'])
def socios_create(request):
  serializer = SocioSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)

@api_view(['PUT'])
def socios_update(request, pk):
  socio = Socio.objects.get(id=pk)
  serializer = DetalleSocioSerializer(instance=socio, data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)

@api_view(['PUT'])
def activar_socio(request, pk):
  socio = Socio.objects.get(id=pk)
  socio.estado = "A"
  socio.save()
  return Response('Socio activado')

@api_view(['PUT'])
def desactivar_socio(request, pk):
  socio = Socio.objects.get(id=pk)
  socio.estado = "I"
  socio.save()
  return Response('Socio desactivado')

@api_view(['PUT'])
def eliminar_socio(request, pk):
  socio = Socio.objects.get(id=pk)
  socio.estado = "*" # Eliminado
  socio.save()
  return Response('Socio eliminado lógicamente')
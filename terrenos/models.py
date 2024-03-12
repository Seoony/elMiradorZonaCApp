from django.db import models

class Terreno (models.Model):
  manzanas=[
    ('A', 'Mz A, no existe'),
    ('B', 'Mz B'),
    ('G', 'Mz G'),
    ('H', 'Mz H'),
    ('H\'', 'Mz H prima'),
    ('I', 'Mz I'),
    ('J', 'Mz J'),
    ('K', 'Mz K'),
    ('M', 'Mz M'),
    ('Ñ', 'Mz Ñ'),
    ('O', 'Mz O'),
    ('P', 'Mz P'),
    ('Q', 'Mz Q'),
    ('R', 'Mz R'),
    ('S', 'Mz S'),
    ('T', 'Mz T'),
    ('U', 'Mz U'),
    ('V', 'Mz V'),
    ('X', 'Mz X'),
  ]
  codigo = models.CharField(max_length=4, unique=True)
  manzana = models.CharField(max_length=2, choices=manzanas, default='A')
  lote = models.CharField(max_length=2)
  area = models.DecimalField(max_digits=5, decimal_places=2, default=160.00)
  otros_usos = models.BooleanField(default=False)
  disponible = models.BooleanField(default=True)
  socio = models.ForeignKey(
    'socios.Socio', on_delete=models.SET_NULL,
    null=True, blank=True, related_name='socio_asignado')
  observaciones = models.TextField(default="Ninguna")
  creado_por = models.ForeignKey(
    'socios.Socio', on_delete=models.SET_NULL,
    null=True, blank=True, related_name='terreno_creado_por')
  modificado_por = models.ForeignKey(
    'socios.Socio', on_delete=models.SET_NULL,
    null=True, blank=True, related_name='terreno_modificado_por')
  ultima_modificacion = models.DateTimeField(auto_now=True)
  estado = models.CharField(max_length=1, default="A")
  
  def __str__(self):
    return self.manzana + " - " + self.lote
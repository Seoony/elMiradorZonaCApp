from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomSocioManager(BaseUserManager):
  def create_user(self, dni, nombres=None, apellido_pat=None,
                  apellido_mat=None, fecha_nacimiento=None, password=None):
    if not dni or len(dni) != 8:
      raise ValueError('El usuario debe tener un DNI válido')
    try:
      dni_int = int(dni)
      socio = self.model(
        dni=dni,
        nombres=nombres,
        apellido_pat=apellido_pat,
        apellido_mat=apellido_mat,
        fecha_nacimiento=fecha_nacimiento,
      )
      socio.set_password(password)
      socio.save(using=self._db)
      return socio
    except ValueError:
      raise ValueError('El DNI debe contener solo números')

  def create_superuser(self, dni, nombres=None, apellido_pat=None,
                       apellido_mat=None, fecha_nacimiento=None, password=None):
    socio = self.create_user(
      dni=dni,
      nombres=nombres,
      apellido_pat=apellido_pat,
      apellido_mat=apellido_mat,
      fecha_nacimiento=fecha_nacimiento,
      password=password
    )
    socio.is_staff = True
    socio.is_superuser = True
    socio.save(using=self._db)
    return socio

class Socio(AbstractBaseUser, PermissionsMixin):
  dni = models.CharField(max_length=8, unique=True)
  #is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  nombres = models.CharField(max_length=63)
  apellido_pat = models.CharField(max_length=31)
  apellido_mat = models.CharField(max_length=31)
  fecha_nacimiento = models.DateField()
  direccion = models.CharField(max_length=100, default="Asoc. de Vivienda \"El Mirador Zona C\" Mz-A Lt-1")
  celular = models.CharField(max_length=9)
  #fecha_ingreso = models.DateField()
  estado = models.CharField(max_length=1, default="A")
  vivencia = models.BooleanField(default=False)
  exonerado = models.BooleanField(default=False)
  #fecha_salida = models.DateField(allow_null=True, blank=True)
  #motivo_salida = models.CharField(max_length=100, allow_null=True, blank=True, default="")
  observaciones = models.TextField()
  creado_por = models.ForeignKey(
    'self', on_delete=models.SET_NULL,
    null=True, blank=True, related_name='socio_creado_por')
  modificado_por = models.ForeignKey(
    'self', on_delete=models.SET_NULL,
    null=True, blank=True, related_name='socio_modificado_por')
  
  USERNAME_FIELD = 'dni'
  REQUIRED_FIELDS = ['nombres', 'apellido_pat', 'apellido_mat', 'fecha_nacimiento']

  objects = CustomSocioManager()
  def __str__(self):
    return self.nombres + " " + self.apellido_pat + " " + self.apellido_mat
  
  def get_by_natural_key(self, dni):
    return self.get(dni=dni)
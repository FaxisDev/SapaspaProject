from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Contribuyente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    materno = models.CharField(max_length=100)
    numero_interior = models.TextField(null=True,blank=True,)
    numero_exterior = models.TextField(default=None)
    calle = models.TextField(default=None)
    entre_calles = models.TextField(default=None)
    colonia = models.TextField(default=None)
    ciudad = models.TextField(default=None)
    estado = models.TextField(default=None)
    codigo_postal = models.CharField(default=None, max_length=10)
    referencias = models.TextField(null=True, blank=True,)
    telefono = models.CharField(max_length=20, default=None)
    correo_electronico = models.EmailField(default=None)
    estatus = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default='activo'),
     # Otros campos del modelo...
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    id_user = models.ForeignKey(User, on_delete=models.PROTECT,default=None)

    def __str__(self):
        return self.nombre

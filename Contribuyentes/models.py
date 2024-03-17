from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contribuyente(models.Model):
    id = models.AutoField(primary_key=True)
    folio_unico = models.CharField(max_length=50, unique=True, null=True, default=None)
    curp = models.CharField(max_length=50, unique=True, null=True, default=None)
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, default=None)
    correo_electronico = models.EmailField(default=None, unique=True)
    estatus = models.CharField(max_length=20, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default='activo'),
     # Otros campos del modelo...
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    id_user = models.ForeignKey(User, on_delete=models.PROTECT,default=None)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Contribuyente'
        verbose_name_plural = 'Contribuyentes'
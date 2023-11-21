from django.db import models

from users.models import Usuario


class ClanesEquipos(models.Model):
    nombre = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
# Create your models here.

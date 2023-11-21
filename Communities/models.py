from django.db import models

from users.models import Usuario


class Comunidades(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
# Create your models here.

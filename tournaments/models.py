from django.db import models
from django.conf import settings
from django.db import models

# Create your models here.
# tournaments/models.py

from django.db import models
from users.models import Usuario


class Torneo(models.Model):
    nombre = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    premio = models.TextField()

    class Inscripcion(models.Model):
        usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

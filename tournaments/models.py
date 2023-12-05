from django.db import models

# Create your models here.
# tournaments/models.py

from django.db import models
from users.models import Usuario


class Torneo(models.Model):
    nombre = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    premio = models.TextField()


    def __str__(self):
        return self.nombre

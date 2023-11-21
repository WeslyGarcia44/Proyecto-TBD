from django.db import models
class RangoUsuario(models.Model):
    nombre = models.CharField(max_length=255)
    nivel = models.IntegerField()

    def __str__(self):
        return self.nombre
# Create your models here.

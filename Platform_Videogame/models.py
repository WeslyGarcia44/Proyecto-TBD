from django.db import models
class PlataformaVideojuego(models.Model):
    nombre = models.CharField(max_length=255, primary_key=True)
    empresa = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
# Create your models here.

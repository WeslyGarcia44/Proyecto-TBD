from django.db import models
class DesarrolladoraVideojuego(models.Model):
    nombre = models.CharField(max_length=255, primary_key=True)
    pais = models.CharField(max_length=100)
    fechaFundacion = models.DateField()

    def __str__(self):
        return self.nombre
# Create your models here.

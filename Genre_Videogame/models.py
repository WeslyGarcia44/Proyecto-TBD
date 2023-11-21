from django.db import models
class GeneroVideojuego(models.Model):
    nombre = models.CharField(max_length=255, primary_key=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
# Create your models here.

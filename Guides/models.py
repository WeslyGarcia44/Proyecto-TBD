from django.db import models

from games.models import Videojuego


class Guias(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
# Create your models here.

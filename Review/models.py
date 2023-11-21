from django.db import models

from Game_Developer.models import DesarrolladoraVideojuego
from games.models import Videojuego
from users.models import Usuario


class Reseña(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    fecha = models.DateField()
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)
    desarrolladora = models.ForeignKey(DesarrolladoraVideojuego, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
# Create your models here.

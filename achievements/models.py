# achievements/models.py

from django.db import models
from django.conf import settings
from games.models import Game  # Asegúrate de que la importación sea correcta según tu estructura

class Achievement(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='achievements')
    name = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField(upload_to='achievement_icons/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.game.title}"

class UserAchievement(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_achievements')
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    obtained_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'achievement')  # Evita duplicados

    def __str__(self):
        return f"{self.user.username} - {self.achievement.name}"

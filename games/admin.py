# games/admin.py

from django.contrib import admin
from .models import Game, UserGameList

admin.site.register(Game)
admin.site.register(UserGameList)

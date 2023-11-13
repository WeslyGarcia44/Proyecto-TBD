# achievements/views.py

from django.shortcuts import render
from .models import Achievement, UserAchievement
from django.http import HttpResponse
def list_achievements(request):
    achievements = Achievement.objects.all()
    return render(request, 'achievements/list_achievements.html', {'achievements': achievements})

def user_achievements(request, user_id):
    user_achievements = UserAchievement.objects.filter(user_id=user_id)
    return render(request, 'achievements/user_achievements.html', {'user_achievements': user_achievements})
# achievements/views.py


def test_view(request):
    # Lógica para la vista
    return HttpResponse("Esta es una vista de prueba.")

from django.shortcuts import render
def home_view(request):
    # Asumiendo que tienes una plantilla 'home.html' en la carpeta de plantillas de tu aplicación o en la carpeta global de plantillas.
    return render(request, 'main/home.html')





def login_view(request):
    return render(request, 'registration/login.html')



def tournaments_view(request):
    return render(request, 'Categories/Tournaments.html')


from django.shortcuts import render

def signup_view(request):
    # Tu lógica para manejar el registro
    return render(request, 'registration/signup.html')

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import User
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log'  # Archivo de registro donde se escribirán los mensajes
)


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        # Usuario está autenticado

        import requests

        url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkYmQ3MGM4NWEwNGJhNThlODc3ZTE1OTQ1MWJjZjQxZiIsInN1YiI6IjY2MmQ1MjhkYTgwNjczMDEyOGU4NTkzZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.0KgaE0j_dIzCFXiyYTzug0UqdYYtAlPYvtLWTG4J824"
        }

        response = requests.get(url, headers=headers)
        import json
        data = json.loads(response.text)

        context = {
            'user_logged_in': True,
            'user': request.user,
            'movies': data['results'],
            'url_prefix': 'https://image.tmdb.org/t/p/w1280'
        }

    else:
        # Usuario no está autenticado
        context = {'user_logged_in': False}
    return render(request, 'index.html', context)



from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log'
)

@csrf_protect
def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('correo')
        password = request.POST.get('contrasenia')

        logging.info(f"Correo: {email}, Contraseña: {password}")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            logging.info(f"Usuario autenticado correctamente: {user}")
            print(f"Usuario autenticado correctamente: {user}")
            return redirect('index')
        else:
            messages.error(request, "Credenciales inválidas. Inténtalo de nuevo.")
            logging.error("Credenciales inválidas. Inténtalo de nuevo.")

    return render(request, 'auth/login.html')



def register(request):
    if request.method == 'POST':
        name = request.POST['nombre']
        email = request.POST['correo']
        password = request.POST['contrasenia']
        confirm_password = request.POST['contrasenia_confirm']

        if password != confirm_password:
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('register')

        try:
            new_user = User(name=name, email=email)
            new_user.set_password(password)
            new_user.save()
            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Error al registrar usuario: {e}')
            return redirect('register')

    return render(request, 'auth/register.html')


from django.contrib.auth import logout as user_logout
from django.shortcuts import redirect

def logout(request):
    user_logout(request)
    return redirect('index')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
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
        # Usuario autenticado: pasar contexto para usuario autenticado
        context = {
            'is_authenticated': True,
            'username': request.user.username,
        }
    else:
        # Usuario no autenticado: pasar contexto para usuario no autenticado
        context = {
            'is_authenticated': False,
        }
    return render(request, 'index.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST['correo']
        password = request.POST['contrasenia']

        # Autenticar al usuario
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Iniciar sesión
            login(request, user)
            logging.info(f'Inicio de sesión exitoso para el usuario: {user.username}')
            return redirect('index')  # Redirigir a la página de inicio después del inicio de sesión exitoso
        else:
            messages.error(request, 'Credenciales inválidas. Inténtalo de nuevo.')
    return render(request, 'auth/login.html')


def register(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        name = request.POST['nombre']
        email = request.POST['correo']
        password = request.POST['contrasenia']
        confirm_password = request.POST['contrasenia_confirm']

        # Validar contraseñas
        if password != confirm_password:
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('register')  # Redirigir de vuelta al formulario de registro

        # Crear un nuevo usuario
        try:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = name
            user.save()
            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
            return redirect('login')  # Redirigir al inicio de sesión después del registro
        except Exception as e:
            messages.error(request, f'Error al registrar usuario: {e}')
            return redirect('register')  # Redirigir de vuelta al formulario de registro en caso de error
    return render(request, 'auth/register.html')
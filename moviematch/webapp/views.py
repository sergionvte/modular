from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'auth/login.html')


def crear_usuario(request):
    return render(request, 'auth/crear_usuario.html')
from django.shortcuts import render
from appserviceshop.models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView,CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


def Iniciosesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                return render(request, "index.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "iniciosesion.html", {"mensaje": "Datos incorrectos"})
        else:
            return render(request, "iniciosesion.html", {"mensaje": "Formulario erroneo"})
    form = AuthenticationForm()
    return render(request, "iniciosesion.html", {'form': form})

@login_required
def Logout(request):
    return render(request, "cerrarsesion.html")


def Registrousuario(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                return render(request, "index.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "Usuario Registrado.html", {"mensaje": "Datos incorrectos"})
        else:
            return render(request, "iniciosesion.html", {"mensaje": "Formulario erroneo"})
    form = AuthenticationForm()
    return render(request, "iniciosesion.html", {'form': form})

@login_required
def Logout(request):
    return render(request, "cerrarsesion.html")
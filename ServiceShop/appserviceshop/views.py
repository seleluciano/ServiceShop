from django.shortcuts import render, redirect
from appserviceshop.models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm,UserEditForm,AvatarFormulario
from django.contrib.auth.decorators import login_required
#from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView,CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Servicio,Avatar
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash


@login_required
def Inicio(request):
    return render(request, 'index.html')

@login_required
def Logout(request):
    return render(request, 'cerrarsesion.html')

@login_required
def Carrito(request):
    return render(request, 'carrito.html')

def Iniciosesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                return redirect('inicio')  # Redirige al inicio o a la página deseada
            else:
                return render(request, "iniciosesion.html", {"mensaje": "Datos incorrectos", "hide_navbar": True})
        else:
            return render(request, "iniciosesion.html", {"mensaje": "Formulario erróneo", "hide_navbar": True})
    
    form = AuthenticationForm()
    return render(request, "iniciosesion.html", {'form': form, 'hide_navbar': True})

def Registrarusuario(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "index.html",  {"mensaje": "Usuario Creado :)"})
    else:
        form = UserRegisterForm()

    return render(request, "registrarusuario.html", {'form': form, 'hide_navbar': True})
@login_required 
def Editarperfil(request): 
    usuario = request.user 

    if request.method == 'POST': 
        miFormulario = UserEditForm(request.POST, instance=usuario)
        if miFormulario.is_valid(): 
            informacion = miFormulario.cleaned_data 

            nuevo_username = informacion['username']
            if nuevo_username != usuario.username:
                if User.objects.filter(username=nuevo_username).exists():
                    miFormulario.add_error('username', "El nombre de usuario ya está en uso.")
                else:
                    usuario.username = nuevo_username
            
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            usuario.email = informacion['email']

            # Manejo de contraseña
            if informacion.get('password1') and informacion['password1'] == informacion['password2']:
                usuario.set_password(informacion['password1'])  # Cambia la contraseña
                update_session_auth_hash(request, usuario)  # Mantiene la sesión activa

            usuario.save() 
            return render(request, 'index.html') # Redirigir a otra página después de guardar
    else: 
        miFormulario = UserEditForm(instance=usuario)  # Carga los datos actuales del usuario

    return render(request, "editarperfil.html", {"miFormulario": miFormulario, "usuario": usuario})  

@login_required
def Cambiaravatar(request):
    usuario = request.user
    try:
        avatar = usuario.avatar
    except Avatar.DoesNotExist:
        avatar = None

    if request.method == 'POST':
        miFormulario = AvatarFormulario(request.POST, request.FILES, instance=avatar)  # Asegúrate de incluir request.FILES
        if miFormulario.is_valid():
            miFormulario.save()
            return render(request, "index.html")
    else:
        miFormulario = AvatarFormulario(instance=avatar)

    return render(request, "cambiaravatar.html", {"miFormulario": miFormulario, "avatar": avatar})

@login_required
def Compras(request):
    return render(request, 'miscompras.html')

class Detalleservicio(LoginRequiredMixin,DetailView):
   model=Servicio
   template_name="servicio_detalle.html"

class Crearservicio(LoginRequiredMixin, CreateView):
    model = Servicio
    fields = ['name', 'categoria', 'precio', 'zona', 'descripcion', 'disponibilidadhoraria', 'imagen']
    success_url = reverse_lazy('inicio') 
    template_name = "crearservicio.html"

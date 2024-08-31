from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = '__all__' #['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'localidad', 'provincia', 'codigo_postal']
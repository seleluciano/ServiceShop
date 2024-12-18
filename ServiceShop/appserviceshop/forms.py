from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from .models import *
from django.core.exceptions import ValidationError  # Agregar esta importación

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu nombre'}))
    last_name = forms.CharField(label="Apellido", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu apellido'}))
    username = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu usuario'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu email'}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu contraseña'}))
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repite tu contraseña'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}
    
class UserEditForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
        }
        help_texts = {k: "" for k in fields}

class AvatarFormulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']
        labels = {
            'imagen': 'Imagen de perfil'
        }
        widgets = {
            'imagen': forms.FileInput(attrs={'class': 'form-control'})
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['name', 'categoria', 'precio', 'zona', 'descripcion', 'disponibilidadhoraria', 'imagen']
        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'zona': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'disponibilidadhoraria': forms.TextInput(attrs={'class': 'form-control'}),
        }
  
  
class ReseñaForm(forms.ModelForm):
    class Meta:
        model = Reseña
        fields = ['calificacion', 'texto']
        widgets = {
            'calificacion': forms.Select(choices=[(i, f'{i} estrellas') for i in range(1, 6)]),  # Dropdown de 1 a 5
            'texto': forms.Textarea(attrs={'placeholder': 'Escribe tu comentario aquí', 'rows': 4, 'cols': 40})  # Campo de texto con un tamaño adecuado
        }
        labels = {
            'calificacion': 'Calificación',
            'texto': 'Comentario',
        }

    # Validación personalizada para asegurar que se selecciona una calificación
    def clean_calificacion(self):
        calificacion = self.cleaned_data.get('calificacion')
        if not calificacion:
            raise ValidationError('Debes seleccionar una calificación.')
        return calificacion

class ReseñaUsuarioForm(forms.ModelForm):
    class Meta:
        model = ReseñaUsuario
        fields = ['calificacion', 'texto']
        widgets = {
            'calificacion': forms.Select(choices=[(i, f'{i} estrellas') for i in range(1, 6)]),  # Dropdown de 1 a 5
            'texto': forms.Textarea(attrs={'placeholder': 'Escribe tu comentario aquí', 'rows': 4, 'cols': 40})  # Campo de texto con un tamaño adecuado
        }
        labels = {
            'calificacion': 'Calificación',
            'texto': 'Comentario',
        }

    # Validación personalizada para asegurar que se selecciona una calificación
    def clean_calificacion(self):
        calificacion = self.cleaned_data.get('calificacion')
        if not calificacion:
            raise ValidationError('Debes seleccionar una calificación.')
        return calificacion
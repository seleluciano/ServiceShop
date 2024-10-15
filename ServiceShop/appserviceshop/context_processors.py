from .models import *
from django.templatetags.static import static

def avatar_processor(request):
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(user=request.user).first()
        if avatar and avatar.imagen:
            imagen = avatar.imagen.url  # Si el usuario tiene un avatar, usa su URL
        else:
            imagen = static('img/predeterminado.jpg')  # Imagen predeterminada si no tiene avatar
    else:
        imagen = static('img/predeterminado.jpg')  # Imagen predeterminada para usuarios no autenticados

    return {'imagen': imagen}

def servicios_context(request):
    servicios = Servicio.objects.all()
    return {'servicios': servicios}

def ventas_context(request):
    if request.user.is_authenticated:
        # Obtiene las ventas del usuario actual
        ventas_list = Ventas_M.objects.filter(vendedor=request.user)
    else:
        ventas_list = []

    return {
        'ventas_list': ventas_list
    }
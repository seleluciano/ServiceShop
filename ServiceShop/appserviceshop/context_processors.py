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

# context_processors.py
from .models import Carrito

def carrito_context(request):
    if request.user.is_authenticated:
        try:
            carrito = Carrito.objects.get(usuario=request.user)
            servicios_en_carrito = carrito.servicios.all()
            total_precio = sum(servicio.precio for servicio in servicios_en_carrito)
            cantidad_total = sum(servicio.servicioencarrito_set.first().cantidad for servicio in servicios_en_carrito)  # Calcular la cantidad total

            return {
                'servicios_en_carrito': servicios_en_carrito,
                'total_precio': total_precio,
                'carrito_cantidad': cantidad_total,  # Agregar cantidad total al contexto
            }
        except Carrito.DoesNotExist:
            return {
                'servicios_en_carrito': [],
                'total_precio': 0,
                'carrito_cantidad': 0,  # Si no hay carrito, la cantidad es 0
            }
    return {
        'servicios_en_carrito': [],
        'total_precio': 0,
        'carrito_cantidad': 0,  # Si el usuario no está autenticado, la cantidad es 0
    }

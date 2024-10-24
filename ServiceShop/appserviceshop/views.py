from django.shortcuts import render, redirect
from appserviceshop.models import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm,UserEditForm,AvatarFormulario
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView,CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Servicio, Avatar
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .models import *
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import update_session_auth_hash


@login_required
def Inicio(request):
    servicios = Servicio.objects.all()  # Ejemplo, ajusta según tu modelo
    return render(request, 'index.html')

@login_required
def Logout(request):
    logout(request)
    return render(request, 'cerrarsesion.html')


def Iniciosesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenido {usuario}!")  # Mensaje de éxito
                return redirect('inicio')  # Redirige al inicio o a la página deseada
            else:
                messages.error(request, "Datos incorrectos")  # Mensaje de error
                return render(request, "iniciosesion.html", {"mensaje": "Datos incorrectos", "hide_navbar": True})
        else:
            messages.error(request, "Formulario erróneo")  # Mensaje de error
            return render(request, "iniciosesion.html", {"mensaje": "Formulario erróneo", "hide_navbar": True})
    
    form = AuthenticationForm()
    return render(request, "iniciosesion.html", {'form': form, 'hide_navbar': True})

def Registrarusuario(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            messages.success(request, "Usuario creado exitosamente :)")  # Mensaje de éxito
            return render(request, "iniciosesion.html")
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
                    messages.error(request, "El nombre de usuario ya está en uso.")  # Mensaje de error
                else:
                    usuario.username = nuevo_username
            
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            usuario.email = informacion['email']

            # Manejo de contraseña
            if informacion.get('password1') and informacion['password1'] == informacion['password2']:
                usuario.set_password(informacion['password1'])  # Cambia la contraseña
                update_session_auth_hash(request, usuario)  # Mantiene la sesión activa
                messages.success(request, "Perfil actualizado y contraseña cambiada.")  # Mensaje de éxito
            else:
                messages.success(request, "Perfil actualizado correctamente.")  # Mensaje de éxito sin contraseña

            usuario.save() 
            return redirect('inicio')
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
        miFormulario = AvatarFormulario(request.POST, request.FILES, instance=avatar)
        if miFormulario.is_valid():
            nuevo_avatar = miFormulario.save(commit=False)  # No guardes todavía
            nuevo_avatar.user = usuario  # Asigna el usuario actual
            nuevo_avatar.save()  # Ahora guarda
            messages.success(request, "¡Avatar cambiado exitosamente!")  # Mensaje de éxito
            return redirect('inicio')
            
    else:
        miFormulario = AvatarFormulario(instance=avatar)

    return render(request, "cambiaravatar.html", {"miFormulario": miFormulario, "avatar": avatar})

def mis_compras(request):
    compras = Compras_M.objects.filter(comprador=request.user)

    # Filtrar por fecha
    fecha = request.GET.get('date')
    if fecha:
        compras = compras.filter(fecha_compra__date=fecha)

    # Filtrar por estado
    estado = request.GET.get('status')
    if estado:
        # Asegúrate de que el estado se compara correctamente
        compras = compras.filter(venta__estado__iexact=estado)

    # Filtrar por nombre de servicio
    servicio = request.GET.get('service')
    if servicio:
        compras = compras.filter(servicio__nombre__icontains=servicio)

    # Paginación
    page_number = request.GET.get('page')  # Obtener el número de página actual
    paginator = Paginator(compras, 10)  # Mostrar 10 compras por página
    page_obj = paginator.get_page(page_number)  # Obtener el objeto de la página actual

    return render(request, 'miscompras.html', {'page_obj': page_obj})



@login_required
def mis_ventas(request):
    # Obtener las ventas del usuario manualmente
    ventas = Ventas_M.objects.filter(vendedor=request.user)

    # Filtrar por fecha si se proporciona
    fecha = request.GET.get('date')
    if fecha:
        ventas = ventas.filter(fecha_venta__date=fecha)

    # Filtrar por estado si se proporciona
    estado = request.GET.get('status')
    if estado:
        ventas = ventas.filter(estado__iexact=estado)

    # Paginación
    page_number = request.GET.get('page')
    paginator = Paginator(ventas, 10)
    page_obj = paginator.get_page(page_number)

    return render(request, 'misventas.html', {'page_obj': page_obj})


@login_required
def actualizar_estado_venta(request, venta_id):
      # Obtener la venta correspondiente y verificar que el usuario sea el vendedor
    venta = get_object_or_404(Ventas_M, id=venta_id, vendedor=request.user)
    
    if request.method == 'POST':
        nuevo_estado = request.POST.get('estado')  # Obtener el nuevo estado desde el formulario
        if nuevo_estado in ['En curso', 'Cancelado', 'Completado']:
            venta.estado = nuevo_estado
            venta.save()
            messages.success(request, 'El estado de la venta ha sido actualizado exitosamente.')
        else:
            messages.error(request, 'Estado no válido.')

        # Redirigir a la vista de mis ventas después de la actualización
        return render(request, 'misventas.html')
    
    # Si no es POST, redirigir o mostrar el formulario correspondiente
    messages.error(request, 'Método no permitido.')
    return render(request, 'misventas.html')

@login_required
def Mispublicaciones(request):
    publicaciones_list = Servicio.objects.filter(vendedor=request.user)  # Consulta las ventas del usuario actual
    paginator = Paginator(publicaciones_list, 5)  # Paginación de 5 ventas por página
    page_number = request.GET.get('page')  # Obtener número de página
    page_obj = paginator.get_page(page_number)  # Obtener la página actual

    # Renderiza la plantilla con el contexto de la paginación
    return render(request, 'mispublicaciones.html', {'page_obj': page_obj})

@login_required
def anadir_al_carrito(request, servicio_id):
    servicio = get_object_or_404(Servicio, id=servicio_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)

    # Comprueba si el servicio ya está en el carrito
    servicio_en_carrito, created = ServicioEnCarrito.objects.get_or_create(carrito=carrito, servicio=servicio)

    # Si el servicio ya existe, puedes incrementar la cantidad
    if not created:
        servicio_en_carrito.cantidad += 1
        servicio_en_carrito.save()
        messages.success(request, f"Se ha incrementado la cantidad de '{servicio.name}' en el carrito.")
    else:
        messages.success(request, f"Se ha añadido '{servicio.name}' al carrito.")

    # Redirige a la vista del carrito después de añadir el servicio
    return redirect('ver_carrito')  


@login_required
def ver_carrito(request):
    try:
        carrito = Carrito.objects.get(usuario=request.user)
        # Obtiene todos los servicios en el carrito
        servicios_en_carrito = ServicioEnCarrito.objects.filter(carrito=carrito)  
    except Carrito.DoesNotExist:
        servicios_en_carrito = []  # Si no existe un carrito, se asigna una lista vacía

    # Calcular el precio total
    total_precio = 0
    for servicio_en_carrito in servicios_en_carrito:
        total_precio += servicio_en_carrito.cantidad * servicio_en_carrito.servicio.precio

    return render(request, 'ver_carrito.html', {
        'servicios_en_carrito': servicios_en_carrito,
        'total_precio': total_precio,
    })


@login_required
def actualizar_cantidad(request, servicio_id):
    carrito = get_object_or_404(Carrito, usuario=request.user)
    servicio_en_carrito = get_object_or_404(ServicioEnCarrito, carrito=carrito, servicio__id=servicio_id)

    if request.method == 'POST':
        nueva_cantidad = int(request.POST.get('cantidad', 1))
        servicio_en_carrito.cantidad = nueva_cantidad
        servicio_en_carrito.save()
        
        messages.success(request, 'La cantidad del servicio ha sido actualizada.')
        return redirect('ver_carrito')  # Redirigir a la vista del carrito

    return render(request, 'actualizar_cantidad.html', {'servicio_en_carrito': servicio_en_carrito})


# Vista para eliminar un servicio del carrito
@login_required
def eliminar_del_carrito(request, servicio_id):
    if request.method == 'POST':
        carrito = Carrito.objects.get(usuario=request.user)
        servicio = get_object_or_404(Servicio, id=servicio_id)
        ServicioEnCarrito.objects.filter(carrito=carrito, servicio=servicio).delete()
        return redirect('ver_carrito')

@login_required
def confirmar_carrito(request):
    try:
        carrito = Carrito.objects.get(usuario=request.user)
        total_precio = 0

        # Recorrer los servicios en el carrito
        for servicio_en_carrito in ServicioEnCarrito.objects.filter(carrito=carrito):
            vendedor_servicio=servicio_en_carrito.servicio.vendedor
            # Crear la venta
            venta = Ventas_M.objects.create(
                vendedor=vendedor_servicio,
                servicio=servicio_en_carrito.servicio,
                cantidad=servicio_en_carrito.cantidad,
                total=servicio_en_carrito.cantidad * servicio_en_carrito.servicio.precio,
                estado='En curso',
                carrito=carrito
            )

            # Crear la compra
            compra = Compras_M.objects.create(
                servicio=servicio_en_carrito.servicio,
                comprador=request.user,
                venta=venta,
                cantidad=servicio_en_carrito.cantidad,
                total=servicio_en_carrito.cantidad * servicio_en_carrito.servicio.precio,
                carrito=carrito
            )

            total_precio += compra.total  # Sumar el total de la compra

        # Vaciar el carrito después de confirmar la compra
        carrito.servicios.clear()

        # Agregar un mensaje de éxito
        messages.success(request, f"La compra ha sido confirmada ")
        
        return redirect('inicio')  # Redirigir a la página principal

    except Carrito.DoesNotExist:
        # Manejar el caso de que el carrito no exista
        messages.error(request, "No tienes un carrito activo.")
        return redirect('index')  # Redirigir a la página principal en caso de error

class Detalleservicio(LoginRequiredMixin,DetailView):
   model=Servicio
   template_name="servicio_detalle.html"

class Detallecompra(LoginRequiredMixin, DetailView):
    model = Compras_M
    template_name = "compra_detalle.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Añade cualquier otra información al contexto si es necesario
        return context
    
class Crearservicio(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Servicio
    fields = ['name', 'categoria', 'precio', 'zona', 'descripcion', 'disponibilidadhoraria', 'imagen']
    success_url = reverse_lazy('inicio')
    success_message = "Servicio creado exitosamente."  # Mensaje de éxito
    template_name = "crearservicio.html"

    def form_valid(self, form):
        # Asignar el usuario actual como vendedor
        form.instance.vendedor = self.request.user  # Asignar el vendedor al servicio antes de guardarlo
        form.save()  # Solo guardar el servicio
        return super().form_valid(form)

class Modificarservicio(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Servicio
    fields = ['name', 'descripcion', 'categoria', 'precio', 'zona', 'disponibilidadhoraria', 'imagen']
    success_url = '/appserviceshop/mispublicaciones'  # Asegúrate de que esta URL sea correcta
    template_name = "servicio_form.html"
    success_message = "Servicio modificado correctamente."

class Eliminarservicio(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Servicio
    template_name = "servicio_confirm_delete.html"
    success_url = '/appserviceshop/mispublicaciones'
    success_message = "Servicio eliminado correctamente."  # Mensaje de éxito

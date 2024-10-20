from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imgavatar', default='imgavatar/predeterminado.jpg')

    def __str__(self):
        return f"{settings.MEDIA_URL}{self.imagen}"

class Servicio(models.Model):
    CATEGORIA_CHOICES = [
        ('Tecnologia', 'Tecnología'),
        ('Educacion', 'Educación'),
        ('Salud', 'Salud'),
        ('Alimentacion', 'Alimentación'),
    ]
    
    ZONA_CHOICES = [
        ('Norte', 'Norte'),
        ('Sur', 'Sur'),
        ('Este', 'Este'),
        ('Oeste', 'Oeste'),
    ]

    name = models.CharField(max_length=100)  # Nombre del servicio
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)  # Categoría
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del servicio
    zona = models.CharField(max_length=20, choices=ZONA_CHOICES)  # Zona
    descripcion = models.TextField()  # Descripción del servicio
    disponibilidadhoraria = models.CharField(max_length=100)  # Disponibilidad horaria
    imagen = models.ImageField(upload_to='imgservices/')
    creacion = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    actualizacion = models.DateTimeField(auto_now=True)  # Fecha de última actualización
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="servicios")

    def __str__(self):
        return self.name


class Compras_M(models.Model):
    servicio = models.OneToOneField(Servicio, on_delete=models.CASCADE)
    comprador = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    venta = models.OneToOneField('Ventas_M', on_delete=models.CASCADE, null=True, blank=True)  # Relación con la venta
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 

from django.db import models
from django.contrib.auth.models import User

class Ventas_M(models.Model):
    CATEGORIA_CHOICES = [
        ('En curso', 'En curso'),
        ('Cancelado', 'Cancelado'),
        ('Completado', 'Completado'),
    ]
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=20,
        choices=CATEGORIA_CHOICES,
        default='En curso'  # Valor predeterminado para el estado
    )
    fecha_venta = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"Venta de {self.servicio.nombre} por {self.vendedor.username} - Estado: {self.estado}"


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=1000, decimal_places=2)
    # Otros campos según sea necesario


class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    servicios = models.ManyToManyField(Servicio, through='ServicioEnCarrito')

class ServicioEnCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)



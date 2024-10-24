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
        ('Servicios de Reparación y Mantenimiento', 'Servicios de Reparación y Mantenimiento'),
        ('Consultoría y Servicios Profesionales', 'Consultoría y Servicios Profesionales'),
        ('Belleza y Cuidado Personal', 'Belleza y Cuidado Personal'),
        (' Arte y Publicidad', ' Arte y Publicidad'),
    ]
    
    ZONA_CHOICES = [
        ('Norte', 'Norte'),
        ('Sur', 'Sur'),
        ('Este', 'Este'),
        ('Oeste', 'Oeste'),
    ]

    name = models.CharField(max_length=100)  # Nombre del servicio
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES)  # Categoría
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

class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    servicios = models.ManyToManyField(Servicio, through='ServicioEnCarrito')

class ServicioEnCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)  # Campo para la cantidad

    def __str__(self):
        return f"{self.servicio.nombre} - Cantidad: {self.cantidad}"

    def total(self):
        return self.cantidad * self.servicio.precio  # Método para calcular el total de este servicio en el carrito


class Ventas_M(models.Model):
    CATEGORIA_CHOICES = [
        ('En curso', 'En curso'),
        ('Cancelado', 'Cancelado'),
        ('Completado', 'Completado'),
    ]
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=20,
        choices=CATEGORIA_CHOICES,
        default='En curso'
    )
    cantidad = models.PositiveIntegerField(default=1)  # Campo para la cantidad de servicios comprados
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, null=True, blank=True)  # Relación con el carrito

    def __str__(self):
        return f"Venta de {self.servicio.nombre} por {self.vendedor.username} - Estado: {self.estado} - Cantidad: {self.cantidad}"

class Compras_M(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    comprador = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    venta = models.ForeignKey(Ventas_M, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cantidad = models.PositiveIntegerField(default=1)  # Campo para la cantidad de servicios comprados
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, null=True, blank=True)  # Relación con el carrito

    def __str__(self):
        return f"Compra de {self.servicio.nombre} por {self.comprador.username} - Fecha: {self.fecha_compra}, Cantidad: {self.cantidad}"

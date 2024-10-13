from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


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

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()


class Ventas_M(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_venta = models.DateTimeField(auto_now_add=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=50, choices=[('completada', 'Completada'), ('cancelada', 'Cancelada')])

    def __str__(self):
        return f"{self.servicio.nombre} vendido por {self.vendedor.username}"
    
 

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=1000, decimal_places=2)
    # Otros campos según sea necesario

class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='CarritoProducto')

class CarritoProducto(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

from django.contrib import admin
from .models import Servicio

# Register your models here.

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('name', 'categoria', 'precio', 'zona', 'creacion', 'actualizacion')
    search_fields = ('name', 'categoria', 'zona')
    list_filter = ('categoria', 'zona')
    fields = ('name', 'categoria', 'precio', 'zona', 'descripcion', 'disponibilidadhoraria', 'imagen')

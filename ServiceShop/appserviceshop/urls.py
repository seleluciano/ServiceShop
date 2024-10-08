from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
     path('',views.Inicio,name="inicio"),
     path('cerrarsesion/',views.Logout,name="cerrarsesion"),
     path('registrarusuario/', views.Registrarusuario,name="registrarusuario"),
     path('iniciosesion/',views.Iniciosesion,name="iniciosesion"),
     path('nuevo/', views.Crearservicio.as_view(), name="New"),
     path('carrito/',views.Carrito,name="carrito"),
     path('editarperfil/', views.Editarperfil, name="editarperfil"),
     path('cambiaravatar/',views.Cambiaravatar,name="cambiaravatar"),
     path('miscompras/',views.Compras,name="miscompras"),
    path('<int:pk>', views.Detalleservicio.as_view(), name="Detail"),
     
] 


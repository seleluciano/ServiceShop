from django.urls import path
from . import views

urlpatterns = [
     path('',views.Inicio,name="inicio"),
     path('cerrarsesion/',views.Logout,name="cerrarsesion"),
     path('registrarusuario/', views.Registrarusuario,name="registrarusuario"),
     path('iniciosesion/',views.Iniciosesion,name="iniciosesion"),
     path('nuevo/', views.Crearservicio.as_view(), name="New"),
     path('carrito/',views.Carrito,name="carrito"),
     path('editarperfil/', views.Editarperfil, name="editarperfil"),
     path('cambiaravatar/',views.Cambiaravatar,name="cambiaravatar"),
     path('miscompras/',views.Compra_V,name="miscompras"),
     path('misventas/',views.Venta_V,name="misventas"),
     path('carrito/',views.Carrito,name="carrito"),
     path('añadir_al_carrito/', views.añadir_al_carrito,name="añadir_al_carrito"),
     path('<int:pk>', views.Detalleservicio.as_view(), name="Detail"),
     path('editar/<int:pk>', views.Modificarservicio.as_view(), name="Edit"),
     path('borrar/<int:pk>', views.Eliminarservicio.as_view(), name="Delete"),
     
] 


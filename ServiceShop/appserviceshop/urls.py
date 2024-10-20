from django.urls import path
from . import views

urlpatterns = [
     path('',views.Inicio,name="inicio"),
     path('cerrarsesion/',views.Logout,name="cerrarsesion"),
     path('registrarusuario/', views.Registrarusuario,name="registrarusuario"),
     path('iniciosesion/',views.Iniciosesion,name="iniciosesion"),
     path('nuevo/', views.Crearservicio.as_view(), name="New"),
     path('editarperfil/', views.Editarperfil, name="editarperfil"),
     path('cambiaravatar/',views.Cambiaravatar,name="cambiaravatar"),
     path('miscompras/',views.mis_compras,name="miscompras"),
     path('misventas/',views.mis_ventas,name="misventas"),
     path('mispublicaciones/',views.Mispublicaciones,name="mispublicaciones"),
     path('<int:pk>', views.Detalleservicio.as_view(), name="Detail"),
     path('editar/<int:pk>', views.Modificarservicio.as_view(), name="Edit"),
     path('borrar/<int:pk>', views.Eliminarservicio.as_view(), name="Delete"),
    path('ventas/actualizar_estado/<int:venta_id>/', views.actualizar_estado_venta, name='actualizar_estado_venta'),
     path('carrito/anadir/<int:servicio_id>/', views.anadir_al_carrito, name='anadir_al_carrito'),
     path('carrito/', views.ver_carrito, name='ver_carrito'),
     path('carrito/actualizar/<int:servicio_id>/', views.actualizar_cantidad, name='actualizar_cantidad'),
     path('carrito/eliminar/<int:servicio_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
     path('carrito/confirmar/', views.confirmar_carrito, name='confirmar_carrito'),


] 


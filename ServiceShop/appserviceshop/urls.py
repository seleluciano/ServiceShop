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
     path('compras/<int:pk>/', views.Detallecompra.as_view(), name='Detailcompra'),
     path('servicios/', views.filtrar_servicios, name='filtrar_servicios'),
     path('buscar/', views.buscar_servicios, name='buscar_servicios'),
     path('compra/<int:compra_id>/agregar_resena/', views.crear_resena, name='agregar_resena'),
     path('compra/modificar_resena/<int:pk>/', views.ModificarReseña.as_view(), name='modificar_resena'),
     path('compra/eliminar_resena/<int:pk>/', views.EliminarReseña.as_view(), name='eliminar_resena'),
     path('user/<int:user_id>/rate/', views.rate_user, name='rate_user'),
     path('user/<int:user_id>/', views.user_detail, name='user_detail'),

]
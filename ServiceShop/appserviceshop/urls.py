from django.urls import path, include
from appserviceshop import views
from .views import RegistrarUsuarioViewSet
#from django.contrib import admin
#from rest_framework.routers import DefaultRouter


urlpatterns = [
     path('',views.Inicio,name="inicio"),
     path('cerrarsesion/',views.Logout,name="cerrarsesion"),
     path('appserviceshop/', include('appserviceshop.urls')),
     path('registrarusuario/', views.Logout,name="registrarusuario")
]

#router = routers.DefaultRouter()
#router.register(r'Usuario', RegistrarUsuarioViewSet)  # Cambia 'usuarios' por el nombre que desees para la URL

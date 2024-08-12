from django.urls import path
from appserviceshop import views

urlpatterns = [
     path('',views.Inicio,name="inicio"),
]

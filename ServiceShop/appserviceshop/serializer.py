from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__' #('id', 'username', 'email', 'localidad', 'provincia', 'codigo_postal')
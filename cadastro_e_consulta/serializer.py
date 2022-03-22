from rest_framework import serializers
from cadastro_e_consulta.models import Usuarrio

class UsuariosSDerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarrio
        fields = ['login', 'data_nascimento', 'senha']
        extra_kwargs = {'senha': {'required': False}}
        validators = []
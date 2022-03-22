from django.shortcuts import render
from cadastro_e_consulta.serializer import UsuariosSDerializer
from rest_framework import viewsets
from cadastro_e_consulta.models import Usuarrio

class UsuariosViewset(viewsets.ModelViewSet):
    queryset = Usuarrio.objects.all()
    serializer_class = UsuariosSDerializer
    
from django.contrib import admin
from cadastro_e_consulta.models import Usuarrio

class Usuarios(admin.ModelAdmin):
    list_display = ('id', 'login','data_nascimento')
    search_fields = ('login', 'data_nascimento')

admin.site.register(Usuarrio, Usuarios)
from datetime import datetime
# from typing_extensions import Self
from xmlrpc.client import _datetime_type
from django.db import models
from django.core.validators import MinLengthValidator
from django.forms import ModelForm
from django.utils.crypto import get_random_string
from random import choice
import string

class Usuarrio(models.Model):
    login = models.CharField(max_length=10, unique=True)
    senha = models.CharField(validators=[MinLengthValidator(4)], max_length=10, blank=True,)
    data_nascimento = models.DateField()


    def save(self, *args, **kwargs):
            if  len(self.senha) < 1:
                teste = True
                while teste:
                    tamanho = 8
                    valores = string.ascii_letters + string.digits + string.punctuation
                    nova_senha = ''
                    for i in range(tamanho):
                        nova_senha += choice(valores)
                    outras_senhas = type(self).objects.filter(senha=nova_senha)
                    if len(outras_senhas) < 1:
                        teste = False
                self.senha = nova_senha
            super(Usuarrio, self).save(*args, **kwargs)

        
            

        
    
                


# 


    # def salva_senha(obj):
    # # """ A function to generate a 5 character slug and see if it has been used and contains naughty words."""
    #     if not obj.senha: # if there isn't a slug
    #         obj.senha = get_random_string(5) # create one
    #         senha_repetida = True  
    #     while senha_repetida: # keep checking until we have a valid slug
    #         senha_repetida = False
    #         outras_senhas = type(obj).objects.filter(senha=obj.senha)
    #     if len(outras_senhas) > 0:
    #         # if any other objects have current slug
    #         senha_repetida = True
    #     if senha_repetida:
    #         # create another slug and check it again
    #         obj.senha = get_random_string(5)

    # def save(self, *args, **kwargs):
    # # """ Add Slug creating/checking to save method. """
    #     salva_senha(self) # call slug_save, listed below
    #     Super(SomeModelWithSlug, self).save(*args, **kwargs)
  
    def __str__(self):
        return self.login
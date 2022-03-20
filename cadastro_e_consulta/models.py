from django.db import models

class Usuarrio(models.Model):
    login = models.CharField(max_length=10)
    senha = models.CharField(max_length=10)
    data_nascimento = models.CharField(max_length=10)

    def __str__(self):
        return self.login , self.data_nascimento
from django.db import models


class Funcao(models.Model):
    funcao = models.CharField(max_length=40)


    def __str__(self):
        return self.funcao
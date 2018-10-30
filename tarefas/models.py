from django.db import models
import datetime
from django.utils.translation import ugettext_lazy as _


class Tarefa(models.Model):


    titulo = models.CharField(max_length=40)
    descricao = models.TextField(max_length=400)
    tipo = models.CharField(max_length=40)
    prioridade = models.CharField(max_length=40)
    situacao = models.CharField(max_length=40)
    data_inicio = models.DateField(blank=True, null=True)
    data_fim =models.DateField(blank=True, null=True)
    horas_estimadas = models.CharField(max_length=40)
    horas_gastas = models.CharField(max_length=40)


    def __str__(self):

        return self.titulo
from django.db import models
import datetime
from django.utils.translation import ugettext_lazy as _
from tarefas.escolhas import *
from tarefas import forms

class Tarefa(models.Model):


    nome = models.CharField(max_length=40)
    descricao = models.CharField(max_length=400)
    tipo = models.IntegerField(choices=TIPO_ESCOLHA, default=1)
    prioridade = models.IntegerField(choices=PRIORIDADE_ESCOLHA, default=1)
    situacao = models.IntegerField(choices=SITUACAO_ESCOLHA, default=1)
    data_inicio = models.DateField(blank=True, null=True)
    data_fim =models.DateField(blank=True, null=True)
    horas_estimadas = models.CharField(max_length=40)
    horas_gastas = models.CharField(max_length=40,blank=True,null=True)


    def __str__(self):

        return self.nome
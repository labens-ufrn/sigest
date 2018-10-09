from django.db import models
from situacoes.models import Situacao
from prioridades.models import Prioridade
from tipos.models import Tipo
from django.utils.translation import ugettext_lazy as _


class Tarefa(models.Model):
    titulo = models.CharField(max_length=40),
    descricao = models.TextField(max_length=400),
    tipo = models.ForeignKey(Tipo,null=True, blank=True, on_delete=models.PROTECT),
    prioridade = models.ForeignKey(Prioridade, null=True, blank=True, on_delete=models.PROTECT),
    situacao = models.ForeignKey(Situacao, null=True, blank=True, on_delete=models.PROTECT),
    data_inicio = models.CharField(max_length=40),
    data_fim =models.CharField(max_length=40),
    horas_estimadas = models.CharField(max_length=40),
    horas_gastas = models.CharField(max_length=40),


    def __str__(self):
        return self.titulo
from django.db import models


class Prioridade(models.Model):
    prioridade = models.CharField(max_length=40)

    def __str__(self):
        return self.prioridade

from django.db import models

class Tipo(models.Model):
    tarefa = models.CharField(max_length=40)

    def __str__(self):
        return self.tarefa
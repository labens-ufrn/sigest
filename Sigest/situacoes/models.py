from django.db import models

class Situacao(models.Model):
    situacao = models.CharField(max_length=40)

    def __str__(self):
        return self.situacao
from django.db import models
from funcoes.models import Funcao
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Usuario(User):
    username = models.CharField(_('usuario'), max_length=15, unique=True, help_text =_('Requer 15 caracteres ou menos')),
    password = models.CharField(_('senha'), max_length=15, help_text=('Digite uma senha com 15 caracteres ou menos')),
    funcao = models.ForeignKey(Funcao, null=True, blank=True, on_delete=models.PROTECT)
    matricula = models.IntegerField()

    def __str__(self):
        return self.username
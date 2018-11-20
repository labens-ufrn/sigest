from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser,Group
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class Orientador(AbstractBaseUser):
    username = models.CharField(_('usuario'), max_length=15, unique=True, help_text=_('Requer 15 caracteres ou menos'))
    password = models.CharField(_('senha'), max_length=15, help_text=('Digite uma senha com 15 caracteres ou menos'))
    email = models.EmailField(_('email'), max_length=255, unique=True)
    matricula = models.IntegerField()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username', 'email', 'matricula']



    def __str__(self):
        return self.username


    class Meta:
        permissions = (
            ('cadastrar tarefa', 'O usuario pode cadastrar tarefas'),
        )

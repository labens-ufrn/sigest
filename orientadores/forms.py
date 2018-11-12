from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Orientador
from django.contrib.auth.models import User



class CustomUserCreationForm(UserCreationForm):
    matricula = forms.IntegerField()
    class Meta(UserCreationForm):
        model = User
        fields = ('username',  'email','matricula' )
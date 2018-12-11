from django.contrib.auth import login
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from ..decorators import student_required,advisor_required,supervisor_required,coordinator_required
from usuarios.forms import StudentUpdateForm
from .models import Estagio
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


class EstagioList(ListView):
    model = Estagio
    template_name = 'estagio_list.html'

class EstagioDetail(DetailView):
    model = Estagio
    template_name = 'estagio_detail.html'


class EstagioCreate(CreateView):
    model = Estagio
    fields = ['nome_estagio', 'aluno', 'orientador', 'supervisor,', 'alterna_teoria_pratica', 'carga_horaria_semanal', 'data_inicio', 'data_fim']
    template_name = 'estagio_signup.html'
    success_url = reverse_lazy('/estagios/listar_estagio')

class EstagioUpate(UpdateView):
    model = Estagio
    fields = ['nome_estagio', 'aluno', 'orientador', 'supervisor,', 'alterna_teoria_pratica', 'carga_horaria_semanal','data_inicio', 'data_fim']
    template_name = 'estagio_update.html'
    success_url = reverse_lazy('/estagios/listar_estagio')
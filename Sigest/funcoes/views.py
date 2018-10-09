from .models import Funcao
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy


class FuncaoList(ListView):
    model = Funcao



class FuncaoDetail(DetailView):
    model = Funcao


class FuncaoCreate(CreateView):
    model = Funcao
    fields = ['funcao']
    success_url = '/funcoes/listar_funcao'


class FuncaoUpdate(UpdateView):
    model = Funcao
    fields = ['funcao']
    success_url = reverse_lazy('listar_funcao')


class FuncaoDelete(DeleteView):
    model = Funcao
    success_url = reverse_lazy('listar_funcao')

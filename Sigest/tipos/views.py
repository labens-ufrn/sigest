from .models import Tipo
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy


class TipoList(ListView):
    model = Tipo



class TipoDetail(DetailView):
    model = Tipo


class TipoCreate(CreateView):
    model = Tipo
    fields = ['tarefa']
    success_url = '/tipos/listar_tipo'


class TipoUpdate(UpdateView):
    model = Tipo
    fields = ['tarefa']
    success_url = reverse_lazy('listar_tipo')


class TipoDelete(DeleteView):
    model = Tipo
    success_url = reverse_lazy('listar_tipo')

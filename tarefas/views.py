from .models import Tarefa
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy



class TarefaList(ListView):
    model = Tarefa


class TarefaDetail(DetailView):
    model = Tarefa


class TarefaCreate(CreateView):
    model = Tarefa
    fields = ['titulo', 'descricao', 'tipo', 'prioridade', 'situacao', 'data_inicio', 'data_fim', 'horas_estimadas', 'horas_gastas']
    success_url = '/tarefas/listar_tarefa'

class TarefaUpdate(UpdateView):
    model = Tarefa
    fields = ['titulo', 'descricao', 'tipo', 'prioridade', 'situacao', 'data_inicio', 'data_fim', 'horas_estimadas', 'horas_gastas']
    success_url = reverse_lazy('listar_tarefa')


class TarefaDelete(DeleteView):
    model = Tarefa
    success_url = reverse_lazy('listar_tarefa')
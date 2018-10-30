from django.forms import ModelForm

from .models import Tarefa

class TarefaForm(ModelForm):
    model = Tarefa
    fields = ['titulo', 'descricao', 'tipo', 'prioridade', 'situacao', 'data_inicio', 'data_fim', 'horas_est', 'horas_gas']
from .models import Prioridade
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy


class PrioridadeList(ListView):
    model = Prioridade



class PrioridadeDetail(DetailView):
    model = Prioridade


class PrioridadeCreate(CreateView):
    model = Prioridade
    fields = ['prioridade']
    success_url = '/prioridades/listar_prioridade'


class PrioridadeUpdate(UpdateView):
    model = Prioridade
    fields = ['prioridade']
    success_url = reverse_lazy('listar_prioridade')


class PrioridadeDelete(DeleteView):
    model = Prioridade
    success_url = reverse_lazy('listar_prioridade')

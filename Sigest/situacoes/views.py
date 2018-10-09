from .models import Situacao
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy


class SituacaoList(ListView):
    model = Situacao



class SituacaoDetail(DetailView):
    model = Situacao


class SituacaoCreate(CreateView):
    model = Situacao
    fields = ['situacao']
    success_url = '/situacoes/listar_situacao/'


class SituacaoUpdate(UpdateView):
    model = Situacao
    fields = ['situacao']
    success_url = reverse_lazy('listar_situacao')


class SituacaoDelete(DeleteView):
    model = Situacao
    success_url = reverse_lazy('listar_situacao')

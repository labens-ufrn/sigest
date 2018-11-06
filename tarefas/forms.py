from django import forms


from tarefas.escolhas import *

class TarefaViewerForm(forms.Form):
    tipo = forms.ChoiceField(choices= TIPO_ESCOLHA, label="", initial='', widget=forms.Select(), required=True)
    prioridade = forms.ChoiceField(choices=PRIORIDADE_ESCOLHA, label="", initial='', widget=forms.Select(), required=True)
    situacao = forms.ChoiceField(choices=SITUACAO_ESCOLHA, label="", initial='', widget=forms.Select(), required=True)




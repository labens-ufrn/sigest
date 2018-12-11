from django.db import models
from usuarios.models import Usuario

class Tarefa(models.Model):
    BUG = 'BG'
    DET_CDU = 'DCDU'
    DOCUMENTACAO = 'DOC'
    SUPORTE = 'SP'
    TESTE = 'TS'
    DESING = 'DS'
    REUNIAO = 'RE'
    PLANEJAMENTO = 'PL'
    ESTUDO = 'EST'
    ANALISE = 'AL'
    DEFEITO = 'DF'

    TIPO_ESCOLHA = (
        (BUG, ("Bug")),
        (DET_CDU, ("Det CDU")),
        (DOCUMENTACAO, ("Documentação")),
        (SUPORTE, ("Suporte")),
        (TESTE, ("Teste")),
        (DESING, ("Desing")),
        (REUNIAO, ("Reunião")),
        (PLANEJAMENTO, ("Planejamento")),
        (ESTUDO, ("Estudo")),
        (ANALISE, ("Ánálise")),
        (DEFEITO, ("Defeito")),

    )
    EM_ANDAMENTO_10 = 'EM10'
    EM_ANDAMENTO_20 = 'EM20'
    EM_ANDAMENTO_30 = 'EM30'
    EM_ANDAMENTO_40 = 'EM40'
    EM_ANDAMENTO_50 = 'EM50'
    EM_ANDAMENTO_60 = 'EM60'
    EM_ANDAMENTO_70 = 'EM70'
    EM_ANDAMENTO_80 = 'EM80'
    EM_ANDAMENTO_90 = 'EM90'
    FEEDBACK = 'FB'
    RESOLVIDA = 'RESV'
    FECHADA = 'FECH'

    STATUS_ESCOLHA = (
        (EM_ANDAMENTO_10, ("Em Andamento 10%")),
        (EM_ANDAMENTO_20, ("Em Andamento 20%")),
        (EM_ANDAMENTO_30, ("Em Andamento 30%")),
        (EM_ANDAMENTO_40, ("Em Andamento 40%")),
        (EM_ANDAMENTO_50, ("Em Andamento 50%")),
        (EM_ANDAMENTO_60, ("Em Andamento 60%")),
        (EM_ANDAMENTO_70, ("Em Andamento 70%")),
        (EM_ANDAMENTO_80, ("Em Andamento 80%")),
        (EM_ANDAMENTO_90, ("Em Andamento 90%")),
        (FEEDBACK, ("Feedback")),
        (RESOLVIDA, ("Resolvida")),
        (FECHADA, ("Fechada"))

    )

    BAIXA = 'BA'
    NORMAL = 'NORMAL'
    ALTA = 'ALT'
    URGENTE = 'URG'
    IMEDIATA = 'IMD'

    PRIORIDADE_ESCOLHA = (
        (BAIXA, ("Baixa")),
        (NORMAL, ("Normal")),
        (ALTA, ("Alta")),
        (URGENTE, ("Urgente")),
        (IMEDIATA, ("Imediata")),
    )

    nome = models.CharField(max_length=40)
    descricao = models.CharField(max_length=400)
    tipo = models.CharField(choices=TIPO_ESCOLHA, default=BUG, max_length=50)
    status = models.CharField(choices=STATUS_ESCOLHA, default=EM_ANDAMENTO_10, max_length=50)
    prioridade = models.CharField(choices=PRIORIDADE_ESCOLHA, default=NORMAL, max_length=50)
    data_inicio = models.DateField(blank=False, null=True)
    data_fim = models.DateField(blank=False, null=True)
    horas_estimadas = models.PositiveIntegerField(blank=False, null=True)
    horas_gastas = models.PositiveIntegerField(blank=True, null=True)




from django.utils.translation import ugettext_lazy as _

TIPO_ESCOLHA = (
    (1, _("Bug")),
    (2, _("Det CDU")),
    (3, _("Documentação")),
    (4, _("Suporte")),
    (5, _("Teste")),
    (6, _("Desing")),
    (7, _("Reunião")),
    (8, _("Planejamento")),
    (9, _("Estudo")),
    (10, _("Ánálise")),
    (11, _("Defeito")),


)

SITUACAO_ESCOLHA = (
    (1, _("Em Andamento 10%")),
    (2, _("Em Andamento 20%")),
    (3, _("Em Andamento 30%")),
    (4, _("Em Andamento 40%")),
    (5, _("Em Andamento 50%")),
    (6, _("Em Andamento 60%")),
    (7, _("Em Andamento 70%")),
    (8, _("Em Andamento 80%")),
    (9, _("Em Andamento 90%")),
    (10, _("Feedback")),
    (11, _("Resolvida")),


)


PRIORIDADE_ESCOLHA = (
    (1, _("Baixa")),
    (2, _("Normal")),
    (3, _("Alta")),
    (4, _("Urgente")),
    (5, _("Imediata")),


)
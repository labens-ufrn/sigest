from django.db import models


from usuarios.models import Usuario,Student,Advisor,Supervisor
class Estagio(models.Model):
    nome_estagio = models.CharField(null=True,blank=False,max_length=250)
    aluno = models.ForeignKey(Student, null=True, blank=False, on_delete=models.PROTECT)
    orientador = models.ForeignKey(Advisor, null=True, blank=False, on_delete=models.PROTECT)
    supervisor = models.ForeignKey(Supervisor, null=True, blank=False, on_delete=models.PROTECT)
    alterna_teoria_pratica = models.BooleanField(default=True)
    carga_horaria_semanal = models.PositiveIntegerField()
    data_inicio = models.DateField(blank=False, null=True)
    data_fim = models.DateField(blank=False, null=True)

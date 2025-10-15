from django.db import models
from django.contrib.auth.models import User
from .disciplina import Disciplina

class SessaoEstudo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sessoes_estudo")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.SET_NULL, null=True, blank=True, related_name="sessoes")
    inicio = models.DateTimeField()
    fim = models.DateTimeField()

    @property
    def duracao_minutos(self):
        return int((self.fim - self.inicio).total_seconds() // 60)

    class Meta:
        ordering = ["-inicio"]

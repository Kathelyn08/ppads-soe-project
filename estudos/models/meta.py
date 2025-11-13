from datetime import datetime
from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User
from .atividade import Atividade

class Meta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="metas")
    disciplina = models.ForeignKey("Disciplina", on_delete=models.SET_NULL, null=True, blank=True, related_name="metas")
    descricao = models.TextField(null=True, blank=True)
    alvo = models.IntegerField()
    data_inicial = models.DateTimeField()
    data_final = models.DateTimeField(null=True, blank=True)

    def concluida(self):
        return self.data_final and (
            (self.data_final - self.data_inicial).total_seconds() / 60 / 60 >= self.alvo
        )

    def status(self):
        if self.concluida():
            return "concluída"
        elif self.data_final:
            return "não alcançada"

    def color(self):
        match self.status():
            case "concluída": return "success"
            case "não alcançada": return "secondary"

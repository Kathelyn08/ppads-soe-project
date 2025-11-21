from datetime import datetime, timedelta
from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User
from .atividade import Atividade

class Meta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="metas")
    disciplina = models.ForeignKey("Disciplina", on_delete=models.SET_NULL, null=True, blank=True, related_name="metas")
    nome = models.TextField(null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    alvo = models.IntegerField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def concluida(self):
        return sum([sessao.duracao() for sessao in self.sessoes.all()], timedelta(0)).total_seconds() / 60 / 60 >= self.alvo

    def status(self):
        if self.concluida():
            return "concluída"
        else:
            return "não alcançada"

    def color(self):
        match self.status():
            case "concluída": return "success"
            case "não alcançada": return "secondary"

    def __str__(self):
        return self.nome.__str__() + " (" + self.alvo.__str__() + "h) "
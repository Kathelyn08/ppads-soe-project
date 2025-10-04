from django.db import models
from django.contrib.auth.models import User

class Disciplina(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="disciplinas")
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

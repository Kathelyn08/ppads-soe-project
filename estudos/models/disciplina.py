from django.db import models
from django.contrib.auth.models import User

class Disciplina(models.Model):
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    nome = models.CharField()
    descricao = models.TextField()

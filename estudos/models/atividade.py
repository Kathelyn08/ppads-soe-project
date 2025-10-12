from django.db import models
from django.contrib.auth.models import User
from .disciplina import Disciplina

class Status(models.TextChoices):
    PENDENTE = "PENDENTE", "Pendente"
    EM_ANDAMENTO = "EM_ANDAMENTO", "Em Andamento"
    CONCLUIDA = "CONCLUIDA", "Concluída"

class Prioridade(models.TextChoices):
    BAIXA = "BAIXA", "Baixa"
    MEDIA = "MEDIA", "Média"
    ALTA = "ALTA", "Alta"

class Categoria(models.TextChoices):
    PROVA = "PROVA", "Prova"
    TAREFA = "TAREFA", "Tarefa"
    SEMINARIO = "SEMINARIO", "Seminário"

class Modalidade(models.TextChoices):
    PRESENCIAL = "PRESENCIAL", "Presencial"
    ONLINE = "ONLINE", "Online"

class Atividade(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="atividades")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.SET_NULL, null=True, blank=True, related_name="atividades")

    titulo = models.CharField(max_length=140)
    descricao = models.TextField(blank=True)

    # 1..10
    peso = models.IntegerField(choices=[(i, i) for i in range(1, 11)], default=5)

    data_prazo = models.DateTimeField()
    estimativa_min = models.IntegerField(null=True, blank=True)
    local = models.CharField(max_length=100, null=True, blank=True)

    status = models.CharField(max_length=15, choices=Status.choices, default=Status.PENDENTE)
    categoria = models.CharField(max_length=15, choices=Categoria.choices, default=Categoria.TAREFA)
    prioridade = models.CharField(max_length=10, choices=Prioridade.choices, default=Prioridade.MEDIA)
    modalidade = models.CharField(max_length=12, choices=Modalidade.choices, default=Modalidade.ONLINE)

    criado_em = models.DateTimeField(auto_now_add=True)
    concluido_em = models.DateTimeField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["usuario", "data_prazo"]),
            models.Index(fields=["disciplina"]),
        ]
        ordering = ["data_prazo", "-prioridade", "-peso"]

    def __str__(self):
        return self.titulo

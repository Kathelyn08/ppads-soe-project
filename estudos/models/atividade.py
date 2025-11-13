from datetime import datetime
from django.contrib.auth.models import User
from django.db import models

class Atividade(models.Model):
    class Prioridade(models.IntegerChoices):
        BAIXA = 1, "Baixa"
        MEDIA = 2, "Média"
        ALTA = 3, "Alta"

        def color(self):
            match self:
                case self.BAIXA: return "success"
                case self.MEDIA: return "warning"
                case self.ALTA: return "danger"

    class Categoria(models.TextChoices):
        PROVA = "PROVA", "Prova"
        TAREFA = "TAREFA", "Tarefa"
        SEMINARIO = "SEMINARIO", "Seminário"

    class Modalidade(models.TextChoices):
        PRESENCIAL = "PRESENCIAL", "Presencial"
        ONLINE = "ONLINE", "Online"

    class Status(models.TextChoices):
        PENDENTE = "PENDENTE", "Pendente"
        EM_ANDAMENTO = "EM_ANDAMENTO", "Em andamento"
        CONCLUIDA = "CONCLUIDA", "Concluída"

        def color(self):
            match self:
                case self.PENDENTE: return "secondary"
                case self.EM_ANDAMENTO: return "primary"
                case self.CONCLUIDA: return "success"

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="atividades")
    disciplina = models.ForeignKey("Disciplina", on_delete=models.SET_NULL, null=True, blank=True, related_name="atividades")
    peso = models.PositiveSmallIntegerField(null=True, blank=True, choices=[(i, i) for i in range(1, 11)], default=5)
    titulo = models.CharField(max_length=120)
    descricao = models.TextField(blank=True)
    data_prazo = models.DateTimeField()
    estimativa_min = models.PositiveIntegerField(null=True, blank=True)
    local = models.CharField(max_length=80, null=True, blank=True)
    concluido_em = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDENTE)
    categoria = models.CharField(max_length=15, choices=Categoria.choices, default=Categoria.TAREFA)
    prioridade = models.IntegerField(choices=Prioridade.choices, default=Prioridade.MEDIA)
    modalidade = models.CharField(max_length=12, choices=Modalidade.choices, default=Modalidade.ONLINE)
    criado_em = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["usuario", "data_prazo"]),
            models.Index(fields=["disciplina"]),
        ]
        ordering = [
            "data_prazo",
            "-prioridade",
            "-peso"
        ]

    def __str__(self):
        return self.titulo

    def prioridade_color(self):
        return self.Prioridade(self.prioridade).color()

    def status_color(self):
        return self.Status(self.status).color()

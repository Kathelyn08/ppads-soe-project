from django.db import models

class Atividade(models.Model):
    class Prioridade(models.TextChoices):
        BAIXA = "BAIXA"
        MEDIA = "MEDIA", _("Média")
        ALTA = "ALTA"

    class Categoria(models.TextChoices):
        PROVA = "PROVA"
        TAREFA = "TAREFA"
        SEMINARIO = "SEMINARIO", _("Seminário")

    class Modalidade(models.TextChoices):
        PRESENCIAL = "PRESENCIAL"
        ONLINE = "ONLINE"

    titulo = models.CharField()
    prioridade = models.CharField(choices = Prioridade)
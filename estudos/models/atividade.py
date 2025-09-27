from django.contrib.auth.models import User
from django.db import models 

class Atividade(models.Model):
    class Prioridade(models.TextChoices):
        BAIXA = "BAIXA"
        MEDIA = "MEDIA", "Média"
        ALTA = "ALTA"

    class Categoria(models.TextChoices):
        PROVA = "PROVA"
        TAREFA = "TAREFA"
        SEMINARIO = "SEMINARIO", "Seminário"

    class Modalidade(models.TextChoices):
        PRESENCIAL = "PRESENCIAL"
        ONLINE = "ONLINE"
    
    class Status(models.TextChoices):
        PENDENTE = "PENDENTE"
        EM_ANDAMENTO = "EM_ANDAMENTO"
        CONCLUIDO = "CONCLUIDO", "Concluído"

    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    disciplina = models.ForeignKey("Disciplina", on_delete = models.CASCADE)
    peso = models.IntegerField(choices = zip(range(1,11), range(1,11)))
    titulo = models.CharField(blank = False)
    descricao = models.TextField()
    dataPrazo = models.DateTimeField()
    estimativa_min = models.IntegerField()
    local = models.CharField(null = True)
    concluido_em = models.DateTimeField(null = True)
    status = models.CharField(choices = Status)
    categoria = models.CharField(choices = Categoria)
    prioridade = models.CharField(choices = Prioridade)
    modalidade = models.CharField(choices = Modalidade)
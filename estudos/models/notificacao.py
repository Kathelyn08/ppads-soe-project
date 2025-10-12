from django.db import models
from django.contrib.auth.models import User
from .atividade import Atividade

class Notificacao(models.Model):
    class Categoria(models.TextChoices):
        PRAZO = "PRAZO", "Prazo"
        ESTUDO = "ESTUDO", "Estudo"
        SISTEMA = "SISTEMA", "Sistema"

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notificacoes")
    atividade = models.ForeignKey(Atividade, on_delete=models.SET_NULL, null=True, blank=True, related_name="notificacoes")
    categoria = models.CharField(max_length=10, choices=Categoria.choices, default=Categoria.PRAZO)
    mensagem = models.CharField(max_length=240)
    lida = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-criado_em"]

    def __str__(self):
        return f"{self.get_categoria_display()}: {self.mensagem[:30]}"

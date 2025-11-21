from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone
from ..util import timedelta_text

class Sessao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sessoes")
    meta = models.ForeignKey("Meta", on_delete=models.CASCADE, related_name="sessoes")
    descricao = models.TextField(null=True, blank=True)
    data_inicial = models.DateTimeField(default=timezone.now)
    data_final = models.DateTimeField(null=True, blank=True)

    def duracao(self):
        if self.data_final:
            return (self.data_final - self.data_inicial)
        else:
            return timedelta(0)

    def duracao_texto(self):
        return timedelta_text(self.duracao())

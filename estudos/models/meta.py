from django.db import models
from django.contrib.auth.models import User

class MetaEstudo(models.Model):
    class Periodo(models.TextChoices):
        SEMANA = "SEMANA", "Semana"
        MES = "MES", "Mês"

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="metas_estudo")
    periodo = models.CharField(max_length=10, choices=Periodo.choices, default=Periodo.SEMANA)
    horas_alvo = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "Meta de Estudo"
        verbose_name_plural = "Metas de Estudo"

    def __str__(self):
        return f"{self.usuario} - {self.periodo}: {self.horas_alvo}h"

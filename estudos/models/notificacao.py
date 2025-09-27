from django.db import models

class Notificacao(models.Model):
    class Categoria(models.TextChoices):
        PRAZO = "PRAZO"
        ESTUDO = "ESTUDO"
from django.db import models

class Meta(models.Model):

    class Categoria(models.TextChoices):
        CAPITULO = "CAPITULO", "Capítulo"
        HORA = "HORA"



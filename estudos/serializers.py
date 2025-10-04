from rest_framework import serializers
from .models.disciplina import Disciplina
from .models.atividade import Atividade

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = "__all__"
        read_only_fields = ["usuario"]

class AtividadeSerializer(serializers.ModelSerializer):
    disciplina = DisciplinaSerializer(read_only=True)

    class Meta:
        model = Atividade
        fields = "__all__"
        read_only_fields = ["usuario", "criado_em", "concluido_em"]

from rest_framework import serializers
from estudos.models.disciplina import Disciplina
from estudos.models.atividade import Atividade

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = "__all__"
        read_only_fields = ["usuario"]

class AtividadeSerializer(serializers.ModelSerializer):
    disciplina = DisciplinaSerializer(read_only=True)
    disciplina_id = serializers.PrimaryKeyRelatedField(
        source="disciplina",
        queryset=Disciplina.objects.all(),
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = Atividade
        fields = "__all__"
        read_only_fields = ["usuario", "criado_em", "concluido_em"]

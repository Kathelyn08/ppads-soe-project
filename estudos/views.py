from django.utils import timezone
from django.utils.dateparse import parse_datetime
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models.disciplina import Disciplina
from .models.atividade import Atividade, Status
from .serializers import DisciplinaSerializer, AtividadeSerializer


class Responsavel(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, "usuario"):
            return obj.usuario == request.user
        return getattr(obj, "usuario_id", None) == request.user.id


class SomenteDoUsuarioMixin:
    def get_queryset(self):
        return self.queryset.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class DisciplinaViewSet(SomenteDoUsuarioMixin, viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    permission_classes = [permissions.IsAuthenticated, Responsavel]


class AtividadeViewSet(SomenteDoUsuarioMixin, viewsets.ModelViewSet):
    queryset = Atividade.objects.all()
    serializer_class = AtividadeSerializer
    permission_classes = [permissions.IsAuthenticated, Responsavel]

    def get_queryset(self):
        qs = super().get_queryset()

        status_param = self.request.query_params.get("status")
        if status_param:
            qs = qs.filter(status=status_param)

        de = self.request.query_params.get("de")
        ate = self.request.query_params.get("ate")
        de_dt = parse_datetime(de) if de else None
        ate_dt = parse_datetime(ate) if ate else None
        if de_dt:
            qs = qs.filter(data_prazo__gte=de_dt)
        if ate_dt:
            qs = qs.filter(data_prazo__lte=ate_dt)

        disciplina_id = self.request.query_params.get("disciplinaId")
        if disciplina_id:
            qs = qs.filter(disciplina_id=disciplina_id)

        return qs

    @action(detail=True, methods=["post"])
    def concluir(self, request, pk=None):
        atividade = self.get_object()

        if atividade.status == Status.CONCLUIDA:
            return Response(
                {"Atenção": "Essa ação já foi concluída."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        atividade.status = Status.CONCLUIDA
        atividade.concluido_em = timezone.now()
        atividade.save()

        return Response(
            AtividadeSerializer(atividade, context={"request": request}).data,
            status=status.HTTP_200_OK,
        )

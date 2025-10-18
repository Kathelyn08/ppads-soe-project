from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views import DisciplinaViewSet, AtividadeViewSet, cadastrar_usuario

router = DefaultRouter()
router.register(r"disciplinas", DisciplinaViewSet, basename="disciplinas")
router.register(r"atividades", AtividadeViewSet, basename="atividades")

urlpatterns = [
    path("cadastrar/", cadastrar_usuario, name="cadastrar_usuario"),
]

urlpatterns += router.urls

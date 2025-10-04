from rest_framework.routers import DefaultRouter
from .views import DisciplinaViewSet, AtividadeViewSet

router = DefaultRouter()
router.register(r"disciplinas", DisciplinaViewSet, basename="disciplinas")
router.register(r"atividades", AtividadeViewSet, basename="atividades")

urlpatterns = router.urls

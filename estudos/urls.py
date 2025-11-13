from django.urls import path
from django.contrib.auth import views as auth_views

from .views.dashboard import dashboard
from .views.registro import registro

from .views.atividade import (
    AtividadeListView,
    AtividadeDetailView,
    AtividadeCreateView,
    AtividadeUpdateView,
    AtividadeDeleteView,
    AtividadeMarkFinishedView
)

from .views.disciplina import (
    DisciplinaListView,
    DisciplinaDetailView,
    DisciplinaCreateView,
    DisciplinaUpdateView,
    DisciplinaDeleteView
)

from .views.meta import (
    MetaListView,
    MetaCreateView,
    MetaUpdateView,
    MetaDeleteView
)

from .views.agenda import AgendaView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='conta/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', registro, name='registro'),
    path('dashboard/', dashboard, name='dashboard'),

    path('atividades/', AtividadeListView.as_view(), name='atividade-list'),
    path('atividade/<int:pk>/', AtividadeDetailView.as_view(), name='atividade-detail'),
    path('atividade/novo/', AtividadeCreateView.as_view(), name='atividade-create'),
    path('atividade/<int:pk>/editar/', AtividadeUpdateView.as_view(), name='atividade-update'),
    path('atividade/<int:pk>/excluir/', AtividadeDeleteView.as_view(), name='atividade-delete'),
    path('atividade/<int:pk>/mark-finished/', AtividadeMarkFinishedView.as_view(), name='atividade-mark-finished'),

    path('disciplina/', DisciplinaListView.as_view(), name='disciplina-list'),
    path('disciplina/<int:pk>/', DisciplinaDetailView.as_view(), name='disciplina-detail'),
    path('disciplina/novo/', DisciplinaCreateView.as_view(), name='disciplina-create'),
    path('disciplina/<int:pk>/editar/', DisciplinaUpdateView.as_view(), name='disciplina-update'),
    path('disciplina/<int:pk>/excluir/', DisciplinaDeleteView.as_view(), name='disciplina-delete'),

    path('meta/', MetaListView.as_view(), name='meta-list'),
    path('meta/novo/', MetaCreateView.as_view(), name='meta-create'),
    path('meta/<int:pk>/editar/', MetaUpdateView.as_view(), name='meta-update'),
    path('meta/<int:pk>/excluir/', MetaDeleteView.as_view(), name='meta-delete'),

    path('agenda/', AgendaView.as_view(), name='agenda'),
]

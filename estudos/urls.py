from django.urls import path
from django.contrib.auth import views as auth_views

from .views.dashboard import dashboard
from .views.registro import registro
from .views.atividade import (
    AtividadeListView,
    AtividadeDetailView,
    AtividadeCreateView,
    AtividadeUpdateView,
    AtividadeDeleteView
)

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='conta/login.html'), name='login'),
    path('registro/', registro, name='registro'),

    path('dashboard/', dashboard, name='dashboard'),
    path('atividades/', AtividadeListView.as_view(), name='atividade-list'),
    path('atividade/<int:pk>/', AtividadeDetailView.as_view(), name='atividade-detail'),
    path('atividade/novo/', AtividadeCreateView.as_view(), name='atividade-create'),
    path('atividade/<int:pk>/editar/', AtividadeUpdateView.as_view(), name='atividade-update'),
    path('atividade/<int:pk>/excluir/', AtividadeDeleteView.as_view(), name='atividade-delete'),
]
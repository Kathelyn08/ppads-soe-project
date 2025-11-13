from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models.atividade import Atividade
from ..util import week_range

@login_required
def dashboard(request):
    u = request.user
    recentes = u.atividades.order_by("-criado_em")[:5]
    categorias = {x: u.atividades.filter(categoria=x).count() for x in Atividade.Categoria}
    prioridades = u.atividades.order_by("-data_prazo", "-prioridade")[:5]

    week_start, week_end = week_range()
    semana = (
        u
        .atividades
        .filter(data_prazo__gte=week_start, data_prazo__lte=week_end)
    )
    concluidas = semana.filter(status=Atividade.Status.CONCLUIDA)
    progresso = concluidas.count() / semana.count() * 100

    context = {
        'user': u,
        'recentes': recentes,
        'categorias': categorias,
        'prioridades': prioridades,
        'semana': semana.count(),
        'concluidas': concluidas.count(),
        'progresso': progresso
    }

    return render(request, 'dashboard/dashboard.html', context)


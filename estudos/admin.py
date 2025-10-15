from django.contrib import admin
from .models.disciplina import Disciplina
from .models.atividade import Atividade
from .models.sessaoestudo import SessaoEstudo
from .models.meta import MetaEstudo
from .models.notificacao import Notificacao

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ("nome", "usuario")
    search_fields = ("nome", "usuario__username")

@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ("titulo", "usuario", "disciplina", "prioridade", "data_prazo", "status")
    list_filter = ("status", "prioridade", "disciplina")
    search_fields = ("titulo", "disciplina__nome", "usuario__username")

admin.site.register(SessaoEstudo)
admin.site.register(MetaEstudo)
admin.site.register(Notificacao)


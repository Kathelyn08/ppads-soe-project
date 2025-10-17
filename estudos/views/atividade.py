from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from estudos.models.atividade import Atividade

class AtividadeListView(LoginRequiredMixin, ListView):
    model = Atividade
    template_name = 'atividade/atividade_list.html'
    context_object_name = 'atividades'
    paginate_by = 10

    def get_queryset(self):
        queryset = Atividade.objects.filter(usuario=self.request.user)

        status = self.request.GET.get('status')
        prioridade = self.request.GET.get('prioridade')
        categoria = self.request.GET.get('categoria')
        
        if status:
            queryset = queryset.filter(status=status)
        if prioridade:
            queryset = queryset.filter(prioridade=prioridade)
        if categoria:
            queryset = queryset.filter(categoria=categoria)
            
        return queryset.order_by('data_prazo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_choices'] = Atividade.Status.choices
        context['prioridade_choices'] = Atividade.Prioridade.choices
        context['categoria_choices'] = Atividade.Categoria.choices
        return context

class AtividadeDetailView(LoginRequiredMixin, DetailView):
    model = Atividade
    template_name = 'atividade/atividade_detail.html'
    context_object_name = 'atividade'

    def get_queryset(self):
        return Atividade.objects.filter(usuario=self.request.user)

class AtividadeCreateView(LoginRequiredMixin, CreateView):
    model = Atividade
    template_name = 'atividade/atividade_form.html'
    fields = [
        'disciplina',
        'peso',
        'titulo',
        'descricao',
        'data_prazo',
        'estimativa_min',
        'local',
        'status',
        'categoria',
        'prioridade',
        'modalidade'
    ]
    success_url = reverse_lazy('atividade-list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class AtividadeUpdateView(LoginRequiredMixin, UpdateView):
    model = Atividade
    template_name = 'atividade/atividade_form.html'
    fields = [
        'disciplina',
        'peso',
        'titulo',
        'descricao',
        'data_prazo',
        'estimativa_min',
        'local',
        'status',
        'categoria',
        'prioridade',
        'modalidade'
    ]
    success_url = reverse_lazy('atividade-list')

    def get_queryset(self):
        return Atividade.objects.filter(usuario=self.request.user)

class AtividadeDeleteView(LoginRequiredMixin, DeleteView):
    model = Atividade
    template_name = 'atividade/atividade_confirm_delete.html'
    success_url = reverse_lazy('atividade-list')
    
    def get_queryset(self):
        return Atividade.objects.filter(usuario=self.request.user)
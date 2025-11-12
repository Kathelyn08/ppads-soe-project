from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from estudos.models.disciplina import Disciplina

class DisciplinaListView(LoginRequiredMixin, ListView):
    model = Disciplina
    template_name = 'disciplina/disciplina_list.html'
    context_object_name = 'disciplinas'
    paginate_by = 10

    def get_queryset(self):
        queryset = Disciplina.objects.filter(usuario=self.request.user)
        return queryset.order_by('nome')

class DisciplinaDetailView(LoginRequiredMixin, DetailView):
    model = Disciplina
    template_name = 'disciplina/disciplina_detail.html'
    context_object_name = 'disciplina'

    def get_queryset(self):
        return Disciplina.objects.filter(usuario=self.request.user)

class DisciplinaCreateView(LoginRequiredMixin, CreateView):
    model = Disciplina
    template_name = 'disciplina/disciplina_form.html'
    fields = [
        'nome',
        'descricao',
    ]
    success_url = reverse_lazy('disciplina-list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class DisciplinaUpdateView(LoginRequiredMixin, UpdateView):
    model = Disciplina
    template_name = 'disciplina/disciplina_form.html'
    fields = [
        'nome',
        'descricao',
    ]
    success_url = reverse_lazy('disciplina-list')

    def get_queryset(self):
        return Disciplina.objects.filter(usuario=self.request.user)

class DisciplinaDeleteView(LoginRequiredMixin, DeleteView):
    model = Disciplina
    template_name = 'disciplina/disciplina_confirm_delete.html'
    success_url = reverse_lazy('disciplina-list')
    
    def get_queryset(self):
        return Disciplina.objects.filter(usuario=self.request.user)
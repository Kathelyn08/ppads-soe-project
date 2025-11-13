from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from estudos.models.atividade import Atividade
from estudos.models.disciplina import Disciplina
from django import forms
from datetime import date, timedelta
from itertools import groupby

class Filter(forms.Form):
    disciplina = forms.ModelChoiceField(
        queryset=Disciplina.objects.all(),
        required=False
    )
    data_prazo__gte = forms.DateField(
        label="Data Inicial",
        required=False,
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'})
    )
    data_prazo__lte = forms.DateField(
        label="Data Final",
        required=False,
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'})
    )

    def __init__(self, params, *args, user=None, **kwargs):
        today = date.today()
        week_start = today - timedelta(days=today.weekday() + 1)
        week_end = week_start + timedelta(days=6)
        defaults = {
            "data_prazo__gte": week_start,
            "data_prazo__lte": week_end
        }

        super().__init__(defaults | params, *args, **kwargs)

        for x in self:
          x.field.widget.attrs = { 'class': 'form-control bg-dark text-light border-secondary' }

        self.fields["disciplina"].queryset = user.disciplinas.all().order_by('nome')

class AgendaView(LoginRequiredMixin, ListView):
    model = Atividade
    template_name = 'agenda/agenda_list.html'
    context_object_name = 'atividades'

    def get_queryset(self):
        queryset = self.request.user.atividades.all().order_by('data_prazo', '-prioridade')

        self.form = Filter(self.request.GET.dict(), user=self.request.user)

        if self.form.is_valid():
            filters = {k: v for k, v in self.form.cleaned_data.items() if v is not None}
            queryset = queryset.filter(**filters)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context

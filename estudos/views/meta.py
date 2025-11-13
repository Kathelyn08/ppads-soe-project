from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from estudos.models.meta import Meta
from datetime import date, timedelta
from django import forms
from django.forms import ModelForm
from django.db.models import Q
from ..util import week_range, compact, exclude

class MetaForm(ModelForm):
    class Meta:
        model = Meta
        fields = [
            'disciplina',
            'descricao',
            'alvo',
            'data_inicial',
            'data_final'
        ]
        widgets = {
            'data_inicial': forms.DateTimeInput(
                format="%Y-%m-%dT%H:%M:%S",
                attrs={'type': 'datetime-local'}
            ),
            'data_final': forms.DateTimeInput(
                format="%Y-%m-%dT%H:%M:%S",
                attrs={'type': 'datetime-local'}
            )
        }

class MetaListView(LoginRequiredMixin, ListView):
    model = Meta
    template_name = 'meta/meta_list.html'
    context_object_name = 'metas'

    class Filter(forms.Form):
        data_inicial__gte = forms.DateTimeField(
            label="Data Inicial",
            required=False,
            widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
        )
        data_final__lte = forms.DateTimeField(
            label="Data Final",
            required=False,
            widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
        )

        def __init__(self, params, *args, **kwargs):
            week_start, week_end = week_range()
            defaults = {
                "data_inicial__gte": week_start,
                "data_final__lte": week_end
            }

            super().__init__(defaults | params, *args, **kwargs)
            
            for x in self:
                x.field.widget.format = "%Y-%m-%dT%H:%M:%S"
                x.field.widget.attrs = { 'class': 'form-control bg-dark text-light border-secondary' }

    def get_queryset(self):
        queryset = self.request.user.metas.all().order_by('data_final')

        self.form = self.Filter(self.request.GET.dict())

        if self.form.is_valid():
            filters = compact(self.form.cleaned_data)
            filters['data_inicial__lte'] = filters['data_final__lte']
            queryset = queryset.filter(
                Q(data_final__isnull=True, **exclude(filters, "data_final__lte"))
                | Q(**filters)
            )
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        context['total'] = len(context['metas'])
        context['concluido'] = len([meta for meta in context['metas'] if meta.concluida()])
        context['progresso'] = context['concluido'] / context['total'] * 100

        return context

class MetaCreateView(LoginRequiredMixin, CreateView):
    model = Meta
    template_name = 'meta/meta_form.html'
    form_class = MetaForm
    success_url = reverse_lazy('meta-list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class MetaUpdateView(LoginRequiredMixin, UpdateView):
    model = Meta
    template_name = 'meta/meta_form.html'
    form_class = MetaForm
    success_url = reverse_lazy('meta-list')

    def get_queryset(self):
        return self.request.user.metas.all()

class MetaDeleteView(LoginRequiredMixin, DeleteView):
    model = Meta
    template_name = 'meta/meta_confirm_delete.html'
    success_url = reverse_lazy('meta-list')
    
    def get_queryset(self):
        return self.request.user.metas.all()

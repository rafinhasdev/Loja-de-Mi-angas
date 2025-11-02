from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Micanga

class MicangaListView(ListView):
    model = Micanga
    template_name = 'loja/listar.html'

class MicangaDetailView(DetailView):
    model = Micanga
    template_name = 'loja/detalhe.html'

class MicangaCreateView(CreateView):
    model = Micanga
    fields = ['nome', 'descricao', 'preco', 'cor', 'estoque']
    template_name = 'loja/form.html'
    success_url = reverse_lazy('listar')

class MicangaUpdateView(UpdateView):
    model = Micanga
    fields = ['nome', 'descricao', 'preco', 'cor', 'estoque']
    template_name = 'loja/form.html'
    success_url = reverse_lazy('listar')

class MicangaDeleteView(DeleteView):
    model = Micanga
    template_name = 'loja/confirm_delete.html'
    success_url = reverse_lazy('listar')

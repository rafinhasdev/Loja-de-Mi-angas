from django.urls import path
from .views import *

urlpatterns = [
    path('', MicangaListView.as_view(), name='listar'),
    path('<int:pk>/', MicangaDetailView.as_view(), name='detalhe'),
    path('adicionar/', MicangaCreateView.as_view(), name='criar'),
    path('editar/<int:pk>/', MicangaUpdateView.as_view(), name='editar'),
    path('deletar/<int:pk>/', MicangaDeleteView.as_view(), name='deletar'),
]

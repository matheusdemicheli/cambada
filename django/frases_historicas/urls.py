from django.urls import path
from frases_historicas import views

urlpatterns = [
    path('dia/', views.get_frase_do_dia, name='get_frase_do_dia'),
    path('aleatoria/', views.get_frase_aleatoria, name='get_frase_aleatoria'),
    path('pesquisa/', views.pesquisar_frases, name='pesquisar_frases'),
]

from django.urls import path
from frases_historicas import views

app_name = 'frases_historicas'

urlpatterns = [
    path('', views.index, name='index'),
    path('dia/', views.get_frase_do_dia, name='get_frase_do_dia'),
    path('dia', views.get_frase_do_dia),
    path('aleatoria/', views.get_frase_aleatoria, name='get_frase_aleatoria'),
    path('aleatoria', views.get_frase_aleatoria),
    path('pesquisa/', views.pesquisar_frases, name='pesquisar_frases'),
    path('pesquisa', views.pesquisar_frases),
]

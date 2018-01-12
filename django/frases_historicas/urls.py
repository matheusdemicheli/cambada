from django.conf.urls import patterns, include, url


urlpatterns = patterns('frases_historicas.views',
    url(r'^aleatoria/$', 'get_frase_aleatoria', name='get_frase_aleatoria'),
    url(r'^dia/$', 'get_frase_do_dia', name='get_frase_do_dia'),
    # url(r'^pesquisa/$', 'pesquisar_frase', name='pesquisar_frase'),
)

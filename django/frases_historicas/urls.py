from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^aleatoria/$', 'frases_historicas.views.get_frase_aleatoria', name='get_frase_aleatoria'),
    url(r'^dia/$', 'frases_historicas.views.get_frase_do_dia', name='get_frase_do_dia'),
)

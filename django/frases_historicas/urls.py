from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'frases_historicas.views.get_frase_aleatoria', name='get_frase_aleatoria'),
)

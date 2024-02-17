from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('frases_historicas/', include('frases_historicas.urls')),
    path('webpush/', include('webpush.urls')),
    path('transcricao/', include('transcricao.urls')),
]

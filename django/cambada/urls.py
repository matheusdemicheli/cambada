from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frases_historicas.urls', namespace='frases_historicas')),
    path('webpush/', include('webpush.urls')),
]

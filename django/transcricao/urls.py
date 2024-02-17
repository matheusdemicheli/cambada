from django.urls import path
from transcricao import views

urlpatterns = [
    path('', views.TranscricaoView.as_view(), name='transcricao'),
]

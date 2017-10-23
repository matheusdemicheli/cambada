from random import randint
from django.shortcuts import render
from django.http import JsonResponse
from frases_historicas.models import FraseHistorica

# Create your views here.
def get_frase_aleatoria(request):
    indice = randint(0, FraseHistorica.objects.count())
    frase = FraseHistorica.objects.all()[indice]
    dados = {
        'autor': frase.autor,
        'data': frase.data,
        'texto': frase.texto
    }
    return JsonResponse(dados)
    

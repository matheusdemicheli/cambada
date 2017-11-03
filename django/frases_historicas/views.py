#-*- coding: utf-8 -*-
import datetime
from random import randint
from django.shortcuts import render
from django.http import JsonResponse
from frases_historicas.models import FraseHistorica

# Create your views here.
def get_frase_aleatoria(request):
    """
    Retorna uma frase aleatória.
    """
    indice = randint(0, FraseHistorica.objects.count())
    frase = FraseHistorica.objects.all()[indice]
    dados = {
        'autor': frase.autor,
        'data': frase.data,
        'texto': frase.texto
    }
    return JsonResponse(dados)


def get_frase_do_dia(request):
    """
    Retorna a frase do dia.
    """
    hoje = datetime.date.today()

    try:
        # Busca a frase do dia, se existir.
        frase = FraseHistorica.objects.get(data_exibicao=hoje)

    except FraseHistorica.DoesNotExist:
        # Caso não exista, busca uma frase aleatória que ainda não tenha sido
        # escolhida como frase do dia.
        frases = FraseHistorica.objects.filter(data_exibicao__isnull=True)

        if not frases:
            # Caso todas as frases já foram exibidas ao menos uma vez, atualiza
            # o campo da data de exibição para None.
            FraseHistorica.objects.all().update(data_exibicao__isnull=True)
            frases = FraseHistorica.objects.filter(data_exibicao__isnull=True)

        # Indice aleatório.
        indice = randint(0, frases.count())
        frase = frases[indice]
        frase.data_exibicao = hoje
        frase.save()

    dados = {
        'autor': frase.autor,
        'data': frase.data,
        'texto': frase.texto
    }
    return JsonResponse(dados)
